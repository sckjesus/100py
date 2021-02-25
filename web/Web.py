from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
    a=request.args.get["username"]
    c=["sanitha", "grapesK", "momosa", "nothing", "mookers" ]
    d=["bookman.kaspar/bookgen", "book.com", "seetha.o/momaseetha", "onum/illai", "blue"]
    if str(a) in c:
        print("https://localhost/about")
        return render_template("about.html")
    else:
        return("I don't know you, try again")

@app.route("/about")
def about():
    #a=request.args.get["username"]
    return render_template("about.html")
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


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

if __name__ == "__main__":
    app.run(debug=True)