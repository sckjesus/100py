from flask import Flask, redirect, url_for
import webbrowser

app = Flask(__name__)

listofusers=["sanitha","grapesK","momosa","nothing","mookers"]
listofpasses=["bookman.kaspar.bookgen", "book.com", "chicken.o.momachicken", "onum.illai", "blue"]

@app.route("/")
def nothin():
    return redirect("/sign_in")
#---------------------------------------------------------------------------------------
@app.route("/sign_in")
def tell_them():
    return "Hello! Type your username in the link above by adding a slash(/) and then your username following(example: /bob@chinkser)"
#---------------------------------------------------------------------------------------
@app.route("/sign_in/<username>")
def hello_user(username):
    if str(username) in listofusers:
        return redirect("/sign_in/"+str(username)+"/pass_please")
    else:
        return "Sorry, that was wrong.   <a href='http://127.0.0.1:5000/'> Click this! </a> "  
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
@app.route("/sign_in/sanitha/pass_please")
def password1():
    return "Correct! Now enter your password on the link following a slash(example: /my_password)"

@app.route("/sign_in/grapesK/pass_please")
def password2():
    return "Correct! Now enter your password on the link following a slash(example: /my_password)"

@app.route("/sign_in/momosa/pass_please")
def password3():
    return "Correct! Now enter your password on the link following a slash(example: /my_password)"

@app.route("/sign_in/nothing/pass_please")
def password4():
    return "Correct! Now enter your password on the link following a slash(example: /my_password)"

@app.route("/sign_in/mookers/pass_please")
def password5():
    return "Correct! Now enter your password on the link following a slash(example: /my_password)"
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
@app.route("/sign_in/<username>/pass_please/<passwerdd>")
def passcheck(passwerdd,username):
    if str(passwerdd) in listofpasses:
        if str(username) in listofusers:
            return redirect("/sign_in/"+str(username)+"/pass_please/"+str(passwerdd)+"/done")
        else:
            return "Sorry, that was wrong.   <a href='http://127.0.0.1:5000/'> Click this! </a> "
    else:
        return "Sorry, that was wrong.   <a href='http://127.0.0.1:5000/'> Click this! </a> "
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
@app.route("/sign_in/sanitha/pass_please/bookman.kaspar.bookgen/done")
def hi1():
    return "Hi Susanna!"
@app.route("/sign_in/grapesK/pass_please/book.com/done")
def hi2():
    return "Hi Grace!"
@app.route("/sign_in/momosa/pass_please/chicken.o.momachicken/done")
def hi3():
    return "Hi Samuel!"
@app.route("/sign_in/nothing/pass_please/onum.illai/done")
def hi4():
    return "Hi Fladel!"
@app.route("/sign_in/mookers/pass_please/blue/done")
def hi5():
    return "Hi Chris!"
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
@app.route("/sign_in/momosa/pass_please/chicken.o.momachicken/done/<qwerwe>")
def hello_samuel(qwerwe):
    if str(qwerwe) == "qwertyuioioioiuytrewq":
        return "Hello creator! I'm so glad to see you again!"
    else:
        return webbrowser.open('http://127.0.0.1:5000/')
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
if __name__ == "__main__":
   app.run(debug = True)