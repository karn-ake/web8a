from sqlalchemy import create_engine
import pymssql

server = '192.168.170.196'
user = 'thops1'
password = 'N2Nconnect123'

def querydb(name):

    with pymssql.connect(server, user, password, "UDB2") as conn:
        with conn.cursor() as cursor:
            query = """ select * from dbo.User_Profiles where name = '"""+name+"""' """
            cursor.execute(query)
            for row in cursor:
                print(row)
    
    return cursor

querydb('adisak')

#check_db('adisak')
#check_stkinfo_update('10.141.1.52')