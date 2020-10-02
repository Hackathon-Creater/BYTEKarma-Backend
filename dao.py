from datetime import datetime
from random import randint
import pandas as pd
import cx_Oracle
import db_config
import care_package_assigner as c
import column_transposer as t
import json

def open_connection():
    try:
        global conn
        conn = cx_Oracle.connect(db_config.getConnectionString())
        
    except Exception as e:
        conn = str(e)
    

def save(df):
    
    open_connection()
    
    try:   
        
        if(type(conn).__name__ != 'str'):
            globalCur = conn.cursor()
            listOfPods=[]
            i=1
            for index,row in df.iterrows():
        
                cont_cust=0
                if(row['POD']>=0.5):
                    cont_cust = randint(0,1)                
                new=[]
                new.append(int(row['CIF']))
                new.append(row['POD'])
                new.append(row['Gambling'])
                new.append(row['Amazon'])
                new.append(row['Shopping'])
                new.append(row['Food'])
                new.append(row['Movie'])  
                new.append(row['CC_Bill'])
                new.append(cont_cust)  
                new.append(datetime.now())
                
                sql="select * from global_table where cif = :cif order by transaction_date asc"
                
                globalCur.execute(sql,cif=int(row['CIF']))
        
                cifData=[]
                
                for x in globalCur.fetchall():
                    cifData.append(list(x))
                    
                new.append(c.getCarePackages(t.transposeCifData(cifData)))
                new.append(row['Loan_return'])
                new.append(row['Spend_to_income'])
                new.append(row['Total_income'])
                print(i)
                i+=1
                listOfPods.append(tuple(new)) 
        
            open_connection()
            globalCur = conn.cursor()
            sql = "INSERT INTO PD_TABLE (cif,pod,gambling,amazon,shopping,food,movie,cc_bill,customer_contacted,create_date,CARE_PACKAGE_ASSIGNED,LOAN_RETURN,SPEND_INC_RATIO,TOTAL_INCOME) VALUES (:cif,:pod,:gambling,:amazon,:shopping,:food,:movie,:cc_bill,:customer_contacted,:create_date,:CARE_PACKAGE_ASSIGNED,:Loan_return,:Spend_to_income,:Total_income)"
            print("UPLOAD POD DATA STARTED...")    
            globalCur.executemany(sql,listOfPods)
            globalCur.close()
            conn.commit()
            conn.close()
            print("UPLOAD POD DATA DONE...")
            return "success"

        else:
            return "failed : " + conn

    except Exception as e:
        return "failed : " + str(e)

def search(searchRequestObject):
    
    open_connection()
    
    try:    
        cur = conn.cursor()
        if(type(conn).__name__ != 'str'):
            searchQuery = 'SELECT * FROM v_full_info WHERE '
            
            if searchRequestObject.cif != None:
                whereClause = " cif = " + str(searchRequestObject.cif) + " AND " 
                searchQuery += whereClause
                
            if searchRequestObject.transactionType != None:
                whereClause = " UPPER(summary_of_transaction) LIKE '%" + str(searchRequestObject.transactionType).upper() + "%' AND " 
                searchQuery += whereClause
                
            if searchRequestObject.accountNumber != None:
                whereClause = " account_number = " + str(searchRequestObject.accountNumber) + " AND " 
                searchQuery += whereClause
                
            if searchRequestObject.accountType != None:
                whereClause = " UPPER(accountType) LIKE '%" + str(searchRequestObject.accountType).upper() + " AND " 
                searchQuery += whereClause
                
            if searchRequestObject.city != None:
                whereClause = " upper(it.city) IN ( " + (', '.join('"' + item.upper() + '"' for item in searchRequestObject.city)) + " ) AND " 
                searchQuery += whereClause
                
            if searchRequestObject.country != None:
                whereClause = " upper(it.country) IN (" + (', '.join('"' + item.upper() + '"' for item in searchRequestObject.country)) + " ) AND " 
                print(whereClause)
                searchQuery += whereClause
                
            if searchRequestObject.gender != None:
                whereClause = " it.gender = '" + str(searchRequestObject.gender) + "' AND " 
                searchQuery += whereClause
                
            if searchRequestObject.name != None:
                whereClause = " upper(it.name) LIKE '%" + str(searchRequestObject.name).upper() + "%' AND " 
                searchQuery += whereClause
                
            if searchRequestObject.region != None:
                whereClause = " upper(it.region) IN ( " + (', '.join('"' + item.upper() + '"' for item in searchRequestObject.region)) + ") AND " 
                searchQuery += whereClause
                
            if searchRequestObject.state != None:
                whereClause = "  upper(it.state) IN (" + (', '.join('"' + item.upper() + '"' for item in searchRequestObject.state)) + ") AND " 
                searchQuery += whereClause
                
            searchQuery = searchQuery[:-4]      
            
            cur.execute(searchQuery)
            result = cur.fetchall()
            
            cur.close()
            conn.close()
            return result
        else:
            return "failed : " + conn
        
    except Exception as e:
        return "failed : " + str(e)
    
     

     
