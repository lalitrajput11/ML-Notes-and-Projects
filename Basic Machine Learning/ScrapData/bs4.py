
'''import requests
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
'''

'''import requests

url = "https://www.ccbp.in/blog/articles/python-coding-questions"

response = requests.get(url)

# Save HTML in same folder
with open("python_questions.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("HTML saved successfully!")'''
#######################################################################################
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
    

