import pymssql

server = '192.168.196.26'
user = 'n2nth'
password = 'N2Nconnect123'
db = 'FMDB'

def check_db():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ Select TOP 10 * from z_astsec (NOLOCK) order by TradeDate desc"""
            cursor.execute(query)
            return cursor.fetchall()

def BP_CHART_BOT():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '14','TBONFIX,TBSWFIX,TB1MFIX,TB3MFIX,TB6MFIX,TB1YFIX' """
            cursor.execute(query)
            return "BP_CHART_BOT have already been run"

def BP_CHART_BOT1():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '17','BOTSPAVG,BOTONAVG,BOTSWAVG,BOT1MAVG,BOT3MAVG,BOT6MAVG,BOT1YAVG' """
            cursor.execute(query)
            return "BP_CHART_BOT1 have already been run"

def BP_CHART_BOT2():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '17','THORI,THORA1M,THORA3M,THORA6M,THOR' """
            cursor.execute(query)
            return "BP_CHART_BOT2 have already been run"

def BP_CHART_BOT3():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '17','BTBBON,BTBBTN,BTBBONV,BTBBTNV,BTBBONW,BTBBTNW,BTBBOC,BTBBOCW,BTBB1M,BTBB2M,BTBB3M,BTBB6M,BTBB9M,BTBB1Y,BTBB1MW,BTBB2MW,BTBB3MW,BTBB6MW,BTBB9MW,BTBB1YW,BIBOR1M,BIBOR1Y,BIBOR2M,BIBOR3M,BIBOR6M,BIBORON,BIBORSW,RPTARGET,TH1DRP,TH1DRPBL,TH1MRP,TH1MRPBL,TH2WRP,TH2WRPBL,TH7DRP,TH7DRPBL' """
            cursor.execute(query)
            return "BP_CHART_BOT3 have already been run"

def BP_CHART_BOT4():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '15','BTBADTBB,BTBADTBT,BTBBHTB,BTBBNTBB,BTBBNTBT,BTBBTTB,BTBCDTBB,BTBCDTBT,BTBCYTBB,BTBCYTBT,BTBCZTB,BTBDKTBB,BTBDKTBT,BTBEPTB,BTBEUTBB,BTBEUTBT,BTBHFTB,BTBHKTBB,BTBHKTBT,BTBI1TBB,BTBI1TBT,BTBINTBB,BTBINTBT,BTBIQTB,BTBIRTBB,BTBIRTBT,BTBISTB,BTBJ1TBB,BTBJ1TBT,BTBJDTB,BTBJYTBB,BTBJYTBT,BTBKDTB,BTBKRTB,BTBKSTB,BTBKWTB,BTBLKTB,BTBMIDR,BTBMKTB,BTBMPTB,BTBMRTBB,BTBMRTBT,BTBMVTB,BTBNKTBB,BTBNKTBT,BTBNPTB,BTBNZTBB,BTBNZTBT,BTBOMTB,BTBPGTB,BTBPKTB,BTBPPTBB,BTBPPTBT,BTBPZTB,BTBQATB,BTBRUTB,BTBSATB,BTBSDTBB,BTBSDTBT,BTBSFTBB,BTBSFTBT,BTBSKTBB,BTBSKTBT,BTBSLTB,BTBTDTB,BTBUDTB,BTBUKTBB,BTBUKTBT,BTBUSTBB,BTBUSTBT,BTBVDTB,BTBZRTB' """
            cursor.execute(query)
            return "BP_CHART_BOT4 have already been run"

def BP_CHART_BACK_DATE(stkCode,beginDate,endDate):
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_DATE '"""+stkCode+"""', '"""+beginDate+"""', '"""+endDate+"""'"""
            cursor.execute(query)
            return "BP_CHART_BACK_DATE have already been run"

def BP_CHART_ECO():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_GROUP','ECO' """
            cursor.execute(query)
            return "BP_CHART_ECO have already been run"

def BP_CHART_EOD2():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BP_CHART_EOD2' """
            cursor.execute(query)
            return "BP_CHART_EOD2 have already been run"

def BP_CHART_EXCH231():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '231','WTC' """
            cursor.execute(query)
            return "BP_CHART_EXCH231 have already been run"

def BP_CHART_EXCH232():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '232','BRT' """
            cursor.execute(query)
            return "BP_CHART_EXCH232 have already been run"

def BP_CHART_EXCHG_136():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_EXCHG','136' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_136 have already been run"

def BP_CHART_EXCHG_141():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_EXCHG','141' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_141 have already been run"

def BP_CHART_EXCHG_161():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_EXCHG','161' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_161 have already been run"

def BP_CHART_EXCHG_168():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_EXCHG','168' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_168 have already been run"

def BP_CHART_EXCHG_169():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_EXCHG','169' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_169 have already been run"

def BP_CHART_EXCHG_17():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '17','THBON1M,THBON3M,THBON6M' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_17 have already been run"

def BP_CHART_EXCHG_174():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '174' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_174 have already been run"

def BP_CHART_EXCHG_175():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '175' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_175 have already been run"

def BP_CHART_EXCHG_177():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '177' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_177 have already been run"

def BP_CHART_EXCHG_179():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '179' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_179 have already been run"

def BP_CHART_EXCHG_180():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '180' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_180 have already been run"

def BP_CHART_EXCHG_181():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '181' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_181 have already been run"

def BP_CHART_EXCHG_184():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '184' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_184 have already been run"

