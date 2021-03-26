Authority based System

- Kindly read test.py file as certain decision making statements are written during API request.
  Commonly used data like user_id , role , role_id is stored in session(which is like cache type object in Flask) to avoid redundant database requests.

Packages

- database   : Contains classes for making connection with database
- Admin      : Contains classes and function which can only be called by 'admin' role.
- UserAction : Contains classes and function for performing actions based on different roles.
- UserAction : Contains classes and function for performing actions based on different roles.
- helpingfunctions : Contains commonly used functions.



Database Structure

- table_name : user_table

			
			user_id  		username  		password  		role_id
			(primary_key)	 	(primary_key)		(Not null)		(foreign_key)	
			
			1			sahil				abc123			2
			2			rahul				abc123			2
			3			rahul2				xyz123			1
			
- table_name : role_action_table

			
			role_id  		role  			read		delete 		create 		update  			
			(primary_key)		(Not null)		(boolean)	(boolean)     (boolean)   	(boolean)	
			
			1				admin		True	           True        True               True
			2				sme		True                             True             True
			3				engineer	True               False									

- table_name : resource_role_table

One user can serve different roles for different resources.
			
			id  		        role_id		            user_id		      resource_id
			(primary_key)	 	(foreign_key)		   (foreign_key)		(foreign_key)	
			(serial)                (role_action_table)         (user_table)                (resource_table)
			1			1				3			  1
			2			1				3			  2
			3			2				1			  2




- table_name : resource_table

			
			r_id  			type  			description  		table_name
			(primary_key)	   	(varchar)		(varchar)		(varchar)(Not Null)	
			
			1			book			abc				book_table
			2			car							 car_table
			3			toy			yz123			 	toy_table
			
			
- Different resource table can have different number of columns and different column_name except id column for all of them is row_id.
  Dynamic queries are written to change according to different tables. Following is table example of different tables.
  
- table_name : book_table

			
			row_id  			type  			author  		     book_name
			(primary_key)	(varchar)		(varchar)			              (varchar)	
			
			1				book			Chetan Bhagat			'5 points some thing'
			2				book							         'Art of war'
			
- table_name : car_table

			
			row_id  			type  			company  		     model          manufacturing_cost    geography_tax    
			(primary_key)	             (varchar)		          (varchar)	          (varchar)		(decimal)	 (decimal)
			
			1				car				maruti		    baleno				
			2				car				hyundai	             i20
			 
Alternative for this is to keep all data in one table for different resources, which would like:

			id               resource_id             variable_name             default_value               type              unique_code
			primary_key	(foreign key)             (varchar)                  (varchar)
                                         (resource_table)

                        1                 1                         author                   "Chetan Bhagat"            "book"              abc1

                        2                 1                         book_name                 "5 points some thing"     "book"              abc1
                        3                 1                         book_name                 "Art of war"               "book"              abc2
                        4                 1                         author                                               "book"              abc2
                        5                 2                         company                    "maruti"                  "car"               abc3
                        6                 2                         model                      "baleno"                  "car"               abc3
                        7                 2                         manufacturing_cost          205.5                    "car"               abc3

But in this kind of database we have to use more number of for loops for processing data and it is also difficult to read manually.
I have used proper condition in UserActionLogic for proper role-action authentication and dynamic queries are made in UserActionDAO to deal with all kind of tables.
provided keys in dictionary are same as column_name , This is handled during read_data function.
                        
			 
  
  