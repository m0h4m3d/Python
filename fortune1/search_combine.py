import searcher
import data_load
import indexer

data_load.get_traversal_data()
indexer.process_data("raw_data.pickle","fortunes_shelve")
searcher.search("fortunes_shelve")
