class HelpingFunctionsLogic:
    def is_number_repl_isdigit(self,s):
        """ Returns True is string is a number. """
        return str(s).replace('.','',1).isdigit()
    
    
    def create_dictionary(self,column_list,data_list,resource_id,table_name,table_columns_datatype = None):
        """
        example:
        column_list = ['column1','column2','column3']
        data_list = [('row1_column1_data','row1_column2_data','row1_column3_data'),
        ('row2_column1_data','row2_column2_data','row2_column3_data'),
        ('row3_column1_data','row3_column2_data','row3_column3_data')]
        
        output_list = [
        {resource_id : 1, 'table_name': table_name,'column1':row1_column1_data ,'column2':row1_column2_data, 'column3' :row1_column3_data },
        {resource_id : 1, 'table_name': table_name,'column1':row2_column1_data ,'column2':row2_column2_data, 'column3' :row2_column3_data },
        {resource_id : 1, 'table_name': table_name,'column1':row3_column1_data ,'column2':row3_column2_data, 'column3' :row3_column3_data }
        ]
        
        """
        
        output_list = []
        for row in data_list:
            temp_dic = {}
            temp_dic['resource_id'] = resource_id
            temp_dic['table_name'] = table_name
            for col in range(0,len(column_list)):
                if(table_columns_datatype is not None and table_columns_datatype[col] == 'decimal'):
                    # This line is added because if data type is decimal then we get decimal(4.5) type of data from PostgreSql.
                    #And front end framework might find it difficult to display. 
                    temp_dic[column_list[col]] = float(row[col])
                else:   
                    temp_dic[column_list[col]] = row[col]
                
            output_list.append(temp_dic)
    
        return output_list
    
    
    
    
    def create_string_from_list(self,list,value=None):
        s = "("
        if(value):
            'string for value data'
            for i in range(0,len(list)):
                is_digit = self.is_number_repl_isdigit(list[i])
                if(is_digit):
                    if(i == len(list)-1):
                        s = s+str(list[i]) 
                    else:
                        s = s+str(list[i])+","
                        
                else:
                    if(i == len(list)-1):
                        s = s+"'"+str(list[i])+"'" 
                    else:
                        s = s+"'"+str(list[i])+"',"    
                    
                
                
                
                
            
        else:    
            for i in range(0,len(list)):
                if(i == len(list)-1):
                    s = s+str(list[i]) 
                else:
                    s = s+str(list[i])+","
                    
        s = s+')'
        
        return s
    
if __name__ == "__main__":
    dao = HelpingFunctionsLogic()
    #print(dao.create_string_from_list([1, 3, 2],True))
    column_list = ['column1','column2','column3']
    data_list = [('row1_column1_data','row1_column2_data','row1_column3_data'),
        ('row2_column1_data','row2_column2_data','row2_column3_data'),
        ('row3_column1_data','row3_column2_data','row3_column3_data')]
    print(dao.create_dictionary(column_list,data_list,1,'abc_table'))
            