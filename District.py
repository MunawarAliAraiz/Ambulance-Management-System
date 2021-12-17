import RecordData as f2
class District:
    def __init__(self, name, noOfAreas, noOfHospitals, AmblanceCenter):
        self.name=name
        self.noOfAreas=noOfAreas 
        #list of areas
        self.noOfHospitals=noOfHospitals
        self.AmblanceCenter=AmblanceCenter     
    def setname(self, x):
        self.name=x   
    def getname(self):
        return self.name

    def setnoOfAreas(self, x):
        self.noOfAreas=x   
    def getnoOfAreas(self):
        return self.noOfAreas

    def setnoOfHospitals(self, x):
        self.noOfHospitals=x   
    def getnoOfHospitals(self):
        return self.noOfHospitals

    def setAmblanceCenter(self, x):
        self.AmblanceCenter=x   
    def getAmblanceCenter(self):
        return self.AmblanceCenter


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