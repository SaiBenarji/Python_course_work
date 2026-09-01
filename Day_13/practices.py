'''
a=int(input())

if a >= 0:
    print('positive number')   

b = int(input())

if b%2==0:
    print('Even')


c = int(input())
if c%5==0:
    print('Divisible by 5')

d=int(input())
if d%3==0 and d%7==0:
    print('Divisible by both 3 and 7')


e = int(input())
if (e % 400==0) or (e % 4==0 and e%100!=0):
    print('Leap year')
else:
    print('Non Leap year')    


f = int(input())
if f >=35:
    print('pass')


g=int(input())
if 100 <= abs(g) <= 999:
    print('3-digit number')


h=input()
if h in "aeiouAEIOU":
    print('vowel')
   
i=int(input())
j=int(input())
if i > j:
    print(i,' Is the Greater')
else:
    print(j,'Is the Greater')

k=int(input())
l=int(input())
if k<l:
    print(k, 'is the smaller')
else:
    print(l,'is the smaller')

m=int(input())
if m==0:
    print('Number is Zero')

n=int(input())
if n*10:
    print('Multiple of 10')
else:
    print('ERROR')    


o=int(input())
if o >=18:
    print('Eligible to Vote')
else:
    print('Not Eligible')    



p=int(input())
if p==(1,100):
     45 in p
print('In range')


q=int(input())
r=int(input())
if q==r*r :
    print('4 is square of 2')
else:
    print("Error")
    
a=input()
b=input()
if a == b:
    print('String are Equal')
else:
    print('Error')
   

num=int(input())
if num%2==0 :
    print('not prime number')

else:
    print('prime number')   


a=int(input())
if a%2==0 and a>0:
    print('positive and even number ')

b=input()
if b.isupper():
    print('uppercase letter')
else:
    print('error')

a=int(input())
if a>=30:
    print('It`s hot')
else:
    print('NO')

a=int(input())
if 1000 <= a <= 9999 and a % 2 == 0:
    print("It is a 4-digit even number.")
else:
    print("It is not a 4-digit even number.")

a=input()
if a not in "aeiouAEIOU":
    print('Constant')
else:
    print('Not Constant')


seat=input("Enter the seat type: " )
booking_days= int(input("Enter the day: "))
season=(input("Enter the season type: ")) == "True"
age=int(input("Enter the age: "))
price=5000

if seat=="Bussiness":
    price += price *0.40
elif seat=="Premium Economy":
    price += price *0.20   
if booking_days >30:
    price -= price *0.10
elif booking_days <7:
    price += price *0.25


if season==True:
    price += price *0.20

if age >60:
    price -= price * 0.15

print(price)        

age=int(input("enter the age: "))
health_score=int(input("Enter the score: "))
vehicle_type=input("Enter the vehical type: ")

base=10000

if age <25:
    base += base *0.20

elif age >50:
    base += base *0.15

if health_score >=80:
    base -= base *0.10

elif health_score <60:
    base += base *0.20

if vehicle_type =="Sports car":
    base += base * 0.30
elif vehicle_type =="Suv":
     base += base * 0.15


print(base)

cs = int(input('Enter your cs score:'))
monthly_income=int(input('Enter your monthly_income: '))
lb=int(input('Enter your loan balance:'))

if cs >=750 and monthly_income >=50000 and lb<=20000:
    print('Eligible for loan')
elif 650<cs<749 and monthly_income >=50000 and lb<=20000:
    print('conditional Eligible for loan')
elif cs<650:
    print('Rejected for loan')                           

salary=int(input('Enter the salary: '))
pr=int(input('Enter the pr rating: '))
exp=int(input('Enter the experience:'))
att=int(input('Enter the attendance:'))
bonus=0
salary=0
att=0
if pr ==5:
    bonus +=salary*0.25
elif pr ==4:
    bonus +=salary*0.15
elif pr==3:
    bonus +=salary*0.10
elif pr<3:
    print('Not Eligible for  bonus')
if exp>10:
    bonus +=salary*0.10
elif  5<=exp<=10:
    bonus +=salary*0.05
elif exp <5:
    print('Not Eligible for additional bonus')
if att>=95:
    att=5000
elif 85<=att<=94:
    att=2000
elif att<85:
    print('not eglible for attendance bonus')

else:
    att
bonus=exp+salary+att
print(bonus)    


n = int(input('Enter the number:'))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')


print(int(input('Enter the number:'))*55)

a,b=map(int,input('Enter the numbers:').split())
for n in range(a,b+1):
    if n>1 and all(n%i for i in range(2,int(n**.5)+1)): print(n, end=',')
'''

