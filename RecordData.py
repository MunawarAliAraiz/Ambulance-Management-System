import LinkedList as f1
class RecordData:
    HospitaList=f1.LinkedList()
    FEquipmentList=f1.LinkedList()
    FVehicleList=f1.LinkedList()
    FRequestList=f1.LinkedList()






    __instance = None
    def getInstance():
        if RecordData.__instance == None:
            RecordData()
        return RecordData.__instance
    def __init__(self):
        if RecordData.__instance != None:
            raise Exception("Only one object can be created!")
        else:
            RecordData.__instance = self

    def addHospital(self, x):
        self.HospitaList.InsetAtEnd(x)

    def viewHospital(self):
        hospitalList=[]
        hospitalList=self.HospitaList.ViewList()
        for i in range(len(hospitalList)):
            x=hospitalList[i]
            print(x.getname())
            print(x.getarea())   
            print(x.getnoOfBeds())

    def FindHospital(self,x):
        self.HospitaList.FindNode(x)

    def DeleteHospital(self,x):
        self.HospitaList.DeleteNode(x)

    def GetHospitalIndex(self, x):
        y=self.HospitaList.getIndex(x)
        if(y==-1):
            print("Hospital Not Found")
        else:
            print(y)

    def addEquipment(self, x):
        self.FEquipmentList.InsetAtEnd(x)

    def viewEquipment(self):
        EquipmentList=[]
        EquipmentList=self.FEquipmentList.ViewList()
        for i in range(len(EquipmentList)):
            x=EquipmentList[i]
            print(x.getnumber())
            print(x.getname())   
            print(x.gettype())
            print(x.getuse())   
            print(x.getprice())

    def FindEquipment(self,x):
        self.FEquipmentList.FindNode(x)

    def DeleteEquipment(self,x):
        self.FEquipmentList.DeleteNode(x)

    def GetEquipmentIndex(self, x):
        y=self.FEquipmentList.getIndex(x)
        if(y==-1):
            print("Equipment Not Found")
        else:
            print(y)


    def addVehicle(self, x):
        self.FVehicleList.InsetAtEnd(x)

    def viewVehicle(self):
        VehicleList=[]
        VehicleList=self.FVehicleList.ViewList()
        for i in range(len(VehicleList)):
            x=VehicleList[i]
            print(x.getVehicleNo())
            print(x.getmodel())   
            print(x.gettype())
    def FindVehicle(self,x):
        self.FVehicleList.FindNode(x)

    def DeleteVehicle(self,x):
        self.FVehicleList.DeleteNode(x)

    def GetVehicleIndex(self, x):
        y=self.FVehicleList.getIndex(x)
        if(y==-1):
            print("Equipment Not Found")
        else:
            print(y)


    def addRequest(self, x):
        self.FRequestList.InsetAtEnd(x)

    def viewRequest(self):
        RequestList=[]
        RequestList=self.FRequestList.ViewList()
        for i in range(len(RequestList)):
            x=RequestList[i]
            print(x.getname())
            print(x.getCNIC())   
            print(x.getcellNo())
            print(x.getdistrict())   
            print(x.getarea())
    def FindRequest(self,x):
        self.FRequestList.FindNode(x)

    def DeleteRequest(self,x):
        self.FRequestList.DeleteNode(x)

    def GetRequestIndex(self, x):
        y=self.FRequestList.getIndex(x)
        if(y==-1):
            print("Request Not Found")
        else:
            print(y)