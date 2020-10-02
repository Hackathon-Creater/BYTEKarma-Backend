import json
import pandas as pd
import numpy as np

def mapSearchRequest(request):
    
    searchRequestJsonObject = json.loads(json.dumps(request))
    
    cif = searchRequestJsonObject['cif'] if searchRequestJsonObject['cif'] != '' else None
    country = searchRequestJsonObject['country'] if searchRequestJsonObject['country'] != '' else None
    state = searchRequestJsonObject['state'] if searchRequestJsonObject['state'] != '' else None
    city = searchRequestJsonObject['city'] if searchRequestJsonObject['city'] != '' else None
    region = searchRequestJsonObject['region'] if searchRequestJsonObject['region'] != '' else None
    name = searchRequestJsonObject['name'] if searchRequestJsonObject['name'] != '' else None
    gender = searchRequestJsonObject['gender'] if searchRequestJsonObject['gender'] != '' else None
    transactionType = searchRequestJsonObject['transactionType'] if searchRequestJsonObject['transactionType'] != '' else None
    accountNumber = searchRequestJsonObject['accountNumber'] if searchRequestJsonObject['accountNumber'] != '' else None
    accountType = searchRequestJsonObject['accountType'] if searchRequestJsonObject['accountType'] != '' else None
    
    requestObject = searchRequestObject(cif, country, state, city, region, name, gender, transactionType, accountNumber, accountType)
    
    return requestObject

def mapSearchResponse(resultList):
    objectList = []
    for row in resultList:
        objectList.append(searchResponseObject(row[0],row[1],row[2],row[3],row[4],row[5],row[6].strftime("%Y-%m-%d %H:%M:%S"),row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21].strftime("%Y-%m-%d %H:%M:%S")))
    
    results = [obj.to_dict() for obj in objectList]
    
    return results

# def mapHomePageResponse(result, avgList):
#     return homePageResponse(result[0], result[1], result[2], avgList )

def mapMasterData(f):
    df = pd.DataFrame(pd.read_excel(f))
    masterDatas = []
    for i in df.index:
        masterDataRow = masterData(df['CIF'][i],df['Account Number'][i],df['Account Type'][i],df['Summary of transaction'][i],df['Credit'][i],df['Debit'][i],df['Balance'][i],df['Transaction Date'][i])
        masterDatas.append(masterDataRow)
    return masterDatas
    
