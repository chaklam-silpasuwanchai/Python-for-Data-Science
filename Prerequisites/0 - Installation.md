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
5. [Ensure the migration](#5-ensure-migration)
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


# <a name="5-ensure-migration"></a>5. Ensure the migration

As said in the beginning, my goal is to have as clean as possible set up and easily migrating to new machine. For the past topics, we have achieved **clean set up**. When you want to work, you start Docker, start container, and code. When you are finished, you close everything and kill the **vmmem** process. No process is hogging your resources. Finally, when you are done with any project, you just delete Docker image and destroy containers. **Clean~~!!**

Now, let's establish a plan when your current machine decides to give you up and stop working. What will you do?

First, let's decompose the project into components. What does it need in order to develop a project?

1. A machine: subject to break
2. Python Environment: .Dockerfile, docker-compose.yml -> if you have these two files, you can always create a copy of your environment.
3. Your code: ...
4. Your data: ...

## 1. Buy a new machine

Surely, if the current machine is broken, get a new one. Set up Docker and VScode, and we are half way there.

## 2. Python Environment

Currently, our `.Dockerfile` has Python3. Along the course of development, you will surely need other library such as `numpy` and `pandas`. So, when we are migrating to another machine, we have to have these libraries too.

Currently, our `.Dockerfile` looks like this.
```
FROM ubuntu:20.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
CMD tail -f /dev/null
```

This means there are no libraries when we build and run the image. Sure, once the container is initiated, you can run `pip3 install` inside the container to get library and never destroy your container. But we are planning for **Machine is gone** scenario, so there are ways you can ensure your container will have the libraries it needs.

### 2.1 Put it in the .Dockerfile

You can specify the list of libraries you need in the `.Dockerfile`. This way, every time you build the image, it will always have the libraries. The only downside is you have to keep track of the libraries you are using in the project and put it in the `.Dockerfile`.

```
FROM ubuntu:20.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
RUN pip3 install numpy
RUN pip3 install pandas
CMD tail -f /dev/null
```

### 2.2 Use virtual environment

Virtual Environment is a concept of managing project-level environment. Before the existing of Docker, when you are developing multiple projects and want to ensure conflict free, you use virtual environment. We do not need it in the Docker since we should build one image for one project, but that does not mean there is no benefit of virtual environment when paring with container set up.

When you use virtual environment, there will be a folder consisting of a copy of python and libraries. This is created per project, and you can always create a list of libraries you are using in each project.

Base on the above information, you have two benefits.

1. You can map the volume of that **copy of python and libraries** to the machine disk. Every time you create a new container, just map the volume, and you are good to go.
2. You can save the **list of libraries** as a file and put it in the `.Dockerfile`.

For this approach, I will have my `.Dockerfile` and `docker-compose.yml` as followings

```
FROM ubuntu:20.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
RUN pip3 install pipenv
CMD tail -f /dev/null
```

```
version: '3.9'
services:
  python:
    image: python
    build: 
      context: .
      dockerfile: .Dockerfile
    volumes:
      - .venv/:/root/projects/.venv
    environment:
      # `pipenv` will create an environment in the working directory
      - PIPENV_VENV_IN_PROJECT=1
```

There are couples of virtual environment module for Python. I use `pipenv` for its ability to create Pipfile (list of libraries) for me automatically.

## 3. Your code

If the machine is broken, you may be able to retrieve the code in the HDD/SSD. But, what if the HDD/SSD is also destroyed? Then you would need to have a second copy of your code somewhere else. Here we talk about backup. You will have multiple options and workflows to choose. You might save your code in the Google Drive, OneDrive, and other Drive from other cloud storage provider. You might have your own USB drive and remember to copy the code to the Drive. All of above are fine. However, I want to introduce you to Git and GitHub.

Here is my analogy.
- Youtube - GitHub
- Channel - Repository
- Videos - Files

The two things are similar in managing/hosting/publishing a bunch of objects. However, the similarity end there, but it is good to know some term and compare to the known word.

### GIT
Git is a protocol. It solves the problem of *versioning*. When you have a project, you want to create one repository for that project. Within the repository, Git will **keep track of the changes** and save each change in a node and form a tree. Each node called `commit`. You can have multiple branches (tree) and merge branches to sync up the changes. Because it keeps track of the changes, you can always go back in history for referencing, or even revert the entire project the previous version (back to the future~~).

### GitHub
GitHub is a website that support Git protocol. You can sync up your local repository with the remote (repo in the GitHub) via the Git protocol. This enables easy collaborating with peers and backup.

Now, if you use GitHub, you code + .Dockerfile + docker-compose.yml + Pipfile can all be saved to GitHub. This means if you have to migrate the project, it just a simple pull from the GitHub.

Great, this mean no more manually backup? Sadly, no. GitHub has a limit of how big your file can be uploaded. (Git can keep track of any file size, but GitHub disallowed the big file to be uploaded). Thus means you can not upload your Data to the GitHub and you need to manually back up yourself.

## 4. Your data

Well, manually back up your data. A database, dataset, and other binary files are usually discarded from GitHub repository. You can use OneDrive and Google Drive to back up these data.

## Execution

Here our plan is to put everything into GitHub except some confidential/big data. Our repository will look like this.

```
repository
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--docker-compose.yml
```

When we build the image, it will map the volume `./projects` into the container so that we have access to the source code (you can change to name of the folder). Here we update the `docker-compose.yml` to do that.

```
version: '3.9'
services:
  python:
    image: python
    build: 
      context: .
      dockerfile: .Dockerfile
    volumes:
      - ./projects/:/root/projects
    environment:
      # `pipenv` will create an environment in the working directory
      - PIPENV_VENV_IN_PROJECT=1
```

Now, how do we initiate Git in our local machine?, and sync this repository with GitHub? If you have never used Git before, my suggestion would be to install GitHub Desktop. What I am about to show you will be hated by Git enthusiast around the world and many hardcore Git users will always say "use the command line is a must" which is true in some situations (also applied to Docker). Eventually, you should learn how to use Git in the command line/terminal environment. However, for all people who are not familiar with terminal environment, it usually scared them of. Moreover, in a daily basis, I would spend my time writing code rather than recalling the command for Git's routine. Not to mention that I have to install Git for Windows to have the Git command in my machine.

## GitHub Desktop

Visit <a href="https://desktop.github.com/">GitHub Desktop</a> and download the installer according to your operating system. After all the installation. You will have to have a GitHub account (well, we are about to upload and use GitHub service). Therefore, visit <a href="https://github.com/">GitHub</a> and create yourself an account. Here I would suggest you to create your own personal account using your **personal email address**. Nowadays, GitHub has become another way for the company to know you. Then, to get **GitHub Pro** plan, you have to bind AIT email address once you have created your account.

Once you have an account and login to it in the GitHub Desktop, click menu **File > New repository**

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/github-desktop-new-repo.png)

