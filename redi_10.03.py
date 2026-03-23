#x = input ()
#y=max (100, x)
#print (y) 

#a=input("Enter first number:" )
#b=input("Enter second number:")

#a=int(a)
#b=int(b)

#print ("Sum", a+b)


#x =int(input("Please enter your age:"))
#if x >= 18:
    #print ("You can vote")
#else:
 #   print ("You cannot vote")

x =float(input("Please enter your gross earnings for 2023:"))
if x >= 500000.01:
    print (float (x*0.45))
elif x >= 250000.01:
    print (float (x*0.42))
elif x >= 100000.01:
    print (float (x*0.37))
elif x >= 50000.01:
    print (float (x*0.25))    
elif x >= 32000.01:
    print (float (x*0.15))
elif x >= 0:
    print (" the tax is 0")      
else: 
    print ("negative number for gross earnings is not valid")             
