Word2Vec training - TOI - incremental - (updated 4 September) 
order in which to run files - 
1) filter_file.py -> filters out the activities not containing any comment text 
2) cleanCsv_english.py -> cleans the comment texts with the given clean_str function 
3) gensim_model_english.py -> starts the word2vec training process

Steps 1 and 2 to be done on the incremental data files. (say April, 2020 to Aug, 2020)
Then, append to the existing data file which contains data till March, 2020 ->
i)  cp commentData_net_till_Mar_20_clean_2917.csv commentData_net_till_Aug_20_clean_2917.csv
ii) cat commentData_TOI_Apr_20_till_Aug_20_clean_2917.csv >> commentData_net_till_Aug_20_clean_2917.csv

