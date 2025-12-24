# 1️⃣ What is n8n (1 line)

**n8n** is a **workflow automation tool** (like Zapier) that runs as a **web app**.

👉 When running in Docker:
- Docker runs n8n
- Browser shows the UI
---

# 2️⃣ Pull n8n Image (Download Once)

Run this in terminal:

`docker pull n8nio/n8n`

✔ This downloads the official n8n image  
✔ You only need to do this once

Check:

`docker images`

You should see:

`n8nio/n8n`

---

# 3️⃣ Run n8n Container (Browser Mode)

### 🔥 SIMPLEST WAY (Recommended for learning)

`docker run -it --rm \   -p 5678:5678 \   n8nio/n8n`

Explanation:

- `-p 5678:5678` → expose n8n to browser
    
- `--rm` → auto-remove container when stopped
    
- `-it` → interactive logs
---

# 4️⃣ Open n8n in Browser 🌐

Open your browser and go to:

`http://localhost:5678`

🎉 You will see **n8n workflow editor UI**

This **IS the desktop view**.

---

# 5️⃣ Run n8n in Background (Production-Style)

If you don’t want terminal to stay busy:

`docker run -d \   --name n8n \   -p 5678:5678 \   n8nio/n8n`

Now:

- n8n runs in background
    
- Terminal is free

Check:

`docker ps`

---

# 6️⃣ Stop / Restart n8n

### Stop

`docker stop n8n`

### Start again

`docker start n8n`

Open browser again:

`http://localhost:5678`

---

# 7️⃣ (IMPORTANT) Save n8n Data (Persistence)

Without this, workflows are lost when container stops.

### ✅ Correct Way (Use Volume)

`docker volume create n8n_data`

`docker run -d \   --name n8n \   -p 5678:5678 \   -v n8n_data:/home/node/.n8n \   n8nio/n8n`

docker volume create n8n_data 
docker run -it --rm \
--name n8n \
-p 5678:5678 \ 
-e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
-e TZ="<YOUR_TIMEZONE>" \ 
-e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
-e N8N_RUNNERS_ENABLED=true \ 
-v n8n_data:/home/node/.n8n \ docker.n8n.io/n8nio/n8n
✔ Workflows saved  
✔ Credentials saved

---

# 8️⃣ Verify Everything is Working

`docker logs n8n`

You should see:

`Editor is now accessible via: http://localhost:5678`

---

# 9️⃣ Common Problems & Fixes ❌➡️✅

### ❌ Port already in use

`-p 5679:5678`

Then open:

`http://localhost:5679`

---

### ❌ Permission error

Run Docker without sudo:

`sudo usermod -aG docker $USER newgrp docker`

---
---

---
lalitrajput@lalitrajput-dy5:~$ docker run -d \
  --name n8n \
  -p 5678:5678 \
  -u $(id -u):$(id -g) \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
#################################################

lalitrajput@lalitrajput-dy5:~$ docker ps

CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                                       NAMES
e9b9e4f1f4ff   n8nio/n8n   "tini -- /docker-ent…"   15 seconds ago   Up 15 seconds   0.0.0.0:5678->5678/tcp, :::5678->5678/tcp   n8n

lalitrajput@lalitrajput-dy5:~$ docker stop n8n
n8n

lalitrajput@lalitrajput-dy5:~$ docker logs
"docker logs" requires exactly 1 argument.
See 'docker logs --help'.

Usage:  docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

lalitrajput@lalitrajput-dy5:~$ docker images

REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
n8nio/n8n                latest    4f582dbbf7ea   11 hours ago    1.08GB
kalilinux/kali-rolling   latest    7b1df727593e   3 months ago    123MB
mysql                    latest    5cde95de907d   17 months ago   586MB
sundowndev/phoneinfoga   latest    1110da5cef10   22 months ago   43MB

lalitrajput@lalitrajput-dy5:~$ docker ps

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
l

---
Great 👍 n8n is **running correctly now**.

You currently started it in **interactive mode**, so stopping and using it later is easy. Here are the **right ways**, depending on what you want.

---

## 🛑 Stop n8n (Right Now)

Since your terminal is attached:

### 👉 Just press:

```
Ctrl + C
```

This will:

- Stop the n8n process
    
- Stop the Docker container
    
- Because you used `--rm`, the container is **removed automatically**
    
- ✅ Your data is **SAFE** in `~/.n8n`
    

---

## ▶️ Start n8n Again Later (Same Setup)

When you want to use it again, just run:

```bash
docker run -it --rm \
  -p 5678:5678 \
  -u $(id -u):$(id -g) \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

Then open:

```
http://localhost:5678
```

---

## ⭐ Better Way (Recommended): Run in Background

So you don’t need to keep the terminal open.

### 🔹 Start n8n in background

```bash
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -u $(id -u):$(id -g) \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

---
# Only to this now
### 🔹 Stop it later

```bash
docker stop n8n
```

### 🔹 Start it again

```bash
docker start n8n
```

### 🔹 View logs anytime

```bash
docker logs n8n
```

---

## 🧠 What’s the Difference?

|Mode|Command|When to use|
|---|---|---|
|Interactive|`-it --rm`|Learning / testing|
|Background|`-d --name n8n`|Daily / long-term use ✅|

---

## ✅ Recommended for You

Since you’re into **automation, MySQL, APIs, AI workflows**:

👉 **Use background mode**  
It behaves like a real service.

---

If you want next:

- 🔐 Enable username/password login
    
- 🔁 Auto-start n8n on boot
    
- 🐳 Docker Compose (best practice)
    
- 🔗 MySQL / GitHub / Telegram workflows
    

Just tell me 👍