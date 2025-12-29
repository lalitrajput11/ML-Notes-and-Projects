
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.ccbp.in/blog/articles/python-coding-questions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

questions = []

for tag in soup.find_all(text=True):
    text = tag.strip()
    if re.match(r'^\d+[\.\)\-:]', text):
        questions.append(text)

for q in questions:
    print(q)

---
import requests
import os
from bs4 import BeautifulSoup
import re

url = "https://www.ccbp.in/blog/articles/python-coding-questions"

save_path = "/home/lalitrajput/Tools/ML-Notes-and-Projects/Python/Python DSA/python_questions.html"

response = requests.get(url)
# Make sure folder exists (safety check)

os.makedirs(os.path.dirname(save_path), exist_ok=True)

with open(save_path, "w", encoding="utf-8") as file:
file.write(response.text)

print("HTML saved at:", save_path)

with open("/home/lalitrajput/Tools/ML-Notes-and-Projects/Python/Python DSA/python_questions.html", "r", encoding="utf-8") as file:

html = file.read()

soup = BeautifulSoup(html, "html.parser")
for h3 in soup.find_all("h3"):
question = h3.get_text().strip()
if re.match(r'^\d+\.', question):
print(question)

---
# Different Approach to target : The list of Questions: -
## APPROACH 2: CSS SELECTOR (PRO STYLE)

Same logic, cleaner syntax.

`for h3 in soup.select("h3"):     
text = h3.text.strip()     
if text[0].isdigit():         
	print(text)`

✔ Uses CSS selectors  
✔ Easier to maintain  
✔ Preferred in real projects

---

## APPROACH 3: CONTENT-AWARE (IGNORE HEADER/FOOTER)

Sometimes pages have `<h3>` everywhere.  
So we **limit search to article body**.

### Logic:

> First find main content container, then search inside it.

Example (class name may vary slightly):

`article = soup.find("div", class_="rich-text")  for h3 in article.find_all("h3"):     text = h3.get_text(strip=True)     if text.split(".")[0].isdigit():         print(text)`

✔ Very precise  
✔ Avoids ads/navbars  
✔ Best for large sites

---
# ✅ METHOD 1 (BEST & CLEANEST) — _Check → Create_

`import os  
folder_path = "/home/lalitrajput/Tools/ML-Notes-and-Projects/Python/Python DSA"  
if not os.path.exists(folder_path):     
	os.makedirs(folder_path)    
	 print("Folder did not exist. Created new folder.") 
else:    
	print("Folder already exists.")`

# ✅ METHOD 2 (TRY–EXCEPT) — _True Error Handling_

Use this when:

- Folder creation may fail (permissions, disk, etc.)
- You want **controlled error handling**

`import os  
folder_path = "/home/lalitrajput/Tools/ML-Notes-and-Projects/Python/Python DSA"  
try:     
	os.makedirs(folder_path)     
	print("Folder created successfully.") 
except FileExistsError:     
	print("Folder already exists.") 
except PermissionError:    
	print("Permission denied. Cannot create folder.")
except Exception as e:     
	print("Unexpected error:", e)`

✔ Handles real OS errors  
✔ Production-ready  

---
