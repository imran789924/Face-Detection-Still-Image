#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:18:32 2020

@author: imran
"""

type(a)  =  [ [ 1 , 2 ] , [ 3 , 4 ] , [ 5 , 6 ] ]
b  =  [x for xs in a for x in xs ] #a list of just the "x"s

c = [a for _ in range(len(a))]

type(a) = asarray(a)

a.shape = a.astype('float32')

ab1 = expand_dims(a, axis=1)

a = 'imran'

b = [a for _ in range(10)]

c = list()

c.append(b)

d = asarray(c)