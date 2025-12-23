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