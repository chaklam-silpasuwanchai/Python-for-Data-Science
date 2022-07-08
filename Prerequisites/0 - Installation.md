# Goal
In this course, we will be using Python as a learning language (of cause, this is Python for Data Science course). There are multiple ways you can get Python running in your machine. In this journey, I will show you my way to get Python running in your machine.

My setup consists of
1. Windows 11 home (Operating System)
2. Docker Desktop + WSL2 (App)
3. Visual Code Studio (Text Editor)
4. GitHub Desktop

# Table of Content

0. [What and Why](#0-whatNwhy)
1. [Docker](#1-docker)
2. [Visual Studio Code](#2-vscode)
3. [Docker Compose](#3-docker-compose)
4. [Using Python](#4-using-python)
# <a name="0-whatNwhy"></a>0. What and Why
### What is Python? 
[quote](https://www.w3schools.com/python/python_intro.asp)

> Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
> 
> It is used for:
> 
> - web development (server-side),
> - software development,
> - mathematics,
> - system scripting.

### Why uses Python?
[quote](https://www.w3schools.com/python/python_intro.asp)
> - Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
> - Python has a simple syntax similar to the English language.
> - Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
> - Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
> - Python can be treated in a procedural way, an object-orientated way or a - functional way.

### Before you start
1. There are two major versions of Python which are Python2 and Python3. Note that when you call `python` in your terminal, you are referring to Python2. Instead, you need to explicitly call `python3` to use Python version 3.
2. There are some differences in syntax the two versions. We are recommended that you use version 3 throughout the course.

# <a name="1-docker"></a>1. Docker
## Why?
To me, I want my machine/PC/laptop to be as clean as possible because I use my laptop for my daily routine, games, hobbies, and works. In addition, how can I make sure that I can easily switch to a new machine and continue working.

Previously, my go-to solution was to use Virtual Machine (VM). It was a great experience in many aspects, especially, migrating and backing up works. However, VMs can not access hardware and this limitation alone is a dealbreaker for anyone who wants to work with Deep Learning.

Now that Windows-subsystem-for-Linux (WSL2) is so great and convenient of managing environment of Docker, I never look back.

## Installation

The easiest to get a Docker running in your machine is through Docker Desktop. <a href="https://www.docker.com/products/docker-desktop/">link</a>

Note that for `Linux` users, the last time I tried Docker Desktop on Linux, it was not working properly. It might have change. I don't know.

Note for `MacOS` users, good luck. (I am a Windows enthusiast)

Now, for `Windows` users.
*This guide assumes you have a fresh installation of Windows*

1. Install the `Docker Desktop` from <a href="https://www.docker.com/products/docker-desktop/">link</a>
2. Once the installation is done you may need to restart your OS.
3. Upon a startup, the `Docker Desktop` will launch up. It won't successfully to do so because you do not have WSL2. In the error box, there will be a link to *WSL2 installation guide* from Microsoft. Now, run this command to install WSL2 `wsl --install` in your cmd/terminal.
4. Check the result with this command.
```
> wsl -l -v
  NAME                   STATE           VERSION
* docker-desktop-data    Running         2
  docker-desktop         Running         2
```
This command shows you the kernel and version. If you are not going to use WSL anymore, this is all we need.
5. Launch `Docker Desktop` again.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/docker-desktop.png)

Tips:
If you take a look in the `Task Manager`, there is a process named `Vmmem` running. This is the Docker process. Once the `Docker Desktop` is started, `Vmmem` will always be there. To fully shut the Docker, use `wsl --shutdown` command in the cmd/terminal. 

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/vmmem.png)


# <a name="2-vscode"></a>2. Visual Studio Code (vscode)

Code is simply a text. This means you can write a code with any text editor in the world, including Notepad. That is doable until you have to write a bigger project with many module plus libraries. At this stage, having some help would be nice. 

Here come the Integrated Development Environment (IDE), 

[quote](https://en.wikipedia.org/wiki/Integrated_development_environment)
> a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger. Some IDEs, such as NetBeans and Eclipse, contain the necessary compiler, interpreter, or both; others, such as SharpDevelop and Lazarus, do not.
>
> The boundary between an IDE and other parts of the broader software development environment is not well-defined; sometimes a version control system or various tools to simplify the construction of a graphical user interface (GUI) are integrated. Many modern IDEs also have a class browser, an object browser, and a class hierarchy diagram for use in object-oriented software development.

In my words, in order to enjoy developing code more, a good code developing software is a must, otherwise, you will spend more time fixing basic bug than creating a magic.

Basic bug??

Yes, basic bug, such as syntax error, wrong variable name, undefined blah blah blah. basic bugs.

These are avoidable or, at least, can be mitigated by using a better editor.

In Python, you can use `PyCharm` <a href="https://www.jetbrains.com/pycharm/">link</a> for the ultimate Python experience. However, this only support Python. As I told you earlier, I like to keep my machine as clean as possible. Therefore, if I want to write other languages, I will have to install another IDE for that.

Enter `Visual Studio Code` <a href="https://code.visualstudio.com/">link</a>. To define VScode, it is difficult. 

[quote](https://en.wikipedia.org/wiki/Visual_Studio_Code)
>Visual Studio Code, also commonly referred to as VS Code,[9] is a source-code editor made by Microsoft for Windows, Linux and macOS.[10] Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. Users can change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality.
>
>In the Stack Overflow 2021 Developer Survey, Visual Studio Code was ranked the most popular developer environment tool, with 70% of 82,000 respondents reporting that they use it.[11]

In my words, it is a versatile code editor. It used to be lightweight, and it will somehow is when compare to other IDE. With an extension, it can adapt to any languages. And VScode can feel like a complete IDE with its ability to integrate with Terminal and Docker.

Enough said, download the VScode now. https://code.visualstudio.com/

# <a name="3-docker-compose"></a>3. Docker Compose

Let's get back to Docker because we only install it without learning about it.

Do we really need to understand Docker before we can use it? No. Should we? Yes.

## What is Docker?

[quote](https://en.wikipedia.org/wiki/Docker_(software))
>Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine. It was first started in 2013 and is developed by Docker, Inc. Wikipedia

The key is `virtualization`. It is a form of simulation just like VM but instead of emulating the entire machine, it is only simulating kernels. In a more basic word, I can have Ubuntu 20.04, 18.04, 16.04, CentOS, Redhat, and MacOS running on my Windows. It does not end here, instead of running just a bare bone OS, it can also be pre-installed application. Thus mean, I can run MySQL, PostgreSQL, Reddis, Java, Python, C#, C++, Golang, ... in just a matter of minutes. **Using Docker will shorten installation steps and ensure that anyone who use the same image will have the same environment.**

Wow, that simply the same benefit as VM but no, Docker is not VM as it does not emulate hardware. Instead, Docker sees all of your hardware. That is why we can use GPU.

In Docker, `Docker image` and `Container` are the two confusing words for newcomer. To understand this, let's think how did we install Windows on a fresh machine.

1. Download ISO and create bootable USB
2. Install Windows 
3. Configure and install software we want to use
4. If the PC crash, we restart it.
5. If the PC is broken, we reinstall it and repeat from step 2.

For Docker, if you want to have Ubuntu 20.04 we do the followings:

1. Download Docker Image of Ubuntu 20.04.
2. Run the image. Thus, we have a container that runs Ubuntu 20.04. 
3. We install the software we wanted to use.
4. If we stop the container, we can start is to resume use it.
5. If we destroy the container, we have to recreate it thus repeat from step 2.

There for, `Docker Image` is what we want to start with and `Container` is an instance of what we start. This means you can create multiple Ubuntu 20.04 containers that consist of different software for different purpose, hence reduce the chance of library conflict.

The main different between Docker and VM is the user see a container as a process not an instance. Therefore, the container is deletable. In fact, a container is not expecting to exist forever and is not a thing you have to manage. This causes one feature of Docker, we can always build a new image, and we are expecting to do so.

Here is the summary and simple workflow of Docker.

```
Base Image -> *customize* *build* -> My Image -> *run* -> container
```

For our purpose, we want to use Python and some library like `numpy` and `pandas` on Ubuntu 20.04, then here is what we will do next.

```
Ubuntu 20.04 -> *customize* *build* -> Python Image-> *run* -> Python Container
```

Sure you can find the base image with Python3 but for the sake of knowledge, we will proceed with my plan.


## Base Image
To find what you want to start with, you have to search from the <a href="https://hub.docker.com/">Docker Hub</a>. Simply search for Ubuntu and find what you want. Here is the <a href="https://hub.docker.com/_/ubuntu">Ubuntu official Image</a>. 

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/docker-hub-ubuntu.png)

If you just want an Ubuntu image, 
```
docker pull ubuntu
```

But we want a specific version of Ubuntu. Click `Tags`.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/docker-hub-ubuntu-tags.png)

```
docker pull ubuntu:<tag>
```

Tag is a section to specific the version and to find what version we want, we have to do some research and read the Description of each image provider. For our goal, we will use the following command.
```
docker pull ubuntu:20.04
```

Okay, so run the command? What is this `pull` command anyway?

Pull is to download the image in to your computer, but you don't really need to do that since Docker, when build/run, will `pull` automatically when the image is not found on the machine.

For now, we remember the image name and continue with customizing.

## Custom Image

To customize the image we have to create a `.Dockerfile` file. 

```
FROM ubuntu:20.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
CMD tail -f /dev/null
```

`FROM` will use the `ubuntu:20.04` as a base image. `WORKDIR` is like `cd`, but it will also create a folder when the path is not exist. `RUN` will execute the command in terminal. And, `CMD` is what will the container do (remember that it is designed to be a process for one purpose).

## Build 

We can build the image from `.Dockerfile` using the following command.
```
docker build .
```

## Create container

Once we have the image that we want to use, we will create a container (which is an instance of the image) using the following command.

```
docker run IMAGE[:TAG|@DIGEST]
```

and now we have the container.


## Tedious?
One this that does not appeal to me is a bunch of command I have to remember in order to create a container. We have not yet open the port, mapping volume, assign hardware, and limit the resources. That are a bunch of option we have to specify in the `run` command.

Now we will be more civilize and use `Docker Compose`

## Docker Compose
In a nutshell, docker-compose help you to craft your `run` command in the `yml` format. In addition, the docker-compose helps to manage multiple containers when your app consists of multiple services. 

In our case, we will use it in place of `docker run` command.

Create a file `docker-compose.yml`

```
version: '3.9'
services:
  python: # service/container name
    image: python # image name
    build: 
      context: .
      dockerfile: .Dockerfile
```

Now, normally you will have to use `docker-compose up blah blah` to run the service. Here, I will use `VScode` to start the service. Before that, go to `Extension` and install `docker` extension into your `VScode`.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/vscode-docker-ext.png)

Once you installed this extension, find your `docker-compose.yml` file, right click, and `Compose up`

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/vscode-docker-compose-up.png)

## Summary
Now, all we have to do to get the container is

1. create `.Dockerfile`
2. create `docker-compose.yml`
3. Compose up


# <a name="4-using-python"></a>4. Using Python

Now, we want to access the Python in the container using VSCode. Luckily, things are already simplified. We have to install `Remote - Containers` extension in VSCode.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/vscode-remote-ext.png)

Once we installed that, we can go to Docker menu, right-click on the target container, and select `Attach Visual Studio Code`.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/vscode-remote-container.png)


Now we have Python running. You are ready for this course.