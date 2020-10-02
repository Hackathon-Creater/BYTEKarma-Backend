import pod as pcl
import dao
import pandas as pd
import mapper

from mapper import HomePageResponse

def process(f):
    
    masterDataList = mapper.mapMasterData(f)
    msg1 = dao.saveMasterData(masterDataList)
    
    df = pcl.calc(f)
    msg2 = dao.save(df)
    
    if msg1 == 'success' and msg2 == 'success':
        return "success"
    else:
        return "MASTER DATA UPLOAD : " + msg1 + " |###| PD SAVE : " + msg2
    
def search(searchRequest):
    searchRequestObject = mapper.mapSearchRequest(searchRequest)
    
    resultList = dao.search(searchRequestObject)
    
    if type(resultList).__name__ != 'str':
    
        if len(resultList)>0 :
            searchResponse = mapper.mapSearchResponse(resultList)
            return searchResponse
        else:
            return "no results found"
    else:
        return resultList

def home():
    result = dao.home()
    
    return result
    
def saveInfo(f):
    
    df = pd.DataFrame(pd.read_excel(f));
    msg = dao.saveInfo(df)
    return msg

 
    
    
def getHomeDetails():
    result_contains_card = dao.getCardDetails()
    cardObj = mapper.mapCardDetailsResponse(result_contains_card)
    
    result_conatins_trans_summary = dao.getTransactionPerDay()
    transObj = mapper.mapTransPerDay(result_conatins_trans_summary)
    
    result_contains_spending_perc = dao.getSpendingCategoriesByPerc()
    spendCategoryPercObj = mapper.mapSpendCategoryPerc(result_contains_spending_perc)
    
    result_contains_spending_globally = dao.getSpendingCategoriesGlobally()
    spendCategoryPercGloballyObj = mapper.mapSpendCategoryPercGlobally(result_contains_spending_globally)
    
    
    resp = HomePageResponse(cardObj,transObj,spendCategoryPercObj,spendCategoryPercGloballyObj)
   
    final_response =resp.to_dict()
    return final_response




