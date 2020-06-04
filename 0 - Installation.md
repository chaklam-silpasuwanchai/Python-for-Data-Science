# Table of Content

0. [What and why?](#h1-whatNwhy)
1. [Python Installation](#h1-installation)
    1. [Ubuntu](#h2-ubuntu)
    2. [Windows](#h2-windows)
    3. [MacOS](#h2-macos)
# <a name="h1-whatNwhy"></a>0. What and Why
### What is Python? 
[quote](https://www.w3schools.com/python/python_intro.asp)

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

- web development (server-side),
- software development,
- mathematics,
- system scripting.

### Why uses Python?
[quote](https://www.w3schools.com/python/python_intro.asp)
- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-orientated way or a - functional way.

### Before you start
1. There are two major versions of Python which are Python2 and Python3. Note that when you call `python` in your terminal, you are referring to Python2. Instead, you need to explicit version 3 to call to Python3 (`python3`).
2. There are different syntax between the two versions. We are recommended that you use version 3 throughout the course.

# <a name="h1-installation"></a>1. Python Installation
## <a name="h2-ubuntu"></a>1. For Ubuntu user

[Reference](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)

- [A. Install via `apt`](#h2-1-a)
- [B. Virtual Environment](#h2-1-b)
- [C. Virtual Environment in action](#h2-1-c)
- [D. Jupytor](#h2-1-d)


### <a name="h2-1-a"></a> A. Install via `apt`
1. Open your terminal
2. Update and Upgrade your current packages.
```
$ sudo apt update
$ sudo apt upgrade
```
3. Install `python3`
```
$ sudo apt install python3
```
4. Verify that you have `python3`
```
$ python3 -V
Python 3.8.2
```
5. You would need to install a package/library/module downloader. Similar to Python, there are `pip` for Python2 and `pip3` for Python3.
```
$ sudo apt install python3-pip
```
6. Verify thar you have `pip3`
```
$ pip3 -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```
7. Let's try to install your first package `numpy`
```
$ pip3 install numpy
Collecting numpy
  Using cached numpy-1.18.4-cp38-cp38-manylinux1_x86_64.whl (20.7 MB)
Installing collected packages: numpy
Successfully installed numpy-1.18.4
```

*Note that we are not using `sudo` in front of the command. When you are installing the ubuntu package, it is required to use root privilege here. Using `sudo` in front of any command to run the command as root. However, when you are installing the python package, you do not need to issue root privilege. In fact, doing so is not recommended due to the security concerned.*

8. Install development tools.
```
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

### <a name="h2-1-b"></a> B. Virtual Environment
*For beginners, you can ignore this part but we recommend you to try it out for good practice.*

> Virtual Environment is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. --- [python.org](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#:~:text=virtualenv%20is%20used%20to%20manage,system%20tools%20or%20other%20projects.)

Remember that a package that we download using `pip3` is written by a human. There may be updates to the package for various reasons. Updating the package may cause your projects to crash due to conflicting in the newer version of the library.

To overcome this problem (and many more reasons to do the following), we will set up a Virtual Environment.


1. Our environment manager of choice is `venv`
```
$ sudo apt install python3-venv
```
2. I will set up my first environment for this course names pythonDSAI.
```
$ python3 -m venv pythonDSAI
```
3. It should create a directory that names after the environment name.
```
$ ls pythonDSAI/
bin  include  lib  lib64  pyvenv.cfg  share
```
4. To activate the environment, you have to call the `activate` file under your newly created environment folder using `source` command. 
```
$ source pythonDSAI/bin/activate
(pythonDSAI) $ 
```
5. To exit the environment, simply type `deactivate` from anywhere.
```
(pythonDSAI) deactivate
$ 
```
### <a name="h2-1-c"></a> C. Virtual Environment in action
We have just installed `numpy` under our global environment. For the best practice, we want our `numpy` to be exist under the environment we wanted.
1. Check that `numpy` is installed.
```
$ pip3 list | grep numpy
numpy         1.18.4 
``` 
*`pip3 list` is a command for listing all the installed packages. `grep` is a command that filters out the text and shows the line that has `numpy` in it. The vertical bar `|` is commonly referred to as a "pipe". It is used to pipe one command into another. That is, it directs the output from the first command into the input for the second command.*

2. remove `numpy` from global
```
$ pip3 uninstall numpy
```

3. Activate your target environment.
```
$ source pythonDSAI/bin/activate
(pythonDSAI) $
```

4. Install and verify the `numpy` package only exist in the target environment.
```
(pythonDSAI) $ pip3 install numpy
(pythonDSAI) $ pip3 list | grep numpy
numpy         1.18.4 
(pythonDSAI) $ deactivate
$ pip3 list | grep numpy
$
```

5. Here are the list of library you may need for the next four lectures.
```
(pythonDSAI) pip3 install numpy
(pythonDSAI) pip3 install torch
(pythonDSAI) pip3 install torchvision
(pythonDSAI) pip3 install matplotlib
(pythonDSAI) pip3 install pandas
(pythonDSAI) pip3 install seaborn
(pythonDSAI) pip3 install pandas_datareader
(pythonDSAI) pip3 install sklearn
```
### <a name="h2-1-d"></a> D. Jupytor
[Reference](https://jupyter.org/install)

You will need a text editor to write a code. While there are many great python editors out there, we will use Jupytor for this course to simplify the process of checking your works. 

You can install Jupytor using `pip3` in our global python.

1. Install Jupytor via `pip3`
```
pip3 install jupyterlab
```

2. To start jupytor simply type the following command. Your current folder will be the workspace.
```
jupyter notebook
```
![alt](https://link)
3. 


## <a name="h2-windows"></a>2. For Windows user
## <a name="h2-macos"></a>3. For MacOS user
