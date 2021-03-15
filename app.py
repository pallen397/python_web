from flask import Flask
from flask import render_template
import psycopg2 
import json
from datetime import datetime 
import re

app = Flask(__name__)


# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")  

@app.route("/h2/")
def h2():
    return render_template("h2.html")
    

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route('/widgets')
def get_widgets() :
  conn = psycopg2.connect(
    host="192.168.86.27",
    user="pallen",
    password="54645464",
    database="test"
  )
  cursor = conn.cursor()

  cursor.execute("""SELECT * FROM pallen."Dim_GEO" """)

  row_headers=[x[0] for x in cursor.description] 

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)




if __name__ == "__main__":
  app.run(host ='0.0.0.0')