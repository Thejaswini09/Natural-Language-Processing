# -*- coding: utf-8 -*-
"""NLP_Lab8_NER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d3ClShRhxV-fJ_090pPCYLrd1XeSNWBI
"""

import spacy

nlp = spacy.load('en_core_web_sm')

text = "Barak Obama was born in Hawai. he was the 44th President of the United States"

doc = nlp(text)
for ent in doc.ents:
  print (ent.text, ent.label_)

text = "Apple is looking at buying U.K. startup for $1 billion"

