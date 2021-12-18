import sys
import Hospital as f1
import RecordData as f2
import Employee as f3
import Vehicle as f4
from tkinter import *
from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
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
         self.HospitalFrame.hide()
         self.EquipmentFrame.hide()
         self.VehicleFrame.hide()
         self.PerformanceFrame.hide()
         self.AreaFrame.hide()
         self.equipmentBtn.clicked.connect(self.EquipmentManagement)
         self.areaBtn.clicked.connect(self.AreaManagement)
         self.employeeBtn.clicked.connect(self.EmployeeManagement)
         self.performanceBtn.clicked.connect(self.PerformanceManagement)
         self.vehicleBtn.clicked.connect(self.VehicleManagement)
         self.hospitalBtn.clicked.connect(self.hospitalManagement)
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
        self.HospitalFrame.hide()
        self.EmployeeTab.hide()
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.show()
    
    def AreaManagement(self):
        self.HospitalFrame.hide()
        self.EmployeeTab.hide()
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.EquipmentFrame.hide()
        self.AreaFrame.show()
        
    def PerformanceManagement(self):
        self.HospitalFrame.hide()
        self.EmployeeTab.hide()
        self.VehicleFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.hide()
        self.PerformanceFrame.show()
        
    def VehicleManagement(self):
        self.HospitalFrame.hide()
        self.EmployeeTab.hide()
        self.PerformanceFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.hide()
        self.VehicleFrame.show()
        self.ShowVehicle()
        self.pushButton_4.clicked.connect(self.AddVehicle)
        self.pushButton_18.clicked.connect(self.setVehicles_2)
        self.pushButton_9.clicked.connect(self.DeleteVehicle)
        
    def ShowVehicle(self):
        self.tableWidget_3.clear()
        self.tableWidget_3.setColumnWidth(0,150)
        self.tableWidget_3.setColumnWidth(1,150)
        self.tableWidget_3.setColumnWidth(3,170)
        listing=[]
        listing=f2.RecordData.FVehicleList.ViewList()
        self.tableWidget_3.setHorizontalHeaderLabels(["Registration No.","Name","Model No.","Type"])
        for i in range(len(listing)):
            self.tableWidget_3.setRowCount(len(listing))
            got=listing[i]
            self.tableWidget_3.setItem( i , 0 ,QTableWidgetItem(got.getVehicleNo()))
            self.tableWidget_3.setItem( i , 1 ,QTableWidgetItem(got.getname()))
            self.tableWidget_3.setItem( i , 2 ,QTableWidgetItem(got.getmodel()))
            self.tableWidget_3.setItem( i , 3 ,QTableWidgetItem(got.gettype()))
            
    def AddVehicle(self):
        a=self.textEdit_6.toPlainText()
        b=self.textEdit_27.toPlainText()
        c=self.comboBox_31.currentText()
        d=self.comboBox_30.currentText()
        h=f4.Vehicle(a,b,c,d)
        ele=f2.RecordData.getInstance()
        ele.addVehicle(h)
        self.textEdit_6.setText("")
        self.textEdit_27.setText("")
        self.ShowVehicle()
        message = "Vehicle Added !!"
        self.messageBox(message)
        self.setVehicles()
        
    def DeleteVehicle(self):
        a = self.comboBox_16.currentText()
        listing=[]
        listing=f2.RecordData.FVehicleList.ViewList()
        for i in range(len(listing)):
            f=listing[i]
            if f.getVehicleNo() == a:
                ele=f2.RecordData.getInstance()
                ele.DeleteVehicle(f)
                self.textEdit_22.setText("")
                self.textEdit_23.setText("")
                self.textEdit_24.setText("")
                message = "Vehicle Deleted !!"
                self.messageBox(message)
                self.setVehicles()
                self.ShowVehicle()
                break
        
    def EmployeeManagement(self):
        self.HospitalFrame.hide()
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.hide()
        self.EmployeeTab.show()
        self.pushButton_2.clicked.connect(self.AddEmployee)
    
    def AddEmployee(self):
        a=self.textEdit.toPlainText()
        b=self.textEdit_2.toPlainText()
        c=self.textEdit_3.toPlainText()
        d=self.textEdit_7.toPlainText()
        e=self.comboBox_2.currentText()
        f=self.comboBox_3.currentText()
        h=f3.Employee(a,b,c,d,"0000",e,f)
        ele=f2.RecordData.getInstance()
        ele.addEmployee(h)
        self.textEdit_33.setText("")
        self.textEdit_32.setText("")
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.textEdit_7.setText("")
        message = "Employee Added !!"
        self.messageBox(message)
        
    def hospitalManagement(self):
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.AreaFrame.hide()
        self.EquipmentFrame.hide()
        self.EmployeeTab.hide()
        self.setHospitals()
        self.HospitalFrame.show()
        self.pushButton_16.clicked.connect(self.AddHospital)
    
    def setHospitals(self):
        self.comboBox_25.clear()
        listing=[]
        listing=f2.RecordData.HospitaList.ViewList()
        for i in range(len(listing)):
            f=listing[i]
            self.comboBox_25.addItem(f.getname())
            
    def setVehicles(self):
        self.comboBox_16.clear()
        listing=[]
        listing=f2.RecordData.FVehicleList.ViewList()
        for i in range(len(listing)):
            f=listing[i]
            self.comboBox_16.addItem(f.getVehicleNo())
            
    def setVehicles_2(self):
        a = self.comboBox_16.currentText()
        listing=[]
        listing=f2.RecordData.FVehicleList.ViewList()
        for i in range(len(listing)):
            f=listing[i]
            if f.getVehicleNo() == a:
                self.textEdit_22.setText(f.getname())
                self.textEdit_23.setText(f.getmodel())
                self.textEdit_24.setText(f.gettype())
    
    def AddHospital(self):
        a=self.textEdit_33.toPlainText()
        b=self.textEdit_32.toPlainText()
        c=self.comboBox_24.currentText()
        h=f1.Hospital(a,c,b)
        ele=f2.RecordData.getInstance()
        ele.addHospital(h)
        self.textEdit_33.setText("")
        self.textEdit_32.setText("")
        self.setHospitals()
        message = "Hospital Added !!"
        self.messageBox(message)
        
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
            
    def messageBox(self,message):
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showinfo("Message",message)
        window.deiconify()
        window.destroy()
        window.quit()
        
         
    def exit(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()