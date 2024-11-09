# import custom functions
from modules.helpers import get_client, get_pg_engine
from modules.extract import extract_data
from modules.load import load_to_postgres 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


query = '''
            SELECT pickup_date, vendor_id, passenger_count, trip_distance, payment_type, fare_amount
            FROM tripdata
            WHERE year(pickup_date) = 2015 AND month(pickup_date) = 1 and dayofmonth(pickup_date) = 3


'''

client = get_client()
engine = get_pg_engine()


def main():
    '''
    runs ETL pipeline to move data from CH dB to postgres DB

    parameter: None

    returns: None  

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

    print('pipeline executed successfully')

if __name__== '__main__':
    main() 
    