import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from flask import Flask
#%%
engine = create_engine('sqlite:///Resources/hawaii.sqlite')
#%%
app = Flask(__name__)
#%%
print('testing')
@app.route('/')

def welcome():
    welcome = "Navigate to the routes: \n
               /api/v1.0/precipitation \n
               /api/v1.0/stations \n
               /api/v1.0/<start> \n
               /api/v1.0/<start>/<end> \n
               "
    return(welcome)

@app.route('/api/v1.0/precipitation')
def prcp():
    conn = engine.connect()
    query = f'''
        SELECT 
            date,
            AVG(prcp) as avg_prcp
        FROM
            measurement
        WHERE
            date >= (SELECT DATE(MAX(date),'-1 year') FROM measurement)
        GROUP BY
            date
        ORDER BY 
            date
    '''
    # Save the query results as a Pandas DataFrame and set the index to the date column
    prcp_df = pd.read_sql(query, conn)
    # Convert the date column to date
    prcp_df['date'] = pd.to_datetime(prcp_df['date'])
    # Sort the dataframe by date
    prcp_df.sort_values('date')
    prcp_json = prcp_df.to_json(orient='records')
    conn.close()
    return prcp_json
#%%
if __name__ == '__main__':
    app.run(debug=True)    
#%%

@app.route('/api/v1.0/stations')

def stations():
    conn = engine.connect()
    query = f'''
        SELECT  
            station,
            name
        FROM
            station
    '''
    # Save the query results as a Pandas DataFrame and set the index to the date column
    station_df = pd.read_sql(query, conn)
    station_json = station_df.to_json(orient='records')
    conn.close()
    return station_json
#%%
if __name__ == '__main__':
    app.run(debug=True) 

@app.route('/api/v1.0/tobs')

def tobs():
    conn = engine.connect()
    query = '''
        SELECT
            date,
            tobs
        FROM
            measurement
        WHERE
            date >= "2016-08-23"
            AND station = "USC00519281"
              '''
    # Save the query results as a Pandas DataFrame and set the index to the date column
    tobs_df = pd.read_sql(query, conn)
    tobs_json = tobs_df.to_json(orient='records')
    conn.close()
    return tobs_json
#%%
if __name__ == '__main__':
    app.run(debug=True)   
   

@app.route('/api/v1.0/<start>')

def start_temp():
    conn = engine.connect()
    query = f'''
        SELECT
            MIN(tobs) AS lowest_temp,
            MAX(tobs) AS highest_temp,
            AVG(tobs) AS average_temp
        FROM
            measurement
        WHERE
            date >= '{start_date}''''
    # Save the query results as a Pandas DataFrame and set the index to the date column
    start_temp_df = pd.read_sql(query, conn)
    start_temp_json = start_temp_df.to_json(orient='records')
    conn.close()
    return start_temp_json
#%%
if __name__ == '__main__':
    app.run(debug=True)   
    
@app.route('/api/v1.0/<start>/<end>')

def start_end_temp():
    conn = engine.connect()
    query = f'''
        SELECT
            MIN(tobs) AS lowest_temp,
            MAX(tobs) AS highest_temp,
            AVG(tobs) AS average_temp
        FROM
            measurement
        WHERE
            date >= '{start_date}' AND date <= '{end_date}''''
    # Save the query results as a Pandas DataFrame and set the index to the date column
    start_end_df = pd.read_sql(query, conn)
    start_end_json = start_end_df.to_json(orient='records')
    conn.close()
    return start_end_json
#%%
if __name__ == '__main__':
    app.run(debug=True)   