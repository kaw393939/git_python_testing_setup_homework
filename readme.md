# Enhanced Homework 2 Instructions

## Overview

Welcome to Homework 2! In this unit, our goal is to establish a professional development setup for Python. This will include familiarizing yourselves with several key tools and practices that are integral to modern software development. Specifically, you'll set up:

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

## Conceptual Readings

Understanding the broader context of these tools and methodologies is crucial. Please read the following materials to gain insights into their professional application:

1. **Automated Testing at Google**: A case study on the importance of automated testing in software development. [Read here](https://itrevolution.com/articles/case-study-automated-testing-google/).
2. **Agile Manifesto**: The foundation of Agile software development, highlighting the role of automated testing. [Read here](https://agilemanifesto.org/principles.html).
3. **The 12 Factor App**: A guide to best practices in maintaining mission-critical software, relevant to our course. [Read here](https://12factor.net/).
4. **Continuous Integration**: An article explaining the practice of continuous testing and deployment, essential for Agile implementation. [Read here](https://martinfowler.com/articles/continuousIntegration.html).

## Tutorial References Created by Instructor

- [GIT Tutorial Guide](gitguide.md)
- [GIT Stash Management](gitstash.md)
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

- Initial Python Setup for Virtual Environments: [Ubuntu Guide](https://www.arubacloud.com/tutorial/how-to-create-a-python-virtual-environment-on-ubuntu.aspx)

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
