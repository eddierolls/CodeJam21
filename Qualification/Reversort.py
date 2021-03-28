# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:54:01 2020

@author: edwar
"""

def main():
    t = int(input()) # read a line with a single integer
    for testNo in range(1, t + 1):
        
        N = int(input())
        L = [(i,int(s)) for i,s in enumerate(input().split(" "))]
        L.sort(key=lambda x:x[1])
        L = [(L[i][0],i) for i in range(N)]
        L.sort(key=lambda x:x[0])
        L = [L[i][1] for i in range(N)]
        
        score = 0
        for i in range(N-1):
            j = L.index(i)
            score += (j-i+1)
            L = L[:i]+list(reversed(L[i:j+1]))+L[j+1:]
            
        
        print("Case #{}: {}".format(testNo, int(score)))

main()