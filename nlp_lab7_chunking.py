# -*- coding: utf-8 -*-
"""NLP_Lab7_Chunking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sh7tw7OWGwcrOXqQXZbssjOOmB1-iwEP
"""

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "the little yelow dog barked at vandana"

tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(pos_tags)
tree = nltk.tree.Tree.fromstring(str(result))
tree.pretty_print()

pos_tags

