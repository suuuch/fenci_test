#-*- coding: utf-8 -*-

import re, jieba
from temp_string import readme_string

class fenci_test(object):
    def __init__(self):
        pass

    def clean_url(self, input_str):
        reobj = re.compile('[a-zA-z]+://[^\s|\u4e00-\u9fa5]*')
        result, number = reobj.subn(' ', input_str)
        # print(number)
        return result

    def clean_email(self, input_str):
        reobj = re.compile('\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*')
        result, number = reobj.subn(' ', input_str)
        # print(number)
        return result

    def clean_number(self, input_str):
        reobj = re.compile('\d+')
        result, number = reobj.subn(' ', input_str)
        # print(number)
        return result

    def clean_special_char(self, input_str):
        reobj = re.compile('[^\u4e00-\u9fa5|,|;|:|\w]')
        result, number = reobj.subn(' ', input_str)
        # print(number)
        return result

    def sentence_split(self, input_str):
        reobj = re.compile(r'[\.|!|?|。|！|？]')
        return reobj.split(input_str)

    def fenci_jieba(self, input_str_list, cut_all=False):
        # 默认是精确模式
        if isinstance(input_str_list, list):
            return map(lambda x: jieba.cut(x, cut_all= cut_all), input_str_list)
        else:
            assert 'input str should be list!'

    def lower_en_word(self, input_str_list):
        if isinstance(input_str_list, list):
            return map(lambda x: x.lower(), input_str_list)
        else:
            assert 'input str should be list!'

if __name__ == '__main__':
    '''
    1.过滤网址
    分句
    2.jieba分词
    3.去标点，去空格
    4.去掉长度小于3的词
    5.去掉non-apha 词，英文去掉\w 词
    6.英文转小写
    7.去停顿词
    '''

    ft = fenci_test()
    rst = ft.clean_url(readme_string)
    rst = ft.clean_email(rst)
    rst = ft.sentence_split(rst)
    rst = ft.fenci_jieba(rst)

    result_list = []
    for r in rst:
        r = map(ft.clean_number, r)
        word_list = (map(ft.clean_special_char, r))
        word_list = list(filter(lambda x: len(x) >= 3 , word_list))
        result_list.extend(ft.lower_en_word(word_list))

    print(set(result_list))
