# Comprehensive GIT Command Line Tutorial for Managing a Development Environment

## Introduction

This tutorial aims to provide a thorough understanding of using Git from the command line. Git is a powerful version control system that helps developers manage and track changes in their code over time. We'll cover various essential commands, focusing on undoing commits, managing stashes, handling remotes, and other vital Git functionalities.

### Basic Setup

Before diving into advanced topics, ensure you have Git installed on your system and have configured your username and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Managing Commits

### Undoing Commits

1. **Undoing the Last Commit**: To undo the most recent commit, keeping the changes in the working directory:

   ```bash
   git reset --soft HEAD~1
   ```

2. **Discarding the Last Commit**: To discard the last commit and all changes:

   ```bash
   git reset --hard HEAD~1
   ```

3. **Amending a Commit**: If you need to modify the last commit (e.g., correct a typo), you can do:

   ```bash
   git commit --amend
   ```

   This opens an editor where you can edit the commit message. If you've made any additional changes to the files, you can add them before running this command.

## Managing Stashes

Stashing is useful when you need to switch branches without committing the current working state.

1. **Creating a Stash**:

   ```bash
   git stash
   ```

2. **Listing Stashes**:

   ```bash
   git stash list
   ```

3. **Applying a Stash**:

   - To apply the most recent stash and keep it in the stash list:

     ```bash
     git stash apply
     ```

   - To apply a specific stash (e.g., stash@{1}):

     ```bash
     git stash apply stash@{1}
     ```

   - To apply the most recent stash and remove it from the stash list:

     ```bash
     git stash pop
     ```

4. **Deleting a Stash**:

   - To delete a specific stash (e.g., stash@{1}):

     ```bash
     git stash drop stash@{1}
     ```

   - To clear all stashes:

     ```bash
     git stash clear
     ```

## Managing Remotes

Remotes are versions of your project that are hosted on the internet or network.

1. **Viewing Remotes**: List the remote connections you have to other repositories.

   ```bash
   git remote -v
   ```

2. **Adding a Remote Repository**:

   ```bash
   git remote add [remote-name] [remote-url]
   ```

3. **Fetching from a Remote**: Fetch branches and their respective commits from the remote repository.

   ```bash
   git fetch [remote-name]
   ```

4. **Pushing to a Remote**: Push your branch to a remote repository.

   ```bash
   git push [remote-name] [branch-name]
   ```

5. **Pulling from a Remote**: Fetch and integrate changes from the remote server to your working directory.

   ```bash
   git pull [remote-name] [branch-name]
   ```

6. **Removing a Remote**:

   ```bash
   git remote remove [remote-name]
   ```

## Other Essential Commands

1. **Checking Status**:

   ```bash
   git status
   ```

2. **Viewing Commit History**:

   ```bash
   git log
   ```

3. **Creating a Branch**:

   ```bash
   git branch [branch-name]
   ```

4. **Switching Branches**:

   ```bash
   git checkout [branch-name]
   ```

5. **Merging Branches**:

   ```bash
   git merge [branch-name]
   ```

6. **Deleting a Branch**:

   ```bash
   git branch -d [branch-name]
   ```

7. **Handling Merge Conflicts**: Use a text editor to manually resolve conflicts, then:

   ```bash
   git add [file-name]
   git commit -m "Resolved merge conflict"
   ```

## Conclusion

Git is a cornerstone tool for any developer. Understanding and efficiently using Git commands can significantly improve your development workflow. Remember, practice is key to mastering Git, so don't hesitate to experiment with these commands
