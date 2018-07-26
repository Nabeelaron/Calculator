#text changing example


import sys
from PyQt5.QtWidgets import QApplication , QWidget,QPushButton, QLineEdit ,QComboBox, QRadioButton,QListView,QCheckBox,QDateEdit,QTimeEdit , QLabel
#from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot




class app(QWidget):
	
	previous_value = ""
	next_value = ""

	def __init__(self):
		super().__init__()
		self.type = ""
		self.initUI()

	@pyqtSlot()
	def insert0(self):
		app.previous_value += "0"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert1(self):
		app.previous_value += "1"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert2(self):
		app.previous_value += "2"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert3(self):
		app.previous_value += "3"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert4(self):
		app.previous_value += "4"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert5(self):
		app.previous_value += "5"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert6(self):
		app.previous_value += "6"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert7(self):
		app.previous_value += "7"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert8(self):
		app.previous_value += "8"
		self.textbox_1.setText(app.previous_value)


	@pyqtSlot()
	def insert9(self):
		app.previous_value += "9"
		self.textbox_1.setText(app.previous_value)

	@pyqtSlot()
	def add(self):
		if self.type != '':
			self.equal()
		app.next_value = app.previous_value
		app.previous_value = ""
		self.textbox_1.setText("")
		self.type = "+"


	@pyqtSlot()
	def sub(self):
		if self.type != '':
			self.equal()
		app.next_value = app.previous_value
		self.textbox_1.setText("")
		app.previous_value = ""
		self.type = "-"

	@pyqtSlot()
	def mul(self):
		if self.type != '':
			self.equal()

		app.next_value = app.previous_value
		self.textbox_1.setText("")
		app.previous_value = ""
		self.type = "*"

	@pyqtSlot()
	def div(self):
		if self.type != '':
			self.equal()
		app.next_value = app.previous_value
		self.textbox_1.setText("")
		app.previous_value = ""
		self.type = "/"

	@pyqtSlot()
	def equal(self):
		if self.type == '+':
			result = int(app.previous_value) + int(app.next_value)
		elif self.type == '-':
			result = int(app.previous_value) - int(app.next_value)
		elif self.type == '*':
			result = int(app.previous_value) * int(app.next_value)
		elif self.type == '/':
			result = int(app.next_value) / int(app.previous_value)
		else:
			self.textbox_1.setText(str(app.previous_value))
		self.textbox_1.setText(str(int(result)))
		app.previous_value = str(int(result))
		self.type = ''
		

	def initUI(self):
		self.setWindowTitle("Calculator")
		self.setGeometry(200,200 , 400 , 200)
		
		#interactive parts - definition
		self.textbox_1 = QLineEdit(self)
		

		self.digit_0 = QPushButton("0",self)
		self.digit_1 = QPushButton("1",self)
		self.digit_2 = QPushButton("2",self)
		self.digit_3 = QPushButton("3",self)
		self.digit_4 = QPushButton("4",self)
		self.digit_5 = QPushButton("5",self)
		self.digit_6 = QPushButton("6",self)
		self.digit_7 = QPushButton("7",self)
		self.digit_8 = QPushButton("8",self)
		self.digit_9 = QPushButton("9",self)

		self.button_add = QPushButton("+",self) 
		self.button_sub = QPushButton("-",self)
		self.button_div = QPushButton("/",self)
		self.button_mul = QPushButton("*",self)
		self.button_equal = QPushButton("=",self)

		#interactive parts - alignment and resizing
		self.textbox_1.move(10,10)
		self.textbox_1.resize(385,80)
		self.button_add.move(10,90)
		self.button_sub.move(90,90)
		self.button_div.move(170,90)
		self.button_mul.move(250,90)
		self.button_equal.move(325,90)

		self.digit_0.move(10,110)
		self.digit_1.move(90,110)
		self.digit_2.move(170,110)
		self.digit_3.move(10,130)
		self.digit_4.move(90,130)
		self.digit_5.move(170,130)
		self.digit_6.move(10,150)
		self.digit_7.move(90,150)
		self.digit_8.move(170,150)
		self.digit_9.move(90,170)

		


		
		#action
		self.button_add.clicked.connect(self.add)
		self.button_sub.clicked.connect(self.sub)
		self.button_div.clicked.connect(self.div)
		self.button_mul.clicked.connect(self.mul)
		self.button_equal.clicked.connect(self.equal)
		
		self.digit_1.clicked.connect(self.insert1)
		self.digit_2.clicked.connect(self.insert2)
		self.digit_3.clicked.connect(self.insert3)
		self.digit_4.clicked.connect(self.insert4)
		self.digit_5.clicked.connect(self.insert5)
		self.digit_6.clicked.connect(self.insert6)
		self.digit_7.clicked.connect(self.insert7)
		self.digit_8.clicked.connect(self.insert8)
		self.digit_9.clicked.connect(self.insert9)
		self.digit_0.clicked.connect(self.insert0)
		
		self.show()





if __name__ == '__main__':
	appp = QApplication(sys.argv)
	ex = app()
	
	sys.exit(appp.exec_())