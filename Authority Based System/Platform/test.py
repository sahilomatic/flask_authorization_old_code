from flask import Flask,session,request,jsonify ,render_template,session
import json
import numpy as np

from Admin.AdminLogic import AdminLogic
from Login import LoginLogic
from UserAction.UserActionLogic import UserActionLogic
app = Flask(__name__) # '.' means the current directory

@app.route('/')
def index():
   return "<html><body><h1>'Only backend is created currently.'</h1></body></html>"

@app.route('/login',methods = ['POST'])
def login():
    json_string = request.data
    obj = json.loads(json_string)
    
    user = obj['user']
    password = obj['password']
    
    user_data = LoginLogic().authenticate_user(user,password)
    if(user_data is None):
        return "<html><body><h1>'Login Fail.'</h1></body></html>"
    else:
        # Data is stored in session, at login time
        session['user'] = user
        
        session['role_id'] = user_data[1]
        session['role']  = LoginLogic().get_role(session['role_id']) 
        session['userid'] = user_data[0]
        return "<html><body><h1>'Login Successful.'</h1></body></html>"

@app.route('/logout')
def logout():
    # Data is removed from session, at logout time
    session.pop('user',None)
    session.pop('userid',None)
    session.pop('role',None)
   
    return "<html><body><h1>'Logout Successful.'</h1></body></html>"    

 
#use for changing roles of multiple user
@app.route('/assign_roles_to_user',methods = ['POST'])
def assign_roles_to_user():
    if(session['role']=='admin'):
        json_string = request.data
        obj = json.loads(json_string)
        
        user_list = obj['user_list']
        
        
        return jsonify(AdminLogic().change_user_role(user_list))
    else:
        return "<html><body><h1>'You are not authorized for role change.'</h1></body></html>"


def update_role_for_user_resource_table():
    if(session['role']=='admin'):
        json_string = request.data
        obj = json.loads(json_string)
        
        role_list = obj['role_list']
        
        
        return jsonify(AdminLogic().update_role_for_user_resource_table(role_list))
    else:
        return "<html><body><h1>'You are not authorized for role change.'</h1></body></html>"

def insert_role_for_user_resource_table():
    if(session['role']=='admin'):
        json_string = request.data
        obj = json.loads(json_string)
        
        role_list = obj['role_list']
        
        
        return jsonify(AdminLogic().insert_role_for_user_resource_table(role_list))
    else:
        return "<html><body><h1>'You are not authorized for data insertion.'</h1></body></html>"

@app.route('/change_role_action',methods = ['POST'])
def change_role_action():
    if(session['role']=='admin'):
        json_string = request.data
        obj = json.loads(json_string)
        
        role_list = obj['role_list']
        
        
        return jsonify(AdminLogic().change_role_action(role_list))
    else:
        return "<html><body><h1>'You are not authorized for role change.'</h1></body></html>"

@app.route('/read_resource_data',methods = ['POST'])
def read_resource_data():
    
        json_string = request.data
        obj = json.loads(json_string)
        resource_list = obj['resource_list']
        # Data is stored in session, at login time
        #user = session['user']
        return jsonify(UserActionLogic().read_resource_data(resource_list,session['user_id']))
    
    
    
@app.route('/create_resource_data',methods = ['POST'])
def create_resource_data():
    
        json_string = request.data
        obj = json.loads(json_string)
        resource_list = obj['resource_list']
        
        
        return jsonify(UserActionLogic().create_resource_data(resource_list,session['user_id']))
    


@app.route('/delete_resource_data',methods = ['POST'])
def delete_resource_data():
    
        json_string = request.data
        obj = json.loads(json_string)
        resource_list = obj['resource_list']
        # Data is stored in session, at login time
        
        return jsonify(UserActionLogic().delete_resource_data(resource_list,session['user_id']))
      

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000,debug = True)