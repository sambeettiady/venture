import pandas as pd
import gensim
import gensim.parsing.preprocessing as gpp

os.chdir('/Users/sambeet/Desktop/venture/')

article_dataset = pd.read_csv('articles.csv')
article_dataset.drop_duplicates(subset='text',inplace=True)

def tokenize(text):
    return [token for token in gensim.utils.simple_preprocess(gpp.strip_non_alphanum(gpp.strip_punctuation(gpp.strip_multiple_whitespaces(gensim.utils.deaccent(text))))) if token not in gpp.STOPWORDS]

sentence_stream = [tokenize(article) for article in article_dataset.text]

#LDA
dictionary = gensim.corpora.Dictionary(sentence_stream)

dictionary.filter_extremes(no_below=3, no_above=0.9)
len(dictionary.token2id)
dictionary.compactify()

corpus = [dictionary.doc2bow(text) for text in sentence_stream]
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, update_every=1, passes=1)
lda.print_topics(10)
