import pandas as pd

def load_to_postgres(csv_file_path, table_name, engine, schema):
    '''
    load data from a csv file to postgres DB table

    parameter:
        - csv_file_path(str): path to the csv file
        - table (str): a postgres db table
        - engine (sqlalchemy.engine.Engine): a SQLalchemy engine object
        - schema(str): a posgres DB schema

        Return: None
        '''
    
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name,con=engine, if_exists='replace', index=False, schema=schema)
    
    print(f"{len(df)} successfully loaded to staging")



