print('Q1') 
print('Simple Calculator \nSelect Operation \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Power')
while True:
    choice=int(input('Enter your choice(1/2/3/4/5): '))
    num1=int(input('Enter first number: '))
    num2=int(input('Enter second number: '))
    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    elif choice==4:
        print(num1/num2)
    elif choice==5:
        print(num1**num2)
    else:
        print('Invalid Input')
    select=input('Do you want to continue \nIf yes enter Yes \nIf no enter No')
    if select=='Yes':
        continue
    else:
        break

print('\n')
print('Q2')
List=['1','apple','56','a']
for i in List:
    print(i.isdigit())
    
print('\n')
print('Q3')    
D={'This':1,'is':2,'Computer':3}
D.update({'Programming':4})
print(D)


print('\n')
print('Q4')
D={'This':1,'is':2,'Computer':3,'Programming':4}
print(sum(D.values()))

print('\n')
print('Q5')
List=[]
length=int(input("Enter the length of the list: "))
for i in range(length):
    element=int(input("Enter the element of the list: "))
    List.append(element)
print(List)
for j in range(length):
    for k in range(j+1,length):
        if List[j]==List[k]:
            print(List[j])

print('\n')
print('Q6')
D={'This':1,'is':2,'Computer':3,'Programming':4}
x=input('Enter key')
if x in D.keys():
    print('Already Exist')
else:
    print('not present')


                  
            

    
