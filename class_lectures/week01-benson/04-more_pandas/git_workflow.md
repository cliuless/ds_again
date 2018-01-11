# Git Workflow

## Table of Contents

[Part 0:  Update PS1 file to reflect branch location!](#section-a)  
[Part 1:  Sync repos (do this first thing in the morning)](#section-b)  
[Part 2:  Launch Jupyter notebook from working branch.  ](#section-c)  
[Part 3:  Your working branch](#section-d)  
[Part 4:  Add & Commit File in working branch](#section-e)  
[Part 5:  Submit pull request from `submission` branch](#section-f)  
 
## <a name="section-a"></a>Part 0:  Update PS1 file to reflect branch location!
#### Add the following lines to your ~/.bash_profile
Of course, we'll only have to do this once!

```bash
cd 
nano .bash_profile
```

```
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
```

## <a name="section-b"></a>Part 1:  Sync repos (do this first thing in the morning)
#### Step 1:  Make sure you are in your repo and in the `master` branch

```bash
pwd
/Users/julialintern/winter/fork/nyc18_ds14
```  

```bash
git branch
```  

```bash
 Benson
* master
  notes
  submission0
```
  
#### Step 2a:  sync `thisismetis/nyc18_ds14` with your local copy (remote `upstream` and branch `master`)
```bash
git pull upstream master
```

#### Step 2b:  sync your remote `origin` & branch `master` with your forked repo `julialintern/nyc18_ds14`
```bash
git push origin master
```

#### Step 3:  switch to working branch.  Mine is `notes`
```bash
git checkout notes
```
```bash
  Benson
  master
* notes
  submission0
```
#### Step 4a:   sync `thisismetis/nyc18_ds14` with your remote `upstream` and branch `notes`
```bash
git pull upstream master
```
#### Step 4b:  sync your remote `origin` & branch `notes` with your forked repo `julialintern/nyc18_ds14`
```bash
git push origin notes
```

Viola!  Everything will be synced up now, and it's a good place to begin the day.  :sunny:

---

## <a name="section-c"></a>Part 2:  Launch Jupyter notebok from working branch.  (Mine is `notes`)

#### Step 1:  Check which branch you are in  
```bash
git branch
``` 

#### Step 2:  Switch to working branch 
```bash
git checkout notes
```


#### Step 3:  Launch Jupyter Notebook
```bash
▶ jupyter notebook
```

---

## <a name="section-d"></a>Part 3:  Your working branch

### Note:  this is where you will do any work, in the working branch.  For me, it is `notes`**  

### Classwork
 * If you're going to edit a Jupyter notebook in `class_lectures`, make a copy and rename it.  Can add your name to end of notebook.  
   * Example:  `Intro-to-Pandas.ipynb` --- > `intro_to_pandas_copy.ipynb`
   
* Let's add some changes and save 

```bash
git status
```
*  We dont see changes!  Again, if we rename our file to something with 'copy' changes won't be staged. 
This allows us to edit a file, but git will ignore this ( & file will not be reflected in git status output)

* Note: you might want to push your 'copy'.ipynb version to your origin.  However, (unfortunately, it will appear in 
your next pull request submission!) 

* If you really want a remote copy of your *copy.ipynb* file, it would be best to create your own, separate repository for those files. 

** Before you move off of your branch check *status* ! **   Commit any files you don't want to take with you to master; or remove them. 


### Challenges

 
#### Step 1:  Navigate to working directory
```bash
git checkout submission0
pwd
/Users/julialintern/winter/fork/nyc18_ds14/student_submissions/challenges/00_practice/lintern_julia         
```

#### Step 2:  Create a notebook (in working branch)
 * launch Jupyter Notebook
 * Example:  `mta_challenge.ipynb`
 * Work in this file

When challenge set is ready for submission, go to next step

---

## <a name="section-e"></a>Part 4:  Add & Commit File in working branch


```bash
git status 
```
```bash
git add mta_challenge.ipynb
git status
git commit -m 'add my 2nd practice submission'
```

```bash
git log
```

```bash
git push origin submission0
```
---

## <a name="section-f"></a>Part 5:  Submit pull request from `submission0` branch


Now it's time to merge our changes with the official Metis repo. To do this, we use a pull request from our submission0 branch into the master branch of development.

1. Navigate to your remote origin github repo.
2. Choose the branch you want to generate a pull request from ('Ex: Submission0')
3. Click on 'New Pull Request'
