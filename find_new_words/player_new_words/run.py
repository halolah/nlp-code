#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2019/5/9 23:00 

import jieba
import os
from find_new_words.player_new_words.model import Model
from find_new_words.player_new_words.utils import get_stopwords, load_dic, gene_ngram, load_model, gene_model
from find_new_words.player_new_words.config import basedir


def load_data(file_name, stopwords):
    data = []
    with open(file_name, 'rb')as f:
        for line in f:
            word_list = [x for x in jieba.cut(line.strip(), cut_all=False)if x not in stopwords]
            data.append(word_list)
    return data


def load_tree(data):
    print("------>插入节点")
    for word_list in data:
        ngrams = gene_ngram(word_list, 3)
        for d in ngrams:
            root.insert(d)


if __name__ == '__main__':
    topN = 5
    root_name = basedir + os.path.sep + "data" + os.path.sep + "root.pkl"
    stopwords = get_stopwords()
    if os.path.exists(root_name):
        root = load_model(root_name)
    else:
        dic_dir = basedir + os.path.sep + "data" + os.path.sep + "dict.txt"
        word_fre = load_dic(dic_dir)
        root = Model('*', data=word_fre)
        gene_model(root, root_name)

    file_name = basedir + os.path.sep + "data" + os.path.sep + "demo.txt"
    data = load_data(file_name, stopwords)
    load_tree(data)

    result, add_word = root.find_word(topN)
    print("\n----\n", '增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
    print('#############################')
    for word, score in add_word.items():
        print(word + ' ---->  ', score)
    print('#############################')

    # 前后效果对比
    test_sentence = '蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题'
    print('添加前：')
    print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))

    for word in add_word.keys():
        jieba.add_word(word)
    print("添加后：")
    print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))

