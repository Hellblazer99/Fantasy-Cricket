import sqlite3    
from sqlite3 import Error
from pathlib import Path

def connect(db_file):
    try:
        conn = None
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        print("Connection unsuccesful")
        
    return conn
    

def table(conn, cmd):
    try:
        c = conn.cursor()
        c.execute(cmd)
    except Error as e:
        print(e)

def insertval(conn,values,params):
    try:
        purge = """INSERT INTO '{}' {} VALUES({});""".format(params[0],params[1],params[2])
        cursor = conn.cursor()
        cursor.executemany(purge,values)
        conn.commit()
        print("Total ", cursor.rowcount," records inserted in ",params[0]," table")     
    except Error as e:
        print(e)


def main():
    db_file=str(Path(__file__).parent/"data.db")
    conn = connect(db_file)
    cursor = conn.cursor()
    if conn is not None:
        matchcmd = """CREATE TABLE IF NOT EXISTS match
            (
            id INTEGER NOT NULL PRIMARY KEY,
            player VARCHAR(45) NOT NULL,
            scored INT NULL,
            faced INT NULL,
            fours INT NULL,
            sixes INT NULL,
            bowled INT NULL,
            maiden INT NULL,
            given INT NULL,
            wkts INT NULL,
            catches INT NULL,
            stumping INT NULL,
            ro INT NULL
            );"""
        
        statscmd = """CREATE TABLE IF NOT EXISTS stats
        (
            id INT NOT NULL PRIMARY KEY,
            player VARCHAR(45) NULL,
            matches INT NULL,
            runs INT NULL,
            '100s' INT NULL,
            '50s' INT NULL,
            value INT NULL,
            ctg VARCHAR(8) NOT NULL
        );"""
        teamscmd = """CREATE TABLE IF NOT EXISTS teams 
        (
            name VARCHAR(255) NOT NULL PRIMARY KEY,
            players VARCHAR(1000) NULL,
            value INT NOT NULL
        );"""
        table(conn,matchcmd)
        print("match table created")
        table(conn,statscmd)
        print("stats table created")
        table(conn,teamscmd)
        print("teams table created")

        
        matchheads = 'id', 'player', 'scored', 'faced', 'fours', 'sixes', 'bowled', 'maiden', 'given', 'wkts', 'catches', 'stumping', 'ro'
        matchparams = []
        matchparams.append('match')
        matchparams.append(matchheads)
        matchparams.append('?,?,?,?,?,?,?,?,?,?,?,?,?')
        matchvalues = [(1,'Kohli', 102, 98, 8, 2, 0, 0, 0, 0, 0, 0, 1),
                        (2,'Yuvraj', 12, 20, 1, 0, 48, 0, 36, 1, 0, 0, 0),
                        (3,'Rahane', 49, 75, 3, 0, 0, 0, 0, 0, 1, 0, 0),
                        (4,'Dhawan', 32, 35, 4, 0, 0, 0, 0, 0, 0, 0, 0),
                        (5,'Dhoni', 56, 45, 3, 1, 0, 0, 0, 0, 3, 2, 0),
                        (6,'Axar', 8, 4, 2, 0, 48, 2, 35, 1, 0, 0, 0),
                        (7,'Pandya', 42, 36, 3, 3, 30, 0, 25, 0, 1, 0, 0),
                        (8,'Jadeja', 18, 10, 1, 1, 60, 3, 50, 2, 1, 0, 1),
                        (9,'Kedar', 65, 60, 7, 0, 24, 0, 24, 0, 0, 0, 0),
                        (10,'Ashwin', 23, 42, 3, 0, 60, 2, 45, 6, 0, 0, 0),
                        (11,'Umesh', 0, 0, 0, 0, 54, 0, 50, 4, 1, 0, 0),
                        (12,'Bumrah', 0, 0, 0, 0, 60, 1, 46, 2, 0, 0, 0),
                        (13,'Bhuwaneshwar', 15, 12, 2, 0, 60, 1, 46, 2, 0, 0, 0),
                        (14,'Rohit', 46, 65, 5, 1, 0, 0, 0, 0, 1, 0, 0),
                        (15,'Kartick', 29, 42, 3, 0, 0, 0, 0, 0, 2, 0, 0)]
        
        insertval(conn,matchvalues,matchparams)

        statsheads = 'id', 'player', 'matches', 'runs', "100s", "50s", 'value', 'ctg'
        statparams = []
        statparams.append('stats')
        statparams.append(statsheads)
        statparams.append('?,?,?,?,?,?,?,?')
        statsvalues = [(1, 'Kohli', 189, 8257, 28, 43, 120, 'BAT'),
                        (2, 'Yuvraj', 86, 3589, 10, 21, 100, 'BAT'),
                        (3, 'Rahane', 158, 5435, 11, 31, 100, 'BAT'),
                        (4, 'Dhawan', 25, 565, 2, 1, 85, 'AR'),
                        (5, 'Dhoni', 78, 2573, 3, 19, 75, 'BAT'),
                        (6, 'Axar', 67, 208, 0, 0, 100, 'BOW'),
                        (7, 'Pandya', 70, 77, 0, 0, 75, 'BOW'),
                        (8, 'Jadeja', 16, 1, 0, 0, 85, 'BOW'),
                        (9, 'Kedar', 111, 675, 0, 0, 90, 'BOW'),
                        (10, 'Ashwin', 136, 1914, 0, 10, 100, 'AR'),
                        (11, 'Umesh', 296, 9496, 10, 64, 110, 'WK'),
                        (12, 'Bumrah', 73, 1365, 0, 8, 60, 'WK'),
                        (13, 'Bhuwaneshwar', 17, 289, 0, 2, 75, 'AR'),
                        (14, 'Rohit', 304, 8701, 14, 52, 85, 'BAT'),
                        (15, 'Kartick', 11, 111, 0, 0, 75, 'AR')]
        insertval(conn,statsvalues,statparams)
        conn.close()

if __name__ == '__main__':
    main()