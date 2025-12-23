
### Key Concepts and Challenges in Machine Learning Deployment

- **Machine learning models often perform well in isolated development environments** (e.g., data scientists’ laptops using Python notebooks) but face numerous challenges when deployed in production.
- **Deployment Environment Mismatch:** Production environments (e.g., banks) may use different programming languages (Java over Python), infrastructure (Kubernetes clusters on AWS), and hardware resources, causing performance degradation or failures.
- **Performance Issues:** Models that take seconds per transaction are unsuitable for high-frequency, real-time applications which require millisecond latency.
- **Data Drift:** Over time, new patterns (e.g., emerging fraud types) cause models to degrade because the data distribution changes from the training set.
- **Reproducibility Problem:** Lack of documentation and tracking of model-building steps makes it difficult to update or reproduce models reliably.
- **Monitoring Deficiencies:** Without continuous monitoring, teams only discover model failures after customers report issues.
- **Update Complexity:** Updating models without downtime or disrupting services is challenging without proper operational frameworks.

---

### Core MLOps Solutions

**MLOps addresses these challenges through:**

- **Consistent Environments:** Packaging models with their dependencies (e.g., using Docker containers) ensures that models run identically across development, staging, and production.
- **Performance Testing:** Automated testing within CI/CD pipelines confirms that models meet speed and accuracy requirements before deployment.
- **Data Monitoring:** Tools like TensorFlow Data Validation and Great Expectations monitor incoming data to detect data drift early.
- **Versioning and Experiment Tracking:** Platforms such as MLflow and DVC record all aspects of model training (data, preprocessing steps, parameters) to enable reproducibility and auditability.
- **Real-Time Monitoring and Alerting:** Dashboards powered by Prometheus and Grafana track model accuracy, latency, and error rates, sending alerts when performance drops.
- **Seamless Model Updates:** Deployment tools (e.g., Argo CD, GitLab CI) enable rolling updates without downtime, allowing quick responses to new data or fraud patterns.

---

### Example: Banking Fraud Detection System Workflow with MLOps

|Step|Tools/Concepts|Description|
|---|---|---|
|Data Collection & Cleaning|Airflow, Kubeflow|Automate data pipelines that gather and preprocess daily transaction data.|
|Model Development|Docker, Standardized Environments|Data scientists build models in containers that mirror production environments.|
|Automated Testing|CI/CD pipelines (Jenkins, GitLab CI, GitHub Actions)|Run accuracy, integration, and performance tests before deployment.|
|Deployment|Kubernetes (EKS), Argo CD|Deploy models on scalable infrastructure with zero downtime updates.|
|Monitoring & Alerting|Prometheus, Grafana|Continuously track model health and receive alerts if performance degrades.|
|Retraining & Updating Models|Automated retraining workflows|Trigger retraining on new fraud examples or behavioral changes to maintain accuracy.|

### Importance of MLOps Roles and Skills

- **Data Scientists:** Need MLOps skills to create reproducible, deployable models and understand production constraints.
- **DevOps Engineers:** Have a strong foundation but must learn ML-specific challenges like model drift and feature stores.
- **Engineering Managers:** Must understand MLOps to properly scope projects, budget infrastructure, and manage ML teams.
- **Cloud Engineers:** Require knowledge of ML infrastructure (e.g., GPU scaling, high-throughput storage) for cost-effective and scalable model training and serving.

---

### Analogies and Comparisons

- **MLOps is to machine learning what a kitchen is to cooking:** Even the best chefs (data scientists) need a proper kitchen (MLOps tools and processes) to serve many customers reliably.
- **Traditional Software vs. Machine Learning Systems:** Software is like building a fixed house with a blueprint; ML systems continuously adapt like a self-rearranging house reacting to environment and occupant changes.

---

### Additional Tools Highlighted

