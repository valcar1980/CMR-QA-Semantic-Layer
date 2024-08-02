'''
Created on 19 Nov 2018

@author: ejimenez-ruiz
Edited by: valcar1980
'''

# import pandas as pd
# import re
import sys
# from csv_utils.csv_reader import CSVQAReader
# from semantics.query_rdf_graph import QueryRDFGraph

sys.path.append('../semantics/')
import triple_generator as triplegen

file_csv = '../../data/input/FirstBatch100_scores.csv'

#From excel to CSV (not necessary any more)
#data_xls = pd.read_excel('/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/FirstBatch100.xlsx', 'Sheet1', index_col=None)
#data_xls.to_csv(file_csv, encoding='utf-8')
    

#creates triples
output_file = '../../data/input/FirstBatch100.ttl'
triplegen.TripleGenerator(file_csv, output_file)


# #prepares comments
# qManager = QueryRDFGraph(output_file)
# qres = qManager.getQualityComments()


# #Comments to give to the text mining engine
# file = open("/home/ejimenez-ruiz/Documents/UK_BioBank/Input_Data/Batch1-100/FirstBatch100_comments.txt", 'w') 
        
        
# #Return qres and store in file: id|comment -> row[0]|row[1]
# for row in qres:
#     #print("%s has comment %s" % row)
#     label=row[0].split("#")[1]
    
#     comment=row[1].lower()
    
#     #Minor fixes (moved to triple generator)
#     #comment=comment.replace("&"," and ")
#     #comment=comment.replace("/"," and ")
#     #comment=comment.replace("$","4")
#     #comment=comment.replace("2 ","2ch ")
#     #comment=comment.replace("4 ","4ch ")
#     #comment=comment.replace("vol.","volume")
#     #comment=comment.replace("1 ","one ")
#     #comment=comment.replace("several","multiple")
#     #comment=comment.replace("some","few")
#     #comment=comment.replace("basel","basal")
#     #comment=comment.replace("vol.","volume")
#     #comment=comment.replace("("," ( ")
#     #comment=comment.replace(")"," ) ")
    
#     ##comment=comment.replace(",",", ")
#     ##comment=comment.replace(";",", ")
#     ##comment=comment.replace(".",", ")
#     #comment = re.sub(r'(?<=[.,;])(?=[^\s])', r' ', comment)
    
#     #comment=comment.strip()
    
#     #if comment.endswith("."):
#     #    comment=comment[0:len(comment)-1]
        
    
#     print(label, comment)
#     print(label + "|" + comment, file=file)
            
            
            


