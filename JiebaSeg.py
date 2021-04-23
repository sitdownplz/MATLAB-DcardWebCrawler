# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:44:26 2020

@author: tim
"""

import jieba


def WordSeg(Sentence):
    "jieba.set_dictionary('dict.txt.big.txt')"
    words = jieba.cut(Sentence,HMM=True)
    word_list = list(words);
    return word_list