def mapCardDetailsResponse(result):
    objList= []
    for row in result:
        objList.append(CardDetails(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
    results = [obj.to_dict() for obj in objList]
    return results  
        
def mapTransPerDay(result):
    objList= []
    for row in result:
        objList.append(TransPerDay(row[0], row[1]))
    results = [obj.to_dict() for obj in objList]
    return results  
     

def mapSpendCategoryPerc(result):
    objList= []
    for row in result:
        objList.append(SpendPercChart(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    results = [obj.to_dict() for obj in objList]
    return results  
  
def mapSpendCategoryPercGlobally(result):
    objList= []
    for row in result:
        objList.append(SpendCategoryGlobally(row[0], row[1]))
    results = [obj.to_dict() for obj in objList]
    return results  
  

class searchRequestObject:
   'Search request object'

   def __init__(self, cif, country, state, city, region, name, gender, transactionType, accountNumber, accountType):
      self.cif = cif
      self.country = country
      self.state = state
      self.city = city
      self.region = region
      self.name = name
      self.gender = gender
      self.transactionType = transactionType
      self.accountNumber = accountNumber
      self.accountType = accountType
      
class searchResponseObject:
   'Search response object'

   def __init__(self, cif,account_number,account_type,summary_of_transaction,credit,debit,transaction_date,gender,name,city,state,country,region,pod,gambling,amazon,shopping,food,movie,cc_bill,customer_contacted,create_date):
      self.cif = cif
      self.pod = pod
      self.gambling = gambling
      self.amazon = amazon
      self.shopping = shopping
      self.food = food
      self.movie = movie
      self.cc_bill = cc_bill
      self.customer_contacted = customer_contacted
      self.name = name
      self.city = city
      self.country = country
      self.state = state
      self.region = region
      self.create_date = create_date
      self.gender= gender
      self.account_number = account_number
      self.account_type = account_type
      self.summary_of_transaction = summary_of_transaction
      self.credit = credit
      self.debit = debit
      self.transaction_date = transaction_date

      
   def to_dict(self):
       return { "cif" : self.cif, "pod" : self.pod, "gambling" : self.gambling, "amazon" : self.amazon, "shopping" : self.shopping, "food" : self.food, "movie" : self.movie, "cc_bill" : self.cc_bill, "customer_contacted" : self.customer_contacted, "name" : self.name, "city" : self.city, "country" : self.country, "state" : self.state, "region" : self.region, "create_date" : self.create_date, "gender" : self.gender, "account_number" : self.account_number, "account_type" : self.account_type, "summary_of_transaction" : self.summary_of_transaction, "credit" : self.credit, "debit" : self.debit, "transaction_date" : self.transaction_date }
      
class HomePageResponse:
   'Home page response object'

   def __init__(self, cardDetails, transPerDay,spentCategoryPieChart,spendCategoryGlobally):
      self.cardDetails = cardDetails
      self.transPerDay = transPerDay
      self.spentCategoryPieChart = spentCategoryPieChart
      self.spendCategoryGlobally = spendCategoryGlobally
   def to_dict(self):
       return { "cardDetails" : self.cardDetails, "transPerDay" : self.transPerDay, "spentCategoryPieChart" : self.spentCategoryPieChart , "spendCategoryGlobally" : self.spendCategoryGlobally  }

class CardDetails:    
    def __init__(self,totalCust,contactedCust,riskyCust,custAtObservation,custFailToImprove,gambAvg,amazonAvg,shopAvg,foodAvg,movieAvg,ccAvg,loanAvg):
        self.totalCust = totalCust
        self.contactedCust = contactedCust
        self.riskyCust = riskyCust
        self.custAtObservation = custAtObservation
        self.custFailToImprove = custFailToImprove
        self.gambAvg = gambAvg
        self.shopAvg = shopAvg
        self.foodAvg = foodAvg
        self.movieAvg = movieAvg
        self.ccAvg = ccAvg
        self.loanAvg = loanAvg
   
    def to_dict(self):
        return {"totalCust": self.totalCust,"contactedCust":self.contactedCust,"riskyCust": self.riskyCust,"custAtObservation":self.custAtObservation,"custFailToImprove":self.custFailToImprove,"gambAvg":self.gambAvg,"shopAvg":self.shopAvg,"foodAvg": self.foodAvg,"movieAvg":self.movieAvg,"ccAvg":self.ccAvg,"loanAvg":self.loanAvg}
      
        
class TransPerDay:
    def __init__(self,dateOfSpend,amountSpent):
        self.dateOfSpend = dateOfSpend
        self.amountSpent = amountSpent
   
    def to_dict(self):
        return {"dateOfSpend" :self.dateOfSpend , "amountSpent": self.amountSpent}

        
class SpendPercChart:
    def __init__(self,gambPerc,amazonPerc,shopPerc,foodPerc,moviePerc,ccPerc,loanReturnPerc):
        self.gambPerc = gambPerc
        self.amazonPerc = amazonPerc
        self.shopPerc = shopPerc
        self.foodPerc = foodPerc
        self.moviePerc = moviePerc
        self.ccPerc = ccPerc
        self.loanReturnPerc = loanReturnPerc
   
    def to_dict(self):
        return {"gambPerc" :self.gambPerc , "amazonPerc": self.amazonPerc, "shopPerc": self.shopPerc , "foodPerc": self.foodPerc , "moviePerc": self.moviePerc , "ccPerc": self.ccPerc , "loanReturnPerc": self.loanReturnPerc }



class SpendCategoryGlobally:
    def __init__(self,category,amountSpent):
        self.category = category
        self.amountSpent = amountSpent
        
   
    def to_dict(self):
        return {"category" :self.category , "amountSpent": self.amountSpent}


        
class masterData:
    def __init__(self,cif, accountNumber, accountType, summaryOfTransaction, credit, debit, balanceTenure, transactionDate):
        self.cif = cif
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.summaryOfTransaction = summaryOfTransaction
        self.credit = credit
        self.debit = debit
        self.balanceTenure = balanceTenure
        self.transactionDate = transactionDate

        
        