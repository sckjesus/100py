"""test Flask with this"""

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def rurout():
    return redirect('hello')

@app.route("/hello")
def hello():
    return "Enter your name where the url is after a slash(example, 127.0.0.1:5000/hello/Bob)^"

@app.route('/hello/<name>')
def helloname(name):
    return 'Hello '+name+"!"+" in the url, where the '/hello/' is, change it to '/bye/'."
  
@app.route("/bye/<name>")
def bye(name):
    return "Byebye "+name+"!"

if __name__ == '__main__':
   app.run(debug = True)

