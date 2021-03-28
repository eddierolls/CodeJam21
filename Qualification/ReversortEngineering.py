# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:54:01 2020

@author: edwar
"""


def main():
    t = int(input()) # read a line with a single integer
    for testNo in range(1, t + 1):
        
        N,C = map(int,input().split(" "))
        C -= N-1
        if C<0:
            print("Case #{}: {}".format(testNo, "IMPOSSIBLE"))
            continue
        
        swaps = []
        for i in range(N-1):
            swapWith = min(N-1,C+i)
            swaps.append((i,swapWith))
            C-=(swapWith-i)
            
        if C>0:
            print("Case #{}: {}".format(testNo, "IMPOSSIBLE"))
            continue
        
        out = list(range(1,N+1))
        for a,b in reversed(swaps):
            out = out[:a] + list(reversed(out[a:b+1])) + out[b+1:]
        
        print("Case #{}: {}".format(testNo, " ".join([str(s) for s in out])))

main()