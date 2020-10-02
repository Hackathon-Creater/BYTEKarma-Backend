import pandas as pd

def transposeCifData(cifData):
    
    dates = []
    
    for i in cifData:
        dates.append(i[7].strftime('%m/%d/%Y'))
        
        
    dates = sorted(list(set(dates)))
    
    df=[]
    
    for i in dates:
        new=[]
        pm=0
        sl=0
        ccml=0
        amz=0
        fd=0
        sh=0
        ccb=0
        mv=0
        gb=0
        for row in cifData:
            if(row[7].strftime('%m/%d/%Y') == i):
                new=[]
                if row[3] == "Parental Money":
                    pm = row[4]
                elif row[3] == "Shopping":
                    sh = row[5]
                elif row[3] == "Credit Card Bill":
                    ccb = row[5]
                elif row[3] == "Amazon":
                    amz = row[5]
                elif row[3] == "Food":
                    fd = row[5]
                elif row[3] == "Gambling":
                    gb = row[5]
                elif row[3] == "Salary":
                    sl = row[4]
                elif row[3] == "Credit Card Monthly limit":
                    ccml = row[4]
                elif row[3] == "Movie":
                    mv = row[5]
        new.append(pm)
        new.append(sl)
        new.append(ccml)
        new.append(amz)
        new.append(fd)
        new.append(sh)
        new.append(ccb)
        new.append(mv)
        new.append(gb)
        df.append(new)
            
    
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    c5=[]
    c6=[]
    c7=[]
    c8=[]
    c9=[]
    
    for row in df:
        c1.append(row[0])
        c2.append(row[1])
        c3.append(row[2])
        c4.append(row[3])
        c5.append(row[4])
        c6.append(row[5])
        c7.append(row[6])
        c8.append(row[7])
        c9.append(row[8])
    c1=sorted(c1,reverse=True)
    c2=sorted(c2,reverse=True)
    c3=sorted(c3,reverse=True)
    c4=sorted(c4,reverse=True)
    c5=sorted(c5,reverse=True)
    c6=sorted(c6,reverse=True)
    c7=sorted(c7,reverse=True)
    c8=sorted(c8,reverse=True)
    c9=sorted(c9,reverse=True)
    
    final =[]
    
    for i in range(len(df)):
        new=[]
        new.append(c1[i])
        new.append(c2[i])
        new.append(c3[i])
        new.append(c4[i])
        new.append(c5[i])
        new.append(c6[i])
        new.append(c7[i])
        new.append(c8[i])
        new.append(c9[i])
        final.append(new)
    
    return pd.DataFrame(final, columns = ["Inherited Money","Salary","Credit Card Monthly limit","Amazon","Food","Shopping","Loan disburse","Movie","Gambling"])

    
    
