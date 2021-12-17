import hmm as f1
class Hospital:
    def __init__(self, areas, noOfBed):
        self.area=areas
        self.noOfBeds=noOfBed      
    def setarea(self, x):
        self.area=x   
    def getarea(self):
        print(self.area)
        return self.area 

    def setnoOfBeds (self, x):
        self.noOfBeds =x   
    def getnoOfBeds(self):
        return self.noOfBeds 



list = f1.LinkedList[Hospital]()
list.InsetAtEnd(Hospital(18,16))
r=list.ViewList()  
r.getarea()   