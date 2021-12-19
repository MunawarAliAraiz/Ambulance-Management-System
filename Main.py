import sys
import Hospital as f1
import RecordData as f2
import Employee as f3
import Vehicle as f4
from tkinter import *
from tkinter import messagebox
import Equipment as f5
import District as f6
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
        self.selectcomboBox_15()
        self.setcomboBox_15()
        self.ShowEquipment()
        self.pushButton_3.clicked.connect(self.AddEquipment)
        self.comboBox_15.currentTextChanged.connect(self.onsetcomboBox_15)
    
    def setcomboBox_15(self):
        self.comboBox_15.clear()
        listing=[]
        listing=f2.RecordData.FEquipmentList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            self.comboBox_15.addItem(got.getnumber())
            
            
    def onsetcomboBox_15(self):
        self.selectcomboBox_15()
        
    def selectcomboBox_15(self):
        x=self.comboBox_15.currentText()
        listing=[]
        listing=f2.RecordData.FEquipmentList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            if(got.getnumber()==x):
                self.textEdit_19.setText(got.getname())
                self.textEdit_21.setText(got.getprice())
                self.textEdit_20.setText(got.gettype())
            
            
    def ShowEquipment(self):
        self.tableWidget_2.clear()
        listing=[]
        listing=f2.RecordData.FEquipmentList.ViewList()
        self.tableWidget_2.setHorizontalHeaderLabels(["Number","Name","Type","Price"])
        for i in range(len(listing)):
            self.tableWidget_2.setRowCount(len(listing))
            got=listing[i]
            self.tableWidget_2.setItem( i , 0 ,QTableWidgetItem(got.getnumber()))
            self.tableWidget_2.setItem( i , 1 ,QTableWidgetItem(got.getname()))
            self.tableWidget_2.setItem( i , 2 ,QTableWidgetItem(got.gettype()))
            self.tableWidget_2.setItem( i , 3 ,QTableWidgetItem(got.getprice()))
            
            
    def AddEquipment(self):
        a=self.textEdit_13.toPlainText()
        b=self.textEdit_4.toPlainText()
        c=self.comboBox_4.currentText()
        d=self.textEdit_12.toPlainText()
        e=self.textEdit_5.toPlainText()
        h=f5.Equipment(a,b,c,d,e)
        ele=f2.RecordData.getInstance()
        ele.addEquipment(h)
        self.textEdit_13.setText("")
        self.textEdit_4.setText("")
        self.textEdit_12.setText("")
        self.textEdit_5.setText("")
        self.ShowEquipment()
        message = "Equipment Added "
        self.messageBox(message)
        self.setcomboBox_15()
    
    
    def AreaManagement(self):
        self.HospitalFrame.hide()
        self.EmployeeTab.hide()
        self.VehicleFrame.hide()
        self.PerformanceFrame.hide()
        self.EquipmentFrame.hide()
        self.AreaFrame.show()
        self.selectcomboBox_15()
        self.setcomboBox_15()
        self.ShowEquipment()
        self.label_36.hide()
        self.textEdit_26.hide()
        self.pushButton_10.hide()
        self.pushButton_6.clicked.connect(lambda: self.AddArea("0"))
        self.pushButton_10.clicked.connect(lambda: self.AddArea("1"))
        
    def ShowArea(self):
        self.tableWidget_6.clear()
        listing=[]
        listing=f2.RecordData.FDistrictList.ViewList()
        self.tableWidget_6.setHorizontalHeaderLabels(["Name","No of areas", " Areas ", "Centers"])
        for i in range(len(listing)):
            self.tableWidget_6.setRowCount(len(listing))
            got=listing[i]
            self.tableWidget_6.setItem( i , 0 ,QTableWidgetItem(got.getname()))
            self.tableWidget_6.setItem( i , 1 ,QTableWidgetItem(got.getnoOfAreas()))
            areasReturned=got.getareas()
            s=" "
            for i in range(len(areasReturned)):
                s=s+areasReturned[i]
            self.tableWidget_6.setItem( i , 2 ,QTableWidgetItem(s))
            self.tableWidget_6.setItem( i , 3 ,QTableWidgetItem(got.getAmblanceCenter()))
            
    def AddArea(self,x):
        addedArea = []
        noOfArea = self.textEdit_25.toPlainText()
        noOfAreas = int(noOfArea)
        self.label_36.show()
        self.label_36.setText("Add Area 1")
        self.textEdit_26.show()
        self.pushButton_10.show()
        self.pushButton_6.hide()
        if(x=="1"):
            d=self.textEdit_26.toPlainText()
            addedArea.append(d)
            self.textEdit_26.setText("")
            self.label_36.setText("Add Area "+str(len(addedArea)))
            print(len(addedArea))
            if(len(addedArea)==noOfAreas):
                message = "Areas added Sucessfully"
                self.messageBox(message)
                self.label_36.hide()
                self.textEdit_26.hide()
                self.pushButton_10.hide()
                self.pushButton_6.show()
            return addedArea
        if(x=="0"):
            if(len(addedArea)==noOfAreas):
                a=self.textEdit_15.toPlainText()
                b=self.textEdit_25.toPlainText()
                c=self.comboBox_28.currentText()
                h=f6.District(a,b,addedArea,c)
                ele=f2.RecordData.getInstance()
                ele.addDistrict(h)
                self.textEdit_15.setText("")
                self.textEdit_25.setText("")
                message = "District Added "
                self.messageBox(message)
                self.ShowArea()
                addedArea=[]
            return addedArea
        
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
        self.selectcomboBox_16()
        self.setcomboBox_16()
        self.ShowVehicle()
        self.pushButton_4.clicked.connect(self.AddVehicle)
        self.pushButton_9.clicked.connect(self.DeleteVehicle)
        self.comboBox_16.currentTextChanged.connect(self.onsetcomboBox_16)
    
    def setcomboBox_16(self):
        self.comboBox_16.clear()
        listing=[]
        listing=f2.RecordData.FVehicleList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            self.comboBox_16.addItem(got.getVehicleNo())
            
            
    def onsetcomboBox_16(self):
        self.selectcomboBox_16()

        
    def selectcomboBox_16(self):
        x=self.comboBox_16.currentText()
        listing=[]
        listing=f2.RecordData.FVehicleList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            if(got.getVehicleNo()==x):
                self.textEdit_22.setText(got.getname())
                self.textEdit_23.setText(got.getmodel())
                self.textEdit_24.setText(got.gettype())
            
            
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
        self.setcomboBox_16()
        
        
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
        self.selectcomboBox_9()
        self.setcomboBox_9()
        self.selectcomboBox_14()
        self.setcomboBox_14()
        self.ShowEmployee()
        self.comboBox_9.currentTextChanged.connect(self.onsetcomboBox_9)
        self.comboBox_14.currentTextChanged.connect(self.onsetcomboBox_14)
    
    def setcomboBox_9(self):
        self.comboBox_9.clear()
        listing=[]
        listing=f2.RecordData.FEmployeeList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            self.comboBox_9.addItem(got.getregistratin())
            
    def setcomboBox_14(self):
        self.comboBox_14.clear()
        listing=[]
        listing=f2.RecordData.FEmployeeList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            self.comboBox_14.addItem(got.getregistratin())       
            
    def onsetcomboBox_9(self):
        self.selectcomboBox_9()
    
    def onsetcomboBox_14(self):
        self.selectcomboBox_14()
        
        
    def selectcomboBox_9(self):
        x=self.comboBox_9.currentText()
        listing=[]
        listing=f2.RecordData.FEmployeeList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            if(got.getregistratin()==x):
                self.textEdit_8.setText(got.getname())
                self.textEdit_9.setText(got.getCNIC())
                self.textEdit_10.setText(got.getcellNo())
                self.textEdit_11.setText(got.getemail())
     
    
    def selectcomboBox_14(self):
        x=self.comboBox_14.currentText()
        listing=[]
        listing=f2.RecordData.FEmployeeList.ViewList()
        for i in range(len(listing)):
            got=listing[i]
            if(got.getregistratin()==x):
                self.textEdit_16.setText(got.getname())
                self.textEdit_17.setText(got.getcellNo())
                self.textEdit_18.setText(got.getemail())
            
    def ShowEmployee(self):
        self.tableWidget_5.clear()
        listing=[]
        listing=f2.RecordData.FEmployeeList.ViewList()
        self.tableWidget_5.setHorizontalHeaderLabels(["Reg No", " name","CNIC", "Email", "Type","Cell", "Shift"])
        for i in range(len(listing)):
            self.tableWidget_5.setRowCount(len(listing))
            got=listing[i]
            self.tableWidget_5.setItem( i , 0 ,QTableWidgetItem(got.getregistratin()))
            self.tableWidget_5.setItem( i , 1 ,QTableWidgetItem(got.getname()))
            self.tableWidget_5.setItem( i , 2 ,QTableWidgetItem(got.getCNIC()))
            self.tableWidget_5.setItem( i , 3 ,QTableWidgetItem(got.getemail()))
            self.tableWidget_5.setItem( i , 4 ,QTableWidgetItem(got.gettype()))
            self.tableWidget_5.setItem( i , 5 ,QTableWidgetItem(got.getcellNo()))
            self.tableWidget_5.setItem( i , 6 ,QTableWidgetItem(got.getshift()))      
    
    def AddEmployee(self):
        z=self.textEdit_14.toPlainText()
        a=self.textEdit.toPlainText()
        b=self.textEdit_2.toPlainText()
        c=self.textEdit_3.toPlainText()
        d=self.textEdit_7.toPlainText()
        e=self.comboBox_2.currentText()
        f=self.comboBox_3.currentText()
        h=f3.Employee(z,a,b,c,d,"0000",e,f)
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
        self.ShowEmployee()
        self.setcomboBox_9() 
        self.setcomboBox_14()
        
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