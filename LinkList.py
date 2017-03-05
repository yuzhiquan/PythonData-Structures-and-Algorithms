#coding:utf-8
import random

class LinkNode(object):
    '''
    LinkList
    '''
    def __init__(self,value):
        self.value = value
        self.next = None

    @staticmethod
    def create_linked_list(lterable):
        for index, value in enumerate(lterable):
            tmp = LinkNode(value)
            tmp.next = LinkNode(randomint())
            if index == 0:
                header = tmp
        return header


if __name__ == '__main__':
    s = LinkNode.create_linked_list(( i for i in xrange(10)))
    print s