|Tool/Platform|Purpose|Notes|
|---|---|---|
|Docker|Containerization for environment consistency|Packages models with dependencies|
|Kubernetes (EKS)|Scalable deployment and orchestration|Manages scaling and availability|
|Airflow/Kubeflow|Data pipeline automation|Ensures reliable data ingestion|
|MLflow/DVC|Experiment tracking and version control|Enables reproducibility|
|Prometheus/Grafana|Monitoring and alerting|Real-time performance tracking|
|Jenkins/GitLab CI/GitHub Actions|CI/CD automation|Automates testing and deployment|
|Argo CD|Continuous delivery for Kubernetes|Enables zero-downtime updates|
|TensorFlow Data Validation / Great Expectations|Data validation|Detects data drift early|
|Warp (Mentioned as a helpful dev tool)|Autonomous coding & deployment assistant|Generates production-ready code, supports debugging and logs|

### Conclusion

**MLOps bridges the gap between experimental machine learning models and robust, scalable production AI systems.** By ensuring environment consistency, continuous monitoring, reproducibility, and fast updates, MLOps enables organizations to deploy machine learning models that maintain high performance and reliability over time.

---
---
---
Worp is an agentic development environment that is transforming how engineers code and deploy.
![[Pasted image 20251214090550.png]]
MLOps solves the deployment issue. We don't stop at just Docker containers for production. We need to make sure our model runs reliably at scale. This is where Kubernetes comes in. By deploying our model containers on current cluster like EKS, we solve that environment consistency problem. And Kubernetes then handles all the heavy lifting of scaling our fraud detection service up during busy shopping periods and scaling it down during quiet times. And the best part is that we can define this entire setup as infrastructure as code. using tools like Terraform or AWS cloud formation. This means that the entire MLOps pipeline from development environment to production is documented, version controlled and reproducible for our banking fraud system. more surprises when moving from development to production. The model that worked perfectly on the data scientist's laptop or in development environment will work the same in production environments because we create consistency across different environments. And as I said, all these tools and concepts that we're going through are covered in the MLOps road map that we created for you to accompany this video. So don't forget to download that from below. The second thing MLOps solves is fixing performance issues 
MLOps includes automated testing. This is part of what we call CI/CD or continuous integration, continuous deployment pipelines. For example, before the model goes live, the system or the pipeline runs different types of tests to check if the model is fast enough. So they will do speed testing of the model. Let's say for our banking app, the CSV pipeline runs a test that shows that the model is too slow. the team will identify that before it gets released and they could now optimize the model or use techniques like batch processing and so on to speed it up. MLOps also addresses the data drift in an efficient way. With MLOps, you're constantly watching the new incoming data. It uses data validation tools like TensorFlow data validation or grade expectations to compare what's coming in now with what the model was trained on. So if the new data starts to look different, let's say customers are behaving in completely new ways or fraud patterns change, these data monitoring tools would notice this quickly and they could alert the team or even automatically retrain the model with examples of the new fraud types. With MLOps, everything is recorded automatically using experiment tracking tools like MLflow or DVC data version control. So you have the exact data used for training, all the steps used to clean and prepare the data, all the model settings and parameters, results of each training attempt and so on. For our banking model, these tracking tools mean the team could easily see exactly how the original model was built 

![[Pasted image 20251214092002.png]]
![[Pasted image 20251214092301.png]]
Data engineers set up data pipelines using tools like Airflow or CubeFlow that collect and clean transaction data daily. Data scientists build models in standardized environments using Docker containers, not in some custom lab environments on their laptops, but rather something which is very close to the production environment. When a new model is ready for deployment, CI/CD tools like Jenkins or GitLab CI or GitHub actions run automated tests to check the accuracy and speed for models with unit test, integration tests, performance tests before deployment is allowed. If all tests pass, the model is deployed automatically to a staging environment, maybe a Kubernetes cluster, where additional tests run with real transaction data before it can be deployed to final production environment. If the new version of the fraud detection model demonstrates better performance such as catching more fraud and generating fewer false alarms, the deployment tool like Argo CD or again GitLab CI or GitHub actions can automatically replace the older production model running in the cluster with a new one without a downtime. After it gets deployed to production, the monitoring tools like Prometheus and Graphfana will track how well the model is working 24/7. This is especially important within the first hours or days of deploying a new version to immediately catch any issues that might have slipped through all these automated tests into the production. But also we have an ongoing monitoring for performance degradation of the model because of changing data or changing customer behavior which again is a phenomenon known as model drift. So tools like Prometheus can automate alerting when metrics deviate from expected levels which enable fast response. So when new fraud patterns emerge, the monitoring system alerts the update.

