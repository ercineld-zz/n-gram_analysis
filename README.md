# n-gram_analysis

###N-Gram analysis over sentence dataframe

N-grams of texts are extensively used in text mining and natural language processing tasks. They are basically a set of co-occuring words within a given window.

For instance, for the sentence "Cheap hotels in London".

- If N=2 (known as bigrams), then the ngrams would be:

- Cheap hotels, hotels in, in London

- If N=3, the n-grams would be:

- Cheap hotels in, hotels in London

###How many N-grams in a sentence?

X: Num of words in a given sentence
K: the sentence

the number of n-grams for sentence K:
- N-grams(K) = X - (n-1)
