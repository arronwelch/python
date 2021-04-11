#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/12 0:14

# # O(1)
# print('Hello World')
#
# n = 10
#
# # O(n)
# for i in range(n):
#     print('Hello World',i)
#
# # O(n**2)
# for i in range(n):
#     for j in range(n):
#         print('Hello World',i,j)
#
# # O(n**3)
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print('Hello World',i,j,k)
#
# # 1.run time is differ in computer A and computer B
# # 2.ms s min hour month year
# # 3.O(1) O(n) O(n^2) O(n^3)
#
#
# print('Hello World1')
# print('Hello World2')
# print('Hello World3')  # O(3) -> O(1)
#
# for i in range(n):
#     print('Hello World', i)
#     for j in range(n):
#         print('Hello World',i,j) # n(1+n) n^2+n -> O(n^2)

n = 1024
i = 1
while n > 1:
    print(i,n)
    i+=1
    n = n//2    # 2^6 = 64
                # log2(64) = 6
    # O(logn) half-problem in one done

# normal time complexity:
# O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^2 * logn) < O(n^3)

# complex problem:
# O(n!) O(2^n) O(n^n)

# How to fast judge Algorithm time complexity:
# 1)n range
# 2)loop half-problem:logn
# 3)k-loop:n^k
