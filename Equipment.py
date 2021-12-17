import RecordData as f2
class Equipment:
    def __init__(self, number, name, type, use, price):
        self.number=number
        self.name=name      
        self.type=type
        self.use=use
        self.price=price
    def setnumber(self, x):
        self.number=x   
    def getnumber(self):
        return self.number

    def setname(self, x):
        self.name=x   
    def getname(self):
        return self.name

    def settype(self, x):
        self.type=x   
    def gettype(self):
        return self.type

    def setuse(self, x):
        self.use=x   
    def getuse(self):
        return self.use

    def setprice(self, x):
        self.price=x   
    def getprice(self):
        return self.price


# r=Equipment("0000","corolla","car","////",16)
# a = f2.RecordData.getInstance()
# a.addEquipment(r)
# d=Equipment("1234","sazuki","car","////",16)
# a.addEquipment(d)
# e=Equipment("4321","Toyota","bike","////",16)
# a.addEquipment(e)
# a.FindEquipment(e)
# a.viewEquipment()
# print("//////////////////////////////////////")
# a.DeleteEquipment(e)
# a.viewEquipment()
# a.GetEquipmentIndex(d)