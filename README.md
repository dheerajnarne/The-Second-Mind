# The Second Mind

## Bosch x Tinkerers’ Lab IIT Hyderabad Hackathon – The Second Mind

## Project Overview

The **Research Idea Generation and Evolution System** is designed to automate and enhance the process of generating, evaluating, and refining research ideas. The system leverages **state-of-the-art NLP models, semantic search, and a structured workflow** to create a robust and interactive tool for researchers, innovators, and decision-makers.

---

## Approach

### 1. **Modular and Scalable Architecture**
- Built with a **modular** approach to ensure scalability and maintainability.
- Key system components:
  - **Generation Agent** – Creates new research ideas based on user queries.
  - **Ranking Agent** – Evaluates ideas using predefined criteria.
  - **Evolution Agent** – Refines ideas based on ranking feedback.
  - **Memory Agent** – Stores past ideas and queries for retrieval using semantic search.

### 2. **Leveraging Pre-trained Language Models**
- Uses **T5 Flan** from Hugging Face for:
  - Idea generation
  - Idea ranking and refinement
  - Handling complex prompts and multi-criteria evaluation

### 3. **Semantic Memory and Retrieval**
- Powered by **FAISS (Facebook AI Similarity Search)** and **Sentence Transformers**.
- Enables retrieval of past research ideas based on semantic similarity.

---

## System Components

### **1. MemoryAgent (Retrieves & Stores Past Ideas)**
- Converts research queries into **embeddings** using `SentenceTransformer("all-MiniLM-L6-v2")`.
- Uses **FAISS IndexFlatL2** for fast retrieval.
- Links new ideas with **previous research trends** for context-aware suggestions.

### **2. GenerationAgent (Creates New Ideas)**
- Uses **Pythia 2.8B** to generate structured research ideas.
- Ensures ideas are:
  - **Problem-solving** (addresses real-world challenges)
  - **Feasible** (achievable within five years)
  - **Innovative** (integrates technology or sustainability)

### **3. RankingEvolutionAgent (Evaluates & Refines Ideas)**
- Scores ideas on a **1-10 scale** based on:
  - **Feasibility**
  - **Innovation**
  - **Impact**
- Uses **Pythia 2.8B** to refine low-scoring ideas by improving feasibility, innovation, and real-world impact.

### **4. ReflectionAgent (Ensures Coherence & Validity)**
- Fetches **real-time research trends, cost estimates, and feasibility data** from the web.
- Cross-checks generated ideas for **accuracy** and **logical consistency**.
- Provides feedback on **potential challenges** in the idea.

### **5. ProximityAgent (Links to Past Interactions)**
- Searches **MemoryAgent** for **related past research topics**.
- Identifies **patterns** and **recurring trends** from well-ranked ideas.
- Suggests **modifications** based on previous successful implementations.

### **6. MetaReviewAgent (Optimizes Workflow & Efficiency)**
- Evaluates **processing time, agent interactions, and execution bottlenecks**.
- Suggests **workflow improvements** for better efficiency.
- Ensures optimal collaboration between agents.

### **7. SupervisorAgent (Orchestrates the Entire Process)**
- Manages **idea generation, ranking, validation, and refinement**.
- Coordinates agent tasks dynamically for **efficiency**.
- Generates a **structured research execution plan**, including:
  - **Feasibility Analysis** (technical & resource constraints)
  - **Prototyping & Testing** (validating the idea)
  - **Scaling & Implementation** (real-world deployment)
- Calls **MetaReviewAgent** to refine the workflow for future iterations.
- Outputs a **final research report** with a refined idea, ranking feedback, and an execution roadmap.

---

## ✅ Milestone Completion Status

### **☑ Milestone 1: Build Core Agent System and Memory**
✔ Goal Achieved: **Implemented Supervisor, specialized agents, and basic storage/retrieval.**  
✔ Tasks Completed:
- Supervisor agent assigns tasks.
- Core agents (Generation, Reflection, Ranking, Evolution, Proximity, MetaReview) are functional.
- Basic **storage/retrieval** mechanism in place.
✔ Deliverable: **Supervisor successfully calls agents and stores/recalls test inputs/outputs.**

---

### **☑ Milestone 2: Add Web Extraction and Agent Collaboration**
✔ Goal Achieved: **Integrated real-time web data and linked agents for collaboration.**  
✔ Tasks Completed:
- Implemented **web scraping/API calls** for real-time research data.
- Enhanced agents to **utilize web data** for scoring and refinement.
- Supervisor orchestrates agent interactions **(Generation → Reflection → Ranking)**.
✔ Deliverable: **System processes input using web data and agent handoffs.**

---

### **☑ Milestone 3: Enable Iteration and Demo Prep**
✔ Goal Achieved: **Implemented iterative refinement and finalized prototype.**  
✔ Tasks Completed:
- **Feedback loop** established for continuous idea improvement.
- **Multiple refinement cycles** executed, demonstrating enhancements.
- Demo prepared with **console output and design documentation**.
✔ Deliverable: **System successfully processes, stores, and iterates on ideas for optimization.**

✅ **All Milestones Achieved!**

---

## 🔄 WorkFlow

1. **User Inputs a Research Query**
2. **MemoryAgent Retrieves Past Similar Ideas**
3. **GenerationAgent Creates New Research Ideas**
4. **ReflectionAgent Ensures Relevance & Validity**
5. **RankingEvolutionAgent Evaluates & Refines Ideas**
6. **ProximityAgent Links Ideas to Past Interactions**
7. **MetaReviewAgent Optimizes the Workflow**
8. **SupervisorAgent Orchestrates the Process & Outputs Final Report**
