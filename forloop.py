#print number from 1 to 10
for i in range (1,11):
    print(i)

#print Even numbers from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)

#print odd numbers from 1 to 15
for i in range(1,16):
    if i%2!=0:
        print(i)

#print table of 5
for i in range(1,11):
    print("5x",i,"=",5*i)

#print character of string
name="atmiya"
for letter in name:
    print(letter)

#sum of number from 1 to 5
total=0
for i in range(1,6):
    total=total+i      
    print("sum is:",total)

#print list elements
numbers=[10,20,30,40]
for n in numbers:
    print(n)