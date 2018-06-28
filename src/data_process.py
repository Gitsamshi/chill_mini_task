"""
Created Time : 2018/6/27 22:58
@Author      : Chill Yu
@Description : 
"""
import pandas


def get_xls_data():
    file_path = '../data/toutiao_article.xls'
    df = pandas.read_excel(file_path)
    return df


def get_data_by_row(df, i):
    title = df.at[i, '标题']
    category = df.at[i, '分类']
    content = df.at[i, 'content']
    tags = df.at[i, 'label'].split(',')
    return title, category, content, tags


if __name__ == '__main__':
    data = get_xls_data()
    a, b, c, d = get_data_by_row(data, 0)
    print(a+'。'+c)
    print(d)

