class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    #Is empty
    def IsEmpty(self):
        if(self.head == None):
            return 1
        else:
            return 0

    def InsetAtEnd(self,x):
        NodeToPlace=Node(x)
        if(self.head==None):
            self.head=NodeToPlace
            return
        else:
            currentElement=self.head
            while(currentElement.next!=None):
                currentElement=currentElement.next
            if(currentElement.next==None):
                currentElement.next=NodeToPlace

    def ViewList(self):
        currentElement=self.head
        while(currentElement!=None):
            print(currentElement.val)
            currentElement=currentElement.next

    def FindNode(self, x):
        currentElement=self.head
        while(currentElement!=None):
            if(currentElement.val==x):
                print("Node is found")
                return
            currentElement=currentElement.next
        print("Node not found")

    def getIndex(self,x):
        index=0
        currentElement=self.head
        while(currentElement!=None):
            if(currentElement.val==x):
                return index
            currentElement=currentElement.next
            index=index+1
        return -1

    def deleteFromStart(self):
        currentElement=self.head.next
        self.head=currentElement

    def deleteFromEnd(self):
        currentElement=self.head
        while(currentElement.next!=None):
            z=currentElement
            currentElement=currentElement.next
        z.next=None

    def DeleteNode(self, x):
        z=0
        currentElement=self.head
        while(currentElement!=None):
            if(currentElement.val==x):
                z.next=currentElement.next
            z=currentElement
            currentElement=currentElement.next

list = LinkedList()
#5tf  print(list.IsEmpty())
list.InsetAtEnd(5)
list.InsetAtEnd(7)
list.InsetAtEnd(9)
# list.FindNode(9)
# print(list.getIndex(10))
# list.deleteFromStart()
# list.deleteFromEnd()
# list.DeleteNode(5)
list.ViewList()