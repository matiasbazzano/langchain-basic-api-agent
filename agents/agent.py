import json
from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor
from utils.utils import parse_args
from core.model import LLM
from core.prompts import AGENT_PROMPT
from core.tools import (
    fetch_openapi_spec,
    generate_artifacts,
    save_automation_artifact,
    save_test_case_artifact,
)

load_dotenv()


def run_agent(url: str, want_automation: bool, want_test_case: bool):
    tools = [
        fetch_openapi_spec,
        generate_artifacts,
        save_automation_artifact,
        save_test_case_artifact,
    ]

    agent = create_tool_calling_agent(llm=LLM, tools=tools, prompt=AGENT_PROMPT)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    modes = {"automation": want_automation, "test_case": want_test_case}
    result = executor.invoke({"input": json.dumps({"url": url, "modes": modes})})
    return result


def main():
    args = parse_args()
    result = run_agent(args.url, args.automation, args.test_case)
    print("\nAgent finished: ", result)


if __name__ == "__main__":
    main()
