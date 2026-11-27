#using range
# # for i in range(1,11):
#     print(i) 

#using list
# numbers=[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     print(num)

#using range step up
# for i in range(1,11,2):
#     print(i)


#using while
'''i=1
 while i<=10:
     print(i)
     i+=1'''

#for reverse
'''for i in range(10,0,-1):
  print(i)'''

#reverse using while
'''i=10
 while i>=1:
     print(i)
     i-=1'''

#Print only even numbers
'''for i in range(2,21,2):
         print(i)'''

#Print only even numbers using if function
'''for i in range(1,21):
     if i%2==0:
         print(i)'''

#Calculate the sum of numbers from 1 to 10.
'''count=0
for i in range(1,11):
    count=i+count
print("Sum:",count)'''


#sum using while
'''i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum =", total)'''

#using built-in sum
count=sum(range(1,11))
print("Sum:",count)