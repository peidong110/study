# Here is my study notes over the summer

### Bash

Creating a linux subsystem in windows10 is very helpful and useful, since you're combining the advantages of Linux Ubuntu and Windows 10.
After installing it in Windows Store, type ```sudo apt-get update && sudo apt-get upgrade``` to update available packages.
type ```pwd```, and you will see ```/home/username```
So in order to access your Host directory, you need to create an alias.
Type ```vi .bashrc``` and press ``` i ``` to add the line below to your home directory.
``` alias winDir='cd /mnt/c/Users/<Replace this with your user name without brackets.>/Desktop'```
(No Space between windir and '')
Press ```ESC``` and put ```:wq``` to exit vim.
So you can just type ```winDir``` to access your host machine directory

---
### C++
Source: C++ Primier 5th Edition
A reference is not an object, it's actually just another name of an exising objects.
It must be an object when creating a pointer.
```int &val = 13 ``` 
will cause an error, since 13 is not a object, so in order to fix this, you can just simply write like this
```
int num = 13;
int &ptr = num;
 ```
The output of the programme below is 10 instead of 5. Since ri is the pointer that points to variable i, even if 5 is assigned to the varible i, but when 10 is assigned to ri, the value of i is changed at the same time, this is becasue variable i and pointer ri are sharing the same memory address.
```
#include <iostream>

int main() {
  int i, &ri = i;
  i = 5;
  ri = 10;
  std::cout << i << " " << ri << std::endl;  // 10 10

  return 0;
}
```
Keyword ```const``` is immutable in C++, which means you can not changed the value after intialzing it.
```
const int size = 128;
size = 222; // assigning a new value to const Size will cause an error
```
But you may copy values from other variables 
```
int a = 30;
const int b = a; // this will workm since it's not changing the values but copying.
```
---


### Version Control
Lest we destroy or damage the data in our Master branch, we need to create a branch and make changes in the branch, in order to do that you can just type ```git checkout -b branchName``` And this will create a new branch and switch into that branch. You can modify your changes there. Using ```git status``` will let you know the changes you made. 