def home():
     try:
        open_connection()
     except:
        return 'error 1'
     
     try:
        conn.cursor()
#        cursor.execute("with tc as ( SELECT count(*) from PD_TABLE),cc as (SELECT count(*) from PD_TABLE where customer_contacted = 1),pd as (SELECT count(*) from PD_TABLE where pod > 0.05) select * from tc,cc, pd")
#        result = cursor.fetchall()[0]
        sql =r"""
        select count(distinct cif) as total_cust,
        AVG( customer_contacted = 1 ) as contacted_cust,
        SUM( pod >0.05 ) as risky_cust,
        avg(gambling) as gambling_avg, avg(amazon) as amazon_avg, avg(shopping) as shopping_avg, avg(food) as food_avg, avg(movie) as movie_avg, avg(cc_bill) as ccbill_avg
        from PD_TABLE""" 
        df= pd.read_sql_query(sql,conn)
        conn.close()
        
        return df
     except:
        conn.close()
        return 'error 2'  
        
        
def saveInfo(df):
    
    open_connection()
   
    try:    
        cur = conn.cursor()
        if(type(conn).__name__ != 'str'):
            sql = "INSERT INTO INFO_TABLE (cif,gender,name,city,state,country,region,create_date,email_id) VALUES (:cif,:gender,:name,:city,:state,:country,:region,:create_date,:email_id)"
            listOfInfo=[]
            for index,row in df.iterrows():
                new=[]
                new.append(int(row['CIF']))
                new.append(row['Gender'])
                new.append(row['Name'])
                new.append(row['City'])
                new.append(row['State'])
                new.append(row['Country'])
                new.append(row['Region'])
                new.append(datetime.now())
                new.append('abhishek.tripathi88@gmail.com​')
                listOfInfo.append(tuple(new))
            
            print("UPLOAD USER DATA STARTED...")    
            cur.executemany(sql,listOfInfo)
            
            conn.commit()
            conn.close()
            print("UPLOAD USER DATA DONE...")    
            return "success"
        else:
            return "failed : " + conn
        
    except Exception as e:
        return "failed : " + str(e)
    
    
def saveMasterData(masterDataList):
    
    open_connection()
    
    try:
        cur = conn.cursor()
        if(type(conn).__name__ != 'str'):
            sql = """insert into global_table (CIF,ACCOUNT_NUMBER,ACCOUNT_TYPE,SUMMARY_OF_TRANSACTION,CREDIT,DEBIT,BALANCE_TENURE,TRANSACTION_DATE,CREATE_DATE) """ \
                  """ values(:CIF,:ACCOUNT_NUMBER,:ACCOUNT_TYPE,:SUMMARY_OF_TRANSACTION,:CREDIT,:DEBIT,:BALANCE_TENURE,:TRANSACTION_DATE,:CREATE_DATE) """
            listOfData = []
            for row in masterDataList:
                new = []
                new.append(row.cif.item())
                new.append(row.accountNumber.item())
                new.append(row.accountType)
                new.append(row.summaryOfTransaction)
                new.append(row.credit.item())
                new.append(row.debit.item())
                new.append(row.balanceTenure.item())
                new.append(row.transactionDate)
                new.append(datetime.now())
                listOfData.append(tuple(new))
                
            print("UPLOAD MASTER DATA STARTED...")    
            cur.executemany(sql,listOfData)
            
            
            conn.commit()
            conn.close()
            print("UPLOAD MASTER DATA DONE...")    
            return "success"
            
        else:
            return "failed : " + conn
        
    except Exception as e:
        return "failed : " + str(e)
        
        
def getDataForCif(cif):
    
    open_connection()
    
    try:
        if(type(conn).__name__ != 'str'):
            sql="select * from global_table where cif = :cif order by transaction_date asc"
            cur= conn.cursor()
            cur.execute(sql,cif=cif)

            cifData=[]
            
            for row in cur.fetchall():
                cifData.append(list(row))
            
            
            return cifData
            
        else:
            print('################## ' + conn)
            return "failed : " + conn
        
    except Exception as e:
        print('############## ' + str(e))
        return "failed : " + str(e)


