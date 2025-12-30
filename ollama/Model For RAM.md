
# 🧠 Best Ollama Models for **CPU-Only (Low RAM friendly)**

### **RECOMMENDED**

Use these **only** on CPU:

|Model|Why|
|---|---|
|`phi3:mini`|🔥 Fastest, very low RAM|
|`llama3.2:1b`|Balanced + stable|
|`qwen2.5:1.5b`|Good reasoning, lightweight|
|`gemma:2b`|Clean output, efficient|
|`mistral:7b-instruct-q4`|Best quality (slower but usable)|
**StartWith**
ollama pull phi3:mini
## ❌ What NOT to use on CPU

Avoid these unless you have a GPU:

- `llama3:8b`, `llama3:70b`
- `mixtral`, `deepseek-r1`
- Any model **>7B** or **non-quantized**
- Vision models (`llava`, `bakllava`)
- Flash-attention models

---

## 🧪 Quick health check

`which ollama`
Expected:
`/home/lalitrajput/bin/ollama`

`ollama --version`

`curl http://localhost:11434`

---

# ⚡ Speed & Low-RAM Optimization (IMPORTANT)

### 1️⃣ Limit model size (critical)

Use **quantized models only**:

`ollama pull mistral:7b-instruct-q4`

### 2️⃣ Reduce context size

Run with smaller context:

`OLLAMA_CONTEXT_LENGTH=2048 ollama serve`

### 3️⃣ Keep only **one model loaded**

(Default is fine, but ensure this)

`export OLLAMA_MAX_LOADED_MODELS=1`

Add to `~/.bashrc` if needed.

===========================================================================
# Journey : By CLI

![[Pasted image 20251230181631.png]] 

1.  **ps aux | grep ollama**

lalitra+   36273  0.0  0.1 1858012 29824 pts/0   Sl   17:23   0:00 ollama serve
lalitra+   36309  0.0  0.0   9080  2432 pts/1    S+   17:23   0:00 grep --color=auto ollama

2. **curl http://localhost:11434**

### We can pull here :-
#### Dont forget to run only 1  and do the Ram Optimization
## 2️⃣ Model Setup (INSTALL ONLY THESE)

### 🔥 Phase 1 — Starter (FAST)

`ollama pull phi3:mini`

Use for:
- Learning prompts
- Testing APIs
- Automation logic
- Small summaries
### 🧠 Phase 2 — Quality (Balanced)

`ollama pull qwen2.5:1.5b`

Use for:
- Resume parsing
- Structured extraction
- Business text
### 🎯 Phase 3 — Best CPU Quality

`ollama pull mistral:7b-instruct-q4`

Use for:
- Final outputs
- Reports
- Reasoning tasks

=======================================

ollama serve  
or 
ollama serve & disown (So your terminal stays free:)

Now check:
`ps aux | grep ollama`

ollama list
ollama run phi3:mini
ollama stop   # or pkill ollama

=============================

---
# 🧠 WHAT I did WITH `phi3:mini` (REALISTIC & USEFUL)

Below are **clear tasks**, **how to run them**, and **expected results**.
![[Pasted image 20251230183547.png]]
## 1️⃣ Simple Q&A (Sanity Check)

### Command
`ollama run phi3:mini "What is REST API?"`

### Expected Result
- 1–2 clear sentences
- Fast response (<3 seconds)
## 2️⃣ Text Summarization

### Command
`ollama run phi3:mini "Summarize: REST APIs allow systems to communicate over HTTP using JSON."`

### Expected Result
- Short summary
- No hallucinations
## 3️⃣ Keyword / Skill Extraction (VERY IMPORTANT)

### Command
`ollama run phi3:mini "Extract skills as a JSON array from: Python, SQL, Machine Learning, Docker"`

### Expected Result
`{   "skills": ["Python", "SQL", "Machine Learning", "Docker"] }`

## 4️⃣ Resume Parsing (CORE USE CASE)

### Command
`ollama run phi3:mini " Extract structured JSON with name, email, skills from: John Doe Email: john@example.com Skills: Python, SQL, NLP "`
## 5️⃣ Classification (YES / NO, LABELS)

### Command
`ollama run phi3:mini " Classify the text as Technical or Non-Technical: 'I worked as a Python developer building APIs' "`

## 6️⃣ Data Cleaning / Normalization

### Command
`ollama run phi3:mini " Normalize these skills to standard names: py, python3, SQL database, ml "`
### Expected Result
`{   "normalized_skills": ["Python", "SQL", "Machine Learning"] }`

