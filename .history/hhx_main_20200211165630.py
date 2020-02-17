import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_hhx1 import *
from bmjc14 import *  #导入具体处理过程

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
    def clear(self):
        self.lineEdit_out.clear()
 
    def shuchu(self):
        p=myWin.lineEdit_mulu.text() #取得目录文本框的内容
        d=myWin.lineEdit_riqi.text() #取得日期文本框的内容
        jieguo=chuli(d,p)  #调用外部bmjc14模块中的chuli函数
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(jieguo) #在plainTextEdit输出结果
  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    
    myWin.ok.clicked.connect(myWin.shuchu) #点击ok按钮后执行
   
    # myWin.ok.clicked.connect(myWin.test3)
    sys.exit(app.exec_())