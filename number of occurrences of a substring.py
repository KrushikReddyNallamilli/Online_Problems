
# Question
# Write a program to print the number of occurrences of a substring in the main
# string
# The input contains 2 lines.
# 1st line is the main string 
# 2nd line is the substring
# Sample input:aabcababacaabaaababa
#               ab
# Output:6

# approach 1 :Time:0.02 Mem: 17.968kb
# ip=list(input())
# ss=list(input())
# count=0
# for i in range(0,(len(ip)-len(ss)+1)):
#     intf=0
#     for j in range(0,len(ss)):
#         if ip[i+j]==ss[j]:
#             intf+=1
#     if intf==len(ss):
#         count+=1
# print(count)

# approach 2 : Time:0.02 Mem:17.968kb
# n1=input()
# n2=input()
# k=len(n2)
# count=0
# for i in range(len(n1)-k+1):
#     if(n1[i:1+k]==n2):
#         count+=1
# print(count)
