# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:12:49 2021

@author: edwar
"""
# python interactive_runner.py python local_testing_tool.py 0 -- python MedianSort.py

import sys
import copy

def nextGuess(bounds):
    if bounds[1]-bounds[0]==1:
        return copy.copy(bounds)
    else:
        return [bounds[0]+((bounds[1]-bounds[0])//3),bounds[0]+((bounds[1]-bounds[0])*2)//3]

def main():
    T,N,Q = [int(x) for x in input().split(" ")]
    for testNo in range(1, T + 1):
        
        print("1 2 3")
        sys.stdout.flush()
        Q-=1
        x = int(input())
        
        arr = [(x%3)+1,x,((x+1)%3)+1]
        
        for i in range(3,N):
            placed = False
            bounds = [0,i]
            guesses = nextGuess(bounds)
            while not placed:
                print(" ".join([str(arr[guesses[0]]),str(arr[guesses[1]]),str(i+1)]))
                # print(guesses,bounds,i,arr)
                sys.stdout.flush()
                Q-=1
                x = int(input())
                if x == i+1:
                    bounds = copy.copy(guesses)
                    if bounds[1]-bounds[0]==1:
                        placed = True
                        arr.insert(bounds[1],i+1)
                elif x==arr[guesses[0]]:
                    bounds = [bounds[0],guesses[0]]
                    if bounds[1]==bounds[0]:
                        placed = True
                        arr.insert(bounds[0],i+1)
                elif x==arr[guesses[1]]:
                    if bounds[1]-guesses[1]==1:
                        placed = True
                        arr.insert(bounds[1],i+1)
                    bounds = [guesses[1],bounds[1]]
                guesses = nextGuess(bounds)
                # print(guesses,bounds)
        
        print(" ".join([str(s) for s in arr]))
        sys.stdout.flush()
        result = int(input())
        if result == -1:
            quit()

main()