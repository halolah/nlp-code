#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2019/4/13 10:20

"""
使用正向最大匹配算法(FMM)实现中文分词
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


def cut_words(raw_sentence, word_dic):
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
    words = "/".join(cut_word_list)
    return words


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
        result = cut_words(input_str, words_dic)
        print("分词结果: {}".format(result))


if __name__ == "__main__":
    main()
