import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QFileSystemModel, QFileDialog

# Key Event
from PySide6.QtCore import Qt

import pyqtgraph as pg
import pyqtgraph.opengl as gl
from graphPlotUi import Ui_MainWindow

import numpy as np

# 自作のライブラリ
from my_modules.syntax_highlighter import *

def _clearall(layout):
    children = []
    for i in range(layout.count()):
        child = layout.itemAt(i).widget()
        if child:
            children.append(child)
    for child in children:
        child.deleteLater()
    else:
        pass

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # pathを引数にて指定
        try:
            path = sys.argv[1]
        except IndexError:
            path = '.'
        self.filepath = []

        self.model = QFileSystemModel()
        self.model.setRootPath(path)
        self.model.setNameFilters(['*.jl']) # この設定だけだと、非該当の拡張子はグレー表示
        self.model.setNameFilterDisables(False) # 上記フィルターに該当しないファイルは非表示

        view = self.treeView
        view.setModel(self.model)
        view.setRootIndex(self.model.index(path))
        view.setColumnWidth(0,260)
        # doubleClicked ...
        view.clicked.connect(self.setFileName)


        # ハイライト表示
        self.hl = PythonHighlighter(self.codeView.document())

        # ボタン操作
        self.saveButton.clicked.connect(self.saveFile)
        self.plotButton.clicked.connect(self.generate_xy)
        self.clearButton.clicked.connect(self.clear)
        self.fontCssLegend = '<style type="text/css"> p {font-family: Helvetica, HackGen35 Console NFJ; font-size: 15pt; color: "#ffffff"} </style>'
        self.codeView.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.codeView:
            if event.key() == Qt.Key_Tab and self.codeView.hasFocus():
                # Special tab handling
                tc = self.codeView.textCursor()
                tc.insertText("    ")
                return True
            else:
                return False
        return False


    def onTextChange(self):
        """
        textChanged fires when the highlighter is reassigned the same document.
        Prevent this from showing "run edited code" by checking for actual
        content change
        """
        newText = self.codeView.toPlainText()
        if newText != self.oldText:
            self.oldText = newText
            #self.codeEdited() 


    def init_ui(self):
        self.setGeometry(50, 50, 1200, 960) # WQXGA (Wide-QXGA)
        self.fontCssLegend = '<style type="text/css"> p {font-family: Arial;font-size: 16pt; color: "#FFF"} </style>'


    def setFileName(self, index):
        try:
            import os
            indexItem = self.model.index(index.row(), 0, index.parent())#print(indexItem)
            if os.path.isfile(self.model.filePath(indexItem)):
                self.filepath.insert(0,self.model.filePath(indexItem))
                text = open(self.filepath[0], encoding='utf-8').read()
                self.codeView.setPlainText(text)
                text.close()
                #self.filepath.insert(0,self.model.filePath(indexItem))
                #self.listWData.clear()
                #self.listWData.addItems(df.columns)
                #self.graphPlot()
            else:
                pass
                #QMessageBox.warning(None, "Notice!", "Select File!",QMessageBox.Yes)
        except AttributeError as e:
            pass


    def saveFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","python Files (*.py)", options=options)
        try:
            with open(fileName, 'w', encoding='utf-8') as f:
                f.write(self.codeView.toPlainText()) 
        except FileNotFoundError as e:
            pass


    def clear(self):
        self.codeView.clear()


    def generate_xy(self):
        from julia import Main
        jlModelCode = self.codeView.toPlainText()
        Main.eval(jlModelCode)
        x,y,z = Main.GLCalc()
        self.draw_graph(x,y,z)

    def draw_graph(self,plot_data_x, plot_data_y, plot_data_z):
        self.fontCssLegend = '<style type="text/css"> p {font-family: Helvetica, HackGen35 Console NFJ; font-size: 15pt; color: "#ffffff"} </style>'
        styles = {'color':'white',
                        'font-size':'20px',
                        'font-style':'bold',
                        'font-family': 'Helvetica, HackGen35 Console NFJ'
                        }
        import inspect
        def retrieve_name(var):
            callers_local_vars = inspect.currentframe().f_back.f_locals.items()
            return [var_name for var_name, var_val in callers_local_vars if var_val is var]

        self.openGLWidget.clear()
        self.openGLWidget.opts['distance'] = 40
        x = plot_data_x
        y = plot_data_y
        for i in range(len(y)):
            yi = [y[i]]*len(x)
            z = plot_data_z[:,i]
            pts = np.vstack([x,yi,z]).transpose()
            plt = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i,len(y)*1.3)), width=(i+1)/10., antialias=True)
            self.openGLWidget.addItem(plt)

def main():
    #import qdarktheme
    app = QApplication(sys.argv)
    # Apply dark theme to Qt application
    #app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()
    window.show()
    app.exec()

if __name__== '__main__':
    main()
