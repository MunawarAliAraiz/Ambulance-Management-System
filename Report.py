import RecordData as f2
class Report:
    def __init__(self, caseNo, date, emergencyType, ambulanceNo, driverName, requestTime, arrivalTime, returnTime, Feedback):
        self.caseNo=caseNo
        self.date=date  
        self.emergencyType=emergencyType
        self.ambulanceNo=ambulanceNo
        self.driverName=driverName
        self.requestTime=requestTime 
        self.arrivalTime=arrivalTime
        self.returnTime=returnTime
        self.Feedback=Feedback  
    def setcaseNo(self, x):
        self.caseNo=x   
    def getcaseNo(self):
        return self.caseNo

    def setdate(self, x):
        self.date=x   
    def getdate(self):
        return self.date

    def setemergencyType(self, x):
        self.emergencyType=x   
    def getemergencyType(self):
        return self.emergencyType

    def setambulanceNo(self, x):
        self.ambulanceNo=x   
    def getambulanceNo(self):
        return self.ambulanceNo

    def setdriverName(self, x):
        self.driverName=x   
    def getdriverName(self):
        return self.driverName

    def setrequestTime(self, x):
        self.requestTime=x   
    def getrequestTime(self):
        return self.requestTime

    def setarrivalTime(self, x):
        self.arrivalTime=x   
    def getarrivalTime(self):
        return self.arrivalTime

    def setreturnTime(self, x):
        self.returnTime=x   
    def getreturnTime(self):
        return self.returnTime

    def setFeedback(self, x):
        self.Feedback=x   
    def getFeedback(self):
        return self.Feedback



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
        