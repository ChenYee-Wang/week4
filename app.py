from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from markupsafe import escape

from flask.templating import render_template_string

app=Flask(
    __name__, 
    static_folder = "public", 
    static_url_path = "/"
)

app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"

info = ({
        "account":"test",
        "password":"test"
    })

@app.route("/")
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return render_template("index.html")

@app.route("/signin",methods = ["post"])
def signin():
    input = ({
        "account" : request.form["account"],
        "password" : request.form["password"]
    })

    if input == info:
        return redirect("/member")
    else:
        return redirect("/error")

@app.route("/signout",methods = ["get"])
def signout():
    session.pop("input","none")
    return redirect("/")

@app.route("/member")
def member():
    if "user" in session:
        input = session["user"]
    return render_template("member.html")

@app.route("/error")
def error():
    return render_template("error.html")
  
app.run(port = 3000, debug = "true")