# -*- coding: utf-8 -*-
"""лаб3 введение.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-NWhSjbTMdrqQw3_VD0e0wDlVu3aUbKl
"""

#1
n=int(input())
if n==1:
  print("январь")
if n==2:
  print("февраль")
if n==3:
  print("март")
if n==4:
  print("апрель")
if n==5:
  print("май")
if n==6:
  print("июнь")
if n==7:
  print("июль")
if n==8:
  print("август")
if n==9:
  print("сентябрь")
if n==10:
  print("октябрь")
if n==11:
  print("ноябрь")
if n==12:
  print("декабрь")

#2
b=int(input())
if b%2==0:
  print(b,"- четное")
else:
  print(b,"- нечетное")

#3
n=int(input())
if n>=40:
  print("stonks:)")
if n<40:
  print("not stonks:(")

#4
def is_year_lap(y):
  if y%400==0 or y%100!=0:
    k=True
    return k
  else:
    k=False
    return k
y=int(input())
print(is_year_lap(y))

#5
def isprime(n):
  s=True
  for i in range(2,n//2):
    if n%i==0:
      s=False
  return s

n=int(input())
print(isprime(n))

#6
n=int(input())
m=int(input())
c=0
if n==3.6*m or m>=(-138/2)**1.3 and m<=abs((-69/28**5.1)*4):
  c=n
  n=m
  m=n
  print(n,m)

#7
#являются ли они
#все уникальными и посчитать количество четных, отрицательных, а так
#же лежащих в промежутке [-256 ; 1024]
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
ch=0
m=0
pr=0
if a!=b and b!=c and c!=d and d!=e:
  if a<0:
    m+=1
  if b<0:
    m+=1
  if c<0:
    m+=1
  if d<0:
    m+=1
  if e<0:
    m+=1
  if a%2==0:
    ch+=1
  if b%2==0:
    ch+=1
  if d%2==0:
    ch+=1
  if c%2==0:
    ch+=1
  if e%2==0:
    ch+=1
  if -256<=a<=1024:
    pr+=1
  if -256<=b<=1024:
    pr+=1
  if -256<=c<=1024:
    pr+=1
  if -256<=d<=1024:
    pr+=1
  if -256<=e<=1024:
    pr+=1
print(ch,m,pr)

#8
#(a2 +b3 )/c +3  /4
a=int(input())
b=int(input())
c=int(input())
res=((a**2+b**3)/(c+3))/4
if res%2==0:
  print("ответ четный")
else:
  print("ответ нечетный")