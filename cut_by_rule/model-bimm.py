#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2019/4/15 11:38

"""
使用双向最大匹配算法(FMM)实现中文分词
"""


words_dic = []


def init():
    """
    read  and load dic file.
    :return:
    """
    with open("dic/dic.txt", encoding="utf-8") as dic_input:
        for word in dic_input:
            words_dic.append(word.strip())


def bmm_cut_word(raw_sentence, word_dic):
    """
    cut words if words in words dic
    :param raw_sentence: user input words
    :param word_dic: system words dic
    :return:
    """
    # 统计字典中词的最大长度
    word_dic_length = max(len(word) for word in word_dic)

    # 统计输入语句的最大长度
    sentence = raw_sentence.strip()
    raw_length = len(sentence)

    cut_word_list = []
    while raw_length > 0:
        max_length = min(word_dic_length, raw_length)
        sub_sentence = sentence[-max_length:]
        while max_length > 0:
            if sub_sentence in word_dic:
                cut_word_list.append(sub_sentence)
                break
            elif max_length == 1:
                cut_word_list.append(sub_sentence)
                break
            else:
                max_length = max_length - 1
                sub_sentence = sub_sentence[-max_length:]
        sentence = sentence[0: -max_length]
        raw_length = raw_length - max_length
    cut_word_list.reverse()
    return cut_word_list


def fmm_cut_words(raw_sentence, word_dic):
    """
    cut words if words in words dic
    :param raw_sentence: user input words
    :param word_dic: system words dic
    :return:
    """
    # 统计字典中词的最大长度
    max_length = max(len(word)for word in word_dic)

    # 统计输入语句的最大长度
    sentence = raw_sentence.strip()
    word_length = len(sentence)

    cut_word_list = []
    while word_length > 0:
        max_cut_length = min(word_length, max_length)
        sub_sentence = sentence[0:max_cut_length]
        while max_cut_length > 0:
            if sub_sentence in words_dic:
                cut_word_list.append(sub_sentence)
                break
            elif max_cut_length == 1:
                cut_word_list.append(sub_sentence)
                break
            else:
                max_cut_length = max_cut_length - 1
                sub_sentence = sub_sentence[0:max_cut_length]
        sentence = sentence[max_cut_length:]
        word_length = word_length - max_cut_length
    return cut_word_list


def bimm_cut_words(raw_sentence, word_dic):
    """
    cut words if words in words dic
    :param raw_sentence: user input words
    :param word_dic: system words dic
    :return:
    """
    bmm_word_list = bmm_cut_word(raw_sentence, word_dic)
    fmm_word_list = fmm_cut_words(raw_sentence, word_dic)
    bmm_word_len = len(bmm_word_list)
    fmm_word_len = len(fmm_word_list)
    if bmm_word_len != fmm_word_len:
        if bmm_word_len < fmm_word_len:
            return bmm_word_list
        else:
            return fmm_word_len
    else:
        fsingle = 0
        bsingle = 0
        is_same = True
        for i in range(len(fmm_word_list)):
            if fmm_word_list[i] not in bmm_word_list:
                is_same = False
            if len(fmm_word_list[i]) == 1:
                fsingle = fsingle + 1
            if len(bmm_word_list[i]) == 1:
                bsingle = bsingle + 1
        if is_same:
            return fmm_word_list
        elif bsingle > fsingle:
            return fmm_word_list
        else:
            return bmm_word_list


def main():
    """
    main function
    :return:
    """
    init()
    while True:
        print("Please input your words：")
        input_str = input()
        if not input_str:
            break
        result = bimm_cut_words(input_str, words_dic)
        print("分词结果: {}".format(result))


if __name__ == "__main__":
    main()
