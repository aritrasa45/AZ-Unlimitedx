
<h1 align="center">
  AZ-Unlimitedx v2 🤩
</h1>




 
<h2>
This code is a simple number generator program that allows the user to input a starting number and how many numbers they want to print.
</h2>
<p align="center">
  <img src="https://github.com/aritrasa45/AZ-Unlimitedx/blob/main/Screenshot.jpg" height="200px"/>
</p>

<h2>Usage of it? -🦸</h2>

<li>In summary, this program is a simple interactive number generator that allows the user to specify a starting number and how many numbers they want to print. It provides colorful output using the colorama library and includes error handling for incorrect user inputs.</li>

<li>Overall, this code is a simple but functional number generator program. It can be used to generate a sequence of numbers for various purposes, such as testing or debug</li>
</h2>

<h3>Breakdown of the code -🥌</h3>

1. The code uses the time module for time-related functions and the colorama library for adding color to the output.
```jsx
import time
from colorama import Fore,Back,Style,init
init()
```

1. The input_close(x) function checks if the user input is 'y'. If it is not 'y', it prints an error message, waits for a short duration, then exits the program. If the input is 'y', it continues 
```jsx
def input_close(x):
	if(x!='y'):
		print("wrong input")
		time.sleep(0.2)
		print("closing...")
		time.sleep(0.2)
		exit(1)
	else:
		pass	

```
2. The print_opreation(num, a) function prints numbers starting from num up to a.
```jsx
def print_opreation(num,a):
    while(num<a):
    	print(num)
    	num= num + 1	

```

4. The code prints a welcome message with a green color using Fore.GREEN from the colorama library.
```jsx
print(Fore.GREEN + """ 
________  ________      
|\   __  \|\   ____\     
\ \  \|\  \ \  \___|_    
 \ \   __  \ \_____  \               
  \ \  \ \  \|____|\  \  
   \ \__\ \__\____\_\  \ 
    \|__|\|__|\_________\
             
                         
""")
print(Style.RESET_ALL)	
```
5. It asks the user if they want to continue and takes their input. If the input is not 'y', it prints an error message and exits. If it is 'y', the program continues.
```jsx
x=input(Fore.RED + "do u want to continue? \n [y/n]")
print(Style.RESET_ALL)  
input_close(x)
```

7. It then asks the user for 'a" input for  starting number and 'num' input for how many number the user want to print from 'a' to 'sum'.
```jsx
num=int(input("enter from which you want to start number  : "))
time.sleep(0.2)
print("ok")
time.sleep(0.5)

a=int(input("input how many numbers \n you want to print   : "))
time.sleep(0.5)
```

9. After getting the input, it asks the user if they want to continue, similar to step 5.
```jsx
z= input("Do you want to countinue!?  : ")
time.sleep(0.5)
input_close(z)
```

10. If the user input is 'y', it calls the print_opreation function to generate and print the numbers starting from the given starting number.
```jsx
def print_opreation(num,a):
    while(num<a):
    	print(num)
    	num= num + 1
```





> [!WARNING]
> Warning: This GitHub repository is protected by the GNU General Public License (GPL) license. This means that copying the contents of this repository without proper permission is strictly prohibited. Any unauthorized use may be subject to legal action. Please respect the terms of the GPL license and seek permission from the repository owner before utilizing any code or materials from this repository.



To contract admin for usage and permission[Telegram](https://telegram.me/zsxxsz1)


> [!IMPORTANT]
> Its currently in early stage, new updates are coming soon!


 
 
<h3 align="center">
  Install On Terminal
</h3>
<li>avalable on every terminal with latest pip and python installed</li>

git clone https://github.com/aritrasa45/AZ-Unlimitedx.git

<pre>cd AZ-Unlimitedx</pre>
<br>

<pre>pip -r install requirements.txt</pre>
 <br>
 <pre>python main.py</pre>




<h3 align="center">
  Update Repo
</h3>
<br>
<pre>git pull </pre>



       





