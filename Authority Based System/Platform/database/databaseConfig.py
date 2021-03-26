from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class CreateConnection:
    def connect(self):
        engine = create_engine('postgresql://username:password@database_instance:port_number/database_name')    
        
        Session = sessionmaker(bind=engine)
        
        session = Session()
        
        
        return session
    
    
if __name__ == "__main__":
    dao =  CreateConnection()
    dao.connect()    

