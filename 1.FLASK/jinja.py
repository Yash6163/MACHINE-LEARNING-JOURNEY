from flask import Flask,render_template,request 
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

##variable rule -> using jinja 2 our data is redirectred to naother website adn access and displayed ther
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score >50 : 
        res="PASSED"
    else :
        res="FAILED"

    expression={"score" :score,"res":res}
    return render_template('result.html',results=expression)
#if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result1.html',results=score)
@app.route("/submit",methods=['GET','POST']) #using get post we submit our info in the form let's say and it used and store there
def submit():
    if(request.method=='POST'):
        name=request.form['name']
        return f"HELLO {name} !"
    return render_template("form.html")

if __name__=='__main__' :
    app.run(debug=True)