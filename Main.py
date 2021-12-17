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
    
    def employee_Window(self):
         self.hide()
         super(Ui, self).__init__()
         uic.loadUi('EmployeeMenu.ui',self)
         self.show()
         self.SelectCaseTab.hide()
         self.SelectEquipmentFrame.hide()
         self.ViewRouteFrame.show()
         self.ViewVehicleFrame.hide()
         self.EmergencyRequestsFrame.hide()
         self.equipmentBtn.clicked.connect(self.selectEquipment)
         self.routeBtn.clicked.connect(self.viewRoute)
         self.emergencyBtn.clicked.connect(self.emergencyReq)
         self.caseBtn.clicked.connect(self.selectCase)
         self.vehicleBtn.clicked.connect(self.viewVehicle)
         self.logoutBtn.clicked.connect(self.login_Window)
         
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
         
    def emergencyReq(self):
        self.SelectCaseTab.hide()
        self.SelectEquipmentFrame.hide()
        self.ViewRouteFrame.hide()
        self.ViewVehicleFrame.hide()
        self.EmergencyRequestsFrame.show()
    
    def viewRoute(self):
        self.SelectCaseTab.hide()
        self.EmergencyRequestsFrame.hide()
        self.SelectEquipmentFrame.hide()
        self.ViewVehicleFrame.hide()
        self.ViewRouteFrame.show()
        
    def viewVehicle(self):
        self.SelectCaseTab.hide()
        self.EmergencyRequestsFrame.hide()
        self.SelectEquipmentFrame.hide()
        self.ViewRouteFrame.hide()
        self.ViewVehicleFrame.show()
        
    def selectEquipment(self):
        self.SelectCaseTab.hide()
        self.EmergencyRequestsFrame.hide()
        self.ViewRouteFrame.hide()
        self.ViewVehicleFrame.hide()
        self.SelectEquipmentFrame.show()
        
    def selectCase(self):
        self.EmergencyRequestsFrame.hide()
        self.SelectEquipmentFrame.hide()
        self.ViewRouteFrame.hide()
        self.ViewVehicleFrame.hide()
        self.SelectCaseTab.show()
        
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
         self.loginBtn.clicked.connect(self.login_type)
         self.backBtn.clicked.connect(self.main_Window)
         self.exitBtn.clicked.connect(self.exit)
         
    def emergency_Window(self):
         self.hide()
         super(Ui, self).__init__()
         uic.loadUi('EmergencyForm.ui',self)
         self.show()
         self.backBtn.clicked.connect(self.main_Window)
         self.exitBtn.clicked.connect(self.exit)
         
    def login_type(self):
        if self.adminBtn.isChecked():
            self.admin_Window()
        elif self.employeeBtn.isChecked():
            self.employee_Window()
            
        
         
    def exit(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()