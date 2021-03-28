# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:54:01 2020

@author: edwar
"""
import math
import random
import time

def inputHere(f = None):
    if f is None:
        out = input()
    else:
        out = f.readline().strip()
    return out

def fakeScores():
    playerSkill = [random.uniform(-3,3) for _ in range(100)]
    questionDifficulty = [random.uniform(-3,3) for _ in range(10000)]
    scores = [[-1]*10000 for _ in range(100)]
    for x in range(100):
        for y in range(10000):
            s = 1/(1+math.exp(-(playerSkill[x]-questionDifficulty[y])))
            r = random.random()
            scores[x][y] = 1 if s>r else 0
    for y in range(10000):
        r = random.random()
        if r>0.5:
            scores[0][y] = 1
    return scores

def crossEntropy(y,yhat):
    return (y*math.log(yhat) + (1-y)*math.log(1-yhat))

def Hinge(y,yHat):
    return max(0, y - (1-2*y)*yHat)

def main(fileName = None):
    if fileName is not None:
        fileName = open(fileName,'r')
    T = int(inputHere(fileName))
    P = int(inputHere(fileName))
    t = time.time()
    scores = fakeScores()
    totalScore=0
    for testNo in range(1, T + 1):
        """
        scores = []
        for _ in range(100):
            scores.append([int(s) for s in inputHere(fileName)])
        """
        playerScore = [sum(x) for x in scores]
        playerRank = sorted(enumerate(playerScore),key=lambda x:x[1])
        playerRank = [(i,playerRank[i][0]) for i in range(100)]
        playerRank.sort(key=lambda x:x[1])
        playerSkill = [-3+(playerRank[i][0]/100)*6 for i in range(100)]
        playerSkillExp = [math.exp(-x) for x in playerSkill]
        questionScore = [sum([scores[j][i] for j in range(100)]) for i in range(10000)]
        questionRank = sorted(enumerate(questionScore),key=lambda x:x[1])
        questionRank = list(reversed(questionRank))
        questionRank = [(i,questionRank[i][0]) for i in range(10000)]
        questionRank.sort(key=lambda x:x[1])
        questionDifficulty = [-3+(questionRank[i][0]/10000)*6 for i in range(10000)]
        questionDifficultyExp = [math.exp(x) for x in questionDifficulty]
        
        biggestSurprise = -99999
        surpriseIndex = 0
        for x in range(100):
            surpriseScore = 0
            for y in range(10000):
                s = 1/(1+(playerSkillExp[x]*questionDifficultyExp[y]))
                #surpriseScore+=-crossEntropy(scores[x][y],s)
                surpriseScore+=Hinge(scores[x][y],s)
            #print(surpriseScore,x+1)
            if surpriseScore>biggestSurprise:
                surpriseIndex = x+1
                biggestSurprise = surpriseScore
        
        print("Case #{}: {}".format(testNo, str(surpriseIndex)))
        if surpriseIndex==1:
            totalScore+=1
    print(totalScore)
#main('cheating_detection_sample_ts1_input2.txt')
main()