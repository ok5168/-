#!/usr/bin/python3
 2 # -*- coding: utf-8 -*-
 3 
 4 """
 5 ZetCode PyQt5 教程
 6 在这个例子中, 我们用PyQt5创建了一个简单的窗口。
 7 
 8 作者: Jan Bodnar
 9 网站: zetcode.com 
10 最后一次编辑: January 2015
11 """
12 
13 import sys
14 from PyQt5.QtWidgets import QApplication, QWidget
15 
16 
17 if __name__ == '__main__':
18     
19     app = QApplication(sys.argv)
20 
21     w = QWidget()
22     w.resize(250, 150)
23     w.move(300, 300)
24     w.setWindowTitle('Simple')
25     w.show()
26     
27     sys.exit(app.exec_())