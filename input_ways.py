'''input ways to print'''

# a = 15
# print(a)

# x = input()
# print(x)                                                                    # 36 56.32 str

# s = input("Enter your name : ")

# print("My name is ",s)                                                       # My name is  Mohammad
# print("My name is ",s,sep='-')                                               # My name is -Mohammad
# print("My name is",' ',s)                                                    # My name is   Mohammad
# print("My name is ",int(s))                                                  # ValueError
# print("My name is ",float(s))                                                # ValueError
# print("My name is "+str(s))                                                  # My name is   Mohammad
# print("My name is"+" "+s)                                                    # My name is   Mohammad


# d = input()
# print("My favorite car is"+' '+ d)                                           # My favorite car is Bucati
# print("My favorite car is " ,d)                                              # My favorite car is Bucati
# print("My favorite car is ",d,sep="-")                                       # My favorite car is-Bucati


# e = int(input())
# print("My favorite number is"+' '+str(e))                                      # My favorite number is 7
# print("My favorite number is",e)                                               # My favorite number is 7
# print("My favorite number is",e,sep='*')                                       # My favorite number is*7
# print("My favorite number is",float(e),sep='/')                                # My favorite number is/7.0

# f =float(input())
# print("My graduation percentage is",f,'%')                                       # My graduation percentage is 89.0 %
# print("My graduation percentage",'',str(f) , '%')                                # My graduation percentage  89.0 %
# print("My graduation percentage",int(f),'%')                                     # My graduation percentage 89 %
# print("My graduation percentage "+str(f)+'%')                                    # My graduation percentage 89.0%
# print("My graduation percentage",(f),'%')                                        # My graduation percentage 89.0 %


# w = float(input("Enter your  BMI :"))                                       # BMI : Body mass index
# print("Your BMI is ",w)                                                     # Your BMI is  36.2
# print("Your BMI is ",w,sep="*")                                             # Your BMI is  *36.2
# print("Your BMI is ",int(w))                                                # Your BMI is  36
# print("Your BMI is ",float(w))                                              # Your BMI is  36.2
# print("Your BMI is "+str(w))                                                # Your BMI is 36.2


# name=input("Enter your name :")
# age = input("Enter your age :")
# per= input("Enter your graduation percentage :")

# print(name,age,percentage)                                                  # Mohammad 23 72%
# print(age,percentage,name)                                                  # 23 72% Mohammad
# print(age,percentage,age)                                                   # 23 72% 23


# print("My name is",name,"My age is",age,
# "My graduation percenage is",per)                                            # My name is Mohammad My age is 23 My graduation percenage is 72%

# print("My name is "+name+' '+"My age is "+age+' '
# +"My graduation percentage is "+per+"%")                                     # My name is Shahed My age is 23 My graduation percentage is72%


# place = input("Enter your vaccation spot :")
# days = input("How many days :")
# cost = input("How much money spent :")


# print("My favorite vaccation spot is ",place, \
#      "I will spent one",days,"And the cost of my trip is around",cost)      # My favorite vaccation spot is  Mauritius I will spent one week And the cost of my trip is around 1M$

# print("My favorite vaccation spot is "+
# place+' '+"I will spent"+' '+days,"days"+' '+"And the cost of the trip is around "+(cost))  # My favorite vaccation spot is sanfrancisco I will spent 45 days And the cost of the trip is around 11cr


# q = "I am a
# programmer"

# print("i am"
# " a programmer")

# print("My favorite vaccation spot is %s \
# I will spent  %d days  And the cost of my trip is around %.2f"%(place,days,cost))      # My favorite vaccation spot is Dubai I will spent  8 days  And the cost of my trip is around 1000000.00

# print("My favorite vaccation spot is {}, I will spend one {} \
# And the cost of my trip is around {}".format(place,days,cost) )     # My favorite vaccation spot is Dubai, I will spend one 11 And the cost of my trip is around 1M$


# print("My favorite vaccation spot is {1}, I will spend {2} days. \
# And the cost of my trip is around {0}".format(cost,place,days))  # My favorite vaccation spot is Manali, I will spend 7 days. And the cost of my trip is around 1M$


# print(f"My favorite vaccation spot is {place}, I will spend {days} days. \
#  And the cost of my trip is around {cost}")                         # My favorite vaccation spot is Goa, I will spend 4 days.  And the cost of my trip is around 10000

''' If I want to add sum of two numbers from the user input'''

# a =int(input())
# b =int(input())
# print(a+b)


''' what if I want to add 100 numbers at a time'''


# a,b = [float(c) for c in input("Enter any two numbers :").split()]
# print(a-b)                                                        # -13.3
# print(a*b)                                                      # 540
# print(b/a)                                                          # 5.0
# print(a/b)                                                          # 0.5


# d = (float(z) for z in input().split('-'))
# print(sum(d))                                                       # 141.32


''' for other arthematic operations we need to import math package'''

import math

a= [float(w) for w in input().split('*')]
print(math.prod(a))                                                   # 75819744.0


                                                   



# a = '123466236589523'
# print((a[0])+(a[-3]))                                                   # 15 why? 