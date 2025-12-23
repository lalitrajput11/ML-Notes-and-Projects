### Roadmap to Become a Strong AI-ML Intern  (From Zero → Job-Ready in 4–8 Months)

This roadmap is tailored exactly to Firmway’s requirements. It assumes you are starting from little/no coding or AI experience. Dedicate 12–20 hours/week and you’ll be ready to contribute from day 1 of the internship.

#### Phase 0 – Absolute Basics (Weeks 1–2)

Goal: Be able to open a terminal and write your first Python program.

- Install Python 3.11+, VS Code, Git
- Learn basic Linux commands (ls, cd, mkdir, rm, grep)
- Python basics: variables, lists, dicts, loops, functions, if/else
- Resources (all free):
    - Automate the Boring Stuff with Python (Chapters 1–6)
    - freeCodeCamp Python 4-hour YouTube video
- Daily practice: 50–100 small exercises on Exercism.io or HackerRank (Python track)

#### Phase 1 – Core Python + Git Mastery (Weeks 3–6)

Firmway explicitly wants clean, maintainable Python code + strong Git habits.

1. Intermediate Python (2 weeks)
    - OOP (classes, inheritance, dunder methods)
    - Error handling (try/except)
    - Virtual environments & pip
    - Working with JSON, CSV, logging
    - Type hints & mypy (Firmway loves clean code)
2. Git & GitHub (1 week)
    - Branching workflow (feature branches, PRs)
    - Resolving merge conflicts
    - Writing good commit messages
    - GitHub flow (fork → clone → branch → PR)
3. Testing with PyTest (1 week)
    - Writing unit tests, fixtures, parametrization
    - Coverage, assertions

- Resources:
    - Real Python tutorials
    - “Python Testing with pytest” by Brian Okken (read first 5 chapters – free PDFs available)
    - Git official docs + GitHub Skills lab (free interactive)

Mini-Project #1 (Week 6): Build a clean Python CLI tool (e.g., expense tracker) with:

- Proper project structure
- Type hints
- 90%+ PyTest coverage
- GitHub repo with README + good commit history

#### Phase 2 – Data Handling & Feature Engineering (Weeks 7–11)

Firmway works with enterprise data → you must be comfortable cleaning messy data.

1. NumPy & Pandas mastery (2 weeks)
    - Vectorized operations
    - Handling missing data, duplicates
    - Groupby, pivot tables, merge/join
2. Feature Engineering (1 week)
    - Encoding categorical variables
    - Scaling/normalization
    - Date/time features
    - Text cleaning & regex
3. Working with real datasets
    - Kaggle datasets (Titanic → House Prices → Tabular Playground)
    - Open government/enterprise-style datasets

- Resources:
    - Kaggle Learn Pandas & Feature Engineering courses (free)
    - “Python for Data Analysis” by Wes McKinney (free PDF)

Mini-Project #2: End-to-end data pipeline on a Kaggle competition (score in top 30–40%). Upload notebook + cleaned dataset + GitHub repo.

#### Phase 3 – Machine Learning Fundamentals (Weeks 12–18)

Firmway uses scikit-learn heavily for enterprise features.

1. Scikit-learn full mastery (3 weeks)
    - Pipelines & ColumnTransformer
    - Cross-validation, GridSearchCV, Optuna
    - All major algorithms: Linear/Logistic Regression, Trees, XGBoost, SVM, KNN
    - Metrics deep dive (precision/recall/F1, ROC-AUC, confusion matrix)
2. ML Engineering Best Practices (1 week)
    - Train/validation/test splits
    - Preventing leakage
    - Experiment tracking (MLflow or Weights & Biases free tier)
    - Model persistence (joblib/pickle)

Mini-Project #3: Build a production-ready credit-risk or customer-churn model using XGBoost + MLflow tracking + PyTest for data pipeline tests.

#### Phase 4 – Deep Learning & Modern Stack (Weeks 19–26)

Firmway integrates DL models into backend services.

1. PyTorch basics → intermediate (4 weeks)
    - Tensors, autograd
    - nn.Module, Datasets & DataLoaders
    - Training loops from scratch
    - Transfer learning (timm, Hugging Face)
2. Common architectures you’ll likely see
    - Tabular → Deep learning (TabNet, FT-Transformer)
    - Text → Transformers (BERT fine-tuning)
    - Time series → LSTMs/Transformers
3. Model serving basics
    - TorchServe or FastAPI + ONNX
    - Logging predictions

Mini-Project #4: Fine-tune a Hugging Face transformer on a text classification or NER enterprise task (e.g., invoice category detection) and wrap it in a FastAPI endpoint.

#### Phase 5 – Production & Engineering Excellence (Weeks 27–32)

This is what separates interns who just train models from ones who ship to large enterprises.

1. FastAPI basics (1 week)
    - Routers, Pydantic models, dependency injection
2. Docker basics (1 week)
    - Dockerfile for ML models
3. CI/CD with GitHub Actions (1 week)
    - Run PyTest + linting on every PR
4. Logging & monitoring (basics)
    - structlog, Sentry basics

Final Capstone Project (2 weeks) – This will be your interview golden ticket: “Enterprise Lead Scoring SaaS Module”

- Ingest CSV → clean & feature engineer (Pandas pipeline with tests)
- Train XGBoost + fine-tuned tabular transformer
- Track experiments with MLflow
- Serve both models via FastAPI (/predict endpoint)
- Dockerize + GitHub Actions CI
- Full README with architecture diagram
- Deploy free on Render.com or Railway.app

#### Bonus (Ongoing)

- Contribute small PRs to open-source ML repos (great resume signal)
- Write weekly LinkedIn/technical blog posts about what you built
- Record 2–3 minute demo videos of your projects

### 8-Week Crash Plan (If you only have 2 months)

Week 1–2 → Python + Git + PyTest Week 3–4 → Pandas + scikit-learn full stack Week 5–6 → PyTorch basics + one DL project Week 7 → FastAPI + Docker basics Week 8 → Capstone project (simplified version)

### Portfolio You Should Have Before Applying to Firmway

1. GitHub profile with 5+ well-documented repos
2. At least 2 projects with >90% test coverage
3. One end-to-end ML project served via API (link in resume)
4. Clean READMEs, requirements.txt, pyproject.toml/poetry
5. LinkedIn with project descriptions