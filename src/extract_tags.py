#coding=utf-8
"""
Created Time : 2018/6/28 10:53
@Author      : Chill Yu
@Description : 
"""
import pandas as pd
import numpy as np
from src import data_process as dp
from pyhanlp import *
from jpype import *

data = dp.get_xls_data()
# print(data.shape[0])

title, category, content, tags = dp.get_data_by_row(data, 2728)
article = category + ':' + title + '。' + content

def article_segment(article):
    print(HanLP.newSegment('perceptron').segment(article))
    print(HanLP.segment(article))

def gen_tags_all():
    # print(HanLP.segment(article))
    with open('../out/tags.txt', 'w', encoding='utf-8') as fw:
        for i in range(data.shape[0]):
            title, category, content, labels = dp.get_data_by_row(data, i)
            article = category + ':' + title + '。' + content
            tags = []
            keywords = HanLP.extractKeyword(article, 8)
            for word in keywords:
                if len(word) > 1:
                    tags.append(word)
            phrases = HanLP.extractPhrase(article, 6)
            for word in phrases:
                tags.append(str(word))
            newwords = HanLP.extractWords(article, 4)
            for word in newwords:
                tags.append(str(word))

            # segment = HanLP.newSegment().enableAllNamedEntityRecognize(True)
            # term_list = segment.seg(article)
            term_list = HanLP.segment(article)
            # print(term_list)
            ners = []
            pos_list = ["nr", "nrj", "nrf", "nr1", "nr2",
                        # "ns", "nsf",
                        # "nt", "ntc", "ntcf", "ntcb", "ntch", "nto", "ntu", "nts", "nth"
                        ]
            for term in term_list:
                if str(term.nature) in pos_list and len(ners) < 2:
                    ners.append(term.word)
                    tags.append(term.word)
            print(tags)
            for tag in tags:
                fw.write(tag + ',')
            fw.write('\n')


def gen_tags_keywords():
    with open('../out/tags_keywords.txt', 'w', encoding='utf-8') as fw:
        for i in range(data.shape[0]):
            title, category, content, labels = dp.get_data_by_row(data, i)
            article = category + ':' + title + '。' + content
            keywords = HanLP.extractKeyword(article, 10)
            tags = []
            for word in keywords:
                if len(word) > 1 and len(tags) < 5:
                    tags.append(word)
                    fw.write(word + ',')
            fw.write('\n')
            print(tags)


def evaluation(file_path):
    df = pd.read_csv(file_path, header=-1)
    hit = 0
    sum_labels = 0
    for i in range(data.shape[0]):
        title, category, content, labels = dp.get_data_by_row(data, i)
        sum_labels += len(labels)
        hit_list = []
        for j in range(df.shape[1]):
            if df.iat[i, j] != df.iat[i, j]:
                break
            elif df.iat[i, j] in labels:
                hit_list.append(df.iat[i, j])
                hit += 1
        print(hit_list)

    print(hit)
    print(sum_labels)
    print(hit/sum_labels)

if __name__ == '__main__':
    # article_segment()
    # gen_tags_keywords()
    # gen_tags_all()
    evaluation('../out/tags.txt')  #0.22508972825158094
    # evaluation('../out/tags_keywords.txt')  # 0.13049051444197574
