from flask import Flask, render_template, send_from_directory, request, send_file
from flask_mysqldb import MySQL
import json
import docxCreator
import os
import random
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ma$terChief117'
app.config['MYSQL_DB'] = 'acc2013'

mysql = MySQL(app)

#Resource Endpoints -----------------------------------------------------------------------------------------------------------
@app.route("/", methods=['GET', 'POST'])
def home():
    return send_from_directory('web', 'index.html')

@app.route('/NewEntry', methods=['GET'])
def NewEntry():
    return send_from_directory("web", "newEntry.html")

@app.route('/js/report.js', methods=["GET"])
def getReportScript():
    doctype = 'text/js'
    return send_from_directory('web/js', 'report.js', mimetype=doctype)

#Use this to serve logo -- change file name in send_from_directory to serve different logos
@app.route('/images/Logo.png', methods=["GET"])
def getLogo():
    return send_from_directory('web/images', 'Logo_blk.png')

@app.route('/css/layout.css', methods=["GET"])
def getLayout():
    return send_from_directory('web/css', 'layout.css')

@app.route("/Report", methods=['GET'])
def report():
    
    return send_from_directory("web", "report.html")

#------------------------------------------------------------------------------------------------------------------------------


#Functional Endpoints ---------------------------------------------------------------------------------------------------------

@app.route("/GetReport", methods=['POST'])
def GetReport():
    #date = request.values['date']
    data = request.get_json()
    date = data["date"]
    print(date)
    
    command = "select * from articles where articles.DOE LIKE '" + date+"%'"

    cur = mysql.connection.cursor()
    cur.execute(command)
    data = cur._rows

    object = {
        "teams": [{

        }]
    }

    appendObject = {
        "name": data[0][1],
        "titles": [data[0][2]]
    }

    prevTeam = data[0][1]

    iterData = iter(data)
    next(iterData)
    for row in iterData:
        teamName = row[1]
        article = row[2]

        if prevTeam == teamName:
            #same team so just append to appendObject articles
            appendObject['titles'].append(article)
        else:
            #different team, so append the appendObject to the actual json
            object['teams'].append(appendObject)
            appendObject = {
                "name": teamName,
                "titles" : [article]
            }
            prevTeam = teamName
    object['teams'].append(appendObject)
    del object['teams'][0] 

    docxCreator.parseReport(object, date)

    path = os.getcwd()
    print(path)
    return send_file(path + "\documents\\report.docx", as_attachment=True, attachment_filename="report_" + date + ".docx")

#------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(port = 5000)
