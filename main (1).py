#pattern of square
x=int(input())
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print()


#pattern of triangle
x=int(input())
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print()

#pattern of numbers 
x=int(input())
for i in range(x):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

#pattern of pyrimid
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

#pattern of diamond
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(x-2,-1,-1):
    for j in range(x-i-1):
         print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
  #hollow pattern 
x=int(input())
for i in range(x+4):
    for j in range(x-i+4):
        print(" ",end="")
    for j in range(i+1):
        if(i%2!=0):
            break
        else:
         print("*",end=" ")
    print()
#hollow pattern 2
n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

#hollow square pattern
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
          print(" ",end=" ")
    print()
#hollow right angle triangle pattern
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or i ==j:
            print("*",end=" ")
        else:
          print(" ",end=" ")
    print()

    





    
