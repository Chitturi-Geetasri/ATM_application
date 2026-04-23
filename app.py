from flask import Flask,request,redirect,url_for,render_template 
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('Welcome.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        print(request.form)
    return render_template('register.html')
app.run(use_reloader=True,debug=True)