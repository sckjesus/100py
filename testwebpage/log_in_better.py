from flask import Flask, redirect, url_for, render_template, request
import webbrowser

app = Flask(__name__)
username=request("username", render_template("user.html"))
listofusers=["sanitha","grapesK","momosa","nothing","mookers"]
listofpasses=["bookman.kaspar.bookgen", "book.com", "chicken.o.momachicken", "onum.illai", "blue"]
@app.route("/")
def nothin():
    return render_template("user.html")
#---------------------------------------------------------------------------------------
@app.route("/sign_in",methods = ['POST', 'GET'])
def tell_them():
    if request.method == 'POST':
        username = request.form['username']
        return redirect("http://127.0.0.1:5000/sign_in/"+str(username))
    else:
        username = request.args.get('username')
        return redirect("http://127.0.0.1:5000/sign_in/"+str(username))

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
    return render_template("pass.html")

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
@app.route("/nothing/nothing",methods = ['POST', 'GET'])
def ooh():
    if request.method == 'POST':
        password = request.form['password']
        return redirect("http://127.0.0.1:5000/sign_in/sanitha/pass_please/"+str(password))
    else:
        password = request.args.get('password')
        return redirect("http://127.0.0.1:5000/sign_in/sanitha/pass_please"+str(password))
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
@app.route("/sign_in/<username>/pass_please/<passwerdd>")
def passcheck(passwerdd,username):
    if str(passwerdd) in listofpasses:
        if str(username) in listofusers:
            return redirect("/sign_in/"+username+"/pass_please/"+passwerdd)
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