from database.databaseConfig import CreateConnection
from UserAction.UserActionDAO import UserActionDAO
from helpingfunctions.HelpingFunctionsLogic import HelpingFunctionsLogic
class UserActionLogic:
    
    def get_role_rights(self,action_type,role_id):
        session = CreateConnection().connect()
        data = UserActionDAO().get_role_rights(session,role_id)
        
        '''
        data received is of following type:
        [role_id, role , read_boolean , delete_boolean , update_boolean , create_boolean ]
        '''
        action_type = action_type.lower() 
        if(action_type=="read" and data[2] == True):
            return True
        elif(action_type=="delete" and data[3] == True):
            return True    
        elif(action_type=="update" and data[4] == True):
            return True 
        elif(action_type=="create" and data[5] == True):
            return True 
        else:
            return False
        
    
    
    
    
    def read_resource_data(self,resource_list,user_id):
        """
        Data structure 
        Input:
        
        resource_list = [{'resource_id' : 1,'table_name' : 'book_table',
        'row_id_list' : [1,2,3]
        },
        {'resource_id' : 1,'table_name' : 'book_table','row_id_list' : []},
        {'resource_id' : 1,'row_id_list' : [1,2,3]}
        
        ]
        
        result_list:
        
        [
        {resource_id : 1, 'table_name': table_name,'column1':row1_column1_data ,'column2':row1_column2_data, 'column3' :row1_column3_data },
        {resource_id : 1, 'table_name': table_name,'column1':row2_column1_data ,'column2':row2_column2_data, 'column3' :row2_column3_data },
        {resource_id : 1, 'table_name': table_name,'column1':row3_column1_data ,'column2':row3_column2_data, 'column3' :row3_column3_data }
        ]
        
        """
        result_list = []
        error_bool = False
        error_list = []
        session = CreateConnection().connect()
        dao = UserActionDAO()
        for resource in resource_list:
            try:
                role_id = dao.get_role_id(user_id,resource['resource_id'],session)
                create_access = self.get_role_rights("read",role_id)
                if(create_access is False):
                    tmp_error = {}
                    tmp_error['id'] = resource['resource_id']
                    tmp_error['error'] = "User not allowed to read resource"
                    error_list.append(tmp_error)
                    continue
                    
                
                if('table_name' not in resource):
                    resource['table_name'] = dao.get_resource_table_name(resource['resource_id'])
                
                
                table_data_list = dao.get_table_rows(session,resource)
                
                table_columns_data = dao.get_column_name(session,resource['table_name'])
                table_columns_list = table_columns_data['column']
                table_columns_datatype = table_columns_data['data_type']
                # As length of column_list and table_data is same
                
                temp_dic_list = HelpingFunctionsLogic().create_dictionary(table_columns_list,table_data_list,resource['resource_id'],resource['table_name'],table_columns_datatype)
                
                result_list = result_list + temp_dic_list
                
            except Exception as e:
                tmp_error = {}
                tmp_error['id'] = resource['resource_id']
                tmp_error['error'] = str(e)
                error_list.append(tmp_error)
        
        if(len(error_list)>0):
            error_bool = True
            
        if session :
            session.close()
        
        return {'error': error_bool , 'error_list':error_list , 'result_list': result_list }        
        
    
    def delete_resource_data(self,resource_list,user_id): 
        '''
        Input data structure:
        resource_list = [{'resource_id' : 1,'table_name' : 'book_table',
        'row_id_list' : [1,2,3] ,'drop':False
        },
        {'resource_id' : 1,'table_name' : 'book_table','row_id_list' : []  ,'drop':True},
        {'resource_id' : 1,'row_id_list' : [1,2,3],'drop':False}
        
        ]  
        ''' 
        error_bool = False
        error_list = []
        session = CreateConnection().connect()
        dao = UserActionDAO()
        for resource in resource_list:
            try:
                role_id = dao.get_role_id(user_id,resource['resource_id'],session)
                create_access = self.get_role_rights("delete",role_id)
                if(create_access is False):
                    tmp_error = {}
                    tmp_error['id'] = resource['resource_id']
                    tmp_error['error'] = "'Delete access not allowed to user'"
                    error_list.append(tmp_error)
                    continue
                
                
                if('table_name' not in resource):
                    resource['table_name'] = dao.get_resource_table_name(resource['resource_id'])
                
                dao.delete_table_data(session,resource)
                
                
            except Exception as e:
                tmp_error = {}
                tmp_error['id'] = resource['resource_id']
                tmp_error['error'] = str(e)
                error_list.append(tmp_error)
        
        if(len(error_list)>0):
            error_bool = True
            
        if session :
            session.close()
        
        return {'error': error_bool , 'error_list':error_list }
    
    
    def create_resource_data(self,resource_list,user_id):
        '''
        Input Data Structure , kept same as output of read_resource_data
        resource_list = [
        {resource_id : 1, 'table_name': table_name,'column1':row1_column1_data ,'column2':row1_column2_data, 'column3' :row1_column3_data },
        {resource_id : 2, 'table_name': table_name,'column1':row2_column1_data ,'column2':row2_column2_data, 'column3' :row2_column3_data },
        {resource_id : 3, 'table_name': table_name,'column1':row3_column1_data ,'column2':row3_column2_data, 'column3' :row3_column3_data }
        ]
        
        Assumption is made that keywords are kept same as column name in table ,
        similar to data sent by read_resource_data()
        '''
        error_bool = False
        error_list = []
        session = CreateConnection().connect()
        dao = UserActionDAO()
        for resource in resource_list:
            try:
                role_id = dao.get_role_id(user_id,resource['resource_id'],session)
                create_access = self.get_role_rights("create",role_id)
                if(create_access is False):
                    tmp_error = {}
                    tmp_error['id'] = resource['resource_id']
                    tmp_error['error'] = "Create access not allowed to user"
                    error_list.append(tmp_error)
                    continue
                
                
                if('table_name' not in resource):
                    resource['table_name'] = dao.get_resource_table_name(resource['resource_id'])
                table_name = resource['table_name']
                row_id = resource['row_id']
                del resource['table_name']
                del resource['resource_id']
                del resource['row_id']
                
                dao.create_table_data(session,resource,table_name)
                
                
            except Exception as e:
                tmp_error = {}
                tmp_error['id'] = row_id
                tmp_error['error'] = str(e)
                error_list.append(tmp_error)
        
        if(len(error_list)>0):
            error_bool = True
            
        if session :
            session.close()
        
        return {'error': error_bool , 'error_list':error_list }
        
        
        
        
        
        
        