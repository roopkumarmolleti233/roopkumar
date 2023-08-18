import re

arr='''Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.
'''
print(arr)
#arr=arr.split("Haskell,")[1].split(', Assembly')[0]
arr=re.split("Haskell, |, Assembly",arr)[1]

print(arr)
