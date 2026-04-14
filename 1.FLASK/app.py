from flask import Flask
'''
it creates an instance of the Flask class
which will be the (WSGI) application
'''
####WSGI APPLICATION
app=Flask(__name__)

@app.route("/")                
def welcome():
    return "welcome to this flask course. This should be an mazing course"

@app.route("/index")                
def index():
    return "welcome to the index page"

if __name__=='__main__' :
    app.run(debug=True)