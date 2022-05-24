#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:52:09 2022

@author: gideon
"""

import time
       
def cbt(): 
    user = input("CBT candidate Name: ")
    print('Welcome',user)
    time.sleep(1)
    questions = {1: ['Which of this is the capital of Nigeria?\n(a) Lagos\n(b)Kano\n(c)Abuja', 'c'],
                  2: ['What is the number of states in Nigeria?\n(a)37\n(b)36\n(c)44','b'],
                  3: ['What is the number of LGAs in Nigeria?\n(a)768\n(b)774\n(c)780','b'],
                  4: ['Who is INEC chairman?\n(a)Prof Mamhood Yakubu\n(b)Prof Wole Soyinka\n(c)Prof Adeyami Paul','a'],
                  5: ['How many political parties participated in the 2019 presidential election?\n(a)18\n(b)77\n(c)73','c']}
    total_score = 25
    score = 0
    options = ['a','b','c']
    for i in questions:
        que = questions[i]
        print('\n')
        print(i,'.',que[0])
        ans = str(input("Submit answer: ")).strip().lower()
        if ans not in options:
            print("Error! Only letters a-c allowed!")
            ans = str(input("Submit answer: ")).strip().lower()
        if ans in que[1]:
            score += 5
    percent = score/total_score
    percentage = "{:.0%}".format(percent)
    time.sleep(1)
    print('\n')
    print('DEAR',user,', Thank you for taking the test.')
    print('YOUR TOTAL SCORE IS',score,'.')
    print('YOUR PERCENTAGE SCORE IS', percentage,'.')
    if percent >= 0.5:
        print("CONGRATULATIONS!!! YOU PASSED.")
    else:
        print("BELOW PASS, TRY AGAIN NEXT TIME.")
        
cbt()