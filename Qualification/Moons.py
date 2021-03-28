# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:54:01 2020

@author: edwar
"""

def main():
    t = int(input()) # read a line with a single integer
    for testNo in range(1, t + 1):
        
        x,y,s = input().split(" ")
        x = int(x)
        y = int(y)
        s = list(s)
        
        if s.count('?')==len(s):
            score = 0
            print("Case #{}: {}".format(testNo, score))
            continue
        
        for i in range(len(s)):
            if s[i]!='?':
                firstLetter = s[i]
                firstIndex = i
                break
        
        s = [firstLetter]*(firstIndex) + s[i:]
        
        score = 0
        for i in range(1,len(s)):
            if s[i]=='?':
                s[i]=s[i-1]
            elif s[i]=='C' and s[i-1]=='J':
                score+=y
            elif s[i]=='J' and s[i-1]=='C':
                score+=x
        
        print("Case #{}: {}".format(testNo, score))

main()