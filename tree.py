class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None 
        self.parent = None
        
    def preOrder(self):
        print(self.data , end= " ")
        if(self.left != None):
            self.left.preOrder()
        if(self.right != None):
            self.right.preOrder()
    
    def inOrder(self):
        if(self.left != None):
            self.left.inOrder()
        print(self.data , end= " ")
        if(self.right != None):
            self.right.inOrder()
    
    def postOrder(self):
        if(self.left != None):
            self.left.postOrder()
        if(self.right != None):
            self.right.postOrder()
        print(self.data , end= " ")
                    
    def insertNode(self,key):
        
        if(self.data==None):
            self.data=key
        else:
            if(self.data>key):
                if(self.left== None):
                    self.left=Tree(key)
                    self.left.parent=self
                else:
                    self.left.insertNode(key)
            else:
                if(self.right== None):
                    self.right=Tree(key)
                    self.right.parent=self
                else:
                    self.root.right.insertNode(key)
        
    def searching(self,key):
        if(self.data==key):
            print("Node is found!")
        else:
            if(self.data>key):
                if(self.left == None):
                    print("Node is not present!")
                else:
                    self.left.searching(key)
            else:
                if(self.right == None):
                    print("Node is not present!")
                else:
                    self.right.searching(key)
        
    def findMax(self):
        if(self.right!= None):
            self.right.findMax()
        else:
            print(self.data)
    
    def findMin(self):
        if(self.left!= None):
            self.left.findMin()
        else:
            print(self.data)
        
    def helpSuccessor1(self):
        if(self.left!= None):
            self.left.helpSuccessor1()
        else:
            return self.data
     
    def helpSuccessor2(self,b):
        if(self.parent != None):
            if(self.parent.data>b):
                print(self.parent.data)
            else:
                self.parent.helpSuccessor2(b)
        else:
            print("Has no successor")
            
    def successor(self,key):
        if(self.data==key):
            if(self.right != None):
                a = self.right.helpSuccessor1()
                print(a)
            else:
                if(self == self.parent.left):
                    print(self.parent.data)
                if(self == self.parent.right):
                    b=self.data
                    self.helpSuccessor2(b)
        else:
            if(self.data>key):
                if(self.left == None):
                    print("Node is not present!")
                else:
                    self.left.successor(key)
            else:
                if(self.right == None):
                    print("Node is not present!")
                else:
                    self.right.successor(key)    
    
    def helppredessor1(self):
        if(self.right!= None):
            self.right.helppredessor1()
        else:
            print(self.data)
     
    def helppredessor2(self,b):
        if(self.parent != None):
            if(self.parent.data < b):
                print(self.parent.data)
            else:
                self.parent.helppredessor2(b)
        else:
            print("Has no predessor")
            
    def predessor(self,key):
        if(self.data==key):
            if(self.left != None):
                self.left.helppredessor1()
            else:
                if(self == self.parent.left):
                    b=self.data
                    self.helppredessor2(b)
                if(self == self.parent.right):
                    print(self.parent.data)
        else:
            if(self.data>key):
                if(self.left == None):
                    print("Node is not present!")
                else:
                    self.left.predessor(key)
            else:
                if(self.right == None):
                    print("Node is not present!")
                else:
                    self.right.predessor(key)
    
    def Parent(self,key):
        if(self.data==key):
            try:
                print(self.parent.data)
            except:
                print("Its the most basic node having no parent")
        else:
            if(self.data>key):
                if(self.left == None):
                    print("Node is not present!")
                else:
                    self.left.Parent(key)
            else:
                if(self.right == None):
                    print("Node is not present!")
                else:
                    self.right.Parent(key)
    
    def listOfChild(self,key):
        if(self.data==key):
            if(self.left!=None):
                self.left.inOrder()
            if(self.right!=None):
                self.right.inOrder()
        else:
            if(self.data>key):
                if(self.left == None):
                    print("Node is not present!")
                else:
                    self.left.listOfChild(key)
            else:
                if(self.right == None):
                    print("Node is not present!")
                else:
                    self.right.listOfChild(key)