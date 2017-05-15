#!/usr/bin/python
# coding:utf-8

from tgrocery import Grocery

if __name__ == '__main__':
    grocery = Grocery('sample')

    train_src = [

    ]

    grocery.train(train_src)
    grocery.save()


    new_grocery = Grocery('sample')
    new_grocery.load()

    print('=======')
