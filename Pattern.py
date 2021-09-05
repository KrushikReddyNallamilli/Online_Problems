Question:
# print the below pattern for example n=5
# 5
# Output
# 1 2 3 4 5 
# 10 9 8 7 6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25

# approach 1 Time:0.16 Mem: 89.024kb
# n=int(input())
# c=1
# for i in range(1,n+1):
#     if i%2==0:
#         c+=n-1
#     for j in range(n):
#         if i%2==0:
#             print(c,end=" ")
#             c-=1
#         else:
#             print(c,end=" ")
#             c+=1            
#     print()
#     if i%2==0:
#         c+=n+1

#  approach 2: Time:0.08 Mem: 89.024kb

# n=int(input())
# a=0
# c=0
# for i in range(1,(n+1)):
#     res=[]
#     c+=1
#     for j in range(1,(n+1)):
#         a=str(int(a)+1)
#         res.append(a)
#         res.append(" ")
#     if c%2!=0:
#         res="".join(res)
#     else:
#         res.pop()
#         res.reverse()
#         res="".join(res)
#     print(res)

# approach 3: Time:0.13 Mem: 89.024kb
# n=int(input())
# for i in range(n):
#     if(i%2==0):
#         for k in range((n*i)+1,(n*i)+n):
#             print(k,end=" ")
#         print(k+1)
#     else:
#         for k in range((n*i)+n,(n*i)+1,-1):
#             print(k,end=" ")
#         print(k-1)
