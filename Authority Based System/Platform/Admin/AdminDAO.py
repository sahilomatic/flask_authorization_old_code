from database.databaseConfig import CreateConnection
class AdminDAO:
    def authenticate_user(self,username,session,action_type): 
        data = session.execute('select username,role from user_table where lower(username) = :u',{'u':username.lower()}).fetchall()
        print(username)
        if(action_type is None):
            if(data is None):
                return False
            else:
                if(len(data)>0):
                    return True
        else:
            return data[0]    
    
    def update_roles(self,user_data,session):
        
        session.execute('''UPDATE user_table SET role_id = :r 
                    WHERE username = :u and user_id = :id''',{'u':user_data['user'],
                                                        'id':user_data['user_id'], 
                                                        'r':user_data['role_id'],
                                                        
                                                         })
        
        "Updates won't reflect in database without below statement"
        session.commit()
        
        
    def update_roles_Action(self,role_data,session):
        
        session.execute('''UPDATE role_action_table SET read = :r, update = :u,create = :c, delete = :d 
                    WHERE  role_id = :id''',{'u':role_data['user'],
                                                        'id':role_data['role_id'], 
                                                        'r':role_data['read'],
                                                        'u':role_data['update'],
                                                        'c':role_data['create'],
                                                        'd':role_data['delete']
                                                         })
        
        "Updates won't reflect in database without below statement"
        session.commit()
        
    
    def update_role_for_user_resource_table(self,role_data,session): 
        session.execute('''UPDATE resource_role_table SET role_id = :r
                    WHERE  resource_id = :rid and user_id = :uid''',{'r':role_data['role_id'],
                                                        'rid':role_data['resource_id'], 
                                                        'uid': role_data['user_id']
                                                        
                                                         })
        
        "Updates won't reflect in database without below statement"
        session.commit() 
        
    def insert_role_for_user_resource_table(self,role_data,session): 
        session.execute('''insert into resource_role_table values(:r,:uid,:rid)''',{'r':role_data['role_id'],
                                                        'rid':role_data['resource_id'], 
                                                        'uid': role_data['user_id']
                                                        
                                                         })
        
        "Updates won't reflect in database without below statement"
        session.commit()  
        
        
if __name__ == "__main__":
    dao = AdminDAO()
    l = [{'user':'Rajesh','read':True,'write':False,'delete': False , 'id':1},
         {'user':'Tonny','read':True,'write':True,'delete': False , 'id':2},
         {'user':'Rohit','read':True,'write':True,'delete': True , 'id':3}]
    session = CreateConnection().connect()
    for i in l:
        dao.authenticate_user(i['user'],session,None)