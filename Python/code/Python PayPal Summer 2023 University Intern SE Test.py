#!/bin/python3
import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
"""
def fizzBuzz(n):
    for n in range (1,n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)




def isWeird(n):
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")



n = int(input())
for n in range(0,n):
    listNum = []
    listNum.append(print(n**2))

"""
"""
def getUniqueCharater(s):

    unique = {} # Created dict 

    for count in s:
        if count in unique:
            unique[count] += 1
        else:
            unique[count] = 1

    for i in range(len(s)):
        if unique[s[i]] == 1:
            return i + 1
    return -1

print(getUniqueCharater("hello"))
"""



########## PLUS MINUS #####################
"""
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for num in arr:
        if num == 0:
            zero += 1
        elif num < 0:
            negative += 1
        elif num > 0:
            positive += 1
            
    print(positive / len(arr))
    print(negative / len(arr))
    print(zero / len(arr))

plusMinus([1,1,0,-1,-1])
"""
################################################

######## miniMaxSum ####################
"""
def miniMaxSum(arr):
    arr.sort()
    # find the smallest number
    smallestNum = arr[0]
    largestNUm = arr[-1]

    sum = 0

    for num in arr:
        sum += num

    print((sum - largestNUm),(sum-smallestNum))


miniMaxSum([5,4,3,2,1])

"""
####################################################

####### timeConverstions ####################
"""
from datetime import datetime

def timeConversion(s):

    s = datetime.strptime(s,'%I:%M:%S%p') #<---- allows string to be read as time

    military = s.strftime('%H:%M:%S') #<------ Changes s.time into 24-Hour time with proper format
    return military

print(timeConversion('1:05:45PM'))

"""
################################
###### breakingScores ######################
"""
def breakingRecords(scores):
    least = 0
    greatest = 0
    recordsBroken = []


    for i in range(len(scores)-1):
        if scores[i] > scores[i + 1]:
            greatest += 1
        if scores[i] < scores[i + 1]:
            least += 1

    recordsBroken.append(greatest - 2)
    recordsBroken.append(least)
    print(recordsBroken)


print(breakingRecords([10,5,20,20,4,5,2,25,1]))
"""

"""
def breakingRecords(scores):
    most_breaks = 0
    least_breaks = 0

    most_points = scores[0]
    least_points = scores[0]

    for i in range(1, len(scores)):
        if scores[i] > most_points:
            most_breaks += 1
            most_points = scores[i]
        elif scores[i] < least_points:
            least_breaks += 1
            least_points = scores[i]
    return [most_breaks, least_breaks]

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result = breakingRecords(scores)
print(result[0], result[1])


"""

def minValue(a,b,c) -> int:
    minVal = a

    if b < minVal:
        minVal = b
    if c < minVal:
        minVal = c
    return minVal

print(minValue(3,2,5))


def maxValNumOfOccurrences(nums):
    maxVal = nums[0]
    count = 0

    for val in nums:
        if val > maxVal:
            maxVal = val
            count = 1
        elif val == maxVal:
            count += 1
    return [maxVal,count]

print(maxValNumOfOccurrences([2,7,11,11,2,5,7]))