- **Name**: The repository name. This is the same name as your folder if you already created one.
- **Description**: Can leave as blank.
- **Local path**: This is where your repository/folder exist. Read more below.
- **Initialize this repository with a README**: Well, it will just create README.md. If you already have one, you can ignore.
- **Git ignore**: If you want to exclude anything of the repository, you put it in the `.gitignore`. Here, you select a template base on the programming language you about to use which normally have the same list of ignored files. 
- **License**: By default, your project is publicly available. To allow anyone else to use your project legally, you need to specify a term of use through the license file. Right now you can ignore this, but in the future, you should take sometime to choose the license you want to use.

Now, about the local path. GitHub Desktop does not expect you to point the destination to the already exist project/folder. Thus, it will create a new folder if the folder/path is not exist. For us and our situation, we already have a folder with our code on it. Therefore, we have to be more specific. For my case, I have all of my projects/code in `D:\MyProjects`. Inside this folder, I have a bunch of folders for different project I am/was working on. My new repository is here to. Here is the structure of my machine.

```
D:\
|--**MyOtherFolders**/
|--MyProjects/
  |--**Project1**/
  |--**Project2**/
  |--repository <<<< My new project
      |--projects/
          |--.venv/
          |--Dataset/
              |--Train/
                  |--data1
                  |--data2
              |--Test/
                  |--data3
                  |--data4
          |--**folders**/
          |--**files**
          |--Pipfile
          |--Pipfile.lock 
      |--.Dockerfile
      |--docker-compose.yml
  |--**Project3**/
  |--**Project4**/
|--**MyOtherFiles**
```

Now, I should name my `repository`. I will name it `DSAI-python` to reflex that this is the repository for this course.

```
D:\
|--**MyOtherFolders**/
|--MyProjects/
  |--**Project1**/
  |--**Project2**/
  |--DSAI-python <<<< My new project
      |--projects/
          |--.venv/
          |--Dataset/
              |--Train/
                  |--data1
                  |--data2
              |--Test/
                  |--data3
                  |--data4
          |--**folders**/
          |--**files**
          |--Pipfile
          |--Pipfile.lock 
      |--.Dockerfile
      |--docker-compose.yml
  |--**Project3**/
  |--**Project4**/
|--**MyOtherFiles**
```

