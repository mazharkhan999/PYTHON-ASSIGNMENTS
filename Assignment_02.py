#Q1
mpbs=int(input("Enter marks of MPBS: "))
ss=int(input("Enter marks SS: "))
dld=int(input("Enter marks of DLDS: "))
dsa=int(input("Enter marks of DSA: "))
dbms=int(input("Enter marks of DBMS: "))
avg=(mpbs+ss+dld+dsa+dbms)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")

#Q2
a=int(input('enter integer'))
if a%2==0:
    print (a," is even")
else:
    print(a," is odd")



#Q3
lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    element = int(input("Enter elements: ")) 
  
    lst.append(element) # adding the element 
      
print(len(lst))

#Q4
total = 0
list1 = [11, 5, 17, 18, 23]  
for ele in range(0, len(list1)): 
    total = total + list1[ele] 
  
# printing total value 
print("Sum of all elements in given list: ", total)



#Q5
list1 = [5, 56, 89, 84, 20] 
list1.sort() 
print("Largest element is:", list1[-1])


#Q6
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []

for item in a:
    if item < 5:
        new_list.append(item)

print(new_list)
