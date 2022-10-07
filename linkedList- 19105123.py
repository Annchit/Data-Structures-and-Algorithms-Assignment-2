# IN CASE THERE ARE DUPLICATE VALUES IN THE LIST THEN THE FIRST VALUE FOUND FROM THE START WILL GET PICKED AS A LOCATION FOR INSERTION

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    # THE INSERT FUNCTION WILL PERFORM STANDARD 'INSERT AT THE END OF THE LIST' OPERATION
    def insert(self, newdata):
        NewNode = Node(newdata)
        # in case the list is empty, we keep this base case which will assign the first element
        if self.headval is None:
            self.headval = NewNode
            return
        prevElement = self.headval
        while (prevElement.nextval):
            prevElement = prevElement.nextval
        prevElement.nextval = NewNode

    # THIS IS THE REQUIRED FUNCTION WHICH FINDS THE LOCATION OF THE ELEMENT IN FRONT OF WHICH WE NEED TO INSERT
    # ONCE FOUND, IT UPDATES THE NEXT POINTER OF THE FOUND LOCATION AND THEN THE NEWLY ADDED ELEMENT
    def findNodeAndInsert(self, currentData, newData):
        if self.headval is None:
            return
        prevElement = self.headval
        while (prevElement):
            if prevElement.dataval is not currentData:
                prevElement = prevElement.nextval
            else:
                newNode = Node(newData)
                newNode.nextval = prevElement.nextval
                prevElement.nextval = newNode
                break
        print("no location found with the specified current value\n")

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


if __name__ == "__main__":

    iterSize = int(input("give the size of original linked list "))
    list = LinkedList()

    i = 0
    while i < iterSize:
        element = int(input("give next element\n"))
        list.insert(element)
        i += 1

    insertedElement = int(
        input("what element do you wish to insert in between\n"))
    print("the current linked list before insertion is\n")
    list.listprint()
    location = int(
        input("\nin front of which element do you wish to insert it \n"))

    list.findNodeAndInsert(location, insertedElement)
    print("the updated list is\n")
    list.listprint()
