# import custom functions
from modules.helpers import get_client, get_postgres_engine
from modules.extract import extract_data
from modules.load import load_to_postgres 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from datetime import datetime, timedelta

client = get_client()
engine = get_postgres_engine() 

### Modification to get Max_date from the staging table(last loaded date)
Session = sessionmaker(bind=engine)
session = Session()
result = session.execute(text('select max(pickup_date) from "STG".tripdata'))
max_date = result.fetchone()[0]
session.close()


### Getting the new date
new_date = (datetime.strptime(max_date, '%Y-%m-%d')+ timedelta(days=1)).date()


query = f'''
            SELECT pickup_date, vendor_id, passenger_count, trip_distance, payment_type, fare_amount
            FROM tripdata
            WHERE pickup_date = toDate('{max_date}') + 1
            '''




def main():
    '''
    Main function to run data pipeline modules
    1. -------
    2. -------

    parameters: None

    Returns: None  
    ''' 

    # Extract the data
    extract_data(client, query)

    # Load the data to the staging
    load_to_postgres('tripdata.csv', 'tripdata', engine, 'STG')

    #excute stord procedure
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(text('CALL "STG".prc_agg_tripdata()'))
    session.commit()

    print('Stored procedure executed')

    print(f'pipeline executed successfully for {new_date}')

if __name__== '__main__':
    main() 
    