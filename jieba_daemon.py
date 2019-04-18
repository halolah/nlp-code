#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2019/4/15 21:22 

import jieba

# 全模式
def full_cut_word(word_list):
    full_seg_list = jieba.cut(word_list, cut_all=True, HMM=True)
    return full_seg_list

# 精确模式
def default_cut_word(word_list):
    default_seg_list = jieba.cut(word_list, cut_all=False)
    print("Default Mode: " + "/ ".join(default_seg_list))
    return default_seg_list

# 搜索引擎模式
def search_cut_word(word_list):
    search_seg_list = jieba.cut_for_search(word_list)
    print(", ".join(search_seg_list))
    return search_seg_list

def main():
    while True:
        print("Please input your words：")
        input_str = input()
        if not input_str:
            break
        res = full_cut_word(input_str)
        print("分词结果是" + "/".join(list(res)))

if __name__ == '__main__':
    main()