def BP_CHART_EXCHG_185():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '185' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_185 have already been run"

def BP_CHART_EXCHG_186():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '186' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_186 have already been run"

def BP_CHART_EXCHG_194():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '194' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_194 have already been run"

def BP_CHART_EXCHG_195():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '195' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_195 have already been run"

def BP_CHART_EXCHG_196():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '196' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_196 have already been run"

def BP_CHART_EXCHG_198():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '198' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_198 have already been run"

def BP_CHART_EXCHG_199():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '199' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_199 have already been run"

def BP_CHART_EXCHG_211():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '211' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_211 have already been run"

def BP_CHART_EXCHG_212():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '212','USDONFSR,USDSWFSR,USD1MFSR,USD2MFSR,USD3MFSR,USD6MFSR,USD1YFSR,GBPONFSR,GBPSWFSR,GBP1MFSR,GBP2MFSR,GBP3MFSR,GBP6MFSR,GBP1YFSR,EURONFSR,EURSWFSR,EUR1MFSR,EUR2MFSR,EUR3MFSR,EUR6MFSR,EUR1YFSR,CHFSNFSR,CHFSWFSR,CHF1MFSR,CHF2MFSR,CHF3MFSR,CHF6MFSR,CHF1YFSR' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_212 have already been run"

def BP_CHART_EXCHG_212_1():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '212','RUKPR' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_212_1 have already been run"

def BP_CHART_EXCHG_213():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '213','JPYSNFSR,JPYSWFSR,JPY1MFSR,JPY2MFSR,JPY3MFSR,JPY6MFSR,JPY1YFSR' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_213 have already been run"

def BP_CHART_EXCHG_213_1():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '213','RJYPR' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_213_1 have already been run"

def BP_CHART_EXCHG_215():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '215' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_215 have already been run"


def BP_CHART_EXCHG_233():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '233' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_233 have already been run"

def BP_CHART_EXCHG_241():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '241' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_241 have already been run"

def BP_CHART_EXCHG_34():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '34' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_34 have already been run"

def BP_CHART_EXCHG_35():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '35' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_35 have already been run"

def BP_CHART_EXCHG_4():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '4' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_4 have already been run"

def BP_CHART_EXCHG_62():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '62' """
            cursor.execute(query)
            return "BP_CHART_EXCHG_62 have already been run"

def BP_CHART_FOREX():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_GROUP','FOREX' """
            cursor.execute(query)
            return "BP_CHART_FOREX have already been run"

def BP_CHART_MKTCAP():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_GROUP 'MKTCAP,PER,SETV' """
            cursor.execute(query)
            return "BP_CHART_MKTCAP have already been run"

def BP_CHART_NAV():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_GROUP','NAV' """
            cursor.execute(query)
            return "BP_CHART_NAV have already been run"

def BP_CHART_NAV2_MANULITE():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_GROUP 'NAV','MN-AEPLUS-A,MN-APREIT-A,MN-APREIT-R,MN-BALANCE,MN-USBANK-A,MS-ASIAN SM,MS-ASM RMF,MS-CHINA VALUE,MS-EE EURO,MS-EUROPE-A,MS-EUROPE-D,MS-HCARE-A,MS-HCARE-D,MS-INDIA-A,MS-INDIA-D' """
            cursor.execute(query)
            return "BP_CHART_NAV2_MANULITE have already been run"

def BP_CHART_OIL():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_GROUP','OIL' """
            cursor.execute(query)
            return "BP_CHART_OIL have already been run"

def BP_CHART_SETTSUM():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_GROUP 'SETINDEX','SETV9,SETVCB,SETVCS,SETVFB,SETVFS,SETVIB,SETVIS,SETVPB,SETVPS,MAIV,MAIVCB,MAIVCS,MAIVFB,MAIVFS,MAIVIB,MAIVIS,MAIVPB,MAIVPS' """
            cursor.execute(query)
            return "BP_CHART_SETTSUM have already been run"

def BP_CHART_STOCKSTAT1():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_GROUP 'STOCKDY,STOCKEPS,STOCKMC,STOCKPB' """
            cursor.execute(query)
            return "BP_CHART_STOCKSTAT1 have already been run"

def BP_CHART_STOCKSTAT2():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_GROUP 'STOCKPE,STOCKV' """
            cursor.execute(query)
            return "BP_CHART_STOCKSTAT2 have already been run"

def BP_CHART_T0100():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BP_CHART_T0100' """
            cursor.execute(query)
            return "BP_CHART_T0100 have already been run"

def BP_CHART_T0630():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BP_CHART_T0630' """
            cursor.execute(query)
            return "BP_CHART_T0630 have already been run"

def BP_CHART_T1010():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BP_CHART_T1010' """
            cursor.execute(query)
            return "BP_CHART_T1010 have already been run"

def BP_CHART_ThaiGOLD():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART_BY_SYMBOLS_EXCHG '7','GTAGB,GTAGO' """
            cursor.execute(query)
            return "BP_CHART_ThaiGOLD have already been run"

def BP_CHART_WARRANT():
    with pymssql.connect(server, user, password, db) as conn:
        with conn.cursor() as cursor:
            query = """ BP_CHART 'BY_GROUP','WARRANT' """
            cursor.execute(query)
            return "BP_CHART_WARRANT have already been run"
            
BP_CHART_BACK_DATE('CCI,M1,M2,NSERVICE,PCI,TISI,TISI(E),TRADEBAL,TTBFD','2020-01-01','2021-05-31')