## 7️⃣ Rule-Based Scoring (LIGHT)

### Command
`ollama run phi3:mini " Score this resume out of 10 for Python developer: Skills: Python, SQL Experience: 2 years "`
### Expected Result
`{   "score": 7,   "reason": "Strong Python skills but limited experience" }`

## 8️⃣ Prompt → JSON (Automation-Ready)

### Command
`ollama run phi3:mini " Return ONLY JSON. Extract: - skills - years_experience Text: Python developer with 3 years experience "`
### Expected Result
`{   "skills": ["Python"],   "years_experience": 3 }`

## 9️⃣ REST API Usage (Same Tasks, Programmatic)

### Command
`curl -X POST http://localhost:11434/api/generate \   -H "Content-Type: application/json" \   -d '{     "model": "phi3:mini",     "prompt": "Extract skills as JSON from: Python, SQL, NLP",     "temperature": 0.2,     "num_predict": 100,     "stream": false   }'`

### Expected Result
- JSON response with `"response"` containing extracted skills

---

# Explanation of Ollama + LLM architecture, how offline usage works, and how the files are stored and managed :-

---

## **1. Diagram: Ollama + LLM Architecture + Offline Usage**

```
                 +------------------+
                 |  Your System     |
                 | (CPU only,lessGB)|
                 +--------+---------+
                          |
                          | 1. Install Ollama
                          v
                 +------------------+
                 |   Ollama CLI /   |
                 |   Local Server   |
                 +--------+---------+
                          |
           ------------------------------
           |                            |
           v                            v
  +------------------+          +------------------+
  |  Download Model  |          | Serve LLM Locally|
  |  (e.g., Mistral) |--------->|  Inference       |
  +------------------+          +------------------+
           |
           | Stored locally in:
           | ~/.ollama/models/<model_name>/
           |
           v
  +------------------+
  | LLM Model Files  |
  | - Config files   |
  | - Weights (.bin) |
  | - Tokenizer data |
  +------------------+
           |
           v
  +------------------+
  |  Offline AI Tasks|
  |  - Text Generation|
  |  - Summarization |
  |  - Semantic Search|
  |  - Chat / Q&A    |
  +------------------+
```

---

### **2. Explanation of Diagram**

1. **Your System**
    
    - Limited CPU & RAM (3 GB). You can run **tiny models only**.
    
2. **Ollama**
    
    - Installs as a **CLI + local server**.
    - Manages **model downloads** and queries.
    - Acts as an interface between your apps and the LLM.
        
3. **Model Download & Storage**
    
    - Models like **Mistral or LLaMA** are downloaded.
    - Stored locally in your home directory:
        ```
        ~/.ollama/models/<model_name>/
        ```
        
    - Files inside a model folder:
        
        - `config.json` → Model configuration
        - `pytorch_model.bin` → Weights of the model
        - `tokenizer.json` → Tokenizer for splitting text into tokens

1. **Local Serving / Inference**
    
    - Ollama runs the model **locally**.
    - You can query it for tasks **offline**.
    
2. **Offline AI Tasks**
    
    - Generate text
    - Summarize documents
    - Semantic search in your local files
    - Build a local chatbot

---

### **3. Steps to Install and Use Ollama Offline**

1. **Install Ollama**
    
    ```bash
    curl https://ollama.com/install.sh | bash
    ```
        
    or download the installer from Ollama’s official site.
    
1. **Check Installation**
    ```bash
    ollama --version
    ```
    
2. **Download a Model**
    
    ```bash
    ollama pull mistral
    ```
    - This downloads the model to: `~/.ollama/models/mistral/`
    - Files include `config.json`, `pytorch_model.bin`, `tokenizer.json`

1. **Serve the Model Locally**
    
    ```bash
    ollama serve
    ```
    - Opens a local endpoint to query the model via CLI or other apps.

1. **Query Model Offline**

    ```bash
    ollama run mistral --prompt "Summarize this text"
    ```

---

### **4. How to Make Your Own Models (Optional)**

1. **Get a Pre-trained Model** (small version for CPU):
    
    - Hugging Face: `distilGPT2`, `mistral-7B-instruct` (tiny version)
        
2. **Convert / Optimize for Ollama**
    
    - Ollama supports `.onnx` or PyTorch `.bin` models.
    - Ensure tokenizer and config files are included.

