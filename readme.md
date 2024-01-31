# Enhanced Homework 2 Instructions

## Overview

Welcome to Homework 2! In this unit, our goal is to establish a professional development setup for Python. This will include familiarizing yourselves with several key tools and practices that are integral to modern software development. All you need to do to complete this assignment is setup a new project that works just like mine in the video.  You need to be able to run pytest, pylint, and coverage.  You also need to read all the articles in the required section.



### [Instructor Unit Video](https://youtu.be/HElKd45vVjk)
Specifically, you'll set up:

- **Python Virtual Environments**: Essential for managing project-specific dependencies.
- **Pytest**: A powerful framework for writing and running Python tests.
- **Pylint**: A tool for analyzing your Python code for errors and enforcing a coding standard.
- **Coverage**: A tool for measuring the coverage of your unit tests.
- **Git**: To practice version control techniques such as branching, merging, and using stash.

Additionally, we will delve into integrating these tools with Visual Studio Code (VSCode) and Windows Subsystem for Linux (WSL 2), enhancing your ability to manage development tasks.

**Note: You should practice GIT and setting up a project more than one time, until you feel comfortable with all the commands.  Even if you us VScode, you should still use the terminal for as many GIT commands as possible.  Building a solid foundation with GIT will help you a lot in the long run**

## Learning Objectives

By the end of this homework, you should be able to:

1. Set up a Python virtual environment and manage dependencies.
2. Use `pip freeze` to create a `requirements.txt` file.
3. Configure and utilize pytest, pylint, and coverage in a Python project.
4. Apply git commands for effective version control.
5. Integrate VSCode with WSL 2 for a streamlined development process.

## Conceptual Readings Required

Understanding the broader context of these tools and methodologies is crucial. Please read the following materials to gain insights into their professional application:

1. **Automated Testing at Google**: A case study on the importance of automated testing in software development. [Read here](https://itrevolution.com/articles/case-study-automated-testing-google/).
2. **Agile Manifesto**: The foundation of Agile software development, highlighting the role of automated testing. [Read here](https://agilemanifesto.org/principles.html).
3. **The 12 Factor App**: A guide to best practices in maintaining mission-critical software, relevant to our course. [Read here](https://12factor.net/).
4. **Continuous Integration**: An article explaining the practice of continuous testing and deployment, essential for Agile implementation. [Read here](https://martinfowler.com/articles/continuousIntegration.html).

## Instructions 
You need to do the following for this assignment:

1.  Install python using the Mac or Ubuntu instructions below.  You will only do this step once for the course on your commputer.   Mac needs Brew package manager to install Python and Ubuntu needs to just run the command:

```bash
sudo apt update -y
sudo apt install python3-pip
pip3 --version 
```

2. Install python virtual environment, so you can manage the virtual environment to issolate your dependences from the global version of python.  You need to do this once for your computer, this is a global python package.
```bash
pip3 install virtualenv
```
**note** You should try the following to test your install with my project, after you have installed python and the virtual environment manager:
```bash
git clone git@github.com:kaw393939/git_python_testing_setup_homework.git
cd git_python_testing_setup_homework
source venv/bin/activate
pip3 install -r requirements.txt
pytest --pylint --cov
```

3. Now Make a project directory not inside my own project if you cloned mine. **DO NOT CREATE A NEW REPO INSIDE OF THE ONE YOU CLONE FROM ME OR YOU WILL HAVE PROBLEMS**, setup the virtual environment in the directory that you make for your projectand activate it.  For more information see [here](https://www.geeksforgeeks.org/python-virtual-environment/).  You need to do this for each new python project.

```bash
cd .. <-- goes up a directory to get out of the project  you cloned to test your install of python.  Make sure you do a pwd to see where your going to make your project from scratch.

mkdir myproject
cd myproject
virtualenv venv <- Makes a virtual environment in the venv directory (you can make this any directory but you will have to remember it to activate it correctlty)
source ./venv/bin/activate <- you should see (venv) in the terminal command line to indicate that the venv environment of your project is activated
```
4.  Once the virtual environment is a active then install the python dependencies using pip:
```bash
pip3 install pytest pytest-pylint pytest-cov

```

5. Once you have the libraries installed you need to freeze the requiremnts and create your requirments.txt file.  You need to do this so that the versions of the libaries / dependencies you use are saved, so that your project can be installed somewhere else.

```bash
pip3 freeze > requirements.txt

```

**Note** When someone copies / clones your repository they will install the specfic library / dependency requirements for your  project using the command: 

```bash 
pip3 install -r requirments.txt
```

6.  Once you have this done, you will need to create the "tests" and "calculator" folders and add the __init__.py file to each folder.  You need a .gitignore with the same contents as mine, you need the .pylintrc file, and the pytest.ini file.  You will need to put the same code that I have in those files.

7.  Once you have the files made make sure you have the code that I have in my calculator folder's __init__.py file in yours and add the code for your test to the test_calculator.py file.  Essentially, you should have the same files as what I have in this repository.

8.  Run the tests:

```bash
pytest <-runs the tests without pylint or coverage
pytest --pylint <- Runs tests with pylint static code analysis
pytest --pylint --cov <-Runs tests, pylint, and coverage to check if you have all your code tested.

```
9.  Once you have a new project setup and everything working, just submit a link to your repository to Canvas.

## Tutorial References Created by Instructor

- [GIT Tutorial Guide](gitguide.md)
- [Git Merge Conflicts](merge_conflicts.md)

### I recommend that you go through this interactive tutorial on GIT to learn as much as you can about the command line operation of GIT:

#### [Excellent Tutorial on GIT](https://learngitbranching.js.org/?locale=en_US)

## Key Commands

Here are some fundamental Git commands you'll be using:

- **Add a file to staging**: `git add .gitignore`
- **Commit changes**: `git commit -m "added git ignore with sw* files"`
- **Check status and staging**: `git status`
- **Update local branch with remote changes**: `git pull --rebase origin main`

## Python Setup Instructions

### Ubuntu

- Initial Python Setup: [Ubuntu Guide](https://www.redswitches.com/blog/install-python-pip-on-ubuntu/)
- Install the Python virtual environment manager [here](https://www.geeksforgeeks.org/python-virtual-environment/)

### Mac

1. Install Brew Package Manager: [Brew Installation](https://brew.sh/)
2. Set Up Python Virtual Environments with Brew: [Mac Guide](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)

Note: Once virtual environments are set up on Mac, you can follow the same instructions as for Ubuntu.

## Python Readings

These readings will help you understand the tools you'll be using:

- Pip Freeze for Beginners: [Read here](https://dev.to/eskabore/pip-freeze-requirementstxt-a-beginners-guide-5e2m)
- Introduction to Pytest: [Read here](https://realpython.com/pytest-python-testing/)
- Pylint Documentation: [Read here](https://pylint.pycqa.org/en/v3.0.3/index.html)
- Pytest Documentation: [Read here](https://docs.pytest.org/en/7.4.x/)

## Setting Up VSCode with WSL 2

To efficiently open and manage your projects with VSCode instead of the terminal, follow this guide:

- [Setting up WSL and VSCode](https://youtu.be/XY6lTlIW_hM)

---

**Reminder**: Practice and understanding are key. Don’t hesitate to reach out if you have questions or need further clarifications. Happy coding!
