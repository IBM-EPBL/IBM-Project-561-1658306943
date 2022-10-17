from flask import Flask, redirect, url_for, request app = Flask(_name) @app.route('/success/<name>') 
def success(name):
return 'welcome %s' % name @app.route('/login',methods = ['POST', 'GET']) 
def login(): 
if request.method == 'POST': user = request.form['nm'] 
return redirect(url_for('success',name = user))
else: user = request.args.get('nm') 
return redirect(url_for('success',name = user)) 
if __name_ == '_main_': app.run(debug = True)