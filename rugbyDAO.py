import mysql.connector
import dbConfig as cfg

class RugbyDAO:
    db=""

    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['username'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )
          
    # create a new team in rugby database 
    def createTeam(self, values):
        cursor = self.db.cursor()
        sql = "insert into team (name, conf, country, points) values (%s, %s, %s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid
       
    # return all rows in team table
    def getAllTeams(self):
        cursor = self.db.cursor()
        sql = "select * from team"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []

        for result in results:
            returnArray.append(self.toDict(result))

        return returnArray
   
    # return unique team details based on id
    def findTeamByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from team where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.toDict(result)
    
    # update a team based on id provided
    def updateTeam(self, values):
        cursor = self.db.cursor()
        sql = "update team set name = %s, conf = %s, country = %s, points = %s where id = %s"
        cursor.execute(sql, values)

        self.db.commit()

    # delete record from league table based on id
    def deleteLeague(self, id):
        cursor = self.db.cursor()
        sql = "delete from league where id =  %s"
        values = (id,)
        cursor.execute(sql, values)

        self.db.commit()
        print("League deleted")
    
    # delete record from team table based on id
    def deleteTeam(self, id):
        cursor = self.db.cursor()
        sql = "delete from team where id =  %s"
        values = (id,)
        cursor.execute(sql, values)

        self.db.commit()
        print("Team deleted")

    def toDict(self, result):
        colnames = ['id', 'name', 'conf', 'country', 'points']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item

rugbyDAO = RugbyDAO()