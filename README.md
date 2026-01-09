# LangChain Basic API Agent

This repository contains a simple LangChain-based agent that consumes a public OpenAPI (Swagger) specification and generates artifacts such as automation scripts and test cases based on user input.  
It is intended as a hands-on example to understand how agents, tools, and prompts can be combined to solve practical problems.

> **Note:** At the moment, the agent only supports **publicly accessible Swagger/OpenAPI URLs**. Authentication-protected specs are not supported.

---

## 1. Setup Instructions

### Step 1: Clone this repo
```bash
git clone https://gitlab.endava.com/testing-accelerators/langchain-basic-api-agent.git
cd langchain-basic-api-agent
```

### Step 2: Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate  # For Windows
source .venv/bin/activate  # For MacOS / Linux
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create your `.env` file

Create an `.env` file in the project root path with this structure and credentials:

```env
OPENAI_API_KEY=<your_openai_api_key>
```
---

## 2. Running the Agent

The agent is executed from the command line and requires a **public Swagger/OpenAPI URL** as input.  
You can control which artifacts are generated using optional parameters (at least one)

### Generate test cases only
```bash
python -m agents.agent <swagger_url> -test_case
```

### Generate automation scripts only
```bash
python -m agents.agent <swagger_url> -automation
```

### Generate both test cases and automation scripts
```bash
python -m agents.agent <swagger_url> -test_case -automation
```

Example:
```bash
python -m agents.agent https://api.swaggerhub.com/apis/endava-adf/Auth-Demo/1.0.0 -automation -test_case
```

---

## 3. What the Agent Does

When executed, the agent will:

1. Download the OpenAPI/Swagger specification from the provided URL
2. Validate and normalize the specification
3. Analyze available endpoints and schemas
4. Generate artifacts based on the selected mode(s):
   - **Automation scripts** (saved to the `output/` folder)
   - **Test cases** (saved to the `output/` folder)

All steps are executed using LangChain tool calling and a structured agent prompt.

---

## 4. Output

Generated artifacts are saved locally under the `output/` directory:

```text
output/
├── tests.spec.js
└── test_cases.txt
```
