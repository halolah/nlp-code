#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2019/4/14 22:20 
"""
使用逆向最大匹配算法(BMM)实现中文分词
"""
words_dic = []


def init():
    """
    read and load system dict.
    :return:
    """
    with open("dic/dic.txt", encoding="utf-8") as dic_input:
        for words in dic_input:
            words_dic.append(words.strip())


def cut_word(raw_sentence, word_dic):
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
    words = "/".join(cut_word_list)
    return words


def main():
    init()
    while True:
        print("Please input your words：")
        input_str = input()
        if not input_str:
            break
        result = cut_word(input_str, words_dic)
        print("分词结果: {}".format(result))


if __name__ == '__main__':
    main()



