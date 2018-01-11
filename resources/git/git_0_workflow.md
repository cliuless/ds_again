# Git Workflow

## Table of Contents
[Part 1:  Sync repos (do this first thing in the morning)](#section-a)  
[Part 2:  Launch Jupyter notebook from working branch.  ](#section-b)  
[Part 3:  Your working branch](#section-c)  
[Part 4:  Add & Commit File in working branch](#section-d)  
[Part 5:  Submit pull request from `master` branch](#section-e)  
 

## <a name="section-a"></a>Part 1:  Sync repos (do this first thing in the morning)

#### Step 1:  Make sure you are in your repo and in the `master` branch
```bash
pwd
```
>```bash
pwd
/Users/julialintern/winter/fork/nyc18_ds14
```  

```bash
git branch
```  

>```bash
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

## <a name="section-b"></a>Part 2:  Launch Jupyter notebok from working branch.  (Mine is `notes`)

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

## <a name="section-c"></a>Part 3:  Your working branch

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

## <a name="section-d"></a>Part 4:  Add & Commit File in working branch


```bash
git status 
```
```bash
git add mta_challenge.ipynb
git commit -m 'add my 2nd practice submission'
```

```bash
git log
```

```bash
git push origin submission0
```
---

## <a name="section-e"></a>Part 5:  Submit pull request from `submission0` branch


Now it's time to merge our changes with the official Metis repo. To do this, we use a pull request from our submission0 branch into the master branch of development.

1. Go to our fork and click the button 'New Pull Request'. It's next to the 'Branch: master' button and on the same section where the 'Clone and Download' button is.  
![](img/click_pull_req.png)

2. Click the branch to the right, and click the branch you want to merge (sorry, it was meant to be submission0!):  
![](img/pr_click_sub1.png)

3. Click create pull request:  
 ![](img/create_pr.png)

4. Type in a title for the pull request, and click 'Create Pull Request':
 ![](img/submit_pr.png)
 
5. If you go into the Metis repo, under the Pull Requests section, you'll now see your pull request there!
 ![](img/prs.png)
 
Great, so now we've pulled our submission0 branch into the master branch of development on the Metis repo. But that means now all the other changes the other students are making to the main thread of development aren't reflected in either our fork or our local clone. Let's sync up.


