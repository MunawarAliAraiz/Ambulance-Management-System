import Vehicle as vehicle
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
        listToReturn=[]
        currentElement=self.head
        while(currentElement!=None):
            listToReturn.append(currentElement.val)
            currentElement=currentElement.next
        return listToReturn


    def FindNode(self, x):
        currentElement=self.head
        while(currentElement!=None):
            if(currentElement.val==x):
                print("Node is found")
                return True
            currentElement=currentElement.next
        print("Node not found")
        return False

    
    def length(self):
        index=1
        currentElement=self.head
        while(currentElement!=None):
            index=index+1
            currentElement=currentElement.next
        return index
        
        
    def UpdateNode(self, x, y):
        currentElement=self.head
        while(currentElement!=None):
            if(currentElement.val==x):
                currentElement.val=y 
                return
            currentElement=currentElement.next



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
        if(self.getIndex(x)==0):
            self.deleteFromStart()
            return
        currentElement=self.head
        while(currentElement.next!=None):
            if(currentElement.next.val==x):
                if currentElement.next.next == None:
                    currentElement.next = None
                    return
                else:    
                    currentElement.next = currentElement.next.next
                    return
            currentElement=currentElement.next
            

