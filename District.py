import RecordData as f2
class District:
    def __init__(self, name, noOfAreas, noOfHospitals,areas, AmblanceCenter):
        self.name=name
        self.noOfAreas=noOfAreas 
        self.noOfHospitals=noOfHospitals
        self.areas=areas
        self.AmblanceCenter=AmblanceCenter     
    def setname(self, x):
        self.name=x   
    def getname(self):
        return self.name

    def setnoOfAreas(self, x):
        self.noOfAreas=x   
    def getnoOfAreas(self):
        return self.noOfAreas

    def setareas(self, x):
        self.areas.append(x)   
    def getareas(self):
        return self.areas

    def setnoOfHospitals(self, x):
        self.noOfHospitals=x   
    def getnoOfHospitals(self):
        return self.noOfHospitals

    def setAmblanceCenter(self, x):
        self.AmblanceCenter=x   
    def getAmblanceCenter(self):
        return self.AmblanceCenter


# r=District("0000","corolla","car",["asad", "saad"],"16")
# a = f2.RecordData.getInstance()
# a.addDistrict(r)
# d=District("1234","sazuki","car",["asad", "saad"],16)
# a.addDistrict(d)
# e=District("4321","Toyota","bike",["asad", "saad"],16)
# a.addDistrict(e)
# a.FindDistrict(e)
# a.viewDistrict()
# print("//////////////////////////////////////")
# a.DeleteDistrict(e)
# a.viewDistrict()
# a.GetDistrictIndex(d)