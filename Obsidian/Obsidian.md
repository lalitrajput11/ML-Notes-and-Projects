
---
### 1️⃣ Make sure Obsidian AppImage is executable (one-time)

`chmod +x ~/Tools/Obsidian-1.10.6.AppImage`

### 2️⃣ Open your project folder in Obsidian

From inside `ML-Notes-and-Projects` (or from anywhere):

`~/Tools/Obsidian-1.10.6.AppImage ~/Tools/ML-Notes-and-Projects

---
Changed the path already :-
### 3️⃣ (Optional but recommended) Create a shortcut command `obsidian`

So you don’t need the full path every time:

Fixing the path 

`sudo ln -s ~/Tools/Obsidian-1.10.6.AppImage /usr/local/bin/obsidian`

## sudo ln -s /home/lalitrajput/Tools/Obsidian-1.10.6.AppImage /usr/local/bin/obsidian

Now you can open the vault with:

`obsidian ~/Tools/ML-Notes-and-Projects`

''' '''

---

### 4️⃣ Open current directory in Obsidian

If you are already inside the folder:

`obsidian .`

---
## 🔹 What each part means

# sudo ln -s /home/lalitrajput/Tools/Obsidian-1.10.6.AppImage /usr/local/bin/obsidian


### 1️⃣ `sudo`

- Runs the command as **administrator (root)**
    
- Required because `/usr/local/bin` is a **system directory**
    
- Normal users cannot write there
    

👉 Think: _“I need system permission”_

---

### 2️⃣ `ln`

- Stands for **link**
    
- Creates a reference to another file
    

---

### 3️⃣ `-s`

- Means **symbolic link** (soft link)
    
- Similar to a **shortcut** in Windows
    
- Points to the original file, not a copy
    

---

### 4️⃣ `~/Tools/Obsidian-1.10.6.AppImage`

- The **real location** of Obsidian
    
- This file remains unchanged
    

---

### 5️⃣ `/usr/local/bin/obsidian`

- The **shortcut name**
    
- Placed in `/usr/local/bin`
    
- That directory is already in your `$PATH`
    

---

## 🔹 What actually happens?

After this command:

`obsidian`

Linux:

1. Searches `$PATH`
    
2. Finds `/usr/local/bin/obsidian`
    
3. That file points to:
    
    `~/Tools/Obsidian-1.10.6.AppImage`
    
4. Obsidian launches 🎉