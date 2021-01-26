'''2798'''
# num, lim = input().split()
# num= int(num)
# lim= int(lim)
# num_list= list(map(int, input().split()))
# max_num=0
#
# for i in range(num):
#     for j in range(i+1,num):
#         for k in range(j+1,num):
#             if (num_list[i]+num_list[j]+num_list[k]) > max_num:
#                 if(num_list[i]+num_list[j]+num_list[k]<=lim):
#                     max_num= num_list[i]+num_list[j]+num_list[k]
#             # print(num_list[i], num_list[j], num_list[k])
# print(max_num)

'''2231'''
# num= int(input())
# result=0
# for i in range(1, num+1):
#     a= list(map(int, str(i)))
#     result = i+sum(a)
#     # print(result)
#     if result==num:
#         print(i)
#         break
#     if i==num:
#         print(0)

'''	7568'''
# iter= int(input())
# array=[]
# for _ in range(iter):
#     weight, height = map(int, input().split())
#     array.append((weight, height))
# for i in array:
#     rank=1
#     for j in array:
#         if i[0]<j[0]  and i[1] <j[1]:
#             rank+=1
#     print(rank , end=" ")

'''1018'''
# def check_BW(ex):
#     cnt1=0
#     for i in range(8):
#         for j in range(8):
#             i_ = (0 if i in [0,2,4,6] else 1)
#             j_ = (0 if j in [0,2,4,6] else 1)
#             if (i_==0 and j==0) or (i_ ==1 and j_ ==1):
#                 if ex[i][j] != 'B':
#                     cnt1+=1
#             if(i_ ==0 and j_==1) or (i_==1 and j_ ==0):
#                 if ex[i][j] != 'W':
#                     cnt1+=1
#     cnt2 =0
#     for i in range(8):
#         for j in range(8):
#             i_ = (0 if i in [0, 2, 4, 6] else 1)
#             j_ = (0 if j in [0, 2, 4, 6] else 1)
#             if (i_ == 0 and j == 0) or (i_ == 1 and j_ == 1):
#                 if ex[i][j] != 'W':
#                     cnt2 += 1
#             if (i_ == 0 and j_ == 1) or (i_ == 1 and j_ == 0):
#                 if ex[i][j] != 'B':
#                     cnt2 += 1
#     return min(cnt1, cnt2)
#
# n,m = map(int, input().split())
# # print(n,m)
# s= [list(input()) for i in range(n)]
# check = list()
# for i in range(n-7):
#     for j in range(m-7):
#         ex= [z[(0+j) : (8+j)] for z in s[(0+i):(8+i)]]
#         check.append(check_BW(ex))
# print(check)
#--------------------------------------------------------------
# from copy import copy, deepcopy
# n,m = map(int,input().split())
# a, ans = [], []
# for _ in range(n):
#     a.append(list(input()))
#
#
# for i in range(n-7):
#     for j in range(m-7):
#         cnt1, cnt2 = 0,0
#
#         # 체스판 경우의 수 slicing
#         c = [a[i+x][j:j+8] for x in range(8)]
#         init = deepcopy(c)
#
#         if init[0][0] == "W":
#             cnt1 = 1
#
#          # 첫 체스 시작판이 Black 인 경우
#         c[0][0] = "B"
#         for y in range(0,7):
#             for x in range(0,7):
#                 if c[y][x] == "B":
#                     if c[y+1][x] == "B":
#                         c[y+1][x] = "W"
#                         cnt1 +=1
#                     if c[y][x+1] == "B":
#                         c[y][x+1] = "W"
#                         cnt1 += 1
#                 else:
#                     if c[y+1][x] == "W":
#                         c[y+1][x] = "B"
#                         cnt1 +=1
#                     if c[y][x+1] == "W":
#                         c[y][x+1] = "B"
#                         cnt1 += 1
#
#         if (c[7][7] == c[6][7] or c[7][7] == c[7][6]):
#             cnt1 += 1
#
#         #  첫 체스 시작판이 White 인 경우
#         if init[0][0] == "B":
#             cnt2 += 1
#         init[0][0] = "W"
#         for y in range(0,7):
#             for x in range(0,7):
#                 if init[y][x] == "B":
#                     if init[y+1][x] == "B":
#                         init[y+1][x] = "W"
#                         cnt2 +=1
#                     if init[y][x+1] == "B":
#                         init[y][x+1] = "W"
#                         cnt2 += 1
#                 else:
#                     if init[y+1][x] == "W":
#                         init[y+1][x] = "B"
#                         cnt2 +=1
#                     if init[y][x+1] == "W":
#                         init[y][x+1] = "B"
#                         cnt2 += 1
#         if (init[7][7] == init[6][7] or init[7][7] == init[7][6]):
#             cnt2 += 1
#
#         ans.append(min(cnt1,cnt2))
#
# print(min(ans))

'''1436'''
# # num = int(input())
# # print((num-1)*1000+666)
# num = int(input())
# init=666
# while(num):
#     if '666' in str(init):
#         num-=1
#         # print(num)
#     init+=1
#     # print("init",init)
# print(init-1)