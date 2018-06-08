import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
from nltk import word_tokenize
from nltk.util import ngrams
import string

#Read the data and pass over to list
df = pd.read_excel('text_data.xlsx')
sentences = list(df.Subject)

#Start the text mining process
stemmer = SnowballStemmer("english")
ngram_count = defaultdict(lambda: 0)
N = 2
english_stopwords = stopwords.words('English')

for sentence in sentences:
    all_words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    clean_words = [w for w in all_words
                   if w not in english_stopwords
                   and w not in string.punctuation]
    # Use stems
    stems = [stemmer.stem(x) for x in clean_words]
    for gram in ngrams(stems, N):
        ngram_count[gram] += 1
  
# Assign to the dataframe
data = pd.DataFrame(list(ngram_count.items()), columns=['N-Gram(2)', 'Freq'])
data = data.sort_values(by=['Freq'], ascending =False)

# Output to the excel file
writer = pd.ExcelWriter('top 2-gram.xlsx')
data.to_excel(writer)
writer.save()