3. **Place in Ollama Folder**
    
    ```
    ~/.ollama/models/my_model/
    ```
    
    - `my_model/config.json`
    - `my_model/pytorch_model.bin`
    - `my_model/tokenizer.json`
        
4. **Serve & Test Offline**
    
    ```bash
    ollama serve
    ollama run my_model --prompt "Hello AI"
    ```
    

---

### ✅ **Key Points for Your System**

- Tiny models only (3 GB RAM CPU)
- Offline usage fully possible
- Ollama handles downloads, file storage, and local serving
- You can integrate it with automation workflows or local app    

---

---

## **1. What are these models?**

When we talk about “these models” in the context of Ollama, we mean **Large Language Models (LLMs)**.

- **Definition**: LLMs are AI models trained on huge amounts of text data to understand and generate human-like language.
- **Examples**: GPT, Mistral, LLaMA, Falcon, etc.
- **Purpose**: They can read, summarize, generate text, answer questions, translate, and even reason.

**Tiny models**: There are smaller versions optimized to run on limited hardware (like your 3 GB RAM system). These are called **lightweight or distilled models**.

---

## **2. How do these models give ability to a system?**

Installing and running these models locally gives your system the ability to:

1. **Understand natural language** – it can “read” and “interpret” text.
2. **Generate text** – write summaries, reports, emails, or code.
3. **Answer questions** – like a chatbot, even on offline data.
4. **Semantic search** – find meaning in documents, not just keywords.
5. **Automation** – trigger actions based on text commands (e.g., in n8n workflows).


Basically, your system becomes **AI-enabled**, capable of processing human language intelligently.

---

## **3. Can you use them offline?**

✅ Yes, this is one of the **biggest advantages of Ollama**.

- Once you **download the model**, it resides locally.
- No internet is required to query the model.
- Limitations: **big models need more RAM/CPU/GPU**. On your 3 GB CPU system:
    - Only **tiny models** will run slowly.
    - You can experiment with **short queries** or **text-based automation**.


---

## **4. Fundamentals & Architecture of LLMs**

### **A. Fundamental Concepts**
1. **Tokens**: LLMs don’t see words; they see tokens (pieces of text).
2. **Embeddings**: Converts tokens into numerical vectors representing meaning.
3. **Attention Mechanism**: Lets the model “focus” on important words when generating text.
4. **Layers**: LLMs have many layers of computations called **transformer blocks**.

### **B. Architecture (Transformers)**
Most modern LLMs are based on **Transformer architecture**:
- **Input Layer**: Tokenizes text into embeddings.
- **Encoder (optional in some models)**: Understands context (used in BERT).
- **Decoder (used in GPT)**: Generates new text based on context.
- **Attention Heads**: Multiple attention heads detect relationships between words.
- **Output Layer**: Converts vectors back to human-readable words.

**Flow**:  
`Text → Tokenization → Embedding → Transformer blocks → Attention → Output → Generated text`

---

## **5. How do they work? (High-level)**

1. **Training phase** (done before you download the model):
    - Models learn patterns from massive text datasets.
    - Learn grammar, facts, logic, and even reasoning.
    
2. **Inference phase** (what you do with Ollama):    
    - You input a query or prompt.
    - Model predicts the next word/token repeatedly.
    - Generates coherent responses based on learned patterns.

---

## **6. Role of Ollama**

Ollama acts as a **bridge between you and the model**:
- Downloads and manages models locally.
- Provides **APIs/CLI** to query models from your programs.
- Lets you integrate LLMs with workflows (like n8n).
- Handles **model serving**, so you don’t need to write complicated AI code.
- Offline capability: Once model is downloaded, internet is not required.

Think of Ollama as a **“local AI server manager”**.

---

## **7. Uses in Modern Days**

1. **Business Automation**: Summarize emails, analyze reports, generate content.
2. **Customer Support**: Offline chatbots for internal systems.
3. **Education**: Automated tutoring, generating practice questions, explanations.
4. **Healthcare**: Summarize patient notes, assist in research papers.
5. **Software Development**: Code generation, bug fixes, documentation.
6. **Research & Data Analysis**: Quickly extract insights from large datasets.
7. **Personal Productivity**: Notes summarization, task management, language translation.

---
- Ollama enables offline AI and integration.
- Modern use-cases: content, automation, search, coding, analysis, chatbots.
- Fundamental architecture: **Transformer-based**, using tokens, embeddings, attention, and layers.
---

