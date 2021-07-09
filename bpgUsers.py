import pymssql

#BPG DB configureation
server1 = '192.168.170.81'
userName1 = 'thops1'
password1 = 'N2Nconnect123'
dbName1 = 'EBCGF'

def queryUsersStatus(status):
    with pymssql.connect(server1, userName1, password1, dbName1) as conn:
        with conn.cursor() as cursor:
            query = """ SELECT LoginID, [Status], CliCode,ActiveDate,Email,PwdExpiryDate FROM MF_CliInfo WHERE [Status] = '"""+status+"""' """
            cursor.execute(query)
            return cursor.fetchall()

def readAccountsFromFile():
    with open('E:\\Scripts\\uploads\\users.txt','r') as users:
        return "','".join(users.read().splitlines())

def queryUsersSuspensebyAccount():
    accounts = readAccountsFromFile()
    #print(accounts)
    #print(query)
    with pymssql.connect(server1, userName1, password1, dbName1) as conn:
        with conn.cursor() as cursor:        
            query = """ SELECT LoginID, [Status], CliCode,ActiveDate,Email,PwdExpiryDate FROM MF_CliInfo WHERE [Status] = 'S' AND LoginID in ('"""+accounts+"""') """
            cursor.execute(query)
            return cursor.fetchall()

def suspenseUsersbyAccount():
    accounts = readAccountsFromFile()
    with pymssql.connect(server1, userName1, password1, dbName1) as conn:
        with conn.cursor() as cursor:
            updateAccounts = """ UPDATE MF_CliInfo SET [Status] = 'S' WHERE LoginID in ('"""+accounts+"""') """
            cursor.execute(updateAccounts)
            conn.commit()
            return "Accounts have already been suspensed"
#print(queryUsersStatus('s'))
#print(readAccountsFromFile())
#print(queryUsersSuspensebyAccount())
#print(suspenseUsersbyAccount())