from flask import Flask, render_template, send_from_directory, request
from flask_mysqldb import MySQL
import json
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ma$terChief117'
app.config['MYSQL_DB'] = 'classicmodels'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        info = request.form
        date = info['date']
        cur = mysql.connection.cursor()
        #cur.execute("select * from customers")
        #data = cur._rows
        #obj = {
        #    "data" : data[0][0]
        #}
        mysql.connection.commit()
        cur.close()
        return date
    return send_from_directory('Templates', 'index.html')

@app.route("/GetReport", methods=['GET', 'POST'])
def getReport():
    
    return send_from_directory("Templates", "report.html")


@app.route("/NewEntry", methods=['GET'])
def newEntry():

    return send_from_directory("Templates", "newEntry.html")

@app.route("/PostEntry", methods=["POST"])
def postEntry(data):

    return data