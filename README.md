### Bash and Linux
Linux subsystem in Windows10:<br/>
Creating a linux subsystem in windows10 is very helpful and useful, since you're combining the advantages of Linux Ubuntu and Windows 10.
After installing it in Windows Store, type ```sudo apt-get update && sudo apt-get upgrade``` to update available packages.
type ```pwd```, and you will see ```/home/username```
So in order to access your Host directory, you need to create an alias.
Type ```vi .bashrc``` and press ``` i ``` to add the line below to your home directory.
``` alias winDir='cd /mnt/c/Users/<Replace this with your user name without brackets.>/Desktop'```
(No Space between windir and '')
Press ```ESC``` and put ```:wq``` to exit vim.
So you can just type ```winDir``` to access your host machine directory
<br>
How to change the host name of linunx machine? ```sudo hostname newName``` and key in your password, you will be able to update your host name at runtime. However this will be changed back to your previos name when you shut down your machien or reboot it. You need to change the actual name in configuration which is in ```/etc``` <br />
How to become a super user? ```sudo su -``` <br />
### history 
If you want to check out the history of commands you ran in the past, you can achieve that by type ```history``` and you will be able see a list like 
```
 1999  repo sync -j8
 2000  ls
 2001  history 
 2002  2201
 2003  history 
``` 
Sometimes command can be long and it's hard to retype it again. So if you do not want to type it manually again, you can do !NumberOfId, if I want to rerun command ```repo sync -j8``` You can just type ```!1999``` to help you to do that


### find
If you want to look for a file in a folder, you can use find keyword
```find . -name fileName.extension```
If the file exits terminal will return ./fileName.extension, else nothing will be returned.



---

### C++
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
### [Google Test Framework & GMock](https://github.com/google/googletest)

They are used to test code and interface of a cpp file. They are like Junit Test in Java
Google Test Framework 
Let's say we have three functions in a class called happy.cpp: <br />
```
class happy{
   void sayHello(){implementation omitted}
   void stringConcatenation(string & name){implementation omitted}
   void act(string &name, int age){implementation omitted}
}
```
These 3 functions are all in a cpp file called happy.cpp/ happy.cc
If we want to test out them, we can create a file called happyMock that inherits from happy.cpp,
```
class happyMock: public happy{
 
    MOCK_METHOD0(sayHello());
    MOCK_METHOD1(stringConcatenation(string & name));
    MOCK_METHOD2(string &name, int age));
    //MOCK_METHODX, where X is the parameter in your your function
}
```

---

### Version Control
Lest we destroy or damage the data in our Master branch, we need to create a branch and make changes in the branch, in order to do that you can just type ```git checkout -b branchName``` And this will create a new branch and switch into that branch. If you want to go switch to the previous branch you've been working on, you can type ```git checkout -``` You can modify your changes there by using ```git status``` will let you know the changes you made.  ```git add .``` will all the changed files. ```git commit -m "Replace this with your commit mssages" ``` will make the commit, and leave a commit message. ```git push origin branchName``` will push all the changes to that branch. However if you add something which you did not intend to add, you can use ```git reset branchName^``` to reset the banch and clear all the history. 
<br />
So after resetting the branch, when you are trying to add files and push changes to your own branch. You might face a problem which indicates ```Updates were rejected becasue the tip of your current branch is behind.``` The reasons for this happening is that you just uploaded files that you don't want, now when you reset the branch, and you're not adding items(files you don't whant) this time. In order to solve this issue, you can actually use ```git push -f origin branchName``` to forece git to make changes. At this point you have successfully deleting files you do not want.


---


### Data Structure
**Linked list** is a data structure that stores **references && nodes**
references would be able to store front and back references at the same time or not, nodes stores all the data.
It's efficient and quick to insert a new node or deleting a node, however it's not very efficient to specificaly look for a node

---

### Latex
How to bold a word or letter in Latex file?:```\textbf{textddddddd}```<br / >
How to add code fragment in Latex file?:
```
\begin{verbatim}
print("Hello World")
\end{verbatim}

\begin{lstlisting}[language=c++, frame= single]
Cout << "ddddd"<<endl;
Cout << "ddddd"<<endl;
\end{lstlisting}
```

