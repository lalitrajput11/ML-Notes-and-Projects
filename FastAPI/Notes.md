 
    
- **Why FastAPI?**
    
    - FastAPI is the **industry-standard framework** for building robust, scalable APIs that power machine learning and AI models in production.
    - , **9 out of 10 companies** use FastAPI to deploy their ML model APIs.
    - Learning FastAPI is essential for AI professionals who want to present their models to the world via web or mobile applications.
- **Role of API in AI and Software:**
    
    - An **API (Application Programming Interface)** acts as a **connector between different software components**, such as the frontend and backend of an application.
    - APIs enable software components to communicate using **defined rules, protocols (e.g., HTTP), and data formats (e.g., JSON)**.
    -![[Pasted image 20251210073123.png]]
    - In AI/ML contexts, APIs allow models to be accessed without exposing the underlying code or data directly, providing a secure and standardized interface.
    -![[Pasted image 20251210073023.png]]
Any course , we want to get from any particular website, through frontend.

    
- **Monolithic Architecture vs API-based Architecture:**
    
    - Pre-API era websites used a **monolithic architecture** where frontend and backend were tightly coupled in one application. This made sharing data or functionality with third parties difficult.
    - For example, IRCTC’s train information system in monolithic form couldn’t easily share data with partner travel companies like MakeMyTrip.

**Need for API's
In pre-existing API era >>
Database > Backend  System > Frontend(User Based) (HTTP Request).

In Monolithic > Backend and Frontend  are tighlty coupled inside a common Directory like src.
But we cant give our databse and baskend access  to other,  for scaling. So we don't follow Monolithic approach.

