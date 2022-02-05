# ciò che c'è sotto funziona solo se prima installi pacchetto gensim

from gensim.models import Word2Vec
from gensim.test.utils import common_texts, common_dictionary, common_corpus
model = Word2Vec(sentences=common_corpus, vector_size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")
model = Word2Vec.load("word2vec.model")

# sim = model.wv.similarity('dog', 'cat')

import gensim.downloader
print(list(gensim.downloader.info()['models'].keys()))
model1 = gensim.downloader.load('glove-wiki-gigaword-300')
model2 = gensim.downloader.load('word2vec-google-news-300')

sim = model2.similarity('user', 'account')

print(sim)