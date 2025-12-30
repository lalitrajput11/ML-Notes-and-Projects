### **1️⃣ Check if Ollama is installed**

Open your terminal and run:

`which ollama`

### **2️⃣ Check Ollama version**

To confirm it’s installed and working:

`ollama --version`

### **3️⃣ Check if Ollama server is running**

Ollama usually runs a local server to serve models. Check with:

`ps aux | grep ollama`

### **4️⃣ Stop Ollama**

If it’s running, you can stop it using the **process ID (PID)** from the previous command:

`kill <PID>`

Or forcefully:

`kill -9 <PID>`


=======================================================================

### **1️⃣ Check if Ollama is running**

In your terminal, run:

`ps aux | grep ollama`

### **2️⃣ Stop Ollama**

Use the PID you found:

`kill 12345`

If it doesn’t stop, force it:

`kill -9 12345`

**ps aux | grep ollama**
when running

# Stop anytime with:

`pkill ollama`

# 🔁 (Recommended) Run Ollama in background

So your terminal stays free:

`ollama serve & disown`

Now check:

`ps aux | grep ollama`

---

## 🛑 Stop Ollama anytime (clean)

`pkill ollama`

or

`ps aux | grep ollama kill <PID>`