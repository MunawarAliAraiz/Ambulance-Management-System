import RecordData as f2
class Hospital:
    def __init__(self, name, areas, noOfBed):
        self.name=name
        self.area=areas
        self.noOfBeds=noOfBed  
    
    def setname(self, x):
        self.name=x   
    def getname(self):
        return self.name 

    def setarea(self, x):
        self.area=x   
    def getarea(self):
        return self.area 

    def setnoOfBeds(self, x):
        self.noOfBeds =x   
    def getnoOfBeds(self):
        return self.noOfBeds 



# r=Hospital("asad", 18,16)
# a = f2.RecordData.getInstance()
# a.addHospital(r)
# d=Hospital("saad", 18,16)
# a.addHospital(d)
# e=Hospital("saad", 18,16)
# a.addHospital(e)
# a.FindHospital(e)
# a.viewHospital()
# print("//////////////////////////////////////")
# a.DeleteHospital(e)
# a.viewHospital()
# a.GetHospitalIndex(d)
