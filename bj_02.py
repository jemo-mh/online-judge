'''
8393'''
# num = int(input())
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)

''' 10171'''
# print('\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

'''2588'''
# a=int(input())
# # b=int(input())
# # a1= a//100
# # a2= (a-100*a1)//10
# # a3=a%10
# # b1= b//100
# # b2= (b-100*b1)//10
# # b3=b%10
# # print(a*b3)
# # print(a*b2)
# # print(a*b1)
# # print((a*b1)*100+(a*b2)*10+a*b3)


'''9498'''
# score= int(input())
# if score>=90:
#     print("A")
# elif(score>=80 and score<90 ):
#     print("B")
# elif(score>=70 and score<80):
#     print("C")
# elif(score>=60 and score<70):
#     print("D")
# else:
#     print("F")

'''14681'''
# x_cor= int(input())
# y_cor= int(input())
# if x_cor>0:
#     if(y_cor>0):
#         print(1)
#     else:
#         print(4)
# elif(x_cor<0):
#     if(y_cor>0):
#         print(2)
#     else:
#         print(3)

'''2753'''
# year=int(input())
# if year%4 ==0:
#     if year%100 == 0:
#         if year%400==0:
#             print(1)
#         else:
#             print(0)
#     else:
#         print(1)
# else:
#     print(0)

'''2884'''
# time =input().split()
# time = list(map(int, time))
# hour = time[0]
# min= time[1]
# if min>44:
#     print('{} {}'.format(hour, min-45))
# elif min<=44 and hour>0:
#     print('{} {}'.format(hour-1, min+15))
# else:
#     print('{} {}'.format(23, min+15))


'''15552'''
# import sys
# num=int(input())
# for i in range(num):
#     a,b =map(int, sys.stdin.readline().split())
#     print(a+b)
#

'''2741'''
# num = int(input())
# for i in range(1,num+1):
#     print(i)

'''2742'''
# num= int(input())
# list=[]
# for i in range(1,num+1):
#     list.append(i)
# list.reverse()
# for i in range(num):
#     print(list[i])

''' 11021'''
# iter= int(input())
# for i in range(iter):
#     a,b =map(int, input().split())
#     print('Case #{}: {}'.format(i+1, a+b))

''' 11022'''
# iter= int(input())
# for i in range(iter):
#     a,b =map(int, input().split())
#     print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))

'''10871'''
# A, X = map(int, input().split())
# listl=[]
# answer=[]
# listl= list(map(int, input().split()))
# for i in range(len(listl)):
#     if listl[i]<X:
#         print(listl[i],end=" ")

''' 10952'''
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A + B)
#         # print(A + B)
#     # if( (A==0 and B==0) or (A<0) or (B>10) ):
#     #     break
#     except:
#         break

'''1110'''
# cnt=0
# tmp=0
# num = int(input())
# num1=num
# while True:
#     a = num // 10
#     b = num % 10
#     tmp=(a+b)%10
#     num=10*b+tmp
#     cnt += 1
#     if(num1==num):
#         print(cnt)
#         break






