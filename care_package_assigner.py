from sklearn.metrics import r2_score
import pandas as pd
import dao

def getCarePackages(df):
    g = list(df['Gambling'])
    r=[]
    
    for i in range(df.shape[1]-1):
        new=[]
        new.append(i)
        new.append(r2_score(g, list(df.iloc[:,i])))
        r.append(new)
        
    r = sorted(r,key=lambda x: (x[1]), reverse=True)
    
    carePackageList = dao.getAllCarePackages()
    
    for i in carePackageList:
        if df.columns[r[0][0]] == i[1]:
            return i[0]
    

