str  = "dhruvi"
print(str[1:4])
# str  = "dhruvoi"
# print(str[-3:-1])

age  = 21

if(age >=18):
    print("can apply for license")


marks = 69
if(marks>=90):
    print("grade= A")
elif(marks>=80 and marks<90):
     print("grade= B")
elif(marks>=70 and marks<80):
     print("grade= C")
elif(marks>=70):
     print("grade= D")
else :
    print("fail")



number = int(input("enter number "))
if(number % 2== 0):
    print("number if even")
else:
    print("number is odd")


a = int(input("enter first number"))
b = int(input("enter sec number"))
c = int(input("enter third number"))
if(a>=b and a >= c):
    print("first is large",a)
elif(b >=c):
    print("sec is large",b)
else:
     print("third is large ",c)



number  = int(input("enter number"))
if(number  % 7 == 0):
    print("divided 7 ")
else:
    print("not")



movies = []
mov = input("enter 1st movie:")
movies.append(mov)
mov = input("enter 2st movie:")
movies.append(mov)
mov = input("enter 3st movie:")
movies.append(mov)
print(movies)



list1 = [1,2,1]
list2 =[1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list2):
    print("palindronme")
else:
    print("not pali.....")
