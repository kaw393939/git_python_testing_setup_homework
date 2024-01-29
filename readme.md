# Homework 2 

In this unit, you will setup a professional development environment for Python that includes the unit testing frameowrk pytest, the static code analysis tool called Pylint, and a unit test coverage tool called coverage.  You will also learn how to use python virtual environments to issolate your dependencies and how to use pip freeze to create a requirements.txt file that will lock your dependencies.  You should use this project as an opportunity to practice git branch, merge, and the stash management in the text tutorial below.

In this homework we are going to practice some GIT commands and setup a professional Python project with a virtual environment, pytest, and pylint.  Take a look at the VScode / WSL 2 video to see how to integrate VScode with the command line, so you can use a GUI to edit text files.  T

# Conceptual Readings

I want you to read the agile manifesto, 12 factor app, and the continuous integration articles as well as the case study on using automated tests at Google, so that you have some context for the professional application of the tools and ideas we are learning in this unit.  Without understanding the context of why we are learning to code like this, it will be difficult for you to apprecate the value of the skills we are learning.

*  [Authomated Testing at Google](https://itrevolution.com/articles/case-study-automated-testing-google/)
*  [This is the origins of Agile development and to understand Agile software development you need to understand and implement automated tests](https://agilemanifesto.org/principles.html)
*  [The 12 Factor App is a big picture overview of the best practices of maintining misson critical software.  Throughout the course we will be touching on various aspects of this as we develop our knoledge and skill as software engineers](https://12factor.net/)
*  [This is the original article that was written that explained continuous integration, which is the practice of constantly testing and deploying software, which is required to implement agile](https://martinfowler.com/articles/continuousIntegration.html)

# Tutorial References Created by Instructor
*  [GIT Stash](gitstash.md)

# Commands

* Adding a file to the stage: add .gitignore
* Performing a Commit: git commit -m "added git ignore with sw* files"
* Checking the status and whats on the commit stage: git status
*  Git command to take changes from a remote and update a local branch:  git pull --rebase origin main
# Python Setup Instructions
## Ubuntu
[Initial Python Setup Instructions for Virtual Environments on Ubuntu](https://www.arubacloud.com/tutorial/how-to-create-a-python-virtual-environment-on-ubuntu.aspx)
# Mac
[Install Brew Package Manager Mac - Used for Git and Python Install](https://brew.sh/)
[Pythonn Virtual Environments on Mac with Brew package manager for Mac - You need to install Brew](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
Once you have virtual environments installed on mac, everything will work the same as Ubuntu linux instructions that I'm providing for windows users running on Ubuntu using WSL2

# Python Readings
[Pip Freeze for Beginners](https://dev.to/eskabore/pip-freeze-requirementstxt-a-beginners-guide-5e2m#:~:text=Pip%20Freeze%20is%20a%20command,virtual%20environment%20on%20another%20machine.)
[Introduction to Pytest](https://realpython.com/pytest-python-testing/)
[Pylint Documentation](https://pylint.pycqa.org/en/v3.0.3/index.html)
[Pytest Documentation](https://docs.pytest.org/en/7.4.x/)

# Setup VSCode with WSL 2, so you can easily open the project with vscode instead of using the terminal vi editor
[Setting up WSL and VSCode](https://youtu.be/XY6lTlIW_hM)
