# General information

This is an application template which should be a starting point of implementing simple solution for processing **multiple** PDF
files with use of artificial intelligence.

Project exposes endpoint:

- `/ask` that is supposed to be an input for user question related to aforementioned file

The template is equipped with some tools to be used in the implementation. These tools are not **mandatory** though.

- FastAPI
- LangChain
- OpenAI

# Tasks

## Task 1:

- Make a code review of the template

## Task 2:

- Add RAG using example PDF's.

- Add implementation for client's question processing in `ask/` endpoint.

---

## Quick-start

```bash
# 1. ensure Python3.12 is installed

# 2a. create enviroment and install dependencies  # UNIX
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements.dev.txt

# 2b. create enviroment and install dependencies  # WINDOWS
python3.12 -m venv .venv
./.venv/Scripts/Activate.bat  # cmd
./.venv/Scripts/Activate.ps1  # powershell
pip install -r requirements.txt
pip install -r requirements.dev.txt

# 3. put your OpenAI key in .env file (file should be located in the repo main folder)
OPENAI_API_KEY="sk-..."

# 4. run the API
python run.py
```

## Testing guideline - example questions and answers

Use the following test cases to verify the initial behaviour of the `/ask` endpoint. For each case, copy-paste the corresponding `curl` command into your terminal.

1. **Who has produced the report?**

   - Expected answer: European Lab Project Task Force (PTF) / Workstream A5 (also called “Stream A5” in this report) of the PTF
   - Reference: Page 3 — Executive Summary → STREAM OBJECTIVES
   - Command:
     ```bash
     curl -X POST http://localhost:8000/ask \
          -H "Content-Type: application/json" \
          -d '{"question": "Who has produced the report?"}'
     ```

2. **How many salient points does the report define?**

   - Expected answer: Six salient points (also called major conclusions)
   - Reference: Page 3 — Executive Summary → SYNTHESIS OF THE ASSESSMENT REPORT
   - Command:
     ```bash
     curl -X POST http://localhost:8000/ask \
          -H "Content-Type: application/json" \
          -d '{"question": "How many salient points does the report define?"}'
     ```

3. **What objectives did Stream A5 focus on after the PTF-NFRS meeting on 11 September 2020?**

   - Expected answer:
     a) Conduct a comprehensive analysis of all non-financial reporting requirements applicable to Financial Institutions (link to be made with A1)
     b) Assess whether direct impacts are material for asset managers/owners, banks and insurance undertakings, and require specific non-financial reporting provisions
     c) Identify specific indirect impacts of lending/financing activities, asset management and insurance and the related non-financial reporting challenges currently faced by financial institutions
     d) Assess necessary steps to give sustainable finance appropriate data
   - Reference: Page 8 — INTRODUCTION AND OBJECTIVES
   - Note: These don't have to match word for word. It's enough to point to the at least some specific information from the reference. There might be more objectives in the document.
   - Command:
     ```bash
     curl -X POST http://localhost:8000/ask \
          -H "Content-Type: application/json" \
          -d '{"question": "What objectives did Stream A5 focus on after the PTF-NFRS meeting on September 11, 2020?"}'
     ```

4. **Are asset managers with fewer than 500 employees required to report through NFRD?**

   - Expected answer: No
   - Reference: Page 30 — point 86 (lines 4-5)
   - Command:
     ```bash
     curl -X POST http://localhost:8000/ask \
          -H "Content-Type: application/json" \
          -d '{"question": "Are asset managers with less than 500 employees required to report through NFRD?"}'
     ```

5. **When shall the level 1 of the SFDR regulation enter into application?**
   - Expected answer: 1 March 2021
   - Reference: Page 33 — point 96
   - Command:
     ```bash
     curl -X POST http://localhost:8000/ask \
          -H "Content-Type: application/json" \
          -d '{"question": "When shall the level 1 of the SFDR regulation enter into application?"}'
     ```
