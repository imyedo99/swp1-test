import sys
import time
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.scoredb = []
        self.absscoredb = []
        self.showScoreDB(self.scoredb)

    def initUI(self):

        player = QLabel("Player : ")
        time = QLabel("Time : ")
        result = QLabel("Result : ")

        self.playertitle = QLineEdit()
        self.timetitle = QTextEdit()
        self.resulttilte = QTextEdit()

        Ok = QPushButton("Ok")
        Start = QPushButton("Start")
        Stop = QPushButton("Stop")
        Reset = QPushButton("Reset")

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(player)
        hbox1.addWidget(self.playertitle,15)
        hbox1.addWidget(Ok)
        hbox1.addWidget(Reset)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(time)
        hbox2.addWidget(self.timetitle,15)
        hbox2.addWidget(Start)
        hbox2.addWidget(Stop)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(result)
        hbox3.addWidget(self.resulttilte,100)

        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)

        self.setLayout(vbox1)

        Ok.clicked.connect(self.okInfo)
        Start.clicked.connect(self.startInfo)
        Stop.clicked.connect(self.stopInfo)
        Reset.clicked.connect(self.resetInfo)

        self.setGeometry(300,300,500,250)
        self.setWindowTitle("AD_Project_Timing")
        self.show()

    def okInfo(self):
        playertext = self.playertitle.text()
        if playertext == "":
            playertext = 0
        self.timetitle.setText('Ready? -> Start')
        return int(playertext)

    def startInfo(self):
        self.start = time.time()

        self.timetitle.setText("5초를 세고 Stop버튼을 누르세요.")

    def stopInfo(self):
        self.end = time.time()
        self.timetitle.setText('Ready? -> Start')
        self.scoredb.append(5-(self.end-self.start))
        self.showScoreDB(self.scoredb)

    def resetInfo(self):
        self.scoredb = []
        self.absscoredb = []
        self.resulttilte.setText('')
        self.playertitle.setText('')
        self.timetitle.setText('')

    def showScoreDB(self, scoredb):

        Info = ""
        i = 0
        self.absscoredb
        for i in range(len(scoredb)):
            Info += str(i + 1)
            Info += ':'
            Info += str(scoredb[i]) + " "
            Info += "\n"
        self.resulttilte.setText(Info)
        for j in scoredb:
            self.absscoredb.append(abs(j))
            print(self.absscoredb)
        if i == self.okInfo()-1:
            self.resulttilte.setText(Info
                                     + "Best Player is "
                                     + str(self.absscoredb.index(min(self.absscoredb))+1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
