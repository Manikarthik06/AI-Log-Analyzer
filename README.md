AI Log Analyzer with RAG & Cybersecurity Incident Reporting
Project Overview
AI Log Analyzer is a cybersecurity project that automatically parses Linux system logs, detects Indicators of Compromise (IOCs), stores log embeddings in a vector database, retrieves relevant log entries using Retrieval-Augmented Generation (RAG), generates AI-powered security analysis using a local Large Language Model (LLM), visualizes log statistics through an interactive dashboard, and creates downloadable cybersecurity incident reports in PDF format.
The entire project runs locally without relying on cloud-based AI services.

Objectives
* Parse raw Linux log files.
* Detect suspicious security events.
* Store logs in a vector database.
* Perform semantic search on logs.
* Use an LLM for cybersecurity analysis.
* Generate professional incident reports.
* Visualize security metrics.
* Build a portfolio-ready cybersecurity project.

Project Architecture
                Linux Log File
                       │
                       ▼
               Log Parsing Module
                       │
                       ▼
          IOC Detection & Classification
                       │
                       ▼
             Structured Pandas DataFrame
                       │
                       ▼
        Sentence Transformer Embeddings
                       │
                       ▼
                  ChromaDB
             (Vector Database)
                       │
              User Security Query
                       │
                       ▼
             Semantic Retrieval
                       │
                       ▼
                  Ollama Llama3
                       │
                       ▼
             AI Security Analysis
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   Streamlit Dashboard       PDF Incident Report

Technologies Used
Programming Language
* Python

Libraries
Data Processing
* pandas

Regular Expressions
* re

Vector Database
* ChromaDB

Embedding Model
* SentenceTransformers
* all-MiniLM-L6-v2

Large Language Model
* Ollama
* Llama3

Dashboard
* Streamlit

PDF Generation
* ReportLab

Visualization
* Plotly
* Matplotlib (optional)

Others
* os
* json
* datetime

Project Workflow
Step 1
Read Linux authentication logs.
↓
Step 2
Parse logs using Regular Expressions.
↓
Step 3
Convert parsed logs into a DataFrame.
↓
Step 4
Identify Indicators of Compromise.
↓
Step 5
Generate embeddings using Sentence Transformers.
↓
Step 6
Store embeddings in ChromaDB.
↓
Step 7
User enters a security-related question.
↓
Step 8
Relevant logs are retrieved using semantic similarity.
↓
Step 9
Retrieved logs are passed to Llama3.
↓
Step 10
Llama3 generates an incident analysis.
↓
Step 11
Dashboard visualizes statistics.
↓
Step 12
Generate downloadable PDF Incident Report.
￼
Core Cybersecurity Concepts Used
* Log Analysis
* Linux Authentication Logs
* Authentication Failure Detection
* Privilege Escalation Detection
* Brute Force Detection
* Indicators of Compromise (IOC)
* Security Event Classification
* Threat Analysis
* Incident Reporting
* Security Monitoring
* Blue Team Concepts

Core AI Concepts Used
Retrieval-Augmented Generation (RAG)
Instead of asking the LLM to answer from its own knowledge, relevant log entries are first retrieved from ChromaDB and then supplied as context to the model. This allows responses to be grounded in the actual log data.

Embeddings
Logs are converted into numerical vectors using the Sentence Transformer model (all-MiniLM-L6-v2). Similar logs have similar vector representations, enabling semantic search.

Semantic Search
User questions are embedded into vectors. ChromaDB compares these vectors with stored log embeddings and retrieves the most relevant entries using similarity search.

Local Large Language Model
The project uses Llama3 through Ollama, allowing AI-powered log analysis to run completely offline.

Core Python Concepts Used
* Functions
* Modules
* File Handling
* Dictionaries
* Lists
* Loops
* Conditional Statements
* Regular Expressions
* Exception Handling
* DataFrames
* JSON Handling

Core Data Science Concepts
* Data Cleaning
* Data Parsing
* Feature Extraction
* Embeddings
* Similarity Search
* Data Visualization

Core Streamlit Concepts
* Dashboard Layout
* Buttons
* Metrics
* Tables
* Charts
* Download Button
* Session State

Core ChromaDB Concepts
* Client
* Collection
* Embeddings
* IDs
* Metadata
* Query
* Semantic Retrieval

Core ReportLab Concepts
* SimpleDocTemplate
* Paragraph
* Spacer
* Table
* TableStyle
* PDF Styling
* Dynamic Content Generation

Skills Demonstrated
* Python Programming
* Cybersecurity
* Linux Log Analysis
* Artificial Intelligence
* Retrieval-Augmented Generation (RAG)
* Large Language Models
* Vector Databases
* Natural Language Processing
* Streamlit Dashboard Development
* PDF Report Generation
* Git
* GitHub

Learning Outcomes
This project demonstrates the integration of cybersecurity, artificial intelligence, natural language processing, vector databases, and data visualization into a practical security analysis platform. It provides hands-on experience with modern AI-assisted security workflows while reinforcing Python programming, log analysis, semantic search, and incident response concepts.

Author
Mani Karthik Garlapati
Computer Science Undergraduate
Focused on Cybersecurity, Artificial Intelligence, Cloud Computing, and Security Engineering.

License
This project is intended for educational and portfolio purposes.
