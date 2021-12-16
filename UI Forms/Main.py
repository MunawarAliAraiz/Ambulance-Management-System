import sys
from PyQt5 import QtWidgets, uic
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('StartingWindow.ui',self)
        self.show()
        self.loginBtn.clicked.connect(self.login_Window)
        self.emergencyBtn.clicked.connect(self.emergency_Window)
    
    def main_Window(self):
         self.hide()
         super(Ui, self).__init__()
         uic.loadUi('StartingWindow.ui',self)
         self.show()
         self.loginBtn.clicked.connect(self.login_Window)
         self.emergencyBtn.clicked.connect(self.emergency_Window)
    
    def admin_Window(self):
         self.hide()
         super(Ui, self).__init__()
         uic.loadUi('AdminMenu.ui',self)
         self.show()
         self.EquipmentFrame.hide()
         self.VehicleFrame.hide()
         self.PerformanceFrame.hide()
         self.AreaFrame.hide()
         self.equipmentBtn.clicked.connect(self.EquipmentManagement)
         self.areaBtn.clicked.connect(self.AreaManagement)
         self.employeeBtn.clicked.connect(self.EmployeeManagement)
         self.performanceBtn.clicked.connect(self.PerformanceManagement)
         self.vehicleBtn.clicked.connect(self.VehicleManagement)
         self.logoutBtn.clicked.connect(self.login_Window)
         
    def EquipmentManagement(self):
        self.EmployeeTab.hide()
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.show()
    
    def AreaManagement(self):
        self.EmployeeTab.hide()
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.EquipmentFrame.hide()
        self.AreaFrame.show()
        
    def PerformanceManagement(self):
        self.EmployeeTab.hide()
        self.VehicleFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.hide()
        self.PerformanceFrame.show()
        
    def VehicleManagement(self):
        self.EmployeeTab.hide()
        self.PerformanceFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.hide()
        self.VehicleFrame.show()
        
    def EmployeeManagement(self):
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.hide()
        self.EmployeeTab.show()
         
    def login_Window(self):
         self.hide()
         super(Ui, self).__init__()
         uic.loadUi('Login.ui',self)
         self.show()
         self.loginBtn.clicked.connect(self.admin_Window)
         self.backBtn.clicked.connect(self.main_Window)
         self.exitBtn.clicked.connect(self.exit)
         
    def emergency_Window(self):
         self.hide()
         super(Ui, self).__init__()
         uic.loadUi('EmergencyForm.ui',self)
         self.show()
         self.backBtn.clicked.connect(self.main_Window)
         self.exitBtn.clicked.connect(self.exit)
         
    def exit(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()