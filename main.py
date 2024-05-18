# all rights reserved to the owner
#take permission before use
import time
from colorama import Fore,Style, Back, init

init()
def input_close(x):
	if(x!='y'):
		print("wrong input")
		time.sleep(0.2)
		print("closing...")
		time.sleep(0.2)
		exit(1)
	else:
		pass	

def print_opreation(num,a):
    while(num<a):
    	print(num)
    	num= num + 1	
    	
def print_slow(num,a):
    	while(a>num):
    		print(num)
    		num= num + 1
    		time.sleep(0.2)
   
    			
    		
def timer(m):
     	while(m>0):
     		print("Printing in",m,"seconds",end='\r')
     		time.sleep(1)
     		m = m -1
     		if(m==0):
     		     	print("\n starting....")     	
     		     	
         		
    		
time.sleep(0.3)
print(Fore.GREEN + """________  ________      
|\   __  \|\   ____\     
\ \  \|\  \ \  \___|_    
 \ \   __  \ \_____  
  \ \  \ \  \|____|\  \  
   \ \__\ \__\____\_\  \ 
    \|__|\|__|\_________\
                         
""")
print(Style.RESET_ALL)	
time.sleep(0.5)
		
print(Style.BRIGHT + "welcome to number generrator \n V2")
print(Style.RESET_ALL)
time.sleep(0.3)

x=input(Fore.RED + "do u want to continue? \n [y/n]")
print(Style.RESET_ALL)  
input_close(x)
time.sleep(0.5)

num=int(input("enter from which you want to start number  : "))

time.sleep(0.2)
print("ok")
time.sleep(0.5)

a=int(input("input how many numbers \n you want to print   : "))

time.sleep(0.5)

z= input("Do you want to continue?[Y/n]")
time.sleep(0.5)
l= input("Do you need print Delays? \n [Y/n]")

if(l!='y'):
	print_opreation(num,a)
	print(Style.BRIGHT+"Thank You")
	print(Style.RESET_ALL)
	
else:
	print(Fore.RED+"Note: Its in early stage")
	print(Style.RESET_ALL)
	time.sleep(0.2)
	print(Fore.GREEN+"you can change the timer of code!")
	print(Style.RESET_ALL)
	e= 10
	timer(e)
	print_slow(num,a)
	print(Style.BRIGHT+"Thank You")
	print(Style.RESET_ALL)

