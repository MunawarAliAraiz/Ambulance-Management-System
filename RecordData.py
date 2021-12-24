import LinkedList as f1
import csv
class RecordData:
    HospitaList=f1.LinkedList()
    FEquipmentList=f1.LinkedList()
    FVehicleList=f1.LinkedList()
    FRequestList=f1.LinkedList()
    FEmployeeList=f1.LinkedList()
    FReportList=f1.LinkedList()
    FDistrictList=f1.LinkedList()



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

    def UpdateHospital(self,x,y):
        self.HospitaList.UpdateNode(x,y)

    def GetHospitalIndex(self, x):
        y=self.HospitaList.getIndex(x)
        if(y==-1):
            print("Hospital Not Found")
        else:
            print(y)

    def addEquipment(self, x):
        self.FEquipmentList.InsetAtEnd(x)

    def SaveEquipment(self):
        listing=[]
        listing=self.FEquipmentList.ViewList()
        rows = []
        for i in range(len(listing)):
            got = listing[i]
            row = []
            row.append(got.getnumber())
            row.append(got.getname())
            row.append(got.gettype())
            row.append(got.getuse())
            row.append(got.getprice())
            rows.append(row)
        fields = ['Number','Name', 'Type', 'Use', 'Price']
        # name of csv file 
        filename = "Equipments.csv"
    
        # writing to csv file 
        with open(filename, 'w',newline='', encoding='utf-8') as csvfile: 
            csvwriter = csv.writer(csvfile) 
        
            csvwriter.writerow(fields) 
        
            csvwriter.writerows(rows)
        
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

    def UpdateEquipment(self,x,y):
        self.FEquipmentList.UpdateNode(x,y)

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

    def UpdateVehicle(self,x,y):
        self.FVehicleList.UpdateNode(x,y)

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

    def UpdateRequest(self,x,y):
        self.FRequestList.UpdateNode(x,y)

    def GetRequestIndex(self, x):
        y=self.FRequestList.getIndex(x)
        if(y==-1):
            print("Request Not Found")
        else:
            print(y)


    def addEmployee(self, x):
        self.FEmployeeList.InsetAtEnd(x)

    def viewEmployee(self):
        EmployeeList=[]
        EmployeeList=self.FEmployeeList.ViewList()
        for i in range(len(EmployeeList)):
            x=EmployeeList[i]
            print(x.getname())
            print(x.getCNIC())   
            print(x.getcellNo())
            print(x.getemail())   
            print(x.getpassword())
            print(x.gettype())   
            print(x.getshift())

    def FindEmployee(self,x):
        self.FEmployeeList.FindNode(x)

    def DeleteEmployee(self,x):
        self.FEmployeeList.DeleteNode(x)

    def UpdateEmployee(self,x,y):
        self.FEmployeeList.UpdateNode(x,y)

    def GetEmployeeIndex(self, x):
        y=self.FEmployeeList.getIndex(x)
        if(y==-1):
            print("Employee Not Found")
        else:
            print(y)


    def addReport(self, x):
        self.FReportList.InsetAtEnd(x)

    def viewReport(self):
        ReportList=[]
        ReportList=self.FReportList.ViewList()
        for i in range(len(ReportList)):
            x=ReportList[i]
            print(x.getcaseNo())
            print(x.getdate())   
            print(x.getemergencyType())
            print(x.getambulancrNo())   
            print(x.getdriverName())
            print(x.getrequestTime())   
            print(x.getarrivalTime())
            print(x.getreturnTime())   
            print(x.getFeedback())           
    def FindReport(self,x):
        self.FReportList.FindNode(x)

    def DeleteReport(self,x):
        self.FReportList.DeleteNode(x)

    def UpdateReport(self,x,y):
        self.FReportList.UpdateNode(x,y)

    def GetReportIndex(self, x):
        y=self.FReportList.getIndex(x)
        if(y==-1):
            print("Report Not Found")
        else:
            print(y)



    def addDistrict(self, x):
        self.FDistrictList.InsetAtEnd(x)

    def viewDistrict(self):
        DistrictList=[]
        DistrictList=self.FDistrictList.ViewList()
        for i in range(len(DistrictList)):
            x=DistrictList[i]
            print(x.getname())
            print(x.getnoOfAreas())   
            print(x.getnoOfHospitals())
            print(x.getareas())   
            print(x.getAmblanceCenter())

    def FindDistrict(self,x):
        self.FDistrictList.FindNode(x)

    def DeleteDistrict(self,x):
        self.FDistrictList.DeleteNode(x)

    def UpdateDistrict(self,x,y):
        self.FDistrictList.UpdateNode(x,y)

    def GetDistrictIndex(self, x):
        y=self.FDistrictList.getIndex(x)
        if(y==-1):
            print("District Not Found")
        else:
            print(y)