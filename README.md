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
