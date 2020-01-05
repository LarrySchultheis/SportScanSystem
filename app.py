from flask import Flask, render_template, send_from_directory, request, send_file
from flask_mysqldb import MySQL
import json
import docxCreator
import os
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ma$terChief117'
app.config['MYSQL_DB'] = 'acc2013'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    # if request.method == "POST":
    #     info = request.form
    #     date = info['date']
    #     cur = mysql.connection.cursor()
    #     #cur.execute("select * from customers")
    #     data = cur._rows
    #     obj = {
    #         "data" : data[0][0]
    #     }
    #     mysql.connection.commit()
    #     cur.close()
    #     return date
    return send_from_directory('web', 'index.html')

@app.route('/js/report.js', methods=["GET"])
def get_script():
    doctype = 'text/js'
    return send_from_directory('web/js', 'report.js', mimetype=doctype)

@app.route("/Report", methods=['GET'])
def report():
    
    return send_from_directory("web", "report.html")

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

    reply = json.dumps(object)
    # print(reply)
    #return send_from_directory("web", "report.html")

    path = os.getcwd()
    print(path)
    return send_file(path + "\documents\\report.docx", attachment_filename="report.docx")

@app.route('/NewEntry', methods=['GET'])
def NewEntry():

    return send_from_directory("web", "newEntry.html")

if __name__ == '__main__':
    app.run(port = 5000)
