import os
import shutil
import fnmatch
import pickle
import time
 
def get_data():
     data = []
     for dirpath, dirs, files in os.walk('E:\\h2h'):
          for single_file in files:
               filepath = os.path.abspath(os.path.join(dirpath, single_file))
               F = open(filepath,'r')
               data = F.read().replace('\n', ' ')
               modified = "Last Modified: "+ time.ctime(os.path.getmtime(filepath))
               size = "Size of file: "+str(os.path.getsize(filepath))
               tup = (filepath,data,modified,size)
               data.append(tup)
     pickle.dump(data,open("raw_data.pickle", "wb"))



               

             
