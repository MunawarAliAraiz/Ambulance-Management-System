import RecordData as f2
class Vehicle:
    def __init__(self, VehicleNo, model, type):
        self.VehicleNo=VehicleNo
        self.model=model     
        self.type=type
    def setVehicleNo(self, x):
        self.VehicleNo=x   
    def getVehicleNo(self):
        return self.VehicleNo

    def setmodel(self, x):
        self.model=x   
    def getmodel(self):
        return self.model

    def settype(self, x):
        self.type=x  
    def gettype(self):
        return self.type



r=Vehicle("0000","corolla","car")
a = f2.RecordData.getInstance()
a.addVehicle(r)
d=Vehicle("1234","sazuki","car")
a.addVehicle(d)
e=Vehicle("4321","Toyota","bike")
a.addVehicle(e)
a.FindVehicle(e)
a.viewVehicle()
print("//////////////////////////////////////")
a.DeleteVehicle(e)
a.viewVehicle()
a.GetVehicleIndex(d)
