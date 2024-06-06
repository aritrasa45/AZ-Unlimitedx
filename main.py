# by aritrasa 
# contract, instagram - 0aritrasa1
# alawys give credits by typing @0aritrasa1
# if using 

import time
import random
from colorama import *
import os
import sys
import platform
import hashlib
from getpass4 import getpass
import string


init(autoreset=True)
os_info = platform.system()

if os_info=='Windows':
	time.sleep(0.5)
	os.system('clear')
	print(f"{Style.BRIGHT}{Back.RED}windows user detected")
	time.sleep(0.3)
	sys.exit()
else:
	pass	

def color():
	print(Style.RESET_ALL)
	
def division(a,b):
	if b== 0:
		print("• you can't divide by 0 !!")
		return 0
	else:
		return a/b
		

def input_close(a):
	if(a!='y' or ''):
		print("wrong input")
		time.sleep(0.2)
		print("closing...")
		time.sleep(2)
		os.system('clear')
		sys.exit()
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
     		print(f"  Printing in {m} seconds",end='\r')
     		time.sleep(1)
     		m = m -1
     		if(m==0):
     		     	print(f"{Fore.BLUE}starting....",end='                         ')     
     		     		

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
		print(f"{Fore.RED}Wrong input, {Fore.BLUE} choose another optipn for sub count")	
		time.sleep(0.5)
		sys.exit()
		time.sleep(0.5)
		os.system('clear')	     					   					
	     		  
time.sleep(0.3)
print(f"""{Fore.CYAN}________  ________      
|\   __  \|\   ____\     
\ \  \|\  \ \  \___|_    
 \ \   __  \ \_____  
  \ \  \ \  \|____|\  \  
   \ \__\ \__\____\_\  \ 
    \|__|\|__|\_________\
                         
""")
print(Style.RESET_ALL)	
time.sleep(0.5)

print(f"{Style.BRIGHT}Hello {os_info} user & welcome to  number generrator V3")
time.sleep(0.5)

print(f"{Fore.BLUE}Testing the platform",end='\r')

time.sleep(1)
print("Done",end='                              ')




time.sleep(0.5)
x=input(f"\n{Fore.RED}do you want to continue? \n [y/n]  : ")
input_close(x)
time.sleep(0.5)

print(f"{Fore.CYAN}[1]:Print ascend number from input\n{Fore.YELLOW}[2]: Print random number")

print(f"{Fore.GREEN}[3]: Calculator\n{Fore.MAGENTA}[4]:Sha256 Comment hash\n{Fore.RED}[5]: Temporary-Encryption")


print(f"{Style.BRIGHT}choose mode")
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
		print(f"{Back.RED}{Style.BRIGHT}{random1} cannot be same in low to high radiates")
		print("Exitting...")	
		time.sleep(2)
		os.system('clear')
		sys.exit()
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
		sys.exit()
	z= input(f"{Fore.RED}Do you want to continue?[Y/n]  : ")
	time.sleep(0.5)
	input_close(z)
	

	l= input(f"{Fore.GREEN}Do you need print Delays? \n [Y/n]  : ")
	if(l!='y'):
		print_opreation(num,a)
		print(f"{Style.BRIGHT}Thank You")

	else:
		print(f"{Fore.RED}Note: Its in early stage")
		time.sleep(0.2)
		print(f"{Fore.GREEN}you can change the timer of code!")
		e= 10
		timer(e)
		print_slow(num,a)
		print(f"{Style.BRIGHT}Thank You")
		
				
elif sum3 =='3':
	while True:
		try:
			x = int(input("\n• Enter first number  : "))
			y = int(input("• Enter second number  : "))	


		except ValueError:
			print(f"{Fore.RED}No texts")  
			color()
			break
	
		print(f"\n{Style.BRIGHT}▪︎ Select options{Style.RESET_ALL}\n{Fore.GREEN}\n[1]: Addition{Fore.BLUE}\n[2]: substraction{Fore.CYAN}\n[3]: Multiplication{Fore.MAGENTA}\n[4]: Division")
	
		z = input("Enter : ")
		if z == '1':
			print(f"{Fore.GREEN}The addition is{x+y}")
	
		elif z == '2':
			print(f"{Fore.BLUE}The substraction is{x-y}")
		
		elif z == '3':
			print(f"{Fore.CYAN}The multiplication is {x*y}")		
	
		elif z == '4':
			print(f"{Fore.MAGENTA}The Division is",division(x,y))
		
     

		else:
		      print(f"{Fore.RED}Wrong input")
		      break
	
	
elif sum3 =='4':
	password = getpass(f"{Fore.MAGENTA}Enter password to hash  :  ")
	hash_object = hashlib.sha256(password.encode())
	print('\n',hash_object.hexdigest())


elif sum3 =='5':
	init(autoreset=True)
	def color():
		print(Style.RESET_ALL)
	chars = "" + string.punctuation + string.digits + string.ascii_letters
	chars = list(chars)
	key = chars.copy()
	random.shuffle(key)
	print(f"{Fore.YELLOW}welcome\nhere you can temporarily encrypt a mesage with a key & it will stay until the programe is closed\n")
	time.sleep(0.5)
	plain_text = getpass(f"{Fore.YELLOW}▪︎{Fore.CYAN}Enter a message to encrypt: ") 
	color()
	cipher_text = ""
	for letter in plain_text:
		time.sleep(0.5)
		index = chars.index(letter)
		cipher_text += key [index]
		print(f"{Fore.GREEN}{cipher_text}",end='\r')
		color()
	y = input(f"{Fore.BLUE}▪︎{Fore.RED}Decrypt{Fore.GREEN} {cipher_text}{Fore.RED} [Y/n]")
	color()
	if y=='y' or ' ':
		pass
	
	else:
		sys.exit()	
	cipher_txt = input(f"{Fore.YELLOW}▪︎{Fore.CYAN}Enter a message to decrypt: ")
	print(Style.RESET_ALL)
	if cipher_text != cipher_txt:
		print(f"{Fore.GREEN}Wrong key")
		sys.exit()
 
	plain_text = ""
	for letter in cipher_text:
		index = key.index(letter) 
		plain_text += chars[index]
		time.sleep(0.5)
		print(f"{Fore.GREEN}original message: {plain_text}")
		color()


else:
	print("wrong choice")
	time.sleep(0.5)
	print("leaving....")
	time.sleep(3)
	os.system('clear')
	sys.exit()


time.sleep(0.4)
print(f"\n{Fore.GREEN}Thank you for using")  
time.sleep(0.4)
			
time8= 60
function(time8)

			
