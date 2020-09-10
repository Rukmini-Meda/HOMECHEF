# HOMECHEF
  This project is a part of Applied Software Engineering - 1 ( ASE ) Course at IIIT Sri City. The project provides a platform for home entrepreneurs who want to cook and earn. It also helps users in finding volunteers to help for an event.
  
#### You can find our project live [here](http://homechef30.pythonanywhere.com/)
#### If you find the project interesting and have ideas for the project or have found bugs in the project, feel free to raise an issue.
#### If you like the project, don't forget to give it a :star:


## Guidelines for development and contribution

    An issue must be created for any feature addition or bug fixation. It should be labelled accordingly. Developers working on a particular issue must create a branch and commit changes in that branch. Further, a pull request from that branch must be made to the master branch of this repository for merging. Following are the steps that have to be strictly followed for contributing to this project
    
#### 1. Fork the repository :fork_and_knife:
#### 2. Clone your fork to your local machine
```
git clone https://github.com/<your_username>/HOMECHEF.git
```
#### 3. Setup upstream remote
```
git remote add upstream https://github.com/Rukmini-Meda/HOMECHEF.git
```
#### 4. Verify remote - upstream URL should refer to this repository and origin should refer to your fork
```
git remote -v
```
#### 5. Keep fork and local repos up to date with the upstream

Checkout to master branch
```
git checkout master
```
Fetches from upstream and origin and prunes any deleted branches
```
git fetch --all --prune
```
Reset the head to the last commit in the upstream's master repo
```
git reset --hard upstream/master
```
Push these changes to origin so that both fork and local repos are made up to date
```
git push origin master
```
#### 6. Create a new branch

```
git checkout -b <new-branch-name>
```
#### 7. View all branches and verify newly created branch

```
git branch -v
```
#### 8. Code and make changes
#### 9. Add your changes accordingly
```
git add *
```
or
```
git add .
```
or
```
git add <file-or-folder-name>
```
#### 10. Commit your changes
```
git commit -m <commit-message>
```
#### 11. Push your changes to your fork
```
git push origin head
```
#### 12. Go to your fork in GITHUB and click on create a pull request to make a PR to master branch
#### 13. If any further changes are required, make them in the same branch and follow 9, 10, 11 steps


