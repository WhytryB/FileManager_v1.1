# -*- coding:utf-8 -*-
from PyQt5 import QtCore,QtWidgets,QtGui
import sys, subprocess
from PyQt5.QtWidgets import (QWidget, QLabel,
QComboBox, QApplication,QMainWindow, QTextEdit,
QAction, QFileDialog,QFileSystemModel, QTreeView, QVBoxLayout
,QPushButton,QListView,QListWidget,QFrame)
from PyQt5.QtGui import QIcon
import shutil        
import os
from PyQt5.QtCore import QDir
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag   
import  pyperclip
import send2trash

        
            
            
            

class MyWindow(QtWidgets.QWidget):
		
		
	def closeEvent(self, e):
		result = QtWidgets.QMessageBox.question(self,
		"Подтверждение закрытия окна",
		"Вы действительно хотите закрыть окно?",
		QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, 
		QtWidgets.QMessageBox.No)
		if result == QtWidgets.QMessageBox.Yes:
			e.accept()
			QtWidgets.QWidget.closeEvent(self , e)
		else:
			e.ignore()
		

	def on_clicked(self):
		opener ="open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call([opener, self.lineEditFilePath.text()])


	def __init__(self):
		self.title = 'Odin'
		self.left = 10
		self.top = 10
		self.width = 140
		self.height = 900
		super().__init__()
		self.initUI()
	

	def initUI(self):
		self.setWindowTitle(self.title)
		self.textEdit = QtWidgets.QTextEdit()
		self.pathRoot= QtCore.QDir.rootPath()
		self.setGeometry(self.left, self.top, self.width, self.height)
		font = QtGui.QFont()
		font.setFamily("Liberation Mono")
		font.setBold(True)
		font.setWeight(105)
		font1 = QtGui.QFont()
		font1.setFamily("")
		font1.setBold(True)
		font1.setWeight(40)
		self.model = QFileSystemModel()
		self.model.setReadOnly(False)
		self.model.setRootPath(self.pathRoot)
		self.tree = QTreeView()
		self.tree.setModel(self.model)
		self.tree.setColumnHidden(1, False)
		self.tree.setColumnHidden(2, False)
		self.tree.setColumnHidden(3, False)
		self.tree.setColumnWidth(0, 700 )
		self.tree.setItemsExpandable(True)
		self.tree.setWordWrap(True)
		self.tree.allColumnsShowFocus()
		self.tree.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
		self.tree.setRootIndex(self.model.index(""))
		self.tree.setUniformRowHeights(True)
		self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.tree.customContextMenuRequested.connect(self.openMenu)
		resolution = QtWidgets.QDesktopWidget().screenGeometry()
		self.tree.setContextMenuPolicy
		self.listo = QtWidgets.QListWidget()
		self.item = QtWidgets.QListWidgetItem()
		self.listo.addItem(self.item)
		__sortingEnabled = self.listo.isSortingEnabled()
		self.item1 = QtWidgets.QListWidgetItem()
		self.listo.addItem(self.item1)
		self.item2 = QtWidgets.QListWidgetItem()
		self.listo.addItem(self.item2)
		self.item3 = QtWidgets.QListWidgetItem()
		self.listo.addItem(self.item3)
		self.item4 = QtWidgets.QListWidgetItem()
		self.listo.addItem(self.item4)
		self.item5 = QtWidgets.QListWidgetItem()
		self.listo.addItem(self.item5)
		self.line = QtWidgets.QFrame(self.listo)
		self.item = self.listo.item(1)
		self.item.setText( "Рабочий стол")
		self.item1 = self.listo.item(2)
		self.item1.setText( "Документы")
		self.item2 = self.listo.item(3)
		self.item2.setText( "Загрузки")
		self.item3 = self.listo.item(0)
		self.item3.setText( "Домашняя папка")
		self.item4 = self.listo.item(4)
		self.item4.setText( "Видео")
		self.item5 = self.listo.item(5)
		self.item5.setText( "Изображения")
		self.item.setFont(font)
		self.item1.setFont(font)
		self.item2.setFont(font)
		self.item3.setFont(font)
		self.item4.setFont(font)
		self.item5.setFont(font)
		self.indexRoot = self.model.index(self.model.rootPath())
		self.tree.setRootIndex(self.indexRoot)
		self.tree.clicked.connect(self.on_treeView_clicked)
		self.labelFilePath = QtWidgets.QLabel(self)
		self.labelFilePath.setText("       Путь к файлу:")
		self.lineEditFilePath = QtWidgets.QLineEdit(self)
		self.newLabel = QtWidgets.QLineEdit(self)
		self.editnewLabel=QtWidgets.QLabel(self)
		self.editnewLabel.setText("Напишите имя новой директории:")
		self.tree.setFont(font1)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.setAcceptDrops(True)
		spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.tree.setMinimumSize(QtCore.QSize(700, 640))
		self.listo.setMaximumSize(QtCore.QSize(200,800))
		self.tree.setAnimated(True)
		self.tree.setIndentation(15)
		self.tree.setSortingEnabled(True)
		self.form = QtWidgets.QFormLayout()
		self.tree.setWindowTitle("Odin")
		self.vbox = QtWidgets.QHBoxLayout()
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.addWidget(self.labelFilePath, 0, 0)
		self.gridLayout.addWidget(self.lineEditFilePath, 0, 1)
		self.gridLayout.addWidget(self.editnewLabel ,1, 0)
		self.gridLayout.addWidget(self.newLabel,1,1 )
		self.windowLayout = QtWidgets.QHBoxLayout()
		self.tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.hbox = QtWidgets.QHBoxLayout()
		self.form.addRow(self.gridLayout)
		self.form.addRow(self.hbox)
		self.form.addRow(self.vbox)
		self.vbox.addWidget(self.line)
		self.vbox.addWidget(self.listo)
		self.vbox.addWidget(self.tree)
		self.setLayout(self.form)
		self.labelFilePath.setFont(font)
		self.lineEditFilePath.setFont(font)
		self.editnewLabel.setFont(font)
		self.newLabel.setFont(font)
		self.tree.setAutoScroll(True)
		self.tree.setAutoScrollMargin(100)
		self.listo.itemClicked.connect(self.Clicked)
		self.setWindowIcon(QIcon('www.png'))
		palette = QtGui.QPalette()
		palette1= QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor("#EDE9F0"))
		brush1 = QtGui.QBrush(QtGui.QColor("#EDE9F0"))
		brush.setStyle(QtCore.Qt.SolidPattern)
		brush1.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Base, brush)
		palette1.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Base, brush1)
		self.listo.setPalette(palette)
		self.newLabel.setPalette(palette1)
		self.lineEditFilePath.setPalette(palette1)
		self.show()
		
	def Clicked(self,item):
		if self.listo.currentItem().text()=="Рабочий стол":
			self.listo.itemClicked.connect(self.WorkStation)
		elif self.listo.currentItem().text()=="Документы":
			self.listo.itemClicked.connect(self.docum)
		elif self.listo.currentItem().text()=="Загрузки":
			self.listo.itemClicked.connect(self.zagr)
		elif self.listo.currentItem().text()=="Домашняя папка":
			self.listo.itemClicked.connect(self.homef)
		elif self.listo.currentItem().text()=="Видео":
			self.listo.itemClicked.connect(self.video)
		elif self.listo.currentItem().text()=="Изображения":
			self.listo.itemClicked.connect(self.izo)

        
        
	def openMenu(self, position):
		menu = QtWidgets.QMenu()
		addDes = QtWidgets.QAction('Открыть файл', menu)
		creat = QtWidgets.QAction("Создать директорию", menu)
		delet = QtWidgets.QAction("Удалить" , menu)
		cop =QtWidgets.QAction("Копировать" , menu)
		cut = QtWidgets.QAction("Вставить" , menu)
		alll=QtWidgets.QAction("Выделить всё",menu)
		cock = QtWidgets.QAction("Раскрыть всё",menu)
		creat.triggered.connect(self.create)
		delet.triggered.connect(self.delete)
		cop.triggered.connect(self.copyact)
		cut.triggered.connect(self.cut_act)
		alll.triggered.connect(self.select)
		cock.triggered.connect(self.cocki)
		addDes.triggered.connect(self.adddescript)
		menu.addAction(creat)
		menu.addAction(delet)
		menu.addAction(cop)
		menu.addAction(cut)
		menu.addAction(addDes)
		menu.addAction(alll)
		menu.addAction(cock)
		menu.exec_(self.tree.viewport().mapToGlobal(position))
        
	def cocki(self):
		self.tree.expandAll()
		
	def adddescript(self):
		opener ="open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call([opener, self.lineEditFilePath.text()])
	
	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def copyact(self):
		path =(os.path.join(self.lineEditFilePath.text()))
		shutil.copytree(path,os.path.join('.../Desktop/odin/cash/1'))
		
	def select(self):
		self.tree.selectAll()	
		
	def cut_act(self):
		path=(os.path.join(self.lineEditFilePath.text(),self.newLabel.text()))
		shutil.copytree('.../Desktop/odin/cash/1',os.path.join(self.lineEditFilePath.text(),self.newLabel.text()))
		send2trash.send2trash('.../Desktop/odin/cash/1')
		
		
	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def on_treeView_clicked(self, index):
		self.indexItem = self.model.index(index.row(), 0, index.parent())
		self.filePath = self.model.filePath(self.indexItem)
		self.filePath1 = self.model.filePath(self.indexItem)
		self.lineEditFilePath.setText(self.filePath)

	def delete(self):
		path=(os.path.join(self.lineEditFilePath.text(),self.newLabel.text()))
		path1=(os.path.join(self.filePath1,self.lineEditFilePath.text()))
		send2trash.send2trash(path1)

			
	def create(self):
		path =(os.path.join(self.lineEditFilePath.text(),self.newLabel.text()))
		os.mkdir(path) 
		print('Дириктория создана')		
	def WorkStation(self,index):
		self.model.setRootPath('.../Desktop')
		self.tree.setRootIndex(self.model.index(".../Desktop"))
		self.lineEditFilePath.setText('.../Desktop')
	def zagr(self):
		self.model.setRootPath('...user/Downloads')
		self.tree.setRootIndex(self.model.index("...user/Downloads"))
		self.lineEditFilePath.setText('...user/Downloads')
	
	def homef(self):
		self.model.setRootPath('')
		self.tree.setRootIndex(self.model.index(""))
	def docum(self):
		self.model.setRootPath('...user/Documents')
		self.tree.setRootIndex(self.model.index("...user/Documents"))
		self.lineEditFilePath.setText('...user/Documents')
	def video(self):
		self.model.setRootPath('...user/Video')
		self.tree.setRootIndex(self.model.index("...user/Video"))
		self.lineEditFilePath.setText('...user/Video')
		
	def izo(self):
		self.model.setRootPath('...user/Image')
		self.tree.setRootIndex(self.model.index("...user/Image"))
		self.lineEditFilePath.setText('...user/Image')
	def dragEnterEvent(self, e):
		e.accept()
    
	def dropEvent(self, e):	
		position = e.pos()
		self.button.move(position)
		e.setDropAction(Qt.MoveAction)
		e.accept()
		

if __name__=="__main__":

		app=QtWidgets.QApplication(sys.argv)

		window = MyWindow()
		pal = window.palette()
		pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                     QtGui.QColor("#F2F1F0"))

		window.setPalette(pal)
		window.setWindowTitle("Odin")
		window.resize(1400, 800)
		window.show()
		sys.exit(app.exec_())
