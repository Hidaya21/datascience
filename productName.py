import pandas as pd
#assming already have data into excel
df = pd.read_excel('Readin.xlsx',sheet_name = " prodects")
for idrex, row in df.iterrows():
    productName =row['pName']
    category =row['Category']
    price=row['Price']
    
    currentProdeuct=product(productName,category,price)
    pList.append(currentProdeuct)
#   print(currentProdeuct.discount())
    currentProdeuct.discount(5)
    print("after",currentProdeuct.discrip())
    print("%20s%20s%10.2f" %(productName. get_name(),category.get_category(),price.get_price())
    print("-")
print(len(LpList))


    
