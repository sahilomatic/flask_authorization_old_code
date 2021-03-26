from database.databaseConfig import CreateConnection
from Admin.AdminDAO import AdminDAO
class AdminLogic:
    def change_user_role(self,user_list):
        '''
        Assumption is made that user_list is a list of dictionary,
        which contain username and foreign key role_id from role_action_table
        for example:
        [{'user':'Rajesh','role_id':2 , 'user_id':1},
         {'user':'Tonny','role_id':1 , 'user_id':2},
         {'user':'Rohit','role_id':3 , 'user_id':3}]
        
        '''
        'single object created to avoid redundant statement'
        dao = AdminDAO()
        
        '''single session object created as database connection is time consuming task
        and should be kept minimum'''
        session = CreateConnection().connect()
        error_list = []
        error_bool = False
        for i in user_list: 
            temp_error = {}
            temp_error['user'] = i['user']
            temp_error['user_id'] = i['user_id']
            user_found = dao.authenticate_user(i['user'],session,None)
            if(user_found==False):
                temp_error['error'] = 'User not found in database.'
                error_list.append(temp_error)
            elif(user_found):
                try:
                    dao.update_roles(i,session)   
                except Exception as e:
                    temp_error['error'] = str(e)
                    error_list.append(temp_error)
                    continue
        if(len(error_list)>0):
            error_bool = True
        
        if session:
            session.close()
        return {'ERROR': error_bool , 'error_list': error_list}
    
    
    def change_role_action(self,role_list):
        '''
        Assumption is made that role_list is a list of dictionary,
        which contain role_id and  read, write ,delete action boolean values
        for example:
        [{'role_list':1,'read':True,'write':False,'delete': False , },
         {'role_list':2,'read':True,'write':True,'delete': False , },
         {'role_list':3,'read':True,'write':True,'delete': True }]
        
        '''
        'single object created to avoid redundant statement'
        dao = AdminDAO()
        
        '''single session object created as database connection is time consuming task
        and should be kept minimum'''
        session = CreateConnection().connect()
        error_list = []
        error_bool = False
        for i in role_list:
            temp_error = {}
            temp_error['role_id'] = i['role_id']
            try:
                dao.update_roles(i,session)   
            except Exception as e:
                temp_error['error'] = str(e)
                error_list.append(temp_error)
                continue
        if(len(error_list)>0):
            error_bool = True
        
        if session:
            session.close()
        return {'ERROR': error_bool , 'error_list': error_list}
    
    
    def update_role_for_user_resource_table(self,role_list):
        '''
        Assumption is made that role_list is a list of dictionary,
        which contain  foreign key resource_id,role_id,user_id from role_action_table
        for example:
        [{'resource_id':3,'role_id':2 , 'user_id':1, 'user':'Rajesh'},
         {'resource_id':2,'role_id':1 , 'user_id':2 , 'user':'Tonny'},
         {'resource_id':1,'role_id':3 , 'user_id':3, 'user':'Rohit'}]
        
        '''
        'single object created to avoid redundant statement'
        dao = AdminDAO()
        
        '''single session object created as database connection is time consuming task
        and should be kept minimum'''
        session = CreateConnection().connect()
        error_list = []
        error_bool = False
        for i in role_list: 
            temp_error = {}
            temp_error['user'] = i['user']
            temp_error['user_id'] = i['user_id']
            user_found = dao.authenticate_user(i['user'],session,None)
            if(user_found==False):
                temp_error['error'] = 'User not found in database.'
                error_list.append(temp_error)
            elif(user_found):
                try:
                    dao.update_role_for_user_resource_table(i,session)   
                except Exception as e:
                    temp_error['error'] = str(e)
                    error_list.append(temp_error)
                    continue
        if(len(error_list)>0):
            error_bool = True
        
        if session:
            session.close()
        return {'ERROR': error_bool , 'error_list': error_list}
    
    
    def insert_role_for_user_resource_table(self,role_list):
        '''
        Assumption is made that role_list is a list of dictionary,
        which contain  foreign key resource_id,role_id,user_id from role_action_table
        for example:
        [{'resource_id':3,'role_id':2 , 'user_id':1, 'user':'Rajesh'},
         {'resource_id':2,'role_id':1 , 'user_id':2 , 'user':'Tonny'},
         {'resource_id':1,'role_id':3 , 'user_id':3, 'user':'Rohit'}]
        
        '''
        'single object created to avoid redundant statement'
        dao = AdminDAO()
        
        '''single session object created as database connection is time consuming task
        and should be kept minimum'''
        session = CreateConnection().connect()
        error_list = []
        error_bool = False
        for i in role_list: 
            temp_error = {}
            temp_error['user'] = i['user']
            temp_error['user_id'] = i['user_id']
            user_found = dao.authenticate_user(i['user'],session,None)
            if(user_found==False):
                temp_error['error'] = 'User not found in database.'
                error_list.append(temp_error)
            elif(user_found):
                try:
                    dao.insert_role_for_user_resource_table(i,session)   
                except Exception as e:
                    temp_error['error'] = str(e)
                    error_list.append(temp_error)
                    continue
        if(len(error_list)>0):
            error_bool = True
        
        if session:
            session.close()
        return {'ERROR': error_bool , 'error_list': error_list}
            
        
    
if __name__ == "__main__":
    dao = AdminLogic()
    l = [{'user':'Rajesh','read':True,'write':False,'delete': False , 'id':1},
         {'user':'Tonny','read':True,'write':True,'delete': False , 'id':2},
         {'user':'Rohit','read':True,'write':True,'delete': True , 'id':3},
         {'user':'Ronny','read':True,'write':True,'delete': True , 'id':3}]
    print(dao.change_user_action_type(l))