In the menu of create new repository, the `Name` is `DSAI-python` and `Local path` is `D:\MyProjects`. I will leave other fields as default. Then, `Create repository`.

Back to my `DSAI-python`, I will have one new folder on the root path. If you can not see it, you have to enable Hidden folder.

```
DSAI-python
|--.git/ <<<<< new
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--.gitattributes
|--docker-compose.yml
```

## Gitignore

If we go back to the GitHub Desktop, we will notice that GitHub Desktop already commit one change with message "Initial commit" and in the commit, our `Dataset` has already *added* into the repository. For my purpose, we want to exclude this from the repository.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/github-desktop-init-commit.png)


To fix this, we have to revert the commit and exclude the `Dataset` from the git using `.gitignore`.

1. Revert the `Initial commit` by right-click on the commit and select `Undo commit...`
![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/github-desktop-undo-commit.png)

2. Create a file `.gitignore` in the root path.

```
DSAI-python
|--.git/
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--.gitattributes
|--.gitignore
|--docker-compose.yml
```

3. Add `Dataset` into the `.gitignore` and save the file

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/github-desktop-ignore.png)

Notice that all files in the Dataset folder is gone from the changes tab.

4. Commit to **main**

Now, Git will ignore the entire of Dataset folder even the assistance of the folder. This causes one thing, when you publish this to GitHub, there will be no sign of Dataset folder. Thus, when anyone clones the repository, they will have to create a folder themselves. 

Okay, if I want to keep my folder but not my files, I have to change the `.gitignore` from folder name to filename, is not it? No.

Even though you have spent your time listing all the files you want to exclude, if, in the end, the folder is empty, it won't appear in the repository. **Any folder that is empty will not appear in the repository**. Thus, if you wish to have a folder in your repository, you need to have at least one file. In the convention of Git, we put `.keep`, `.keeps` or `.gitkeep` in any folder we want to keep it existence in the repository. Then, we add `!.keep`, `!.keeps`, or `!.gitkeep` in the last line of `.gitignore` to exclude the ignoring of the file. Finally, we change from ignoring `Dataset` folder to ignoring files in the folder using `Dataset/*`

Here is my `.gitignore`

```
Dataset/*
!.keep
```

Here is my folder structure

```
DSAI-python
|--.git/
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
        |--.keep
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--.gitattributes
|--.gitignore
|--docker-compose.yml
```

Note that this will not work with any file that is already added to repository. You can only ignore files that is not included in the repository only. If you make a mistake and want to ignore a file after many commits, there is a way and I will leave it to you to figure it out.

## Publishing the repository

Now you have a repository running in your local machine. You can make changes and create commits or make a new branch and merge as many as you desire. When you are ready, you can publish this repository to GitHub. To do that, click `Publish repository`.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Python-for-DS-AI/master/.0%20-%20installation_image/github-desktop-new-repo.png)

Here you can change the name of the repository (this will not affect the folder name in your local machine) and an option whether to make this repository a private or not. Once done choosing, just click `Publish repository`. Done~~!!

## Syncing and Collaborating

Now, you have two repositories (local and remote/GitHub), and you wish that both repositories will look the same. To achieve you have to push and pull. Here is a diagram.

![alt](https://greenido.files.wordpress.com/2013/07/git-local-remote.png?w=696&h=570)

Every time you are committing, you are only interacting with the local repository. To sync the local repository, you have to `push` the changes/commits to the remote (GitHub) one. 

Now, if you have a second machine or your friend are also working on the same project using the same repository, that means there is another local repository in that another machine. Are you confusing? Let's imagine you have a PDF file you want to share with your friend. You choose to upload the PDF to Google Drive and share the link to your friend (`push`). Your friends see the file exist in the Google Drive. They will have to download in to their machine (`pull`). In this context, I map to the following analogy.

- PDF - commit
- You machine - Local Repository
- Google Drive - GitHub/Remote Repository
- Upload PDF - Push
- Your friend machine - Another local Repository
- Download PDF - Pull

`fetch` is to check for new commits but not push or pull.

In summary, you will have to push and pull consistently to make sure that both repositories are in sync.

## What else?

There is no rule in GitHub. There is only `main` branch and other branches. The meaning of branch is up to you and your team.

Conflict is not an error but rather Git is asking you to help decide what you want. Remember that Git is only tracking changes of files. Conflict happens because in one line of one file is changed from both persons (commit). Conflict can and will happen if more than one person are working on the same file. If you want to avoid this, you have to plan your project structure out and breakdown your code into multiple files and each team member working on different files. Anyhow, it just my suggestion and my best practice. You can always adapt and make your own practice.
