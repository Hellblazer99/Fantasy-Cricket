from PyQt5 import QtCore, QtGui, QtWidgets
#import internshala, Team_Eval, sys
import project, sys
import sqlite3
from sqlite3 import Error
from pathlib import Path

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = project.Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


def getPlayers():
    conn=None
    try:
        db_file=str(Path(__file__).parent/"data.db")
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        print("Connection unsuccesful")
    cursor = conn.cursor()
    qry = 'SELECT player,ctg FROM stats;'
    cursor.execute(qry)
    players = []
    players = cursor.fetchall()
    conn.close()
    return players

def getVal():
    conn=None
    try:
        db_file=str(Path(__file__).parent/"data.db")
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        print("Connection unsuccesful")
    cursor = conn.cursor()
    qry = 'SELECT player,value FROM stats;'
    cursor.execute(qry)
    val = []
    val = cursor.fetchall()
    conn.close()
    return val
    

