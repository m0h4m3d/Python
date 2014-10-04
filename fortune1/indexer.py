import pickle
import shelve
 
def process_data(path,shelver):

    f=open(path,"br")
    data_list=pickle.load(f)
    
    dictionary=shelve.open(shelver)

    for i in range(0,len(data_list)):
            tpl=data_list[i]
            for item in tpl[1].split():
                    st=0
                    try:
                            st=dictionary[item]
                    except:
                            st=set()
                    st.add(tpl[0])
                    dictionary[item]=st

    
    
    dictionary.close()
