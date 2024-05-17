import time 
#made by aritra
#this code is proted by AGPL-3.0 license...not to repost anywhere

print("""
________  ________      
|\   __  \|\   ____\     
\ \  \|\  \ \  \___|_    
 \ \   __  \ \_____  \               
  \ \  \ \  \|____|\  \  
   \ \__\ \__\____\_\  \ 
    \|__|\|__|\_________\
             
                         
""")

time.sleep(1)
print("welcome to number generrator \n V2")
time.sleep(0.5)

x=input("do u want to continue? \n [y/n]")
if(x!='y' ):
	print("wrong input")
	print("closing....")
	time.sleep(0.2)
	exit(1)   
	 
time.sleep(0.5)

num=int(input("enter from which you want to start number  : "))
time.sleep
print("ok")

a=int(input("input how many numbers \n you want to print   : "))

print("ok")

if(a>10000):
	z=input("Do u need 0.01 sec delays? [y/n]")
	if(z=='y'):
	   print("default is 0.01 sec, u can change the code ")
	   time.sleep(1)
	   print("starting in 5 sec")
	   time.sleep(5)
	   
	   while(num<a):
	   	print(num)
	   	time.sleep(0.02) # here you can change the speed 
	   	num= num + 1
	   	time.sleep(0.001)
		
else:
	pass
time.sleep(1.5)





while(num<a):
    print(num)
    num= num + 1
    
print("Thank you")    
    