![[Pasted image 20251214092958.png]]
## CI/CD

### Key Concepts and Workflow Issues Before CI/CD Implementation

Imagine you and your team are developing an application. The first version is done. So now it's time to deploy the app on a server. You check in your code and try to merge it into the main branch. You get merge conflicts because other engineers in your team also made some code changes before you. So you fix those issues manually. You try to merge again. Now a simple Jenkins job runs tests on the main and discovers a bunch of issues. Well, now we rush to fix them because we just broke the main branch. So we fixed those issues and after all these fixes and code changes from different developers all in the main branch and now it's end of sprint. So we want to deploy all our changes because we need to release them at some point, right? So we do a code freeze which means no one's allowed to merge anything to main until we deploy the current state with all those changes. So you and your team start testing the latest state of the main branch to make sure that new features all work properly but also make sure that we didn't break any previous features and functionality. So we do this intense testing manually before we deploy again. We find some issues so we jump on it to fix it . let's manually modify a Docker compose file or Kubernetes manifest file. Or maybe we added a new service. So let's add that Kubernetes YAML file manually as well. And now again someone who is knowledgeable and senior in our team they connect to Kubernetes cluster with cubectl command and apply the new manifest files or if the app is running on a simple server they SSH into the server they stop the containers and restart them with a modified docker compose file and then they give testers.

![[Pasted image 20251214102531.png]]
- **Manual merging and merge conflicts** occur frequently as multiple developers work on the same main branch.
- Tests run only after merging, often breaking the main branch and causing rushed fixes.
- A **code freeze** is imposed before deployment, halting all merges, which delays progress.
- Manual, **intensive testing sessions** are required before deployment, consuming significant time and effort.
![[Pasted image 20251214102629.png]]
- Deployments involve manual steps:
    - Checking out code locally,
    - Bumping version numbers,
    - Building Docker images manually,
    - Editing Docker Compose or Kubernetes manifests,
    - SSH or `kubectl` commands to deploy,
    - Communicating deployment readiness to testers.
- Deploying to production is anxiety-inducing, especially without proper timing or support, and heavily reliant on senior engineers.
- Overall, the process is error-prone, slow, and constrained by human involvement.

---

### Continuous Integration (CI): Improving Code Quality Early

- Tests should run **on feature branches for every commit before merging**, preventing broken code from reaching the main branch.
- Frequent, small commits enable faster bug detection and simpler fixes.
- Running tests on each branch avoids complex bugs caused by multiple features merged simultaneously.
- This approach **reduces merge conflicts and developer frustration**, improving overall workflow efficiency.
- **CI catches issues earlier** and isolates them, leading to a healthier, more stable codebase.

---

### Role of Automated Code Review with Code Rabbit

- An AI-powered tool that automates the initial code review stage by:
    - Detecting bugs, security vulnerabilities, and performance issues early.
    - Providing root cause analysis within pull requests.
- It **augments human reviewers**, freeing them to focus on complex design decisions.
- Aligns perfectly with CI/CD philosophy by catching issues early and keeping pipelines flowing smoothly.

---

### Continuous Delivery (CD): Automating Deployment and Testing

- After successful tests on the main branch, **build automation tools (e.g., Jenkins, GitHub Actions)**:
    - Automatically build Docker images,
    - Tag and push images to registries,
    - Deploy to dev environments using scripted pipelines,
    - Modify Kubernetes manifests automatically.
- This automation eliminates manual checkout, build, and deployment steps.
- Automated **end-to-end and integration tests** run against deployed environments (dev/staging), validating functionality, security, and infrastructure.
- The pipeline can include **dynamic security tests** (e.g., simulated attacks like SQL injections).
- The process removes human error, speeds up releases, and **removes the need for code freezes or senior engineer bottlenecks**.
- This staged deployment with automated testing is referred to as **continuous delivery**.

