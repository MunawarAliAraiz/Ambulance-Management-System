class Request:
    def __init__(self, name, CNIC, cellNo, district, area):
        self.name=name
        self.CNIC=CNIC  
        self.cellNo=cellNo 
        self.district=district
        self.area=area
      
    def setdistrict(self, x):
        self.district=x   
    def getdistrict(self):
        return self.district

    def setarea(self, x):
        self.area=x   
    def getarea(self):
        return self.area  

    def setname(self, x):
        self.name=x   
    def getname(self):
        return self.name 

    def setCNIC(self, x):
        self.CNIC =x   
    def getCNIC(self):
        return self.CNIC

    def setcellNo(self, x):
        self.cellNo =x   
    def getcellNo(self):
        return self.cellNo

    def AddRequest(x):

    def DeleteRequest(x):

    def UpdateRequest(x,y):

    def ViewRequest():
        