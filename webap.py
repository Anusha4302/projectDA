from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from mydb import connection as db
app = Flask(__name__)
import ibm_db,ibm_db_dbi

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;PROTOCOL=TCPIP;UID=rnl73488;PWD=nIeXCWK7L6eLdn00;Security=SSL;SSLSecurityCertificate=DigiCertGlobalRootCA.crt", "", "")
connection = ibm_db_dbi.Connection(conn)
cursor = connection.cursor()

@app.route('/')

@app.route("/register",methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        name = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        print(name,email,password)
        db.register(name,email,password)
        return render_template('login.html', msg = msg) 
    else:
        return render_template('register.html', msg = msg)

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        result_dict = db.login(name,password)
        msg = 'Invalid Username / Password'
        if result_dict != False:
            return render_template('dashboard.html')
        return render_template('login.html', msg = msg)

    else:
        return render_template('login.html', msg = msg)



if __name__== "__main__":
        app.run()



