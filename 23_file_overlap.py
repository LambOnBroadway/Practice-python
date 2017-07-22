# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:13:25 2017

"""

with open('prime_numbers.txt','r') as open_prime:
    prime_numbers=list(map(int,open_prime.read().splitlines()))
with open('happy_numbers.txt','r') as open_happy:
    happy_numbers=list(map(int,open_happy.read().splitlines()))
overlap=sorted(list(set(happy_numbers).intersection(set(prime_numbers))))

 


