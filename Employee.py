import RecordData as f2
class Employee:
    def __init__(self, registration, name, CNIC, cellNo, email, password , Type , shift):
        self.registration=registration
        self.name=name
        self.CNIC=CNIC  
        self.cellNo=cellNo
        self.email=email
        self.password=password
        self.type=Type 
        self.shift=shift   
     
        
    def setregistration(self, x):
        self.registration=x   
    def getregistration(self):
        return self.registration
    
    
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
    
    def setemail(self, x):
        self.email=x   
    def getemail(self):
        return self.email 
    
    def setpassword(self, x):
        self.password=x   
    def getpassword(self):
        return self.password

    def settype(self, x):
        self.type=x   
    def gettype(self):
        return self.type

    def setshift(self, x):
        self.shift=x   
    def getshift(self):
        return self.shift
