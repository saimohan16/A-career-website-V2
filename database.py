# getting data from database using sql alchemy 
import sqlalchemy
import os 
# connectivity 
from sqlalchemy import create_engine,text
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('DB_key')
hello = 'str'
db_connection = f"{key}"
engine = create_engine(db_connection, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    } )
#print(sqlalchemy.__version__)



with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    #print('type of restult:', type(result))
    result_all = result.all() 
    dict_result_all = []
    for j in range(len(result_all)):
        dict_result_all.append(dict(result_all[j]))
    # print('type of result_all:', type(result_all))
    # print(type(result_all[0]))
    # print(result_all[0])
    # print(dict_result_all[0])
    
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        print('type of restult:', type(result))
        #result_all = result.all()
        jobs = []
        for j in result.all():
            jobs.append(dict(j))
    return jobs