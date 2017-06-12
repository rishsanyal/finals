from collections import Counter
import sys, pdb, csv, pdb, math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from collections import defaultdict

# csvfile = pd.read_csv("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/orders.csv")
# columns = ['order_id', 'user_id']
# df1 = pd.DataFrame(csvfile, columns=columns)
# # print(df1.head())
#
# for i in range(500):
#     print(df1.iloc[i]['order_id'])

def numIterms(): #gives us a dictionary with key as the user id and the value as the number of times they've ordered
    finalDict = Counter()
    d = defaultdict(list)
    i = 0
    retCountDict = Counter()
    numTimesOrdered = Counter()
    ordersFile = pd.read_csv("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/order_products__traint.csv",dtype=str)
    readerFile = pd.read_csv("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/orderst.csv")
    colForReaders = ["order_id","user_id"]
    colForOrders = ["order_id"]
    reader = pd.DataFrame(readerFile, columns = colForReaders)
    orders = pd.DataFrame(ordersFile, columns = colForOrders)

    traintList = orders.values
    userList = reader.values

    for temp in userList:
        numTimesOrdered[temp[1]] += 1

    for i in range(len(traintList)):
        retCountDict[traintList[i][0]] += 1 #it's the dictionary where the key is the order id and the value is the number of items
    for i in range(len(userList)):
        userID = userList[i][1]
        orderID = userList[i][0]

        if(retCountDict[str(orderID)]) != 0:
            finalDict[userID] += int(retCountDict[str(orderID)]) #key -> user id and value is the number of items that user ordered
        else:
            continue

    #finalDict -=> has key the user id and the value is the total number of items they ordered
    #numTimesOrdered -=> key as the user id, value as the total number of orders made by user
    print(avgItems(userList,finalDict,numTimesOrdered))

    return 0

def avgItems(uList,fDict, nTimesOrdered): #userList, finalDict, numTimesOrdered
    avgDict = Counter()
    for users in uList:
        user = users[1]
        totalItems = int(fDict[user])
        totalTimes = int(nTimesOrdered[user])
        avgDict[user] += (totalItems/totalTimes)
    return avgDict




def numOrdersPerUser():
    numOrders = Counter()
    i = 0
    reader = pd.read_csv("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/orders.csv",iterator=True, chunksize=1000)
    columnsForReader = ['user_id']
    df1 = pd.DataFrame(reader, columns=columnsForReader)

    for i in range(500):
        numOrders[df1.iloc[i]['user_id']] += 1

    return numOrders


def totalNumItemsOrdered():
    numItems = Counter()
    i = 0
    readerFile = pd.read_csv("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/orders.csv")
    ordersFile = pd.read_csv("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/order_products__prior.csv")
    colForReaders = ["order_id","user_id"]
    colForOrders = ["order_id"]

    reader = pd.DataFrame(readerFile, columns = colForReaders)
    orders = pd.DataFrame(ordersFile, columns = colForOrders)


    for i in range(100):
        itemsUserOrdered = itemsOrdered(reader, orders, reader.iloc[i]["order_id"], i)
        numItems[reader.iloc[i]["user_id"]] += itemsUserOrdered
    return numItems

def itemsOrdered(rDF, oDF, orderID,i):
    orderIdCounter = Counter()
    retNum = 0

    for row in oDF.itertuples():
        if row[1] == orderID:
            retNum += 1
    return retNum

    # userID = ordersDF.iloc[i]["user_id"]
    # orderID = ordersDF.iloc[i]["order_id"]
    #
    # for j in len(itemsDF): #not sure about how to iterate through the thing
    #     if itemsDF.iloc[j]["order_id"] == orderID:
    #         orderIdCounter[orderID] += 1
def aussie():
    userDict = pickle.load( open( "save.p", "rb" ) )
    for i in range(1,4):
        print("for i = ",i,"the value is ",userDict[i]) #where i is is the orderid
    return 0

def partOne():
    i = 0
    with open("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/orders.csv") as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            if i < 500 and row[1] != "user_id":
                P1[row[1]] += 1
                i += 1

    lens = np.arange(len(D))
    plt.bar(lens, P1.values(),width=0.3, align='center',alpha = 0.2)
    plt.xticks(lens, P1.keys())
    plt.show()
    csvfile.close()

def main():
    # numOrdersPerUser()
    # print(totalNumItemsOrdered())
    # aussie()
    numIterms()
main()
