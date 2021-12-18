class District:
    def __init__(self, name, noOfAreas,areas, AmblanceCenter):
        self.name=name
        self.noOfAreas=noOfAreas 
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

    def setAmblanceCenter(self, x):
        self.AmblanceCenter=x   
    def getAmblanceCenter(self):
        return self.AmblanceCenter