# by aritrasa 
# contract, instagram - 0aritrasa1

import time
import time
import random
from colorama import Fore,Style, Back, init
import os
import sys
import platform


init()
os_info = platform.system()



def input_close(x):
	if(x!='y'):
		print("wrong input")
		time.sleep(0.2)
		print("closing...")
		time.sleep(2)
		os.system('clear')
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
     		print("  Printing in",m,"seconds",end='\r')
     		time.sleep(1)
     		m = m -1
     		if(m==0):
     		     	print(Fore.BLUE+"starting....",end='                         ')     
     		     	print(Style.RESET_ALL)	

def function(time8):
     		while(time8>0):
     			print(" leaving & clearning in",time8,"seconds",end='\r')
     			time.sleep(1)
     			time8 = time8 -1
     			if(time8==0):
     				print("\n leaving....")
     				time.sleep(2)
     				os.system('clear')     
  
def error_handler(num2,a):
	if(num2>a):
		time.sleep(0.5)
		print(f"{Fore.GREEN}Wrong input, {Fore.BLUE} choose another optipn for sub count")	
		time.sleep(0.5)
		exit(1)
		time.sleep(0.5)
		os.system('clear')	     					   					
	     		  
time.sleep(0.3)
print(f"""{Fore.GREEN}________  ________      
|\   __  \|\   ____\     
\ \  \|\  \ \  \___|_    
 \ \   __  \ \_____  
  \ \  \ \  \|____|\  \  
   \ \__\ \__\____\_\  \ 
    \|__|\|__|\_________\
                         
""")
print(Style.RESET_ALL)	
time.sleep(0.5)

print(f"{Style.BRIGHT}Hello {os_info} user & welcome to  number generrator \n {Fore.YELLOW}V3")
print(Style.RESET_ALL)
time.sleep(0.5)

print(Fore.BLUE,"Testing the platform",end='\r')

time.sleep(3)
print("Done",end='                              ')

print(Style.RESET_ALL)

if os_info=='Windows':
	time.sleep(0.5)
	os.system('clear')
	print(f"{Style.BRIGHT}{Back.RED}windows user detected")
	time.sleep(0.3)
	print(Style.RESET_ALL)
	exit(1)
	
else:
	pass	


x=input(Fore.RED + "do u want to continue? \n [y/n]  : ")
print(Style.RESET_ALL)  
input_close(x)
time.sleep(0.5)

print(f"{Fore.GREEN}1:Print ascend number from input \n 2: Print random number ")


print(Style.BRIGHT,"choose mode")
print(Style.RESET_ALL)
time.sleep(0.5)

sum3= input(" Enter your choice  : ")
time.sleep(0.5)

if(sum3=='2'):
	time.sleep(0.5)
	num_times = int(input("\nHow many times do you want to print a random number  : "))
	time.sleep(0.5)
	random1=int(input("\nEnter First choice radiant  : "))
	time.sleep(0.4)
	random2=int(input("\nEnter last choice radiant  : "))

	
	if(random1==random2):
		time.sleep(0.4)
		print(Back.RED+Style.BRIGHT,random1,"cannot be same in low to high radiates")
		print("Exitting...")	
		time.sleep(2)
		os.system('clear')
		exit(1)
	time.sleep(0.4)
	xy= input("Do you need delays? [Y/n]  : ")

	if xy=='y':
		timez = 10
		timer(timez)
		for i in range(num_times):
			print(random.randint(random1, random2))
			time.sleep(0.3)
	else:
		pass
			
	for i in range(num_times):
		print(random.randint(random1, random2))


elif(sum3=='1'):
	time.sleep(0.5)
	num=int(input("enter from which you want to start number  :  "))


	time.sleep(0.5)
	a=int(input("input how many numbers \n you want to print   :  "))
	error_handler(num,a)
	time.sleep(0.5)
	
	
	if(num==a):
		time.sleep(0.4)
		print("number cannot be same ")
		time.sleep(0.4)
		print("exitting...")
		time.sleep(3)
		os.system('clear')
		exit(1)
	z= input(f"{Fore.RED}Do you want to continue?[Y/n]  : ")
	print(Style.RESET_ALL)
	time.sleep(0.5)
	input_close(z)
	

	l= input(f"{Fore.GREEN}Do you need print Delays? \n [Y/n]  : ")
	print(Style.RESET_ALL)
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
	

else:
	print("wrong choice")
	time.sleep(0.5)
	print("leaving....")
	time.sleep(3)
	os.system('clear')
	exit(1)


time.sleep(0.4)
print(Fore.GREEN+Style.BRIGHT+"Thank you for using")  
time.sleep(0.4)

print(Style.BRIGHT+"To run again")
print(Style.RESET_ALL)
time.sleep(0.4)
print("python main.py")				



time8= 60
function(time8)

			


