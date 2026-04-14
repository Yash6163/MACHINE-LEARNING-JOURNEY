from flask import Flask,render_template 
#help to redirect to the html page
'''
it creates an instance of the Flask class
which will be the (WSGI) application
'''
####WSGI APPLICATION
app=Flask(__name__)

@app.route("/")                
def welcome():
    return render_template('index.html')

@app.route("/index")                
def index():
    return "WELCOME TO THE INDEX PAGE"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__' :
    app.run(debug=True)