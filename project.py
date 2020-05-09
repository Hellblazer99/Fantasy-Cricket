# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'internshala.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidget, QWidget, QFormLayout, QLabel, QGroupBox, QLayout, QPushButton, QMessageBox
import driver
import sqlite3
from sqlite3 import Error
from EvaluateWindow import Ui_EvaluateWindow as Box
from NewWindow import Ui_Form as Form
from ScoreWindow import Ui_ScoreWindow
import sys
from pathlib import Path

class Ui_mainWindow(object):

    def __init__(self):
        self.evalDialog = QtWidgets.QMainWindow()
        self.new_screen = Form()                           
        self.new_screen.setupUi(self.evalDialog)
        
        self.EvaluateWindow= QtWidgets.QMainWindow()
        self.eval_screen= Box()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen= Ui_ScoreWindow()
        self.score_screen.setupUi(self.scoreDialog)

    db_file=str(Path(__file__).parent/"data.db")
    players_avail={}
    players_select={}
    player_value={}
    pointsavail = 1000
    pointsused = 0
    team_name = ""
    val = driver.getVal()
    records=driver.getPlayers()
    bat=0
    bwl=0
    ar=0
    wk=0
        

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(765, 622)
        mainWindow.setStyleSheet("background-color: rgba(196, 188, 255, 250);")
        mainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.topbox = QtWidgets.QGroupBox(self.centralwidget)
        self.topbox.setGeometry(QtCore.QRect(10, 20, 741, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.topbox.setFont(font)
        self.topbox.setMouseTracking(False)
        self.topbox.setStyleSheet("background-color: rgb(220, 220, 220)")
        self.topbox.setTitle("")
        self.topbox.setObjectName("topbox")

        #Your Selection Labels: This is BAT
        self.batsmen = QtWidgets.QLabel(self.topbox)
        self.batsmen.setGeometry(QtCore.QRect(10, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.batsmen.setFont(font)
        self.batsmen.setObjectName("batsmen")

        #BOW
        self.bowlers = QtWidgets.QLabel(self.topbox)
        self.bowlers.setGeometry(QtCore.QRect(180, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bowlers.setFont(font)
        self.bowlers.setObjectName("bowlers")

        #AR
        self.allrnd = QtWidgets.QLabel(self.topbox)
        self.allrnd.setGeometry(QtCore.QRect(360, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.allrnd.setFont(font)
        self.allrnd.setObjectName("allrnd")

        #WK
        self.wktkp = QtWidgets.QLabel(self.topbox)
        self.wktkp.setGeometry(QtCore.QRect(540, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.wktkp.setFont(font)
        self.wktkp.setObjectName("wktkp")

        #Your Selection
        self.your_selections = QtWidgets.QLabel(self.topbox)
        self.your_selections.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro Ext")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setKerning(False)
        self.your_selections.setFont(font)
        self.your_selections.setStyleSheet("font: 75 12pt \"Tekton Pro Ext\";color: rgb(0, 0, 0);")
        self.your_selections.setObjectName("your_selections")

        #Available Points Label
        self.availpoints = QtWidgets.QLabel(self.centralwidget)
        self.availpoints.setGeometry(QtCore.QRect(40, 150, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.availpoints.setFont(font)
        self.availpoints.setObjectName("availpoints")

        #Four radio buttons: This is BOW
        self.bowButton = QtWidgets.QRadioButton(self.centralwidget)
        self.bowButton.setGeometry(QtCore.QRect(110, 190, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bowButton.setFont(font)
        self.bowButton.setObjectName("bowButton")
        self.bowButton.name = "BOW"
        self.bowButton.toggled.connect(lambda: self.fillList(self.bowButton))
        #WK
        self.wkButton = QtWidgets.QRadioButton(self.centralwidget)
        self.wkButton.setGeometry(QtCore.QRect(260, 190, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wkButton.setFont(font)
        self.wkButton.setObjectName("wkButton")
        self.wkButton.name = "WK"
        self.wkButton.toggled.connect(lambda: self.fillList(self.wkButton))
        #BAT
        self.batButton = QtWidgets.QRadioButton(self.centralwidget)
        self.batButton.setGeometry(QtCore.QRect(40, 190, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.batButton.setFont(font)
        self.batButton.setObjectName("batButton")
        self.batButton.name = "BAT"
        self.batButton.toggled.connect(lambda: self.fillList(self.batButton))
        #AR
        self.arButton = QtWidgets.QRadioButton(self.centralwidget)
        self.arButton.setGeometry(QtCore.QRect(190, 190, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.arButton.setFont(font)
        self.arButton.setObjectName("arButton")
        self.arButton.name = "AR"
        self.arButton.toggled.connect(lambda: self.fillList(self.arButton))
        
        #Used Points Label
        self.usedpoints = QtWidgets.QLabel(self.centralwidget)
        self.usedpoints.setEnabled(True)
        self.usedpoints.setGeometry(QtCore.QRect(440, 150, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.usedpoints.setFont(font)
        self.usedpoints.setObjectName("usedpoints")

        #Teamname Label
        self.teamname = QtWidgets.QLabel(self.centralwidget)
        self.teamname.setGeometry(QtCore.QRect(440, 190, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teamname.setFont(font)
        self.teamname.setObjectName("teamname")

        #Available Players List
        self.avail_team = QtWidgets.QListWidget(self.centralwidget)
        self.avail_team.setGeometry(QtCore.QRect(40, 220, 271, 351))
        self.avail_team.setAutoFillBackground(False)
        self.avail_team.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.avail_team.setObjectName("avail_team")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avail_team.setFont(font)

        #Selected Players List
        self.select_team = QtWidgets.QListWidget(self.centralwidget)
        self.select_team.setGeometry(QtCore.QRect(440, 220, 271, 351))
        self.select_team.setAutoFillBackground(False)
        self.select_team.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_team.setObjectName("select_team")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_team.setFont(font)


        self.usedpoints.raise_()
        self.topbox.raise_()
        self.availpoints.raise_()
        self.bowButton.raise_()
        self.wkButton.raise_()
        self.batButton.raise_()
        self.arButton.raise_()
        self.teamname.raise_()
        self.avail_team.raise_()
        self.select_team.raise_()

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        #Drop down menu
        self.actionNew_Team = QtWidgets.QAction(mainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(mainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(mainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(mainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")

        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)

        self.avail_team.itemDoubleClicked.connect(self.removelist1)
        self.select_team.itemDoubleClicked.connect(self.removelist2)

        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.actionQuit = QtWidgets.QAction(mainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.menuManage_Teams.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.quit)

        self.retranslateUi(mainWindow)

        self.actionNew_Team.triggered.connect(lambda: self.newTeam(mainWindow))
        self.actionOpen_Team.triggered.connect(lambda: self.openTeam(mainWindow))
        self.actionSave_Team.triggered.connect(lambda: self.saveTeam())
        self.actionEvaluate_Team.triggered.connect(lambda: self.evaluateTeam())

        
        val = self.eval_screen.Selectmatch.currentText()
        self.eval_screen.SelectTeam.currentTextChanged.connect(self.combo)
        if val != '--SELECT MATCH--':
            self.eval_screen.SelectTeam.currentTextChanged.connect(self.combo2)
        self.eval_screen.Calculate.clicked.connect(self.SCORE)

        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def show(self):
        self.availpoints.setText("Points Available: "+str(self.pointsavail))
        self.usedpoints.setText("Points Used: "+str(self.pointsused))
        self.batsmen.setText("Batsmen(BAT) "+str(self.bat))
        self.bowlers.setText("Bowlers(BOW) "+str(self.bwl))
        self.allrnd.setText("Allrounders(AR) "+str(self.ar))
        self.wktkp.setText("Wicket-keepers(WK) "+str(self.wk))
        
    def enabler(self):
        self.batsmen.setEnabled(True)
        self.bowlers.setEnabled(True)
        self.allrnd.setEnabled(True)
        self.wktkp.setEnabled(True)
        self.your_selections.setEnabled(True)
        self.availpoints.setEnabled(True)
        self.bowButton.setEnabled(True)
        self.wkButton.setEnabled(True)
        self.usedpoints.setEnabled(True)
        self.batButton.setEnabled(True)
        self.arButton.setEnabled(True)
        self.teamname.setEnabled(True)
        self.avail_team.clear()
        self.select_team.clear()
        self.players_avail={}
        self.players_select={}
        self.btn_map = {}
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.pointsavail = 1000
        self.pointsused = 0
        
    def quit(self):
        dialog=QtWidgets.QMessageBox()
        dialog.setWindowTitle("System Message")
        dialog.setText("Are you sure you want to quit?")
        dialog.setIcon(QMessageBox.Information)
        dialog.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        reply=dialog.exec_()
        if reply == QMessageBox.Yes:
            sys.exit()
        
        

        
    def newTeam(self,mainWindow):
        self.enabler()
        qry = "SELECT name FROM teams;"
        conn=None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
            print("Connection unsuccesful")
        cursor = conn.cursor()
        cursor.execute(qry)
        records = cursor.fetchall()
        team_list = []
        for record in records:
            team_list.append(record[0])
        text = " "
        while(1):
            text, ok=QtWidgets.QInputDialog.getText(mainWindow, "Create Team", "Enter name of the team to be created:")
            if ok and text:
                if text not in team_list:
                    self.team_name = text
                    self.teamname.setText(str(text))
                    break
                else:
                    msg = "Team already exists !!"
                    self.popup(msg,QMessageBox.Warning,QMessageBox.Retry,False)
                    continue
            msg = "Team name cannot be empty" 
            self.popup(msg,QMessageBox.Critical,QMessageBox.Retry,False)
        for record in self.records:
            if record[1] not in self.players_avail:
                self.players_avail[record[1]] = []
            self.players_avail[record[1]].append(record[0])

        for value in self.val:
            if value[0] not in self.player_value:
                self.player_value[value[0]] = []
            self.player_value[value[0]] = value[1]
        #print(self.players_avail)
        self.show()
        conn.close()

    def openTeam(self,mainWindow):
        qry = "SELECT name FROM teams;"
        conn=None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
            print("Connection unsuccesful")
        cursor = conn.cursor()
        cursor.execute(qry)
        records = cursor.fetchall()
        team_list = []
        for record in records:
            team_list.append(record[0])
        #print(team_list)
        team , ok = QtWidgets.QInputDialog.getItem(mainWindow,"Choose Team","Choose A Team",team_list,0,False)
        if ok and team:
            self.teamname.setText(team)
        self.enabler()
        self.team_name = team
        qry = "SELECT players,value from teams where name='"+team+"';"
        cursor.execute(qry)
        team_list = cursor.fetchall()[0]
        value = team_list[1]
        team_list = team_list[0]
        team_list = list(team_list.split(','))
        team_list.remove(team_list[-1])
        team_list[0] = team_list[0].split(" ")[1]
        #print(team_list)
        self.pointsused = value
        self.pointsavail = 1000 - value
        self.show()
        for name in team_list:
            qry = "SELECT ctg FROM stats where player='"+name+"';" 
            cursor.execute(qry)
            ctg = cursor.fetchone()[0]
            if ctg not in self.players_select:
                self.players_select[ctg] = []
            self.players_select[ctg].append(name)
            self.select_team.addItem(name)
            
        for record in self.records:
            if record[1] not in self.players_select:
                if record[1] not in self.players_avail:
                    self.players_avail[record[1]] = []
                self.players_avail[record[1]].append(record[0])
            elif record[0] not in self.players_select[record[1]]:
                if record[1] not in self.players_avail:
                    self.players_avail[record[1]] = []
                self.players_avail[record[1]].append(record[0])

        #print(self.players_select)
        #print(self.players_avail)
        for key in self.players_select.keys():
            l = len(self.players_select[key])
            if key == 'BAT':
                self.bat = l
            if key == 'WK':
                self.wk = l
            if key == 'AR':
                self.ar = l
            if key == 'BOW':
                self.bwl = l
        self.show()

            
        self.fillList(self.batButton)
        conn.close()
        
    def saveTeam(self):
        msg = ''
        if self.bat+self.bwl+self.ar+self.wk < 11:
            msg="Can't Save a Team with less than 11 members"
            self.popup(msg,QMessageBox.Critical,QMessageBox.Cancel,False)
            return
        if self.wk == 0:
            msg="Can't Save a Team with no Wicket-Keeper"
            self.popup(msg,QMessageBox.Critical,QMessageBox.Cancel,False)
            return
        count = self.select_team.count()
        selected = " "
        for i in range(count):
            selected+=self.select_team.item(i).text()
            if i<count:
                selected+=","
        qry="INSERT INTO teams (name,players,value) VALUES ('"+self.team_name+"','"+selected+"',"+str(self.pointsused)+");"
        conn=None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
            print("Connection unsuccesful")
        cursor = conn.cursor()
        try:
            cursor.execute(qry)
            self.popup("Team "+self.team_name+" Saved Successfully",QMessageBox.Information,QMessageBox.Ok,False)
            conn.commit()
        except:
            self.popup("Error Occured while Saving",QMessageBox.Critical,QMessageBox.Retry|QMessageBox.Cancel,False)
            conn.rollback()

    def evaluateTeam(self):
        self.EvaluateWindow.show()

    def combo(self):
        self.eval_screen.Selectmatch.currentTextChanged.connect(self.combo2)
        
                
    def combo2(self):
        conn=sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        team = self.eval_screen.SelectTeam.currentText()
        qry = "SELECT players FROM teams WHERE name='"+team+"';"
        cursor.execute(qry)
        team_list = cursor.fetchall()
        team_list = team_list[0][0]
        team_list = list(team_list.split(','))
        team_list.remove(team_list[-1])
        team_list[0] = team_list[0].split(" ")[1]
        
        self.eval_screen.PlayerList.clear()
        for name in team_list:
            item=QtWidgets.QListWidgetItem(name)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#fff821'))
            self.eval_screen.PlayerList.addItem(item)
        total_score = []
        for name in team_list:
            qry = "SELECT ctg FROM stats where player='"+name+"';" 
            cursor.execute(qry)
            ctg = cursor.fetchone()[0]
            if ctg == 'BAT' or ctg == 'AR':
                qry="SELECT scored,fours,sixes from match where player='"+name+"';"
                cursor.execute(qry)
                data = cursor.fetchall()[0]
                scored = int(data[0])
                fours = int(data[1])
                sixes = int(data[2])
                qry="""SELECT "100s","50s" from stats where player='"""+name+"""';"""
                cursor.execute(qry)
                data = cursor.fetchall()
                data = data[0]
                hund = int(data[0])
                fifty = int(data[1])
                total_score.append(scored//2 + 5*fifty + 10*hund + fours + 2*sixes)
                
            if ctg == 'BOW' or ctg == 'AR':
                qry="SELECT wkts,given,bowled from match where player='"+name+"';"
                cursor.execute(qry)
                data = cursor.fetchall()[0]
                wkts = int(data[0])
                given = int(data[1])
                bowled = int(data[2]/6)
                if bowled != 0:
                    econ = given/bowled
                wkts = wkts*10
                if econ >= 3.5 and econ <= 4.5:
                    wkts = wkts + 4
                elif econ >= 2.5:
                    wkts = wkts + 7
                else:
                    wkts = wkts + 10

                if ctg == 'AR':
                    total_score[-1]=total_score[-1]+wkts
                else:
                    total_score.append(wkts)
                 
            if ctg == 'WK' or ctg == 'AR': 
                qry="SELECT catches,stumping,ro from match where player='"+name+"';"
                cursor.execute(qry)
                data = cursor.fetchall()[0]
                catches = int(data[0])
                stumping = int(data[1])
                ro = int(data[2])
                if ctg == 'AR':
                    total_score[-1]=total_score[-1]+10*(catches+stumping+ro)
                else:
                    total_score.append(10*(catches+stumping+ro))
                
        
        self.eval_screen.ScoreList.clear()
        self.teamscore = total_score
        #print(len(total_score))
        for score in total_score:
            items= QtWidgets.QListWidgetItem(str(score))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            items.setFont(font)
            items.setBackground(QtGui.QColor('#30ff37'))
            self.eval_screen.ScoreList.addItem(items)
        conn.close()

    def SCORE(self):
        team = self.eval_screen.SelectTeam.currentText()
        match = self.eval_screen.Selectmatch.currentText()
        if team == '--SELECT TEAM--':
            self.popup("Select a team to evaluate",QMessageBox.Critical,QMessageBox.Ok,False)
            return
        if match == '--SELECT MATCH--':
            self.popup("Select a match to evaluate",QMessageBox.Critical,QMessageBox.Ok,False)
            return
        self.scoreDialog.show()
        self.score_screen.Score.setText(str(sum(self.teamscore)))
        
    def fillList(self,btn):
        #print("In fillList")
        
        self.avail_team.clear()
        self.team = []
        if btn.name not in self.players_avail:
            return
        self.names=self.players_avail[btn.name]
        for name in self.names:
            if btn.name not in self.players_select:
                self.avail_team.addItem(name)
            elif name not in self.players_select[btn.name]:
                self.avail_team.addItem(name)

    def logic(self,ctgr,item):
        msg=''
        if ctgr=="WK" and self.wk>=1:
            msg="Wicketkeepers not more than 1"
        if self.bat+self.bwl+self.ar+self.wk >= 11:
            msg="There can be atmost 11 players"
        if msg!='':
            self.popup(msg,QMessageBox.Warning,QMessageBox.Ok,True)
            return False
        
        if self.pointsavail < 0:
            msg="You Have Exhausted your Points"
            self.popup(msg,QMessageBox.Warning,QMessageBox.Ok,True)
            self.pointsavail = 0
            self.show()
            return False
        
        if ctgr=="BAT":self.bat+=1
        if ctgr=="BOW":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1
        return True

    def removelist1(self,item):
        #print("In removelist1")
        conn=None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
            print("Connection unsuccesful")
        cursor = conn.cursor()

        if self.batButton.isChecked()==True:
            ctgr='BAT'
        if self.bowButton.isChecked()==True:
            ctgr='BOW'
        if self.arButton.isChecked()==True:
            ctgr='AR'
        if self.wkButton.isChecked()==True:
            ctgr='WK'
        ret=self.logic(ctgr,item)
        if ret==True:
            self.avail_team.takeItem(self.avail_team.row(item))
            self.select_team.addItem(item.text())
            qry = "SELECT value FROM stats WHERE player='"+item.text()+"'"
            cursor.execute(qry)
            row = cursor.fetchone()
            conn.close()
            value = row[0]
            self.players_avail[ctgr].remove(item.text())
            if(ctgr not in self.players_select):
                self.players_select[ctgr] = []
            self.players_select[ctgr].append(item.text())
            #print(self.players_avail)
            #print(self.players_select)
            self.pointsavail = self.pointsavail - value
            self.pointsused = self.pointsused + value
            self.show()
        conn.close()

    def removelist2(self,item):
        #print("In removelist2")
        self.select_team.takeItem(self.select_team.row(item))
        conn=None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
            print("Connection unsuccesful")
        cursor = conn.cursor()
        qry = "SELECT ctg,value FROM stats WHERE player='"+item.text()+"'"
        cursor.execute(qry)
        row = cursor.fetchone()
        conn.close()
        ctgr = row[0]
        self.pointsavail = self.pointsavail + row[1]
        self.pointsused = self.pointsused - row[1]
        
        self.players_select[ctgr].remove(item.text())
        if(ctgr not in self.players_avail):
            self.players_avail[ctgr] = []
        self.players_avail[ctgr].append(item.text())
        #print(self.players_select)
        #print(self.players_avail)
            
        
        if ctgr=="BAT":
            self.bat-=1
            if self.batButton.isChecked()==True:
                self.avail_team.addItem(item.text())
        if ctgr=="BOW":
            self.bwl-=1
            if self.bowButton.isChecked()==True:
                self.avail_team.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.arButton.isChecked()==True:
                self.avail_team.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.wkButton.isChecked()==True:
                self.avail_team.addItem(item.text())
        self.show()
        conn.close()
        
    def popup(self,msg,icon,btn,flag):
        dialog=QtWidgets.QMessageBox()
        dialog.setWindowTitle("System Message")
        dialog.setText(msg)
        dialog.setIcon(icon)
        dialog.setStandardButtons(btn)
        if flag == True:
            dialog.setDetailedText("""Please follow the logic of cricket team selection:\nWicketkeepers not more than 1\nTotal number of players less than 11""")
        ret=dialog.exec_()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Fanasy Cricket"))
        self.batsmen.setText(_translate("mainWindow", "Batsmen(BAT)"))
        self.batsmen.setEnabled(False)
        self.bowlers.setText(_translate("mainWindow", "Bowlers(BOW)"))
        self.bowlers.setEnabled(False)
        self.allrnd.setText(_translate("mainWindow", "Allrounders(AR)"))
        self.allrnd.setEnabled(False)
        self.wktkp.setText(_translate("mainWindow", "Wicket-keepers(WK)"))
        self.wktkp.setEnabled(False)
        self.your_selections.setText(_translate("mainWindow", "Your Selections"))
        self.your_selections.setEnabled(False)
        self.availpoints.setText(_translate("mainWindow", "Points Available"))
        self.availpoints.setEnabled(False)
        self.bowButton.setText(_translate("mainWindow", "BOW"))
        self.bowButton.setEnabled(False)
        self.wkButton.setText(_translate("mainWindow", "WK"))
        self.wkButton.setEnabled(False)
        self.usedpoints.setText(_translate("mainWindow", "Points Used"))
        self.usedpoints.setEnabled(False)
        self.batButton.setText(_translate("mainWindow", "BAT"))
        self.batButton.setEnabled(False)
        self.arButton.setText(_translate("mainWindow", "AR"))
        self.arButton.setEnabled(False)
        self.teamname.setText(_translate("mainWindow", "Team Name: "))
        self.teamname.setEnabled(False)
        self.menuManage_Teams.setTitle(_translate("mainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("mainWindow", "New Team"))
        self.actionNew_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen_Team.setText(_translate("mainWindow", "Open Team"))
        self.actionOpen_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Team.setText(_translate("mainWindow", "Save Team"))
        self.actionSave_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEvaluate_Team.setText(_translate("mainWindow", "Evaluate Team"))
        self.actionEvaluate_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionQuit.setText(_translate("mainWindow", "Quit Game"))