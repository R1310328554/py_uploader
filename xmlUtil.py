# -*- coding:utf-8 -*-
from xml.etree import ElementTree


def print_node(node):
    '''打印结点基本信息'''
    print("==============================================")
    print("node.attrib:%s" % node.attrib)

    ty = type(node.attrib)
    print(ty)
    dd = dict(node.attrib)


    try:
        aa = node.attrib['age']

        print(aa)
        age = dd.get("age");
        if aa != "":
            print("node.attrib['age']:%s" % node.attrib['age'])
    except Exception as e:
        print(11)

    print("node.tag:%s" % node.tag)
    print("node.text:%s" % node.text)


def read_xml(text):
    '''读xml文件'''
    # 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）
    # root = ElementTree.parse(r"D:/test.xml")
    root = ElementTree.fromstring(text)

    # 获取element的方法
    # 1 通过getiterator
    lst_node = root.getiterator("person")
    for node in lst_node:
        print_node(node)

def read_xml_from_txt(text, subnode="vid"):
    '''读xml文件'''
    # 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）
    # root = ElementTree.parse(r"D:/test.xml")
    root = ElementTree.fromstring(text)

    # 获取element的方法
    # 1 通过getiterator
    # 3 .find方法
    node_find = root.find(subnode)
    # print_node(node_find)
    return node_find.text


if __name__ == '__main__':

    srctext = '''<?xml version="1.0" encoding="utf-8"  standalone="no" ?>
<root><s>o</s><vid>h0548n9cfsz</vid></root>'''

    tt = read_xml_from_txt(srctext)
    print(tt)