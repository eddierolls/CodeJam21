# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:12:49 2021

@author: edwar
"""


import sys
def main():
    t,B = [int(x) for x in input().split(" ")] # read a line with a single integer
    for testNo in range(1, t + 1):
        
        if B==10:
            out = ans1(B)
        elif B==20:
            out = ans2(B)
        else:
            out = ans3(B)
        
        print(out)
        sys.stdout.flush()
        result = input()
        if result == 'N':
            quit()

main()