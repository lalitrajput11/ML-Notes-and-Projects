
 # Basic Commands
 **How Git Actually works**
 There are four locations :>
 1. LocalWorking Dir
 2. Staging area
 3. Local Repository 
 4. Remote repository
  Git Clone , Git checkout
  git add . , git commit , git push
git pull : fetches changes on remote repository : git fetch + git merge
Switching Merges , Resolve Merging Conflicts

Example : -
## Github

1. git init : empty git repository 'll be initialise ' 
2. git remote add  origin  https: (github repository link.git): connect this project to github repository
3. git status (what changes are there while creating project)
4. git add  . (take file to staging area)
5. git commit  -m "initial commit" 
6.  git push origin master >now , we ' ll push it to the master ' 
7. Git repository is ready

!![[Pasted image 20251209161202.png]]
 
   Git Merge | Git Rebase |Git Squash  
  | Feature                        | `git merge`                               | `git rebase`                          | `git squash` (actually `rebase -i`)   |
  | ------------------------------ | ----------------------------------------- | ------------------------------------- | ------------------------------------- 
   | History type                   | Creates a **merge commit** (non-linear)   | **Linear history** (rewrites history) | Linear + combines many commits into 1 |
  | Looks clean on GitHub?         | Noisy (extra merge commit)                | Very clean                            | Cleanest possible                     |
  | Safe if others already pulled? | 100% safe                                 | Dangerous (never on public branches)  | Dangerous (never on public branches)  |
  | When companies want it         | Rarely (only for release/hotfix branches) | Most startups & big tech prefer this  | Before PR → make 1 clean commit       |
  |                                |                                           |                                       |                                       |
  | Preserves exact commit dates?  | Yes                                       | No (changes dates)                    | No                                    |
![[Pasted image 20251209161945.png]]
1. Git Merge : git checkout main, git merge feature-branch
2. ![[Pasted image 20251209163033.png]]
3. git checkout feature-branch, git rebase main
4. ![[Pasted image 20251209163105.png]]
5. git squash : ![[Pasted image 20251209163202.png]]

### Core Concepts and Workflow

- When working on a feature branch derived from the main branch, both branches can evolve separately, creating diverging commit histories.
- Developers often face the choice of how to integrate changes from the main branch into the feature branch or vice versa, which can be tackled using **git merge**, **git rebase**, or **commit squashing**.

### Git Merge

- **Function**: Combines histories of two branches by creating a new **merge commit**.
- **Effect**: Preserves the entire commit history and branch evolution, showing exactly when branches joined.
- **Result**: The commit graph may become complex with many merge commits (“knots”).
- **Use Case**: Useful when a complete historical record of branch merges is desired.

### Git Rebase

- **Function**: Changes the base of the feature branch to the latest commit on the main branch, then reapplies feature commits on top.
- **Effect**: Creates a **clean, linear commit history** without merge commits.
- **Result**: History looks like a straight line, making it easier to follow.
- **Use Case**: Preferred when a tidy, straightforward history is important; often used to keep feature branches current with main.

### Squash Commits

- **Function**: Combines all commits from a feature branch into a **single commit** before merging into main.
- **Effect**: Maintains a linear history in the main branch while consolidating multiple commits into one.
- **Trade-off**: Loses granular commit details in the main branch but preserves detailed history on the feature branch.
- **Use Case**: Popular on platforms like GitHub for tidying up commit history, balancing cleanliness with some level of detail retention. 
### Core Concepts and Key Insights

- **Git vs Centralized Version Control:**
    
    - Centralized systems (e.g., older Team Foundation Server versions) rely on a single central server for code check-in/out, meaning developers do _not_ have full local copies.
    - If the central server crashes, history and code access are lost.
    - Git, as a **distributed version control system**, lets each developer clone the entire repository locally, enabling offline work and eliminating risk from server downtime.
    - Distributed model supports **scalability** and collaboration across global teams without dependency on server availability.
- **Common Git Commands:**
    
    - `git clone`: Downloads a repository from a remote source (e.g., GitHub) to the local machine.
    - `git push origin master`: Pushes local commits to the remote repository’s master branch.
    - `git remote add origin <url>`: Links a local repository to a remote repository.
    - `git mv`: Command used to rename or move files within the repository.
    - `git commit -m "<message>"`: Creates a commit with a descriptive message.
    - `git revert <commit-id>`: Creates a new commit that undoes changes from a previous commit.
- **Repository Initialization:**
    
    - `git init`: Initializes a standard Git repository with a working directory containing checked-out files.
    - `git init --bare`: Creates a **bare repository** without working files, often used as a centralized remote repository; stores revision history at the root level.
- **Fetching vs Pulling:**
    
    - `git fetch`: Downloads new data from the remote repository but _does not_ merge it into local working files.
    - `git pull`: Fetches new data and **merges** it into the current branch, updating local files.
