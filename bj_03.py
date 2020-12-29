''' 10818'''
# iter=int(input())
# num_list=[]
# num_list=input().split()
# num_list=list(map(int, num_list))
# num_list.sort()
# min=num_list[0]
# max= num_list[-1]
# print(min, max)

''' 2562'''
# num_list=[]
# for i in range(9):
#     num_list.append(int(input()))
# max=0
# flag=-1
# for i in range(9):
#     if int(num_list[i])>max:
#        max=num_list[i]
#        flag=i
# print(max)
# print(flag+1)

''' 2577'''
# num1 =int(input())
# num2 =int(input())
# num3= int(input())
# mul= num1*num2*num3
# str= str(mul)
# mul_list=[]
# for ch in str:
#     mul_list.append(ch)
# cnt0=0
# cnt1=0
# cnt2=0
# cnt3=0
# cnt4=0
# cnt5=0
# cnt6=0
# cnt7=0
# cnt8=0
# cnt9=0
#
# mul_list.sort()
# for i in range(len(mul_list)):
#     if int(mul_list[i])==0:
#         cnt0+=1
#     elif int(mul_list[i])==1:
#         cnt1+=1
#     elif int(mul_list[i])==2:
#         cnt2+=1
#     elif int(mul_list[i])==3:
#         cnt3+=1
#     elif int(mul_list[i])==4:
#         cnt4+=1
#     elif int(mul_list[i])==5:
#         cnt5+=1
#     elif int(mul_list[i])==6:
#         cnt6+=1
#     elif int(mul_list[i])==7:
#         cnt7+=1
#     elif int(mul_list[i])==8:
#         cnt8+=1
#     elif int(mul_list[i])==9:
#         cnt9+=1
# print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(cnt0, cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8, cnt9))

'''3052'''
# num_list=[]
# for i in range(10):
#     num_list.append(int(input())%42)
#
# num_list.sort()
# num_list=set(num_list)
# num_list=list(num_list)
# print(len(num_list))

'''	1546'''
import math
# import statistics as st
# course = int(input())
# score=[]
# score=input().split()
# score=list(map(int,score))
# max=0
# for i in range(len(score)):
#     if(score[i]>max):
#         max=score[i]
# for i in range(len(score)):
#     score[i]=(score[i]/max)*100
# print(st.mean(score))

'''8958'''
# iter= int(input())
# for i in range(iter):
#     num= input()
#     score=0
#     cnt=0
#     for j in range(len(num)):
#         if num[j] =='O':
#             cnt+=1
#             score+=cnt
#         elif num[j] =='X':
#             cnt=0
#             score+=0
#     print(score)

''' 4344'''
# n = int(input())
# for _ in range(n):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:])/nums[0]
#     cnt = 0
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1
#     rate = cnt/nums[0] *100
#     print(f'{rate:.3f}%')

'''15596'''
# num_list=list(map(int, input().split()))
# # print(num_list, len(num_list))
# def solve(list):
#     sum=0
#     for i in range(len(list)):
#         sum=sum+list[i]
#         print(list[i])
#     return sum
# print(solve(num_list))

'''4673'''
# def self_num():
#     li=[]
#     for i in range(1,10001):
#         if i <10:
#             res= i+i
#             li.append(res)
#         elif i<100:
#             res=i+(i//10)+(i%10)
#             li.append(res)
#         elif i<1000:
#             res=i+(i//100)+((i%100)//10) + i%10
#             li.append(res)
#         elif i<10000:
#             res = i + (i // 1000) + ((i % 1000) // 100) + (((i % 1000) % 100) // 10) + i % 10
#             if res<=10000:
#                 li.append(res)
#     li.sort()
#     li1 = [i for i in range(1,10001)]
#     notSelf=[item for item in li1 if item not in li]
#     for i in notSelf:
#         print(i)
#
# self_num()

'''1065'''
# num= int(input())
# def han(n):
#     cnt = 0
#     for i in range(1,n+1):
#         if i<=99:
#             cnt+=1
#         else:
#             num= list(map(int, str(i)))
#             if num[0]-num[1] == num[1]-num[2]:
#                 cnt+=1
#     return cnt
# print(han(num))
#



