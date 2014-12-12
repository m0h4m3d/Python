import WebParser
from datetime import datetime

def webSearcher(web_data):
        newDataList = {str(i+1): web_data[i].lower().split() for i in range(0, len(web_data))}
        Query = str(input("Enter Your Word:"))
        queryList = list(set(Query.lower().split()))
        t1 = datetime.now()
        if ('or' in queryList and 'and' not in queryList):
            queryList.remove('or')
            print ("Performing OR search for:" + ('\t').join(queryList))
            for key,value in newDataList.items():
                for word in queryList:
                    if word in value:
                        found = True
                        print("Found At " + str(key)+'  ' +  web_data[int(key)]  )
                        break
            if found == False:
                    print ("None")
        else:
            if ('and' in queryList and 'or' not in queryList):
                queryList.remove('and')
            elif ('and' in queryList and 'or' in queryList):
                queryList.remove('and')
                queryList.remove('or')
            else:
                queryList = queryList
            print ("Performing AND search for:" + ('\t').join(queryList))
            for key,value in newDataList.items():
                for word in queryList:
                    if word not in value:
                        flag = False
                        break
                    else: flag = True
                if flag == True:
                    found_once = True
                    print("Found At " + str(key)+'  ' +  web_data[int(key)] )
            if flag == False:
                    print ("None")
        t2 = datetime.now()
        print("Execution time:", t2.microsecond-t1.microsecond)


def webSearchCall():
    web_data = WebParser.webParserData()
    webSearcher(web_data)