- **Git Stash:**
    
    - Allows temporarily saving changes without committing them, useful when switching contexts or branches without interrupting the mainline branch.
- **Branching and Merging:**
    
    - Branches allow parallel development of features separate from the mainline (master) branch.
    - `git merge`: Combines changes from one branch into another, preserving history.
    - `git rebase`: Rewrites project history by moving or combining commits, useful for creating a linear history or restarting a project branch.
- **Viewing Commit Changes:**
    
    - `git diff --tree -r <commit-hash>`: Lists files changed in a particular commit.

---
### Summary Table of Git Commands Mentioned

|Command|Purpose|
|---|---|
|`git clone <repo-url>`|Download repository to local machine|
|`git remote add origin <url>`|Link local repo to remote|
|`git push origin master`|Push local changes to remote master branch|
|`git init`|Initialize standard repository with working directory|
|`git init --bare`|Initialize bare repository without working files|
|`git mv <old> <new>`|Rename or move a file|
|`git commit -m "<message>"`|Commit changes with message|
|`git revert <commit-id>`|Undo changes from a previous commit|
|`git fetch`|Download new remote data without merging|
|`git pull`|Download and merge remote data into current branch|
|`git stash`|Temporarily save changes without committing|
|`git diff --tree -r <commit>`|List files changed in a commit|
![[Pasted image 20251209164220.png]]
### Handling Merge Conflicts

- **Merge Conflict Definition:**
    
    - Occurs when two or more branches have conflicting changes to the same files that cannot be automatically merged.
    - Requires manual resolution to decide which changes to keep.
- **Resolving Merge Conflicts via GitHub:**
    
    - Identify pull requests with conflicts.
    - Open conflicted files to see conflict markers.
    - Manually edit files to select desired changes.
    - Mark files as resolved.
    - Commit the merge to finalize.
- **Resolving Merge Conflicts via Command Line:**
    
    - Use Git Bash to navigate to the repository.
    - Identify conflicted files using Git status or conflict markers.
    - Edit files manually in a text editor.
    - Remove conflict markers after resolving.
    - Commit the merged changes and push to remote.

### Key Concepts and Definitions

- **Git:** A free, open-source distributed version control system that tracks code changes, allows merging code, and maintains revision history.
- **Version Control System (VCS):** Software tools that help teams collaborate by managing changes to files over time, ensuring everyone works on the latest version, and enabling rollback to previous states.
- **Distributed Version Control:** Git stores full repositories locally on each developer’s machine, unlike centralized systems where code exists only on a server.
- **GitHub vs Git:** Git is a local tool for version control; GitHub is a cloud-based hosting service for Git repositories.

---

### Important Git Concepts and Commands

|Concept/Command|Description|
|---|---|
|`git init`|Initializes a new local Git repository.|
|States of a file|**Modified, Staged, Committed** - three major file states in Git workflow.|
|Staging area|Intermediate area where changes are formatted and reviewed before a commit.|
|`git add`|Adds files to the staging area.|
|`git commit -m`|Commits staged changes with a message.|
|`git pull origin master`|Fetches changes from the remote master branch and merges them into the local branch.|
|`git push`|Pushes local commits to the remote repository.|
|`git fetch`|Downloads new commits from a remote branch but does not merge them automatically.|
|`git merge`|Integrates changes from one branch into another, preserving commit history.|
|`git rebase`|Reapplies commits from one branch on top of another, rewriting commit history.|
|`git clone`|Creates a local copy of a remote repository for offline editing.|
|`git stash`|Temporarily saves uncommitted changes to a stack to enable switching branches without committing.|
|`git reset --mixed`|Unstages changes from the staging area but keeps them in the working directory.|
|`git merge --abort`|Stops an ongoing merge and reverts to the pre-merge state.|
|`git clean`|Removes untracked files from the working directory.|
|`git commit --amend`|Fixes or modifies the last commit message or content.|
|`git revert`|Creates a new commit that undoes the changes of a previous commit, useful for public commits.|

### Additional Clarifications

- **Difference Between Fork, Branch, and Clone:**
    
    - _Fork:_ A copy of a repository allowing experimentation without affecting the original project, often used for proposing changes.
    - _Clone:_ Creates a local copy of a repository.
    - _Branch:_ Separate lines of development within the same repository allowing parallel work on different features.
- **Resolving Conflicts:**
    
    - Occurs when two branches edit the same lines or files differently.
    - Requires manual intervention: identify conflicted files, modify to resolve, add changes, and commit.
- **Advantages of Git:**
    
    - Distributed development and team collaboration.
    - Tracks every change, allowing quick reversion.
    - Free and open source.
    - Sophisticated branching and merging.
    - Supports efficient workflows and CI/CD pipeline integration.
    - Accelerates release cycles and improves project management.