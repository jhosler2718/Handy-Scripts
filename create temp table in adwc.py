# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 07:16:49 2020

@author: jason.hosler
"""
import cx_Oracle
import pandas as pd
import numpy as np
import dateutil
from datetime import datetime
from dateutil.parser import parse
from datetime import date

from cryptography.fernet import Fernet
with open('S:\Risk\Data Science\Jason\Python Work\codes\Key.bin', 'rb') as keyfile_object:
    for line in keyfile_object:
        key = line

cipher_suite = Fernet(key)
with open('S:\Risk\Data Science\Jason\Python Work\codes\pwd_bytes.bin', 'rb') as pwdfile_object:
    for line in pwdfile_object:
        pwdadwc = line
uncipher_text = (cipher_suite.decrypt(pwdadwc))
text_pwdadwc = bytes(uncipher_text).decode("utf-8") #convert to string

usr = "Jason_Hosler"
tns = "adwce19c_medium"


#GENERATE LIST OF MY TABLES
adwc = cx_Oracle.connect(usr, text_pwdadwc, tns)
my_table_list = pd.read_sql("select OWNER, TABLE_NAME from all_tables where OWNER = 'JASON_HOSLER'", con=adwc)
adwc.close()



#clear out the test table in case it is there
connection = cx_Oracle.connect(usr, text_pwdadwc, tns)
# Obtain a cursor
cursor = connection.cursor()
# Execute the query
sql = """drop table JASON_HOSLER.TEST_JH_TBL"""
cursor.execute(sql)
connection.close()


# Establish the database connection
connection = cx_Oracle.connect(usr, text_pwdadwc, tns)
# Obtain a cursor
cursor = connection.cursor()
# Execute the query creating a table in my schema
sql = """create table test_jh_tbl as select
                   to_char(tran_date,'YYYY') as year
                   ,to_char(tran_date,'MM') as month
                   ,count(txn_uid) as txn_count
                   ,sum(tran_amount) as txn_dollars
                   ,sum(case when auth_ind = 'A' then tran_amount else 0 end) as approve_dollars
                   ,sum(case when auth_ind = 'A' then clm_check_amt else 0 end) as claim_dollars
                   ,sum(case when auth_ind = 'A' then clm_salvage_amt else 0 end) as salvage_dollars

       from adwcprod_owner.V_WE_TXNLOGS   

        where tran_date between '01-SEP-2020' and '30-NOV-2020'
        and chain = 115546
        group by to_char(tran_date,'YYYY')
                   ,to_char(tran_date,'MM')"""
cursor.execute(sql)
connection.close()


#QUERY MY TEST TABLE
adwc = cx_Oracle.connect(usr, text_pwdadwc, tns)
    
dg_txn_vol = pd.read_sql("""select *                  
       from JASON_HOSLER.TEST_JH_TBL                     
        """, con=adwc)        
    
adwc.close()


#now delete the test table in my schema
connection = cx_Oracle.connect(usr, text_pwdadwc, tns)
# Obtain a cursor
cursor = connection.cursor()
# Execute the query
sql = """drop table JASON_HOSLER.TEST_JH_TBL"""
cursor.execute(sql)
connection.close()





#now load the test table I doownloaded into my temp space

#first make sure it is not already there, if so drop it
connection = cx_Oracle.connect(usr, text_pwdadwc, tns)
# Obtain a cursor
cursor = connection.cursor()
# Execute the query
sql = """drop table JASON_HOSLER.TEST_LOAD"""
cursor.execute(sql)
connection.close()



#the laod from the python local space to my schema
from sqlalchemy import types, create_engine
upload_conn = create_engine('oracle+cx_oracle://%s:%s@%s' % (usr, text_pwdadwc, tns), max_identifier_length=128)
dg_txn_vol.to_sql('TEST_LOAD', upload_conn, if_exists='replace')


#now download the table to test that it is really there
adwc = cx_Oracle.connect(usr, text_pwdadwc, tns)
    
dg_txn_vol_b = pd.read_sql("""select *                  
       from JASON_HOSLER.TEST_LOAD                     
        """, con=adwc)        
    
adwc.close()


#clear out the test table, end of exercise
connection = cx_Oracle.connect(usr, text_pwdadwc, tns)
# Obtain a cursor
cursor = connection.cursor()
# Execute the query
sql = """drop table JASON_HOSLER.TEST_LOAD"""
cursor.execute(sql)
connection.close()







