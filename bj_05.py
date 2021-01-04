'''10872'''
# num= int(input())
# answer=1
# for i in range(1,num+1):
#     answer=answer*i
# print(answer)

'''10870'''
# num=int(input())
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif n>=2:
#         return int(fibonacci(n-1)) + int(fibonacci(n-2))
#
# print(fibonacci(num))

'''2447'''
# num= int(input())
# arr=[['*']*num for _ in range(num)]
# v=num
# cnt=0
# while v!=1:
#     v/=3
#     cnt+=1
# # print(cnt)
#
# for cnt_ in range(cnt):
#     idx=[i for i in range(num) if (i//3 **cnt_)%3 ==1]
#     for i in idx:
#         for j in idx:
#             arr[i][j]=" "
#
# print("\n".join(["".join([str(i) for i in row]) for row in arr]))

'''11729'''
# n= int(input())
# move=[]
# def hanoi(n, a, b, c):
#     if n==1:
#         move.append([a,c])
#     else:
#         hanoi(n-1, a, c, b)
#         move.append([a,c])
#         hanoi(n-1, b, a, c)
# hanoi(n, 1, 2,3)
# print(len(move))
# print("\n".join([' '.join(str(i) for i in row)for row in move]))

