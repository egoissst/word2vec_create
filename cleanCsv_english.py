#!/usr/bin/env python
# coding: utf-8


import csv
import re

csv.field_size_limit(100000000)


def string_contains_alphabet(string):    
    if re.search('[a-zA-Z]', string):
        return True
    else:
        return False


def clean_str_updated_26_oct_v2(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    #replace html tags and character entities with space
    string = re.sub(r"(<br/>|<br />|&quot;|&amp;|&gt;|&lt;|&nbsp;|&ndash;|&ensp;|&mdash;|&lsquo;|&rsquo;|&rdquo;|&ldquo;|&bdquo;|&zwj;)", " ", string)
    string = string.strip().lower()
    string = ' ' + string + ' '

    string = re.sub(r"[^A-Za-z0-9!\'*$@#]", " ", string)
    #for removing 's, 'll, etc..
    string = re.sub(r"([a-z])'[a-z]+\b", r"\1", string)
    #removing the single quotes
    string = re.sub(r"\'", "", string)

    # clean 'this is 21st century hell3 a' to 'this is st century hell a'
    string = re.sub(r" [^a-z]+", " ", string)
    string = re.sub(r"[^a-z] ", " ", string)
    string = re.sub(r"\!+ ", " ", string)

    string = re.sub(r' [0-9\. ]+ \s*', ' ', string)  #Strip int digit like 'i have 95.3 apples'
    string = re.sub(r' [^a-z]+ \s*', ' ', string)    #Strip words containing only special charcters or digits

    #reducing multiple consecutive occurrences to two occurrences
    string = re.sub(r'(.)\1{2,}',r'\1\1', string)
    #reduce multiple occurrences of special characters to only once
    string = re.sub(r'([^a-z])\1+', r'\1', string)

    return string.strip().lower()


def clean_str_1544432917(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`*$@#]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
   # string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
   # string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
   # string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def clean_str_updated(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    #replace html tags and character entities with space
    string = re.sub(r"(<br/>|&quot;|&amp;|&gt;|&lt;|&nbsp;|&ndash;|&ensp;|&mdash;|&lsquo;|&rsquo;|&rdquo;|&ldquo;|&bdquo;)", " ", string)
    string = re.sub(r"[^A-Za-z0-9!\'*$@#]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    
    #removing the single quotes
    string = re.sub(r"\'", "", string)
    
    string = re.sub(r"\s{2,}", " ", string)
    string = string.lower()
    
    #reducing multiple consecutive occurrences to two occurrences
    string = re.sub(r'(.)\1{2,}',r'\1\1', string)

    list_words = []
    for x in string.split(" "):
        #remove starting and ending exclamations (!)
        x = re.sub(r"^!+", "", x)
        x = re.sub(r"!+$", "", x)
        #remove starting hashes (#)
        x = re.sub(r"^#+", "", x)
        #remove those tokens that don't contain any alphabets
        if(string_contains_alphabet(x)):
            list_words.append(x)
        
    #rejoin the retrieved list to form a sentence
    string = " ".join(list_words)
    return string.strip().lower()


CSV_FILE_NAME = ""


def createNewCsv(file_path = CSV_FILE_NAME):
    with open(file_path, 'w+') as writeFile:
        pass

def appendListToCsv(list_csv, file_path):
    with open(file_path, 'a', encoding='utf-8') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(list_csv)

def getListFromCsvV2(filePath):
    with open(filePath, 'r', encoding='utf-8') as readFile:
        lines = [line.rstrip('\n') for line in readFile]
        return lines


import pandas as pd

chunksize = 30000
#folder_name = "data_files"
folder_name = "data_files/working_dir"

#csvFilePath = "{}/commentData_TOI_Nov_19_till_Mar_20_filtered.csv".format(folder_name)
#csvFilePath = "{}/commentData_TOI_Apr_20_till_Aug_20_filtered.csv".format(folder_name)
#csvFilePath = "{}/commentData_TOI_Nov_19_till_Mar_20_filtered.csv".format(folder_name)
#csvFilePath = "{}/commentData_TOI_Apr_20_till_Aug_20_filtered.csv".format(folder_name)
csvFilePath = "{}/commentData_TOI_net_till_oct_2019_filtered.csv".format(folder_name)

#csvOutputFilePath = "{}/commentData_TOI_Nov_19_till_Mar_20_cleaned.csv".format(folder_name)
#csvOutputFilePath = "{}/commentData_TOI_Apr_20_till_Aug_20_cleaned.csv".format(folder_name)
#csvOutputFilePath = "{}/commentData_TOI_Nov_19_till_Mar_20_cleaned_cleanstrv2.csv".format(folder_name)
#csvOutputFilePath = "{}/commentData_TOI_Apr_20_till_Aug_20_cleaned_cleanstrv2.csv".format(folder_name)
csvOutputFilePath = "{}/commentData_TOI_net_till_oct_2019_cleaned_cleanstrv2.csv".format(folder_name)

print('creating a new file : {}'.format(csvOutputFilePath))
createNewCsv(csvOutputFilePath)

i=0
for chunk in pd.read_csv(csvFilePath, chunksize=chunksize):
    i+=1
    print ('iteration: ', i)
    
    #if i==2:
    #    print ('stopping at iteration %s as requested'%(i))
    #    break
    
    # index the relevant field 
    column_index = 1
    #list_chunk = chunk.iloc[:,0].tolist()
    list_chunk = chunk.iloc[:,column_index].tolist()
    #print([(str(item)).encode('ascii', 'ignore') for item in list_chunk])
    #csv_output_list = [[clean_str_updated(str(sent))] for sent in list_chunk]
    csv_output_list = [[clean_str_updated_26_oct_v2(str(sent))] for sent in list_chunk if sent]
    print('length csv_output_list : ', len(csv_output_list))
    
    csv_output_list = [x for x in csv_output_list if x[0]]
    print('length csv_output_list rem blank : ', len(csv_output_list))
    
    appendListToCsv(csv_output_list, csvOutputFilePath)


print('\nprocess complete')
