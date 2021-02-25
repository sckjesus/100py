import time
import os
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

HOME_HTML = """
    <html><body>
        <h2>Welcome to my app!</h2>
        <form action="/">
            What's your username?: <input type='text' name='username'><br>
            <input type='submit' value='Continue'>
        <h2>https://localhost/cool</h2>    
        </form>
    </body></html>"""
g_HTML = """
    <html><body>
        <h2>Welcome to my app!</h2>
        <form action="/cool">
            What's your password?: <input type='text' name='favfood'><br>
            <input type='submit' value='Continue'>
        </form>
    </body></html>"""

def mungusaser():
    print("Loading...")
    time.sleep(5)
    os.system('cls')
    return HOME_HTML
    a=request.args.get["username"]
    c=["sanitha", "grapesK", "momosa", "nothing", "mookers" ]
    d=["bookman.kaspar/bookgen", "book.com", "seetha.o/momaseetha", "onum/illai", "blue"]
    if str(a) in c:
        print("https://localhost/cool")
        return g_HTML.format()
    else:
        return("I don't know you, try again")
        mungusaser()
        
def qwerty():
    if str(a)==c[0]:
        return g_HTML
        b=request.args.get["password"]
    elif str(a)==c[1]:
        return g_HTML
        b=request.args.get["password"]
    elif str(a)==c[2]:
        return g_HTML
        b=request.args.get["password"]
    elif str(a)==c[3]:
        return g_HTML
        b=request.args.get["password"]
    elif str(a)==c[4]:
        return g_HTML
        b=request.args.get["password"]
    if str(b) in d:
        return("Welcome "+str(a.capitalize())+"!")
    else:
        return("Try again")
        mungusaser()



@app.route("/")
def google():
    return mungusaser()
@app.route("/cool")
def googly():
    return qwerty()


    


if __name__ == '__main__':
    app.run()