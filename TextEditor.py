import sys
from PySide import QtGui


class TextEditor(QtGui.QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.initUI()

    def initUI(self):
        #self.wrap=True
        self.Title=None
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.textChanged.connect(self.calculate)
        self.setCentralWidget(self.textEdit)
        self.setGeometry(300, 100, 750, 600)
        self.setHead()
        self.setWindowIcon(QtGui.QIcon('./Icon/Logo.png'))
        self.StatusBar()
        self.Action()
        self.ToolBar()
        self.menu()
        self.show()


    def setHead(self):
        default = 'Untiteled'
        if self.Title == None :
            self.setWindowTitle(default+' - ReynText Editor')
        else :
            self.setWindowTitle(self.Title+' - ReynText Editor')
    
    def menu(self):
        #FILE
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.NewAction)
        fileMenu.addAction(self.OpenAction)
        fileMenu.addAction(self.SaveAction)
        fileMenu.addAction(self.SaveAsAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.PrintAction)
        fileMenu.addAction(self.exitAction)
        #EDIT
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(self.UndoAction)
        editMenu.addAction(self.RedoAction)
        editMenu.addSeparator()
        editMenu.addAction(self.cutAction)
        editMenu.addAction(self.CopyAction)
        editMenu.addAction(self.PasteAction)
        editMenu.addAction(self.SellectAllAction)
        editMenu.addSeparator()
        editMenu.addAction(self.CalculateAction)
        editMenu.addAction(self.FindAction)
        editMenu.addAction(self.replaceAction)
        editMenu.addAction(self.GotoAction)
        FormatMenu = menubar.addMenu('&Format')
        FormatMenu.addAction(self.wWrapAction)
        FormatMenu.addAction(self.Font)
        WindowMenu = menubar.addMenu('&Window')
        WindowMenu.addAction(self.zInAction)
        WindowMenu.addAction(self.zOutAction)
        WindowMenu.addAction(self.hideTBarAction)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(self.abaoutAction)

    def Action(self):
        #File SubMenu
        self.NewAction = QtGui.QAction(QtGui.QIcon('./Icon/New.png'),'&New File', self)
        self.NewAction.setShortcut('Ctrl+N')
        self.NewAction.setStatusTip('Creat New File')
        self.NewAction.triggered.connect(self.NewFile)

        self.OpenAction = QtGui.QAction(QtGui.QIcon('./Icon/Open.png'),'&Open', self)
        self.OpenAction.setShortcut('Ctrl+O')
        self.OpenAction.setStatusTip('Open File')
        self.OpenAction.triggered.connect(self.OpenF)

        self.SaveAction = QtGui.QAction(QtGui.QIcon('./Icon/Save.png'),'&Save', self)
        self.SaveAction.setShortcut('Ctrl+S')
        self.SaveAction.setStatusTip('Save Your File')
        self.SaveAction.triggered.connect(self.Save)

        self.SaveAsAction = QtGui.QAction(QtGui.QIcon('./Icon/Save.png'),'&Save As', self)
        self.SaveAsAction.setShortcut('Ctrl+Shift+S')
        self.SaveAsAction.setStatusTip('Save Your File As')
        self.SaveAsAction.triggered.connect(self.SaveAs)

        self.PrintAction = QtGui.QAction(QtGui.QIcon('./Icon/Print.png'),'&Print', self)
        self.PrintAction.setShortcut('Ctrl+P')
        self.PrintAction.setStatusTip('Print Your File')
        #self.exitAction.triggered.connect(self.close)

        self.exitAction = QtGui.QAction(QtGui.QIcon('./Icon/Exit.png'),'&Exit', self)
        self.exitAction.setShortcut('Alt+f4')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.closeEvent)

        #self Edit Sub menu
        self.UndoAction = QtGui.QAction(QtGui.QIcon('./Icon/Undo.png'),'&Undo', self)
        self.UndoAction.setShortcut('Ctrl+Z')
        self.UndoAction.setStatusTip('Step Backward')
        self.UndoAction.triggered.connect(self.textEdit.undo)

        self.RedoAction = QtGui.QAction(QtGui.QIcon('./Icon/Redo.png'),'&Redo', self)
        self.RedoAction.setShortcut('Ctrl+Y')
        self.RedoAction.setStatusTip('Step Forward')
        self.RedoAction.triggered.connect(self.textEdit.redo)

        self.cutAction = QtGui.QAction(QtGui.QIcon('./Icon/Cut.png'),'&Cut', self)
        self.cutAction.setShortcut('Ctrl+X')
        self.cutAction.setStatusTip('Cut Text')
        self.cutAction.triggered.connect(self.textEdit.cut)

        self.CopyAction = QtGui.QAction(QtGui.QIcon('./Icon/Copy.png'),'&Copy', self)
        self.CopyAction.setShortcut('Ctrl+C')
        self.CopyAction.setStatusTip('Copy Text')
        self.CopyAction.triggered.connect(self.textEdit.copy)

        self.PasteAction = QtGui.QAction(QtGui.QIcon('./Icon/Paste.png'),'&Paste', self)
        self.PasteAction.setShortcut('Ctrl+V')
        self.PasteAction.setStatusTip('Paste To Document')
        self.PasteAction.triggered.connect(self.textEdit.paste)

        self.SellectAllAction = QtGui.QAction(QtGui.QIcon('./Icon/all.png'),'&Sellect All', self)
        self.SellectAllAction.setShortcut('Ctrl+A')
        self.SellectAllAction.setStatusTip('Select Whole Document')
        self.SellectAllAction.triggered.connect(self.textEdit.selectAll)

        self.FindAction = QtGui.QAction(QtGui.QIcon('./Icon/Find.png'),'&Find', self)
        self.FindAction.setShortcut('Ctrl+F')
        self.FindAction.setStatusTip('Find Text')
        #self.exitAction.triggered.connect(self.close)

        self.replaceAction = QtGui.QAction(QtGui.QIcon('./Icon/Replace.png'),'&Replace', self)
        self.replaceAction.setShortcut('Ctrl+R')
        self.replaceAction.setStatusTip('Replace Text with')
        #self.exitAction.triggered.connect(self.close)

        self.CalculateAction = QtGui.QAction(QtGui.QIcon('./Icon/Calculate.png'),'&Calculate Character', self)
        self.CalculateAction.setStatusTip('Calculate Character')
        self.CalculateAction.triggered.connect(self.calculate)

        self.GotoAction = QtGui.QAction(QtGui.QIcon('./Icon/Goto.png'),'&Goto Line', self)
        self.GotoAction.setStatusTip('Goto Line')
        #self.exitAction.triggered.connect(self.close)

        #Format Sub menu
        self.wWrapAction = QtGui.QAction(QtGui.QIcon('./Icon/Wrap.png'),'&Word Wrap', self)
        self.wWrapAction.setStatusTip('Word Wrap')
        #self.wWrapAction.triggered.connect(self.wrapText)

        self.Font = QtGui.QAction(QtGui.QIcon('./Icon/Font.png'),'&Change Font', self)
        self.Font.setStatusTip('Change Font')
        #self.exitAction.triggered.connect(self.close)

        #Window Sub menu
        self.zInAction = QtGui.QAction(QtGui.QIcon('./Icon/ZIN.png'),'&Zoom In', self)
        self.zInAction.setShortcut('Ctrl + <')
        self.zInAction.setStatusTip('Zoom in')
        #self.zInAction.triggered.connect(self.close)

        self.zOutAction = QtGui.QAction(QtGui.QIcon('./Icon/ZOUT.png'),'&Zoom Out', self)
        self.zOutAction.setShortcut('Ctrl + >')
        self.zOutAction.setStatusTip('Zoom Out')
        #self.zOutAction.triggered.connect(self.close)

        self.hideTBarAction = QtGui.QAction(QtGui.QIcon('./Icon/Hide.png'),'&Hide Tool Bar', self)
        self.hideTBarAction.setStatusTip('Hide Tool Bar')
        #self.hideTBarAction.triggered.connect(self.close)
        #Help Submenu
        self.abaoutAction = QtGui.QAction(QtGui.QIcon('./Icon/About.png'),'&About', self)
        self.abaoutAction.setStatusTip('About')
        self.abaoutAction.triggered.connect(self.about)

    def ToolBar(self):
        self.Newtoolbar = self.addToolBar('')
        self.Newtoolbar.addAction(self.NewAction)
        self.Newtoolbar.addAction(self.OpenAction)
        self.Newtoolbar.addAction(self.SaveAction)
        self.Newtoolbar.addSeparator()
        self.Newtoolbar.addAction(self.UndoAction)
        self.Newtoolbar.addAction(self.RedoAction)
        self.Newtoolbar.addAction(self.CopyAction)
        self.Newtoolbar.addAction(self.cutAction)
        self.Newtoolbar.addAction(self.PasteAction)
        self.Newtoolbar.addAction(self.SellectAllAction)
        self.Newtoolbar.addAction(self.CalculateAction)
        self.Newtoolbar.addAction(self.FindAction)
        self.Newtoolbar.addAction(self.replaceAction)
        self.Newtoolbar.addSeparator()
        self.Newtoolbar.addAction(self.wWrapAction)
        self.Newtoolbar.addAction(self.Font)
        self.Newtoolbar.addSeparator()
        self.Newtoolbar.addAction(self.zInAction)
        self.Newtoolbar.addAction(self.zOutAction)
        self.Newtoolbar.addAction(self.hideTBarAction)
        self.Newtoolbar.addSeparator()
        self.Newtoolbar.addAction(self.abaoutAction)

    def NewFile(self):
        self.textEdit.clear()
        self.Title = None
        self.setHead()


    def Save(self):
        if self.Title == None :
            self.SaveAs()
        else :
            f = open(self.Title, 'w')
            text = self.textEdit.toPlainText()
            f.write(text)
            f.close()
            self.Title = self.Title
            self.setHead()
    
    def SaveAs(self):  
        saveName = QtGui.QFileDialog.getSaveFileName(self, 'Save text report', 'myText.txt', "text (*.txt)")
        f = open(saveName[0], 'w')
        text = self.textEdit.toPlainText()
        f.write(text)
        f.close()
        self.Title = saveName[0]
        self.setHead()
            
    def OpenF(self):
      dlg = QtGui.QFileDialog()
      dlg.setFileMode(QtGui.QFileDialog.AnyFile)
      dlg.setFilter("Text files (*.txt)")
      filenames = ''
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'r')
			
         with f:
            data = f.read()
            self.textEdit.setText(data)
            f.close()
            self.Title = filenames[0]
            self.setHead()

    def StatusBar(self):
        self.Mystatus = self.statusBar()
        self.Mystatus.showMessage('Welcome To Reyn TextEditor', 3000)
        self.wordnum = QtGui.QLabel('',self)
        self.Mystatus.addPermanentWidget(self.wordnum)

    def calculate(self):
        numText=self.textEdit
        data = self.textEdit.toPlainText()
        n=len(data)
        self.wordnum.setText('Caharacter Num : '+str(n))
        self.Mystatus.showMessage('Caharacter Num : '+str(n),6000)

    def closeEvent(self,event):
        if self.Title == None:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("The document has been modified.")
            msgBox.setInformativeText("Do you want to save your changes?")
            msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QtGui.QMessageBox.Save:
                self.SaveAs()
            elif ret == QtGui.QMessageBox.Discard:
                self.close()
            elif ret == QtGui.QMessageBox.Cancel:
                event.ignore()
        else :
            event.accept()

    def about(self):
        self.about = QtGui.QMessageBox()
        self.about.about(self,'ReynTextEditor','<b>Thank You for using our apps</b>' \
                         '<br>Copyright 2018 ReynaldTech.Inc . All rights reserved.'\
                         'ReynText Editor is made possible by the ReynaldTech open source project and other open source software.')

if __name__ == '__main__':
    #Exception Handling
    try:
        myApp = QtGui.QApplication(sys.argv)
        myWindow = TextEditor()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("closing window....")
    except Exception:
        print(sys.exc_info()[1])
