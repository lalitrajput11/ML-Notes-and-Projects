# 2025-12-09 - Daily ML Study

**Goal today**: Finish Python revision + 1 project
**YouTube watched**
- [x] ## Deploy ML Projects for Free | Render Deployment Tutorial | ML Deployment + https://www.youtube.com/watch?v=WuEGXlokpuQ


**Key points / formulas**


#Deplyment #Render #Github

## Deploy ML Projects for Free | Render Deployment Tutorial | ML Deployment | CampusX

*link 
https://www.youtube.com/watch?v=WuEGXlokpuQ

**Workflow**
1. Train a Ml model
2. Export pickle file
3. create folder /venv/gitignore/paste model > create flask app -> install libs
4. run locally
5. create github repo
6. push code
7. Deploy to render

**Practical**
1. Make a new folder render-demo
2.  open that folder with vs
3. existing file : Dataset , Ml_model .py file, model.pkl
4. new terminal : -m venv myenv (For virtual environment)
5. activate the venv : myenv\Scripts\activate
6. (myenv) : Got triggered
7. create a new file : .gitignore (those environment , we dont want to push at github) > myenve (Folder put it inside here)
8. model.pkl , copy in this folder from the existing
9. New file : app.py (for the flask integration), we ll load the model in this, will show the page at our  website url . as website.index (index.html)
10. lets create flask folder : with name templates : inside it , create file : index.html
11. body : button : predict : 
12. inside (myenv) : pip install libraries ,the same : we are using it in our model. (inside the virtual environment , it ll set all the dependencies )
13. Create  requirement.txt : for the render : that server need to install all the libraries for that particular project : for this : 
14. pip freeze  > requirement.txt : all the name will be shown in this file with library name and version number
15. run locally 
16. python app.py
17. an url ll be come out. (Application : with user interface)
18. Create Github repo : render-demo
19. new terminal : 
## Github

1. git init : empty git repository 'll be initialise ' 
2. git remote add  origin  https: (github repository link.git): connect this project to github repository
3. git status (what changes are there while creating project)
4. git add  . (take file to staging area)
5. git commit  -m "initial commit" 
6.  git push origin master >now , we ' ll push it to the master ' 
7. Git repository is ready

## Render Deployment 
1. profile creation , linking github
2. click web services
3. install
4. connect
5. url of the service 'll be provided' : Deployed
 





