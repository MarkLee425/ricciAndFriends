import mysql.connector
from flask import Flask, request
import time

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "ricci"
DB_NAME = "cathayPacific"
SERVER_HOST="localhost"
SERVER_PORT=8080
PRICE_RATIO=3.6
MIN_PRICE=40
API_KEY="thisIsSecure"

class Database:
    def __init__(self):
        self.host = DB_HOST
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.db_name = DB_NAME
        self.connector = mysql.connector
        self.connection = None

    def connect(self):
        self.connection = self.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db_name  # Add this line to specify the database name
        )
        return self.connection

    def disconnect(self):
        self.connection.close()

connection = Database().connect()
class Cursor:
    def __init__(self):
        self.db = connection

    def initCursor(self):
        return self.db.cursor()

class SQLStatement:
    def createStatement(self, tableName: str, variables: str):
        return "CREATE TABLE " + tableName + " (" + variables + " )"

    def whereStatement(self, condition: str):
        return "WHERE " + condition

    def orderByStatement(self, condition: str):
        return "ORDER BY " + condition
    
    def dropStatement(self, tableName: str):
        return "DROP TABLE " + tableName

    def selectStatement(self, tableName: str, columns: list = [], condition: dict = {}):
        columnString = "*"
        conditionString = ""
        if len(condition) != 0:
            for eachKey, eachVal in condition.items():
                if eachKey.upper() == "WHERE":
                    conditionString += " " + self.whereStatement(eachVal)
                elif eachKey.upper() == "ORDER BY":
                    conditionString += " " + self.orderByStatement(eachVal)
        if len(columns) != 0:
            columnString = ", ".join(columns)
        return "SELECT " + columnString + " FROM " + tableName + conditionString

    def insertStatement(self, tableName: str, columns: list, values: tuple):
        if len(columns) == 0:
            return
        columnString = ", ".join([str(element) for element in columns])
        valueString = ", ".join([str(element) for element in values])
        print("INSERT INTO " + tableName + " (" + columnString + ") VALUES (" + valueString + ")")
        return "INSERT INTO " + tableName + " (" + columnString + ") VALUES (" + valueString + ")"
        

    def deleteStatement(self, tableName: str, condition: dict = {}):
        conditionString = ""
        if len(condition) != 0:
            for eachKey, eachVal in condition.items():
                if eachKey.upper() == "WHERE":
                    conditionString += " " + self.whereStatement(eachVal)
                elif eachKey.upper() == "ORDER BY":
                    conditionString += " " + self.orderByStatement(eachVal)
        return "DELETE FROM " + tableName + conditionString


class SQL:
    def __init__(self, cursor):
        self.cursor = cursor.initCursor()
        self.sql = SQLStatement()
        self.db = connection

    def execute(self, statement: str, saveAsList: bool):
        self.cursor.execute(statement)
        listItem = list()
        if saveAsList:
            for x in self.cursor:
                listItem.append(x[0])
        return listItem

    def checkExistance(self, checkItem: str, command: str):
        listItem = self.execute(command, True)
        return checkItem in listItem

    def createTable(self, tableName: str, variables: str):
        self.cursor.execute(self.sql.createStatement(tableName, variables))

    def dropTable(self, tableName: str):
        self.cursor.execute(self.sql.dropStatement(tableName))

    def select(self, tableName: str, columns: list = [], condition: dict = {}):
        result = self.cursor.execute(self.sql.selectStatement(tableName, columns, condition))
        if len(condition) != 0:
            result = self.cursor.fetchall()
        return result

    def insertSingle(self, tableName: str, columns: list, values: tuple):
        asdf = ("asdf", "qwer")
        self.cursor.execute(self.sql.insertStatement(tableName, columns, values))
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")

    def delete(self, tableName: str, condition: dict = {}):
        self.cursor.execute(self.sql.deleteStatement(tableName, condition))
        self.db.commit()
        print(self.cursor.rowcount, "record(s) deleted")


app = Flask(__name__)
database = Database()
cursor = Cursor()
sql = SQL(cursor)

def sql_workflow():
    sql.createTable("cargoInfo", "_id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, created_at VARCHAR(250) NOT NULL, updated_at VARCHAR(250) NOT NULL, dimension_x FLOAT, dimension_y FLOAT, dimension_z FLOAT, price FLOAT")

""" sql_workflow() """
@app.route("/cargo/info", methods=["GET", "POST"])
def req():
    if (request.headers["Authorization"] != str(API_KEY)):
        return "Unauthorized", 401
    match request.method:
        case "GET":
            _id = request.args.get("id")
            body = request.get_json()
            columns = []
            if "columns" in body:
                if type(body["columns"]) != list:
                    return 'bad request!', 400
                columns = body["columns"]
            return sql.select("cargoInfo", columns, {"where": "_id=" + _id}), 200
        case "POST":
            x = request.args.get('x')
            y = request.args.get('y')
            z = request.args.get('z')
            price = PRICE_RATIO * float(x) * float(y) * float(z)
            print(f'x: {x}, y: {y}, z: {z}, price: {price}') 
            if price < MIN_PRICE:
                price = MIN_PRICE
            sql.insertSingle("cargoInfo", ["created_at", "updated_at", "dimension_x", "dimension_y", "dimension_z", "price"], (str(time.time()), str(time.time()), float(x), float(y), float(z), price))
            return "Success", 200


def start():
    app.run(debug=True, port=SERVER_PORT, host=SERVER_HOST)

start()
""" sql.insertSingle("cathayPacific.cargoInfo", ["created_at", "updated_at", "dimension_x", "dimension_y", "dimension_z", "price"], (str(time.time()), str(time.time()), 1.0, 2.0, 3.0, 4.0)) """