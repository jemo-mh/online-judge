'''10998'''
# listl=[]
# listl = input()
# listl= listl.split()
# print(listl)
# listl= list(map(int, listl))
# cal = listl[0] * listl[1]
# # print(cal)

'''10950'''
# iter = int(input())
# for i in range(iter):
#     listl = input()
#     listl = listl.split()
#     # print(listl)
#     listl = list(map(int, listl))
#     print(listl[0] + listl[1])

'''2438'''
# num=int(input())
# list=[]
# for i in range(1, num+1):
#     print("*" *i)

'''11654'''
# str= input()
# print(ord(str))


'''2440'''
# num=int(input())
# while(num>=1):
#     print("*"*num)
#     num=num-1


'''2523'''
# num= int(input())
# for i in range(1, num+1):
#     print("*" *i)
# num=num-1
# while(num>=1):
#     print("*"*num)
#     num=num-1

'''2438'''
# num=int(input())
# for i in range(1, num+1):
#     print(" "*(num-i)+"*"*i)
    # print("{0:>10}".format("*"*i))

'''1330'''
# num=[]
# num = input()
# num= num.split()
# # print(num)
# num= list(map(int, num))
#
# num0= num[0]
# num1= num[1]
# if(num0>num1):
#     print(">")
# elif(num0<num1):
#     print("<")
# else:
#     print('==')

'''10869'''
# num=[]
# num = input()
# num= num.split()
# # print(num)
# num= list(map(float, num))
# num0= num[0]
# num1= num[1]
# print("{:.0f}".format(num0+num1))
# print("{:.0f}".format(num0-num1))
# print("{:.0f}".format(num0*num1))
# print("{:.0f}".format(num0//num1))
# print("{:.0f}".format(num0%num1))

'''2739'''
# num=int(input())
# # for i in range(1,10):
# #     print("{} * {} = {}".format(num, i, num*i))

# iter=int(input())
# list2=[2,4,8,6]
# list3=[3,9,7,1]
# list4=[4,6,4,6]
# list5=[5]
# list6=[6]
# list7=[7,9,3,1]
# list8=[8,4,2,6]
# list9=[9,1]
# list0=[0]
# list1=[1]
# for i in range(iter):
#     num = input()
#     num = num.split()
#     num = list(map(int, num))
#     if num[0]%10 ==1:
#         out=num[1]%len(list1)
#         print("10")
#     elif num[0]%10 ==0:
#         out=num[1]%len(list0)
#         print(list0[out-1])
#     elif num[0]%10 ==2:
#         out=num[1]%len(list2)
#         print(list2[out-1])
#     elif num[0]%10 ==3:
#         out=num[1]%len(list3)
#         print(list3[out-1])
#     elif num[0]%10 ==4:
#         out=num[1]%len(list4)
#         print(list4[out-1])
#     elif num[0]%10 ==5:
#         out=num[1]%len(list5)
#         print(list5[out-1])
#     elif num[0]%10 ==6:
#         out=num[1]%len(list6)
#         print(list6[out-1])
#     elif num[0]%10 ==7:
#         out=num[1]%len(list7)
#         print(list7[out-1])
#     elif num[0]%10 ==8:
#         out=num[1]%len(list8)
#         print(list8[out-1])
#     elif num[0]%10 ==9:
#         out=num[1]%len(list9)
#         print(list9[out-1])

# for i in range(iter):
#     num = input()
#     num = num.split()
#     num = list(map(int, num))
#     num0=num[0]
#     num1=num[1]
#     A= num[0]%10
#     B=num[1]
#     if A==0:
#         print("0")
#         print("10")
#     elif A == 1 or A==5 or A==6:
#         print("1 5 6")
#         print(A)
#     elif A== (4 or 9):
#         print("4 or 9")
#         b_ = B%2
#         if b_ ==1:
#             print(A)
#         elif b_==0:
#             print(A*A %10)
#     elif A ==2 or A==3 or A==7 or A== 8:
#         # print("target")
#         b_ = B % 4
#         if b_==0:
#             print((A**4)%10)
#         else:
#             print((A**b_)%10)

# for _ in range(iter):
#     a, b = map(int, input().split())
#     a = a % 10
#
#     if a == 0:
#         print(10)
#     elif a == 1 or a == 5 or a == 6:
#         print(a)
#     elif a == 4 or a == 9:
#         b = b % 2
#         if b == 1:
#             print(a)
#         else:
#             print((a * a) % 10)
#     else:
#         b = b % 4
#         if b == 0:
#             print((a ** 4) %10%10%10%10)
#         else:
#             print((a ** b) %10%10%10%10 )

# iter = int(input())
# results=[]
# for i in range(iter):
#     a, b = map(int, input().split())
#     if a%10==0:
#         results.append(10)
#     else:
#         foc = 4+b%4
#         data = str(a**foc)
#         results.append(data[-1])
#     print(results)
#     results.clear()

# T = int(input())
# results = []
#
# for _ in range(T):
#     a, b = map(int, input().split())
#     if a % 10 == 0: results.append(10)
#     else:
#         focus = 4 + b % 4
#         data = str(a ** focus)
#         results.append(data[-1])
#
# for result in results:
#     print(result)