---

### Continuous Deployment and Production Strategies

- Continuous deployment extends continuous delivery by enabling **automatic deployment to production**, often with a simple manual confirmation step.
- Manual approval is usually a single button click, enabling even non-technical stakeholders to trigger production releases.
- To further reduce risk, deployment strategies include:

|Deployment Strategy|Description|Benefits|
|---|---|---|
|**Canary Deployment**|Gradually rolls out new versions to a small subset of users (e.g., 1%, then 5%, etc.) while monitoring for issues before full rollout.|Reduces risk by limiting impact of potential bugs.|
|**Blue-Green Deployment**|Maintains two identical environments (blue = current, green = new). Switches traffic instantly from old to new or back if issues arise.|Provides instant rollback capability, minimizing downtime.|

- These strategies require automated **monitoring and alerting** to detect issues without manual supervision.
- Implementing these methods **increases confidence and frequency of production deployments**.

---

### Benefits and Impact of CI/CD Automation

- **Eliminates manual errors and forgotten deployment steps**.
- Removes dependency on specific team members for releases.
- Enables **faster and more reliable release cycles**.
- Frees up developers and testers from repetitive manual work.
- Supports a culture of **frequent, small, and safe code changes**.
- Forms the backbone of **DevOps practices**, linking development, testing, deployment, and monitoring into a seamless pipeline.
- Though initial setup requires effort (~2-3 days with experience), the long-term gains in efficiency and quality are substantial.

---

### Conclusion

The video stresses that **CI/CD is essential for modern software teams** to reduce stress, increase deployment confidence, and accelerate delivery. It encourages investing in automation and testing to streamline workflows, minimize human error, and adopt safer release strategies, ultimately supporting faster innovation with less risk.

---

### Keywords and Concepts

- **CI (Continuous Integration)**
- **CD (Continuous Delivery / Continuous Deployment)**
- **Code freeze**
- **Merge conflicts**
- **Automated testing (unit, integration, end-to-end, security)**
- **Build automation tools (Jenkins, GitHub Actions, GitLab CI)**
- **Docker images and registries**
- **Kubernetes manifests**

- **Canary deployment**

Canary deployment the idea is super simple. We roll out the new feature to 1% of users or 5% and we observe for an hour and see if nothing blows up. Okay, that's great. Let's crank it up to 10%. Let's observe for two more hours. Okay, let's do 20%, let's see overnight, nothing crazy happens. Now we're good. Let's switch to 100%. So basically, canary deployment is a progressive roll out of an application that splits the traffic between an already deployed version and a new version that we just deployed. And it rolls out the new version to a subset of users before rolling it out fully. And the way it works is usually canary deployments select a small number of servers or nodes for the initial deployment and then gradually or progressively deploy that new version everywhere.

- **Blue-green deployment**

we also have green blue deployment. Again, super simple idea. You create two separate but identical environments. One environment call it blue is running the current application version and one we call it green is running the new application version. And the main idea is that if the new deployment has any issues, we can immediately switch the entire traffic back to the older version. So the main idea is that if something goes wrong, you can easily fall back to the previous version or environment. Again, this requires some work to set up, including setting up monitoring that will continuously check the deployment and alert on any issues instead of human sitting in front of a monitor and watching for an hour if something happens.
- **Automated monitoring and alerting**
- **DevOps automation**

---

### Summary Timeline of Workflow Evolution

| Stage                          | Description                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------------- |
| Manual deployment              | Manual merges, testing, building, and deployment with human error and delays             |
| Continuous Integration (CI)    | Automated testing on feature branches per commit to catch bugs early                     |
| Continuous Delivery (CD)       | Automated builds, deployments to dev/staging, and automated end-to-end testing           |
| Continuous Deployment          | Automatic deployment to production with optional manual approval                         |
| Advanced deployment strategies | Canary and blue-green deployments to reduce production risks and enable instant rollback |
![[Pasted image 20251214101656.png]]

