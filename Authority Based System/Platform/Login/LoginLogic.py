from database.databaseConfig import CreateConnection

class LoginLogic:
    def authenticate_user(self,username,password): 
       
            session = CreateConnection().connect()
           
            data = session.execute('select userid,role_id from user_table where lower(username) = :u and password = :p',{'u':username.lower() , 'p':password}).fetchone()
            if(data is None):
                return None
            else:
                if(len(data)>0):
                    return data[0]
                
                
    def get_role(self,role_id):
        session = CreateConnection().connect()
        data = session.execute('select role from role_action_table where role_id = :r',{'r':role_id}).fetchone()[0]
        return data   
    
     
        
if __name__ == "__main__":
    dao = LoginLogic()
    print(dao.authenticate_user('rajesh','xyz'))