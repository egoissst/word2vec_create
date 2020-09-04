from gensim.models import KeyedVectors

w2v_location = 'pure_MTO_16apr20.cbow.size300.win10.neg15.sample1e-5.min5.bin'
w2v = KeyedVectors.load_word2vec_format(w2v_location, binary=True)

test_word = 'पोस्ट'
print('test_word', test_word.encode('utf-8'))
print(w2v.most_similar(test_word))

