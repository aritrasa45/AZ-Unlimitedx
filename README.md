
<h1 align="center">
  AZ-Unlimitedx v3 🤩
</h1>




 
<h2>
This code is a simple number generator program that allows the user to input a starting number and how many numbers they want to print.
</h2>
<p align="center">
  <img src="https://github.com/aritrasa45/AZ-Unlimitedx/blob/main/20240519_003036.jpg" height="200px"/>
</p>

<h2>Usage of it? -🦸</h2>

<li>In summary, this program is a simple interactive number generator that allows the user to specify a starting number and how many numbers they want to print. It provides colorful output using the colorama library and includes error handling for incorrect user inputs.</li>

<li>Overall, this code is a simple but functional number generator program. It can be used to generate a sequence of numbers for various purposes, such as testing or debug</li>

> [!IMPORTANT]
> <h4>new update 21st march 24</h4>
>
<li>Now it can print certain amount of random number from the limited radiant set by user.</li>
>	
><li>major error handlings and bugs fixes
> added auto clear after 2 second if any user gives wrong input</li>
>	
> <li>added 300 secs of live countdown in the tool when the user id done with it..if the 300 secs passes then it will automaticly clear & end the terminal process</li>
>


<h3>Breakdown of the code -🥌</h3>
<h1 align="center">
  To Make Code like Me
</h1>

<li>Import the Necessary Modules:</li>

- time module for time-related operations.
```jsx
Import time
```


 colorama module for adding colors and styling to console output.

```jsx
From colorama import Fore,Back,Style,init
```

<li> Initialize Colorama: </li>

- init() initializes the colorama module.
```jsx
init()
```

<li>Define a Function to Handle Incorrect Input: </li>

```jsx
def your_error_handler(x,y,z):
```

- input_close(x) checks if the input x is not equal to 'y' and prints error messages before exiting the program.

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


<li> Define Two Functions for Printing Numbers:</li>

- print_opreation(num, a) prints numbers from num to a-1 without delays.

```jsx
def print_opreation(num,a):
    while(num<a):
    	print(num)
    	num= num + 1	

```
- print_slow(num, a) prints numbers from num to a-1 with a 0.2-second delay between each number.

```jsx
def print_slow(num,a):
    	while(a>num):
    		print(num)
    		num= num + 1
    		time.sleep(0.2)

```
<li>Define a Function to Create a Timer: </li>

- timer(m) prints "Printing in m seconds" for m seconds, then prints "starting..." on a new line.

```jsx
def timer(m):
     	while(m>0):
     		print("Printing in",m,"seconds",end='\r')
     		time.sleep(1)
     		m = m -1
     		if(m==0):
     		     	print("\n starting....")     	

```
<li>Welcome Message and Input Validation:</li>

- Prints a welcome message and asks the user if they want to continue.
- Calls input_close(x) to handle incorrect input.

```jsx
print(Style.BRIGHT + "welcome to number generrator \n V2")
print(Style.RESET_ALL)
time.sleep(0.3)

x=input(Fore.RED + "do u want to continue? \n [y/n]")
print(Style.RESET_ALL)  
input_close(x)
time.sleep(0.5)

```

 Get Input from the User:



- Gets the start number (num) and the number of numbers to print (a) from the user.

```jsx
num=int(input("enter from which you want to start number  : "))
a=int(input("input how many numbers \n you want to print   : "))


```

<li>Check for Delay Option: </li>

```jsx
l= input("Do you need print Delays? \n [Y/n]")
```
- Asks the user if they want to add print delays.

<li> Print Numbers: </li>

- Based on the user's choice, either print_opreation() or print_slow() is called to print the numbers.

<h2 align="center">
  Without timer delay
</h2>

```jsx 
def print_opreation(num,a):
    while(num<a):
     print(num)
     num= num + 1 
```
<h2 align="center">
  With timer delay
</h2>

```jsx 
def print_slow(num,a):
     while(a>num):
      print(num)
      num= num + 1
      time.sleep(0.2)
```


<li> Thank the User: </li>

```jsx
print(Style.BRIGHT+"Thank You")
```

- Prints a thank you message.


  
<h3 align="center">
  The End :dependabot:
</h3>


<h1 align="center">
what's the use of it?
</h1>

<li>Code Functionality:</li>

This Python code is a number generator that allows users to specify a starting number and the number of numbers they want to print. It offers two printing options:

1. Printing without delays: Prints the numbers consecutively.
2. Printing with delays: Prints the numbers with a 0.2-second delay between each number.

Use of the Code:

This code can be used for various purposes, such as:

* Generating sequential numbers: For creating lists, sequences, or other data structures.
* Testing and debugging: To verify the behavior of loops or other code that involves numerical sequences.
* Educational purposes: Demonstrating concepts such as loops and time management.
* Creating simple animations or progress bars: By printing numbers with delays, you can create visual effects.

How to Use the Code:

1. Download or copy the code into a Python file.
2. Open the file in a Python development environment (e.g., IDLE, PyCharm).
3. Run the code by pressing F5 or using the "Run" button.
4. Follow the on-screen instructions to specify the starting number, number of numbers, and whether you want to include print delays.
5. The code will generate and print the numbers accordingly.




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



       





