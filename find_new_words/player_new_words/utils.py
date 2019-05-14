#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2019/5/9 22:56 
import pickle
import jieba


def open_txt(file_name):
    with open(file_name) as f:
        while True:
            line = f.readline()
            if not line:
                return
            yield line.strip()


def get_stopwords():
    with open('data/stopword.txt', 'rb')as f:
        stopwords = [line.strip() for line in f]
    return set(stopwords)


def gene_model(model, file_name):
    with open(file_name, 'wb') as fw:
        pickle.dump(model, fw)


def load_model(file_name):
    with open(file_name, 'rb') as f:
        models = pickle.load(f)
    return models


def gene_ngram(input_list, n):
    res = []
    for i in range(1, n+1):
        res.extend(zip(*[input_list[j:]for j in range(i)]))
    return res


def load_dic(file_name):
    """
    加载外部词集
    :param file_name:
    :return:
    """
    word_freq = {}
    print('------> 加载外部词集')
    with open(file_name, 'rb') as f:
        for line in f:
            try:
                line_list = line.strip().split(' ')
                if int(line_list[1]) > 2:
                    word_freq[line_list[0]] = line_list[1]
            except Exception as e:
                print(line)
                continue
    return word_freq
