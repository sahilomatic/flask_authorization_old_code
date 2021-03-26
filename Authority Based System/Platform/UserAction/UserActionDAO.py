from helpingfunctions.HelpingFunctionsLogic import HelpingFunctionsLogic
from database.databaseConfig import CreateConnection


class UserActionDAO:
    
    def get_role_id(self,user_id,resource_id,session):
        data = session.execute('select role_id from resource_role_table where resource_id = :r and user_id =:u',{'r':resource_id , 'u': user_id}).fetchone()[0]
        return data
    
    
    def get_role_rights(self,session,role_id): 
        data = session.execute('select role_id,role,read,delete,update,create from user_action_table where user_id = :u',{'u':role_id}).fetchall()
        # fetchone() returns a tuple (a,)
        return data[0] 
    
    def get_resource_table_name(self,session,id):
        data = session.execute('select table_name from resource_table where r_id = :i',{'i':id}).fetchone()
        
        # fetchone() returns a tuple (a,)
        return data[0]
    
    def get_column_name(self,session,table_name):
        query = """SELECT column_name,data_type FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '"""+ str(table_name)+""" ORDER BY ORDINAL_POSITION"""
        
        data = [session.execute(query).fetchall()]
        '''
        fetchall() will return a list of tuple, like:
        [('a','string'),('b','decimal')]
        
        '''
        
        column = []
        data_type = []
        for i in data:
            column.append(i[0])
            data_type.append(i[1])
        
        return {'column':column , 'data_type': data_type}
    
    def get_table_rows(self,session,resource):
        query = 'select * from '+ str(resource['table_name']) 
        data = None
        if(len(resource['row_id_list'])==0):
            #print(query)
            data = session.execute(query).fetchall()
        else:
            row_id_tuple = tuple(resource['row_id_list'])
            query = query + ' where id in :l'
            #print(query)
            data = session.execute(query,{'l':row_id_tuple}).fetchall()
            
        return list(data)  
    
    
    
    
    def delete_table_data(self,session,resource):
        query = None
        if( 'drop' in resource and resource['drop'] == True):
            query = "drop table "+str(resource['table_name'])
            session.execute(query)
        else:
            if(len(resource['row_id_list'])>0):
                query = 'delete from '+ str(resource['table_name'])+' where id in :l'
                row_id_tuple = tuple(resource['row_id_list'])
                session.execute(query,{'l':row_id_tuple})
        print(query)        
                
        # Table won't get updated without below line
        session.commit()
        
    def create_table_data(self,session,resource,table_name):
        key_list = resource.keys()
        value_list = resource.values()
        dao = HelpingFunctionsLogic()
        
        
        column_string = dao.create_string_from_list(key_list)
        value_string = dao.create_string_from_list(value_list,True)
        
        query = 'insert into '+str(table_name)+column_string + 'values'+value_string
        print(query)
        
        session.execute(query)
        #Below line is important for reflecting changes in database
        session.commit()
        

if __name__ == "__main__":
    dao = UserActionDAO()
    session = CreateConnection().connect()
    '''
    l = {'id':1 ,'column2':'Sahil', 'desc' :'abc' }
    dao.create_table_data(session,l,'books')
    '''
    
    
    b = [{'resource_id' : 1,'table_name' : 'book_table',
        'row_id_list' : [1,2,3] ,'drop':False
        },
        {'resource_id' : 1,'table_name' : 'book_table','row_id_list' : []  ,'drop':True},
        {'resource_id' : 1,'row_id_list' : [1,2,3],'drop':False,'table_name' : 'book_table'}
        
        ]
    
    
    for i in b:
        #dao.delete_table_data(session,i)
        dao.get_table_rows(session,i)
        
        
        
        
        
                
                
            