# myset={1,2,"sanjay",5.66,"ayush","ramesh","ankit","rishikesh","rahul"}
# print(myset)
# print(type(myset))
# print(myset[0]) #error becoz orderwise data is not awailable or store
# myset.add(60)# 60 randomly to set
# print(myset)

# myset.remove(1) #value is present then use remove
# print(myset)


# myset={10,20,30,40}
# yourset={10,50,60,30}
# newset=myset.union(yourset)
# print(newset)
# # print(myset.difference(yourset))
# print(myset.clear())


#wap to accept a,b,c val and find min value
# a=int(input("enter value of a:"))
# b=int(input("enter value of b:"))
# c=int(input("enter value of c:"))
# if a<b:#5
#     if a<c:
#         print("a is smaller")
#     else:
#         print("c is smaller ")
# else:
#     if b<c:
#      print("b is smaller")
#     else:
#      print("c is smaller")

# mylist=[3,5,6,8,2]
# for i in mylist: #1=5
#     print(i)

# for i in range(1,11):#i=1
#     print(i+1," ",i+2,"",i+3)

# username=input("enter Username:")
# password=input("enter password:")
# if username==password:
#     print("login succesful")
# else:
#     print("ïnvalid login")



# brand=input("enter your coldrink name either in lower case or in upper case but not combind:")
# if brand=="pepsi" or brand=="PEPSI:"
#     print("swag")
# elif brand=="dew" or brand=="DEW:"
#     print("dar ke aage jeet hai")
# elif brand=="thumbsup" or "THUMBSUP:"
#     print("taste the thunder")
# else:




# n1=int(input("enter first number:"))
# n2=int(input("enter secondnumber:"))
# n3=int(input("enter third number:"))

# if n1>n2 and n1>n3:
#     print("Biggest Number is:",n1)
# elif n2>n3:
#     print("Biggest Number is:",n2)
# else:
#     print("Biggest Number is:",n3)
    

# count=0
# for i in range(9):
#     if i%2==0:
#         print(i)
#     else:
#         print(i)
#         count +=1
# print("count=",count)


# val= [1,2,3,5,5,5,1,2,4,4,6,6,6]
# print(val.index(1))
# print(val.index(2))
# print(val.index(3))
# print(val.index(4))
# print(val.index(5))
# print(val.index(6))

# x=['A','B','C',]
# y=['A','B','C',]
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x !=z)


# import datetime  error
# datetime=datetime.datetime.now()
# print("Its now:{:%d/%m/%Y %H:%M:%S}".format(date))

# for i in range (1,5):#i=3 will break and it will print i
#     if i==3:
#         break
#     print(i)


# for i in range (1,5):#it will continue the for loop if con
#      if i==3:
#          continue
#      print(i)


# mycart=[10,20,200,300,800,60,700]
# for i in mycart:#i=0,1,2...=10,20,200,300,800....
#     if i>400:
#         print("This is my purchased cart item")
#         continue
#     print(i)


# list=[1,2,3,4,5,6,7,8,9,10]
# sum=0#sum=
# for x in list:
#     sum=sum+x
# print("the sum =",sum)


# rollno=[3,5,7,1,11,4,5,2]
# for x in rollno:
#     if x==2 or x==4 or x==6 or x==8 or x==10:
#         print("even no is found",x)
#         break



# name="nayan"
#      #01234
# for i in name:
#     print(i)

# name="nayanbongale"
# newname=" "
# for i in name:
#     if i not in newname:
#         newname += i
# print(newname)


# name="nayanbongale" #incomplete
# newname=" "
# for i in newname:
#     if i>=-1
#     newname



# name="nayanbongale"
# i=0
# for x in name:
#     if x=='l':
#        print("the character is present at index no",i,"value :",x)
#        break
#     i=i+1

# name="nayanbongale"  #incomplete
# vow=0
# con=0
# vowels=['a','e','i','o','u']
# for i in name:
#     if i in



# for i in range(5,0,-1):
#     print(i)


# fact=1

# for i in range(5,0,-1):
#     fact=fact*i
# print(fact)


mydict={
   "name":"nayan",
     "professional":"developer",
     "empid":1001
 }
#  print(mydict)

# mydict={
#     101: "nayan",
#     102: "keerti",
#     "103": "mohini",
#     "104": "trivani",
#     101: "ashish",
#     104:  "ashish"

# }
# print(mydict)

#with the help of key we have to print values
# a=mydict
# print(a)


#we will replace old value by new
# mydict[102]="peter"
# print(mydict)


#only print key x=0,1     will print two times same value if one is string
# for x in mydict:
#     print(x)


#only print values
# for x in mydict.values():
#     print(x)


#print key n values both
# for x,y in mydict.items():
#     print(x,y)


# mydict["mobile no"]=4646874693
# print(mydict)



newdict=mydict.copy()
print(newdict)










