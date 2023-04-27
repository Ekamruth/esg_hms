from flask import Flask, render_template,request,redirect,flash
from dbconnect import user_info, get_info
import hashlib

app=Flask(__name__,template_folder="htmlfiles")
@app.route("/")
def main_page():
  return render_template('esg_hms.html')

@app.route("/signup")
def signup():
  return render_template('signup.html')

@app.route("/login")
def p_login():
  return render_template('login.html')

@app.route("/acknowledgement", methods=['post'])
def acknowledge():
  info=request.form
  entered_password=info['password']
  salt='esg97'
  mix=entered_password+salt
  h=hashlib.md5(mix.encode())
  data=[]
  data=info.copy()
  data['password']=h.hexdigest()
  user_info(data)
  return render_template('acknowledgement.html', data=data)
  

@app.route("/dashboard/<user_name>",methods=['get'])
def dashboard(user_name):
  login_info=request.form
  login_password=login_info['user_entered_palsssword']
  salt='esg97'
  mix=login_password+salt
  h=hashlib.md5(mix.encode())
  login_data=[]
  login_data=login_info.copy()
  login_data['password']=h.hexdigest()
  info_user_specific=get_info('user_entered_username')
  for i in len(data):
    if login_data['user_entered_username']==info_user_specific['username'] and login_data['user_entered_password']==info_user_specific['password']:
      
      return render_template('dashboard.html')
    else:
      flash('Wrong credentials, please re-login')
      redirect("/login")
        
        
  
  
  

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)


  
