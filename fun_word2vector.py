# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:44:09 2018

@author: issuser
"""

## 1 text to vextor

def text_to_vector (df, column, index):
    text_vector = []
    for i in range(len(df)):
        sentence = df[column][i]
        sentence = sentence[1:]
        sentence = sentence[:-1]
        sentence = sentence.replace("'",'')
        sentence = sentence.replace(" ", '')
        sentence_vector = []
        for j in sentence.split(','):
            try:
                sentence_vector.append(model[j])
            except KeyError:
                pass
            continue
        text_vector.append(sentence_vector)
    return (text_vector)
    
    text_vector = []
    for i in range(len(text)):
        sentence = text['tokenized_words'][i]
        sentence = sentence[1:]
        sentence = sentence[:-1]
        sentence = sentence.replace("'",'')
        sentence = sentence.replace(" ", '')
        sentence_vector = []
        for j in sentence.split(','):
            try:
                sentence_vector.append(model[j])
            except KeyError:
                pass
            continue
        text_vector.append(sentence_vector)

# 2 change n*300 to 1*300
def get_balanced (unbalanced_vector):
    balanced_vector = numpy.zeros(shape=(len(unbalanced_vector), 300))
    for i in range(len(unbalanced_vector)):
        for j in range(len(unbalanced_vector[i])):
            balanced_vector[i] = balanced_vector[i] + unbalanced_vector[i][j]
        balanced_vector[i] = balanced_vector[i]/len(unbalanced_vector[i])
    return(balanced_vector)