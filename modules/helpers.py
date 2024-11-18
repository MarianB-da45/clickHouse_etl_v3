import clickhouse_connect
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(override=True)

def get_client():
    '''
    connect to a clikhouse database using parameters from an .env file
    
    parameter: None

    Returns:
        - Clickhouse_connect.Client: a database client object

        '''
    ## Getting credentials
    host = os.getenv('ch_host')
    username = os.getenv('ch_user')
    password = os.getenv('ch_password')
    port = os.getenv('ch_port')

    ## Getting DB client
    client = clickhouse_connect.get_client(host=host, port=port, username=username, password=password, secure=True)

    return client



def get_postgres_engine():
    '''
    get a  SQLalchemy engine object for postgres DB using parameters in a .env file
        
    Parameter: None

    Returns:
        - SQLALchemy engine (sqlalchemy.engine.Engine)
        
    '''
    engine = create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
                            user = os.getenv('pg_user'),
                            password = os.getenv('pg_password'),
                            host = os.getenv('pg_host'),
                            port = os.getenv('pg_port'), 
                            dbname = os.getenv('pg_dbname')
                                )                                   
                        )
    return engine        
                            

