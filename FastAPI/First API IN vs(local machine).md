# Not Deployed
1. Create a Folder and name it
2. open the vs inside that folder
3. Open the folder in terminal : then code . (Open vs)
4. New Terminal


---

python3 -m venv myenv (myenv has been set)
source/myenv/bin/activate
pip install fastapi uvicorn pydantic
cat << "EOF" > main.py
> from fastapi import FastAPI
> app = FastAPI()
> @app.get('/')
> def hello():
> 	return {"message" : "hello world"}
> @app.get("/about")
> def about():
> 	return {"message " : "this is a sample application !"}
EOF
cat main.py (To see the file )
uvicorn main:app --reload 

uvicorn run this process at a specific link.

ctrl+c : : to quit

---

