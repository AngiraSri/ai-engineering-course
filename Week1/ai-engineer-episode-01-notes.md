# Free AI Engineer Course (8 Weeks)
## Episode 01: Course Intro + Tech Stack Setup (Notes)

**Instructor:** Pratyush Narain (IIT Graduate, SDE-2 at Akamai)  
**Course Style:** Reverse-engineered from modern AI Engineer interview questions. Completely free, production-focused, and practical.

---

## 1. Course Philosophy & Who It Is For

### The Problem with Current AI Courses
The instructor identifies two extremes in existing AI education:
1. **The Pure Math/Research Extreme:** Heavy on Transformer math, backpropagation, and PyTorch internals. Good for PhDs or researchers at Anthropic/OpenAI, but overwhelming and less practical for day-to-day software and AI application engineering.
2. **The "Wrapper" Tutorial Extreme:** 10-minute videos showing "how to build a chatbot/agent" using simple API wrapper calls. While fun, these tutorials do not teach underlying architecture, system internals, or real troubleshooting, making them useless for interviews.

### The Reverse-Engineered Approach
This course is built backwards from **actual technical interview questions** asked by companies hiring AI Engineers, Agentic Engineers, and AI Deployment Engineers. It focuses only on the concepts, tools, and practices you actually need to build production-level software and pass interviews.

### Target Audience
* **College Students:** Even those with no prior AI or Data Structures & Algorithms (DSA) background.
* **Working Professionals (1-3 Years Experience):** Looking to switch to AI-related domains or take on AI projects in service-based companies.
* **Not for:** Those aiming for PhDs, heavy machine learning math, or deep research positions.

---

## 2. Prerequisites & Syllabus

### Prerequisites
* A laptop (even a basic 4GB/8GB RAM machine is fine).
* Internet connection and a physical notebook for taking notes.
* **Basic Python Knowledge:** Understanding variables, lists, tuples, and dictionaries.
  * *Recommendation:* Watch the Python segment of the instructor’s "DSA Basics in 4 Days" playlist (takes about 1 hour).
  * Alternatively, learn on the go as concepts are introduced.

### Course Roadmap (8 Weeks / 40-45 Episodes)
By the end of this course, you will cover:
* **LLM Fundamentals**
* **RAG (Retrieval-Augmented Generation)** & Document Q&A
* **AI Agents & Autonomous Research Agents**
* **LangGraph** (agent orchestration)
* **MCP (Model Context Protocol) Servers**
* **AI Observability & Evaluation**
* **Deployment & Fine-tuning**
* **Capstone Project:** A production-grade, full-stack, end-to-end AI project mimicking industry standards.

---

## 3. Why Cloud APIs Over Local Models (Ollama)?
Many courses rely on **Ollama** to run models locally. However:
* Ollama runs on your local machine and requires heavy RAM and high-end GPUs (e.g., NVIDIA RTX graphics cards).
* For students on budget 4GB/8GB RAM laptops, Ollama will lag or fail to run.
* **The Solution:** This course uses **Groq Cloud** for fast LLM inference and **Qdrant Cloud** for vector databases. Both have generous free tiers, run entirely on the cloud, require no credit cards, and are extremely easy to set up via API keys.

---

## 4. Tech Stack Setup Guide (Step-by-Step)

The instructor demonstrates the installation on Windows (which 90% of students use), but the steps are essentially identical on macOS/Linux.

### Step A: Python Installation
1. Download Python (the video shows 3.14.6/3.12 versions) from the official Python website.
2. Run the installer and **ensure "Add Python to PATH" is checked** (critical for Windows).
3. Verify the installation in your terminal (PowerShell/Command Prompt):
   ```bash
   python --version
   ```

### Step B: Visual Studio Code (VS Code) & Extensions
1. Download and install VS Code.
2. Install the following official Microsoft extensions:
   * **Python** (by Microsoft)
   * **Pylance** (by Microsoft)
   * **Jupyter** (by Microsoft)

### Step C: Git Installation
1. Download and install Git. Keep all default configuration options checked.
2. Verify installation:
   ```bash
   git --version
   ```
3. Set your global Git credentials in the terminal:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
4. Check your configured credentials:
   ```bash
   git config --global --list
   ```

### Step D: UV Package Manager Installation
`uv` is an extremely fast package manager designed as a modern replacement for `pip`.
1. Run the installation script provided in the course resources:
   ```powershell
   # For Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
2. Restart your terminal and verify the installation:
   ```bash
   uv --version
   ```

### Step E: Groq Cloud API Setup (LLM Inference)
1. Go to [Groq Cloud Console](https://console.groq.com/).
2. Log in using Google/Gmail (no credit card required).
3. Navigate to **API Keys** on the sidebar.
4. Click **Create API Key**, name it (e.g., `padho-with-pratyush`), and copy the key immediately. 
   * *Note: Keep this key secure and never share it publicly!*

### Step F: Qdrant Cloud Setup (Vector Database)
1. Go to [Qdrant Cloud](https://cloud.qdrant.io/).
2. Log in using Gmail and skip any onboarding tutorials.
3. Click **Create Free Cluster** (generates a free AWS-hosted vector database instance).
4. Copy both the **Cluster Endpoint (URL)** and the **API Key** immediately to a safe notepad.

---

## 5. Project Directory & Environment Variables

To protect your API credentials and structure your workspace, set up your project directory:

1. Create a workspace folder on your machine (e.g., inside your user folder):
   ```bash
   mkdir padho-with-pratyush
   cd padho-with-pratyush
   ```
2. Create an environment file named `.env` using Notepad/VS Code inside this directory:
   ```bash
   notepad .env
   ```
3. Copy and paste your credentials into the `.env` file **exactly** like this (replace with your actual secret keys, no spaces, no quotes):
   ```env
   GROQ_API_KEY=gsk_your_actual_groq_api_key_here
   QDRANT_URL=https://your-qdrant-cluster-endpoint.aws.qdrant.io
   QDRANT_API_KEY=your_actual_qdrant_api_key_here
   ```
4. Create a folder for the first week:
   ```bash
   mkdir week-1
   ```
5. Open the main folder in VS Code:
   ```bash
   code .
   ```

---

## 6. Verification Checklist
Make sure you can run these commands from your VS Code terminal before starting Episode 02:
- [ ] `python --version` (Prints your Python version)
- [ ] `uv --version` (Prints `uv` package manager version)
- [ ] `git --version` (Prints Git version)
- [ ] `.env` file contains correct, unquoted API keys for Groq and Qdrant.
