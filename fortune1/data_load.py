import os
import shutil
import fnmatch
import pickle

def get_traversal_data():
    lst=list()
    for dirpath, dirs, files in os.walk("fortune1"):
        for single_file in files:
            filepath = os.path.abspath(os.path.join(dirpath, single_file))
            file=open(filepath)
            string=file.read().replace("\n"," ")
            print(string)
            print("Creating a tuple with "+single_file+" file content and "+filepath+" path")
            a=[filepath,string]
            lst.append(a)

    f=open("raw_data.pickle","bw")
    pickle.dump(lst,f)
    f.close
            

get_traversal_data()
            
        