### Key Concepts and Workflow

- **Trunk-Based Development**: The video describes this as a modern git workflow where the main branch is always in a releasable state. Any push to the main branch triggers an automated **CI/CD pipeline** that deploys to development, staging, or production environments without manual testing or intervention.
    
- **Tests in CI Pipelines**:
    
    - **Unit and Integration Tests**: Validate code logic under various scenarios.
    - **Security Tests**: Scan dependencies for vulnerabilities and detect hardcoded secrets or logic issues.
    - **Code Quality Tests**: Detect bad practices like code duplication, outdated APIs, null pointer risks, and insufficient test coverage.
- **Feature Branch Workflow**:
    
    - Developers work on separate feature branches.
    - Tests run on **merge requests (pull requests)** to ensure code is releasable before merging.
    - Running tests only after merging can block the main branch if issues arise, hence tests must run **before merging** to avoid pipeline bottlenecks.
- **Continuous Integration (CI)**:
    
    - Running tests on every **commit** in feature branches provides immediate feedback.
    - This frequent testing helps especially junior engineers learn best practices and fix problems early.
    - This approach exemplifies **“shifting left”**—moving automated testing earlier in the development cycle.
    - Local IDEs also perform some inspections, but centralized CI pipelines ensure consistent enforcement beyond individual developers’ environments.

---

### Using Kadana for Code Quality Checks

- Kadana is a **JetBrains tool** that mirrors IDE inspections in a CI environment.
- It supports multiple languages like **Java, JavaScript, Python**, etc., avoiding the need for multiple language-specific tools.
- Kadana can:
    - Detect code issues with different severity levels.
    - Provide detailed reports with file locations and issue descriptions.
    - Suggest and automatically apply fixes via pull requests.

---

### Building a CI Pipeline with GitHub Actions and Kadana

**Steps to integrate Kadana into a GitHub Actions pipeline:**

|Step|Description|
|---|---|
|1. Create a GitHub Actions workflow|Define triggers (push to main branch or pull requests) and jobs to run Kadana scans.|
|2. Create a Kadana config file (`kadana.yml`)|Configure inspection profiles (starter, recommended), linters, and language-specific settings.|
|3. Connect Kadana Cloud|Upload scan results to Kadana Cloud for visualization and tracking.|
|4. Add Kadana token to GitHub secrets|Securely store the token for Kadana Cloud authentication and upload of scan results.|

- The pipeline runs Kadana scans on every push or pull request.
- Results show in both GitHub UI and Kadana Cloud with filters for severity and detailed issue views.
- Kadana executes hundreds of inspections and reports issues such as invalid configurations, code duplications, null safety problems, and outdated practices.

---

### Automated Fixes with Kadana

- Kadana supports an **auto-fix feature**:
    - Automatically applies suggested fixes.
    - Creates a pull request with the fixes for review.
    - Examples include adding null checks, removing redundant code, refactoring with Lombok annotations.
- This feature requires appropriate permissions and configuration in the CI pipeline.
- Helps junior developers adopt best practices with minimal manual intervention.

---

### Benefits and Best Practices Highlighted

- **Early detection and resolution** of code issues prevent pipeline blockages and improve code quality.
- **Centralized automation** removes dependence on individual developer discipline.
- **Incremental commits** with automated checks enhance learning and reduce technical debt.
- Kadana provides a unified tool for **multi-language code quality analysis**.
- Visualization in Kadana Cloud simplifies issue tracking over time.

---

### Core Insights

- **CI pipelines are essential** for maintaining code quality, security, and deployability in modern software teams.
- Running automated tests **before merging** code protects the main branch and accelerates development.
- Kadana’s integration into CI pipelines offers a **powerful, language-agnostic solution** for code quality checks.
- Automated fix suggestions combined with pull requests enable **continuous code improvement** with minimal manual review.
- Shifting testing left and integrating IDE-like inspections into CI pipelines creates a **robust feedback loop** that benefits junior and senior engineers alike.
https://www.youtube.com/watch?v=MIWH2CpVyXs

---
---
---
