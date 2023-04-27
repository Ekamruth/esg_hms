from sqlalchemy import create_engine,text
import os

db_con=os.environ['db_key']

engine=create_engine(db_con,connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def user_info(data):
  with engine.connect() as conn:
   
    s=("INSERT INTO users(first_name,last_name,user_name,email,password,category,line1,city,state,pincode) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(data['first_name'], data['last_name'], data['user_name'], data['email'], data['password'], data['category'], data['line1'], data['city'], data['state'], data['pincode']))
    conn.execute(text(s))

def get_info(user_name):
  with engine.connect() as conn:
    print(f'getting details of {user_name}')
    s=("SELECT * from users where user_name='%s'" %user_name)
    result=conn.execute(text(s))
    result_all=result.all()
    single_char_info=[]
    for row in result_all:
      single_char_info.append(row._mapping)
    return single_char_info[0]
  
  
  
  
