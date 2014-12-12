import data_load
import indexer
import WebParser
import WebSearcher
import FileSearcher


def webAndFile():
    data_load.get_data()
    file_data = indexer.read_data()
    web_data = WebParser.webParserData()
    print("File search:")
    print("====================================================")
    FileSearcher.fileSearch(file_data)
    print("Web search:")
    print("====================================================")
    WebSearcher.webSearcher(web_data)


webAndFile()
