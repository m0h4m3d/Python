#Mohammed Alsaif - HW3

import shelve
from datetime import datetime

def search(string):

    dictionary=shelve.open(string)
    
    query=input("query:")

    #print(query)

    isAnd=False
    index=query.find("and")
    if(index>=0):
            isAnd=True
    else:
            if(query.find("or")<0):
                isAnd=True

    words=set()
    for item in query.split():
            if(item!="and" and item!="or"):
                    words.add(item)


   
    #print(isAnd)
    string=""
    if(isAnd):
            string="AND"
    else:
            string="OR"

    print("\nPerforming",string, "search for:"+str(words)+"\n")

    dt1 = datetime.now()

    st=set()
    failed=False
    words=list(words)
    if(isAnd):

            try:
                    a=dictionary[words[0]]
                    st={x for x in a}
            except:
                    failed=True

            for word in words:
                    try:
                            st=st.intersection(dictionary[word])
                    except:
                            failed=True
                            break
    else:
            for word in words:
                    try:
                            st=st.union(dictionary[word])
                    except:
                            pass



    dt2 = datetime.now()

    if(failed!=True):
            s=list(st)
            s.sort()
            for item in s:
                    print("Found at",item)
                    
    print("Execution time:", dt2.microsecond-dt1.microsecond)
    dictionary.close()
