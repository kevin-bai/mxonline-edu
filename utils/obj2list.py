# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/3/28 12:20'


# 根据class 获得 属性列表
# 用于xadmin 快速注册
def get_list_display(obj):
    doc = str(obj.__doc__)
    name = str(obj.__name__) + '('
    old_str = doc.replace(name, '').replace(')', '')
    result_list = old_str.split(', ')
    return result_list


def get_search_fields(obj):
    doc = str(obj.__doc__)
    name = str(obj.__name__) + '('
    old_str = doc.replace(name, '').rstrip(')')
    result_list = old_str.split(', ')
    # search_fields_arr = list_display_arr[:]
    result_list.remove('add_time')
    return result_list
