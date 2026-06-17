
### Jinja2 Template Engine
'''
{{}} expressions to print output in html

{%..%} statements for logic like if,for,while, for loops
{#..#} for comments

'''


from flask import Flask, render_template,request,redirect,url_for
'''
It creates an instance of the flask class , which will be your WSGI(Web Server Gateway Interface) application.
'''
app=Flask(__name__)


@app.route('/')
def wilecome():
    return "<html><h1>Wlecome to the flask course</h1><html>"

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/submitiapi.py',methods=['GET','POST'])
def submiti():
    if request.method=='POST':
       name=request.form['name']
       return f"Hello{name}!"
    return render_template('form.html') 

###Variable rules
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template('result.html',result=res)      
###Variable rules with dictionary
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"

    exp={'score':score,'res':res}
    return render_template('result1.html',result=exp)  
## If condition
@app.route('/successif/<int:score>')
def successif(score):
    
    
    return render_template('result.html',result=score)  

## Variable rules

@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template('result.html',result=score) 
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['Science'])
        maths=float(request.form['Maths'])
        c=float(request.form['C'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4

    return  redirect (url_for('successres',score=total_score))


if __name__=="__main__":
    app.run(debug=True)