# IN CASE THERE ARE DUPLICATE VALUES IN THE LIST, THEN THE FIRST VALUE FROM THE START WILL BE PICKED FOR DELETION

class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.prevVal = None
        self.nextVal = None


class DoubleLinkedList:
    def __init__(self):
        self.headVal = None
    
    # THE INSERT FUNCTION WILL PERFORM STANDARD 'INSERT AT THE END OF THE LIST' OPERATION
    def insert(self, newdata):
        NewNode = Node(newdata)
        # in case the list is empty, we keep this base case which will assign the first element
        if self.headVal is None:
            self.headVal = NewNode
            return
        lastElement = self.headVal
        while (lastElement.nextVal):
            lastElement = lastElement.nextVal
        lastElement.nextVal = NewNode
        NewNode.prevVal = lastElement

    # THIS IS THE REQUIRED FUNCTION WHICH FINDS THE LOCATION OF THE ELEMENT WHICH NEEDS TO GET DELETED
    # ONCE FOUND, IT UPDATES THE NEXT POINTER OF THE PREVIOUS ELEMENT AND THEN THE PREVIOUS POINTER OF THE NEW NEXT ELEMENT
    def findNodeAndDelete(self, currentData):

        if self.headVal is None:
            print("The list has no element to delete")
            return 

        # in case no element is found with the given value, we will perform no operation and return as is
        if self.headVal.nextVal is None:
            if self.headVal.dataVal == currentData:
                self.headVal = None
            else:
                print("Item not found")
            return 
        
        # for deleting the first element we update the head of the list with its own next element
        # and then update the prev pointer of the new head as NULL
        if self.headVal.dataVal == currentData:
            self.headVal = self.headVal.nextVal
            self.headVal.prevVal = None
            return

        n = self.headVal
        while n.nextVal is not None:
            if n.dataVal == currentData:
                break
            n = n.nextVal
        
        # if the element to be deleted is between 2 elements, then we just update the prev and next 
        # pointers of the next and prev elements respectively
        if n.nextVal is not None:
            n.prevVal.nextVal = n.nextVal
            n.nextVal.prevVal = n.prevVal
        
        # in case the element to be deleted is the last element, then we update the next pointer of the prev element to NULL
        else:
            if n.dataVal == currentData:
                n.prevVal.nextVal = None
            else:
                print("Element not found")

    def listprint(self):
        printval = self.headVal
        while printval is not None:
            print(printval.dataVal)
            printval = printval.nextVal


if __name__ == "__main__":

    iterSize = int(input("give the size of original linked list "))
    list = DoubleLinkedList()

    i = 0
    while i < iterSize:
        element = int(input("give next element\n"))
        list.insert(element)
        i += 1

    print("the current linked list before deletion is\n")
    list.listprint()
    delElement = int(
        input("\nwhich element do you want to delete\n"))

    list.findNodeAndDelete(delElement)
    print("the updated list is\n")
    list.listprint()