Need for API's :-
To different companies, if they want to access a common database . We cant give the access of a database. API comes here : we build backend and frontend in different folder.
Like as independent application.  
Database > Backend > API (Train> specific funciton > particular Endpoint> it 'll hit a particular function of backend) . Backend is not accessible  or affected >  part of backend is accesible by API end point > in order to get databse's data.
![[Pasted image 20251210074929.png]]


    - APIs solve this by **decoupling frontend and backend**, turning the backend into an independent application accessible through public API endpoints.
    - This enables multiple frontend applications (websites, Android apps, iOS apps) or (differnt companies software )to consume the same backend services uniformly.
- To the API : It does http request .  And software gets the result in json format. Any language can understand it.
- json : is universal data foramt(response is returned in this foramt.)
Api Infrastructure : Common Database, Common Blackend , By one API , we can handle multiple platform , like android , ios and website platform.

- **Benefits for AI/ML Models:**
    
    - Instead of a database, AI applications revolve around a **trained ML model**, which is loaded and served via backend functions exposed through APIs.
    - ![[Pasted image 20251210085514.png]] Old way: Monolithic Architecture (File vised )
    - Companies like OpenAI (ChatGPT), Amazon (recommendation systems), and others use this architecture to serve models to various clients securely and efficiently.
    - ![[Pasted image 20251210085723.png]]
    - APIs allow external applications to interact with models without direct access, enhancing security and scalability.
    
- **Technical Details:**
    
    - Communication between frontend and backend or between different software systems happens over **HTTP protocol**.
    - Data exchanged is formatted in **JSON**, a universal language-independent format understood by all major programming languages.
    - API endpoints are special URLs exposed over the internet that clients can hit to invoke backend functions.
    
- **Playlist Curriculum Overview:**
    
    - **Part 1:** Fundamentals of FastAPI, learning core concepts without focusing on ML.
    - **Part 2:** Integration of FastAPI with ML models — building APIs around trained models and connecting them with frontend apps.
    - **Part 3:** Deployment of APIs using cloud services like AWS, including containerization with Docker and industry-grade production practices.
    - The playlist will contain approximately **15 videos**, aimed to be completed within **21-25 days**.

---


### Definitions and Comparisons

|Term|Definition / Description|
|---|---|
|**API (Application Programming Interface)**|Mechanism that enables communication between software components (e.g., frontend and backend) using protocols and data formats.|
|**Monolithic Architecture**|Single, tightly coupled application where frontend and backend are developed and deployed together.|
|**API-based Architecture**|Decouples frontend and backend; backend exposes functionality via APIs accessible to multiple clients.|
|**HTTP Protocol**|Standard protocol used for communication between clients and servers over the internet.|
|**JSON (JavaScript Object Notation)**|Lightweight, universal data format used for exchanging data between systems, easily readable by many programming languages.|
|**FastAPI**|Modern, fast, and scalable Python framework for building APIs, widely adopted in ML/AI industry.|

### Core Benefits of Using APIs in AI/ML

- Enables **secure and controlled access** to ML models and data.
- Facilitates **multi-platform support** (web, Android, iOS) from a single backend.
- Simplifies **maintenance** and **scalability** by decoupling components.
- Allows **monetization** by exposing selective data or model functionality.
- Uses **standard protocols and data formats** ensuring interoperability.

---

### Conclusion

This introductory video establishes the foundational understanding of APIs, their necessity, and their pivotal role in both software and AI/ML ecosystems. It lays out a clear roadmap for the upcoming FastAPI playlist, which will teach viewers how to build, integrate, and deploy ML-powered APIs using FastAPI, ultimately enabling them to bring AI models to real-world applications with industry-grade practices.

---
---
---

### FastAPI Definition 


- **FastAPI Definition**:  
    FastAPI is a **modern, high-performance web framework for building APIs with Python**. It enables developers to create industry-grade APIs quickly and efficiently.
    
- **Internal Architecture**:  
    FastAPI is built on two key Python libraries:
    
    |Library|Role|
    |---|---|
    |Starlette|Manages HTTP requests and responses; acts as the asynchronous web server interface.|
    |Pydantic|Provides automatic data validation and parsing using Python type hints.(Type checking, It has proper format)|
    
- **Role of Starlette**:  
    It handles HTTP requests from clients, processes them, and sends HTTP responses back, acting as the bridge between the web server and FastAPI code.
    
- **Role of Pydantic**:  
    It **automatically validates incoming data** and ensures data conforms to expected types and formats, essential when building reliable APIs.
    
- **FastAPI Philosophy**:  
    The framework was created to address limitations of older Python API frameworks, focusing on two core philosophies:
    
    Performance increase > Less Latency > Fast to code > Fast to run > Industry level Grade.
    
    
    1. **Fast to run** — APIs built with FastAPI have low latency, handle concurrent requests efficiently, and perform better for industry-grade applications.
    2. **Fast to code** — FastAPI reduces boilerplate code with features like automatic input validation and interactive documentation, enabling faster development.

---
![[Pasted image 20251210091218.png]]
SGI : Server Gateway Interface : helps to convert the http foramt to local backend understandable code  and vice versa.
In API : Logic and function's EndPoint to get the feature(here , we are taking two feature inside the Predictions call of a Machine Learning Model)
:- It helps to set up the communication between the web server and API.

 ***WSG(In Flask):-***
 
 Behind the scene : Based on Werkzueg library .It follows blocking architecture. it is in synchronous nature.Can lead to slow request processing and  and scalability challanges.  
 Concurrency limitations  :- 1 user at a time , 2nd client or request have to wait.
 SGI : is set of protocols, in flask , it is based on werkzeug. Based on Gunicorn(WebServer).
 API : code also in synchronous in nature, designed to handle 1 clinet at a time.
 
### Comparing FastAPI with Flask

| Aspect                   | Flask                                                  | FastAPI                                                            |
| ------------------------ | ------------------------------------------------------ | ------------------------------------------------------------------ |
| Server Gateway Interface | WSGI (Web Server Gateway Interface) - Synchronous      | ASGI (Asynchronous Server Gateway Interface)                       |
| Web Server               | Gunicorn (WSGI server)                                 | Uvicorn (ASGI server)                                              |
| Request Handling         | Synchronous, blocking; processes one request at a time | Asynchronous, non-blocking; handles multiple requests concurrently |
| Concurrency Support      | Limited due to blocking nature                         | Supports concurrency via async/await                               |
| Underlying Library       | Uses Werkzeug for WSGI                                 | Uses Starlette for ASGI                                            |
| Performance              | Slower, latency issues under load                      | Faster, scalable for modern web applications                       |

- **WSGI vs ASGI**: Web server(Sync)/Asynchronous (Uvicorn web server)
    
    - WSGI (used by Flask) is synchronous and blocking, meaning only one request can be processed at a time, causing latency under multiple concurrent requests.
    - ASGI (used by FastAPI) supports asynchronous programming, enabling concurrent request handling, making it suitable for high-performance and real-time applications.
    
- **Async/Await Feature in FastAPI**:  
    FastAPI supports Python’s async/await syntax, allowing the API to process other requests while waiting for slower operations (e.g., ML model predictions), improving throughput.
    

---

### FastAPI’s Development Advantages

**Why FastAPI is so fast :-**


![[Pasted image 20251210092907.png]]

- **Automatic Input Validation**:  
    Thanks to Pydantic integration, FastAPI automatically validates input data types without requiring explicit code, reducing bugs and development time.
    
- **Auto-generated Interactive Documentation**:  
    FastAPI automatically generates API documentation (accessible via `/docs` URL) that is interactive — allowing users to test API endpoints directly from the docs, eliminating the need for external tools like Postman.
    
- **Seamless Integration with Modern Libraries**:  
    FastAPI supports easy integration with popular ML libraries (Scikit-learn, TensorFlow, PyTorch), database ORMs (SQLAlchemy), authentication protocols (OAuth), and deployment tools (Docker, Kubernetes).
    

---

### Practical Setup and Demo Highlights

- **Environment Setup**:
    
    - Create a new folder and open it in VS Code.
    - Create and activate a Python virtual environment.
    - Install FastAPI and Uvicorn (the ASGI server). Starlette is installed as a dependency automatically.
- **Writing a Simple Hello World API**:
    
    - Import FastAPI and create an app instance.
    - Define routes with decorators (e.g., `@app.get("/")`).
    - Create functions that return JSON responses (e.g., `{"message": "Hello World"}`).
    - Run the server using Uvicorn with `--reload` flag for automatic code change detection.
- **Adding Multiple Endpoints**:  
    Demonstrated adding a second endpoint `/about` returning information about the platform, showcasing FastAPI’s ease in managing multiple routes.
    
- **Testing and Documentation**:
    
    - Access API endpoints via browser or tools.
    - Visit `/docs` to see automatically generated interactive Swagger UI docs.
    - The docs allow users to view API endpoints, their expected inputs, and try them out in real time.

---


### Key Takeaways

- **FastAPI is built for speed and developer productivity**, enabling fast-running APIs with minimal code.
- It leverages **async programming** for concurrent request handling, unlike traditional frameworks like Flask.
- The **Starlette library handles HTTP lifecycle**, and **Pydantic handles data validation**, providing a robust foundation.
- FastAPI automatically generates **interactive API documentation**, improving usability and reducing external tool dependency.
- Its design and ecosystem allow **seamless integration with modern ML libraries, databases, and deployment tools**.
- The video provides a clear step-by-step guide to **installing FastAPI, creating endpoints, and running the server** on the local machine.

---
---
---

### FastAPI Methods


