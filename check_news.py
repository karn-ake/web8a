import pymssql

server = '192.168.196.196'
user = 'thops1'
password = 'N2Nconnect123'
db = 'MDS_NEWS'


def hiddenNews(newsId):
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ Update [NEWS] SET [Visible] = 0 Where [ExternalID] = '"""+newsId+"""'"""
            cursor.execute(query)
            conn.commit()
            return queryNewsI(newsId)

def activatedNews(newsId):
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ Update MDS_NEWS.dbo.NEWS SET [Visible] = '1' Where [ExternalID] = '"""+newsId+"""'"""
            cursor.execute(query)
            conn.commit()
            return queryNewsI(newsId)

def queryNewsH(newsHeadline):
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query= """Select top 10 ExternalID, Headline, CAST(CASE WHEN Visible=0 THEN 'HIDDEN' ELSE 'ACTIVE' END as char(6)) from NEWS (NOLOCK) Where Headline like '%"""+newsHeadline+"""%'"""
            cursor.execute(query)
            return cursor.fetchall()

def queryNewsI(newsId):
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query= """Select ExternalID, Headline, CAST(CASE WHEN Visible=0 THEN 'HIDDEN' ELSE 'ACTIVE' END as char(6)) from NEWS (NOLOCK) Where ExternalID in ('"""+newsId+"""')"""
            cursor.execute(query)
            return cursor.fetchall()
            
#hiddenNews('nCTZ202107011510016975')            
print (queryNewsH('%Company Update%'))
   