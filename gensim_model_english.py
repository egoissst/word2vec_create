from gensim.models import Word2Vec
import pandas as pd
import GenericMailerService


to_send_mail_alert = True
#csvFilePath = "data_files/commentData_net_till_Mar_20_clean_2917.csv"
#csvFilePath = "data_files/commentData_MTO_till_15April_2020_cleaned.csv"
#csvFilePath = "data_files/commentData_net_till_Aug_20_clean_2917.csv"
#csvFilePath = "data_files/commentData_test_w2v.csv"
csvFilePath = "data_files/commentData_TOI_net_till_Aug_20_cleaned_cleanstrv2_shuf.csv"

print('Reading csv : ', csvFilePath)

class Raw_Sentences(object):
    def __init__(self, fileloc):
        self.fileloc = fileloc

    def __iter__(self):
        for line in open(self.fileloc, 'r', encoding='utf-8'):
            yield (str(line).replace('\n','')).split(" ")


#def get_row_df_csv(csv_file_path):
#    df_csv = pd.read_csv(csv_file_path, names=['C_T'], header=None)
#    for index, row in df_csv.iterrows():
#        #yield(row['C_T'])
#        yield((str(row['C_T'])).split(" "))

#df_csv = pd.read_csv(csvFilePath, names=['C_T'])
#df_csv = pd.read_csv(csvFilePath, names=['C_T'], header=None)
#list_cmts = df_csv['C_T'].tolist()

print('preparing english word2vec feed')

#word2vec_feed = ((str(sent)).split(" ") for sent in list_cmts)
word2vec_feed = Raw_Sentences(csvFilePath)
#word2vec_feed = get_row_df_csv(csvFilePath)

#print('length word2vec_feed : ', len(word2vec_feed))
print('word2vec feed generator created.. Starting word2vec training')

#sg=0 for CBOW
model = Word2Vec(word2vec_feed, size=300, window=10, min_count=5, workers=24, negative=15, hs=0, sample=0.00001, sg=0)

print('word2vec model created')
print('saving the word2vec model')

#model.save("eng_updated_min5.model")
#model.wv.save_word2vec_format("eng_updated_min5_word2vec.bin",  binary=True)

#model.save("ourdata_01apr20.cbow.size300.win10.neg15.sample1e-5.min5.model")
#model.wv.save_word2vec_format("ourdata_01apr20.cbow.size300.win10.neg15.sample1e-5.min5.bin",  binary=True)

#model.save("toi_eng_till_aug20.cbow.size300.win10.neg15.sample1e-5.min5.model")
#model.wv.save_word2vec_format("toi_eng_till_aug20.cbow.size300.win10.neg15.sample1e-5.min5.bin",  binary=True)

#model.save("toi_eng_till_aug20_cleanstrV2.cbow.size300.win10.neg15.sample1e-5.min5.model")
#model.wv.save_word2vec_format("toi_eng_till_aug20_cleanstrV2.cbow.size300.win10.neg15.sample1e-5.min5.bin",  binary=True)
model.save("toi_eng_till_aug20_cleanstrV2.cbow.size300.win10.neg15.sample1e-5.min5_v2.model")
model.wv.save_word2vec_format("toi_eng_till_aug20_cleanstrV2.cbow.size300.win10.neg15.sample1e-5.min5_v2.bin",  binary=True)

#model.save("toi_test.model")
#model.wv.save_word2vec_format("toi_test.bin",  binary=True)

#model.save("pure_MTO_16apr20.cbow.size300.win10.neg15.sample1e-5.min5.model")
#model.wv.save_word2vec_format("pure_MTO_16apr20.cbow.size300.win10.neg15.sample1e-5.min5.bin",  binary=True)


print('size of vocab : ' , len(model.wv.vocab))
print('process complete')

if to_send_mail_alert:
    mail_obj = GenericMailerService.get_mailer_object_for_ml_process_alert('TOI till AUG 2020 - w2v process complete. Check please.')
    print('sending alert mail')
    GenericMailerService.send_mailer(mail_obj)
