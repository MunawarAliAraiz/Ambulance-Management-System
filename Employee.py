import RecordData as f2
class Employee:
    def __init__(self, name, CNIC, cellNo, email, password , type , shift):
        self.name=name
        self.CNIC=CNIC  
        self.cellNo=cellNo
        self.email=email
        self.password=password
        self.type=type 
        self.shift=shift   
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

r=Equipment("0000","corolla","car","////",16)
a = f2.RecordData.getInstance()
a.addEquipment(r)
d=Equipment("1234","sazuki","car","////",16)
a.addEquipment(d)
e=Equipment("4321","Toyota","bike","////",16)
a.addEquipment(e)
a.FindEquipment(e)
a.viewEquipment()
print("//////////////////////////////////////")
a.DeleteEquipment(e)
a.viewEquipment()
a.GetEquipmentIndex(d)