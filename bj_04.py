'''11720'''
# count= int(input())
# nlist=list(map(int, str(input())))
# # print(nlist)
# sum =0
# for i in range(len(nlist)):
#     sum+=nlist[i]
# print(sum)

'''10809'''
# #@1
# #a b c d e f g h i j k l m n o p q r s t u v w x y z
# #0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
# str= str(input())
# str= list(str)
# answer=[]
# for i in range(26):
#     answer.append(-1)
# for i in range(len(answer)):
#     al= chr(i+97)
#     for j in range(len(str)):
#         if(al == str[j]):
#             answer[i] = j
# print(answer)
# #@2
# word=input()
# al = list(range(97, 123))
# answer=[]
# for x in al:
#     answer.append(word.find(chr(x)))
# for i in answer:
#     print(i, end=' ')

'''2675'''
# iter = int(input())

# for _ in range(iter):
#     str = input().split()
#     answer=[]
#     str1=str[0]
#     str2=list(str[1])
#     # print(str1, str2)
#     for i in range(len(str2)):
#         for j in range(int(str1)):
#             answer.append(str2[i])
#     for i in range(len(answer)):
#         print(' '.join(answer[i]))

# for i in range(iter):
#     c=input().split()
#     print(''.join([i*int(c[0]) for i in c[1]]))

'''1157'''
# string = input()
# string= str(string)
# string=string.upper()
# # print(string)
# alphabet_list =[]
# for _ in range(26):
#     alphabet_list.append(0)
#
# for i in range(len(string)):
#     # print(string[i])
#     for j in range(26):
#         # print (chr(j+65))
#         if chr(j+65) == string[i]:
#             alphabet_list[j] +=1
# # print(alphabet_list)
# answer=[0,0,0]
# max=0
# tmp=0
# for i in range(26):
#     if int(alphabet_list[i]) >= max:
#         max=(alphabet_list[i])
#         answer.append(alphabet_list[i])
#         tmp=i
#     answer.sort()
#     answer.reverse()
# # print(answer, tmp)
# if int(answer[0]) == int(answer[1]):
#     print('?')
# else:
#     # print(tmp)
#     # print(answer)
#     k= chr(65+tmp)
#     print(k)
#@런타임 에러

# string= input().upper()
# num_list= []
# for i in set(string):
#     num_list.append(string.count(i))
# idx=[i for i, x in enumerate(num_list) if x==max(num_list)]
# if len(idx)>1:
#     print('?')
# else:
#     print(list(set(string))[num_list.index(max(num_list))])\

'''1152'''
# str= input().split()
# print(len(str))
#ps. 에바다

'''2908'''
# num1, num2 = input().split()
# # num1=input()
# num1=list(str(num1))
# # num1= list(map(int, num1))
# num1.reverse()
# num2=list(str(num2))
# # num2= list(map(int, num2))
# num2.reverse()
# num1_="".join(num1)
# num2_="".join(num2)
# # print(num1_, num2_)
# if(num1_>num2_):
#     print(num1_)
# else:
#     print(num2_)

'''5622'''
# word= input()
# word=list(str(word))
# time=0
# for i in range(len(word)):
#     if ord(word[i]) <= ord('C'):
#         time+=3
#     elif ord(word[i]) <= ord('F'):
#         time+=4
#     elif ord(word[i]) <= ord('I'):
#         time+=5
#     elif ord(word[i]) <= ord('L'):
#         time+=6
#     elif ord(word[i]) <= ord('O'):
#         time+=7
#     elif ord(word[i]) <= ord('S'):
#         time+=8
#     elif ord(word[i]) <= ord('V'):
#         time+=9
#     elif ord(word[i]) <= ord('Z'):
#         time+=10
# print(time)
#  맞는데 틀렸다그럼 이유를 모르겠음
# alphabet=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# word=input()
# time=0
# for uint in alphabet:
#     for i in uint:
#         for x in word:
#             if i==x:
#                 time+=alphabet.index(uint)+3
# print(time)

'''2941'''
# alphabet =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# alpha= input()
# for t in alphabet:
#     alpha= alpha.replace(t, '.')
# print(alpha)
# print(len(alpha))

'''1316'''
# iter=int(input())
# for _ in range(iter):
#     word= input()
#     for i in range(1, len(word)):
#         if word.find(word[i-1]) > word.find(word[i]):
#             iter-=1
#             break
# print(iter)
