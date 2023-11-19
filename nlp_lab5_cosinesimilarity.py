# -*- coding: utf-8 -*-
"""NLP_Lab5_CosineSimilarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yfNP1ryc6j9FANk0QoMN7BINbtaq7i8Q
"""

# program to measure the similarity between two sentences using cosine similarity
import nltk
from nltk.corpus import stopwords
import nltk.tokenize
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
nltk.download('punkt')
nltk.download('stopwords')

# input sentences
X = "Artificial intelligence is heart of data science"
Y = "Machine Learning is a fragment of Artificial intelligence"
#X = "The cat sat on the mat"
#Y = "The dog slept on the floor"

# convert to lowercase
X = X.lower()
Y = Y.lower()

# tokenization
X_list = word_tokenize(X)
Y_list = word_tokenize(Y)

#remove stop words
sw = stopwords.words('english')
X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}

# form a set containing keywords of both strings
word_set = X_set.union(Y_set)

# create vectors
X_vector = np.zeros(len(word_set))
Y_vector = np.zeros(len(word_set))


i = 0
for word in word_set:
  if word in X_set:
    X_vector[i] = 1
  if word in Y_set:
    Y_vector[i] = 1
  i += 1

similarity = cosine_similarity([X_vector], [Y_vector])
print("Similarity", similarity[0][0])