def getAllCarePackages():
    open_connection()
    
    try:
        cur = conn.cursor()
        if(type(conn).__name__ != 'str'):
            
            sql="select cp_code,corresponding_to_datasheet_column from cp_table"
            
            cur.execute(sql)

            cpData=[]
            
            for row in cur.fetchall():
                cpData.append(list(row))
                
            cur.close()
            conn.close()
            return cpData
            
        else:
            return "failed : " + conn
        
    except Exception as e:
        return "failed : " + str(e)


def getCardDetails():
    open_connection()
    
    try:
        cur =conn.cursor()
        cur.execute("""
        select
        count(distinct cif)  total_cust,
        SUM(case when customer_contacted = 1 then 1 else null end ) as contacted_cust ,
        sum(case when pod>0.05 then 1 else null end)  risky_cust,
        sum(case when spend_inc_ratio > 70 then 1 else null end)  cust_under_obs,
        sum(case when email_count > 3 then 1 else null end)  cust_failed_to_improve,
         avg(gambling) as gambling_avg, avg(amazon) as amazon_avg, avg(shopping) as shopping_avg, avg(food) as food_avg, avg(movie) as movie_avg, avg(cc_bill) as ccbill_avg
        ,avg(loan_return) as loan_avg  from PD_TABLE""")
        result = cur.fetchall()
       
        conn.close()
        return result
    except:
        conn.close()
        return 'error in retriving card details'






def getTransactionPerDay():
    open_connection()
    
    try:
        cur = conn.cursor()
        cur.execute("""
        select to_char(transaction_date,'DD/MON/YYYY') date_of_spending,
        sum (debit) spending from global_table group by transaction_date 
        order by transaction_date 
        """)
        result = cur.fetchall()
       
        
        conn.close()
        return result
    
    except:
        conn.close()
        return 'error in retreiving transaction details'



def getSpendingCategoriesByPerc():
    open_connection()
    
    try:
        cur = conn.cursor()
        cur.execute("""
        select (sum(gambling * total_income)/sum(total_income)) gamb_perc ,
        (sum(amazon * total_income)/sum(total_income)) amazon_perc,
        (sum(shopping * total_income)/sum(total_income)) shop_perc,
        (sum(food * total_income)/sum(total_income)) food_perc,
        (sum(movie * total_income)/sum(total_income)) movie_perc,
        (sum(cc_bill * total_income)/sum(total_income)) cc_bill_perc,
        (sum(loan_return * total_income)/sum(total_income)) loan_return_perc
        from PD_TABLE
        """)
        result = cur.fetchall()
        conn.close()
        return result
    
    except:
        conn.close()
        return 'error in retreiving Spending Categories'




def getSpendingCategoriesGlobally():
    open_connection()
    
    try:
        cur = conn.cursor()
        cur.execute("""
        select t.* 
        from (select summary_of_transaction , sum(Debit) amount_spent from global_table
        group by summary_of_transaction
        order by amount_spent desc)t where rownum  < 6


        """)
        result = cur.fetchall()
        conn.close()
        return result
    
    except:
        conn.close()
        return 'error in retreiving Spending Categories Globally'





def getSpendingCategoriesByCountry(ctry):
    open_connection()
    
    try:
        cur = conn.cursor()
        cur.execute("""
        
        select t.* 
        from (
        select distinct gt.summary_of_transaction , sum(gt.Debit) amount_spent, it.country from global_table gt
        inner join info_table it on gt.cif= it.cif
        group by gt.summary_of_transaction,it.country
        
        order by amount_spent desc)t where upper(t.country) = ? and rownum <6;
        """)
        result = cur.fetchall()
        conn.close()
        conn.close()
        return result
    
    except:
        conn.close()
        return 'error in retreiving Spending Categories By COUNTRTY'
    
    
    
    

def getSpendingCategoriesByRegion(region):
    open_connection()
    
    try:
        conn.cursor()
        sql = r"""
        
        select t.* 
        from (
        select distinct gt.summary_of_transaction , sum(gt.Debit) amount_spent, it.region from global_table gt
        inner join info_table it on gt.cif= it.cif
        group by gt.summary_of_transaction,it.region
        
        order by amount_spent desc)t where upper(t.region) = ? and rownum <6;
        """
        df= pd.read_sql_query(sql,conn,params=(region))
        conn.close()
        return df
    
    except:
        conn.close()
        return 'error in retreiving Spending Categories By REGION'   
    
    

def test():
    open_connection()
    
    try:
        cur = conn.cursor()
        cur.execute('''select to_char(transaction_date,'DD/MON/YYYY') date_of_spending,
        sum (debit) spending from global_table group by transaction_date 
        order by transaction_date ''')
        row_headers=[x[0] for x in cur.description] 
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
             json_data.append(dict(zip(row_headers,result)))
        conn.close()
        return print(json.dumps(json_data))
        
    except:
        conn.close()
        print("eror")
 
