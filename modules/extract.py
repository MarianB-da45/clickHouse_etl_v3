import pandas as pd


def extract_data (client, query):
    '''
    executes a SQL query on a clickhouse DB, retrieves the results and saves to a csv file

    Parameters:
        - Client(Clickhouse_connect.Client): an action CH client instance
        - query(str):A valid SQL select query

    Returns: None

     '''
    
    result = client.query(query)
    rows = result.result_rows
    cols = result.column_names

    client.close()

    # write to a pandas DF
    df = pd.DataFrame(rows, columns = cols)
    df.to_csv('tripdata.csv', index=False)

    print(f"len{df}) rows extracted successfully")