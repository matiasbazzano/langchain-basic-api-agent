import json, requests, yaml, os
from openapi_spec_validator import validate_spec
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from core.schemas import Artifacts
from core.models import DEFAULT_MODEL
from core.prompts import GENERATE_ARTIFACTS_TOOL_PROMPT


@tool("fetch_openapi_spec")
def fetch_openapi_spec(url: str) -> str:
    """Download and validate an OpenAPI/Swagger spec (JSON or YAML) and return it as normalized JSON."""
    r = requests.get(url, timeout=15)
    raw = r.text
    try:
        spec = json.loads(raw)
    except Exception:
        spec = yaml.safe_load(raw)
    validate_spec(spec)
    return json.dumps({"spec_json": json.dumps(spec)})


@tool("generate_artifacts")
def generate_artifacts(spec_json: str, modes: dict | None = None) -> str:
    """Generate automation and/or test case artifacts from an OpenAPI spec JSON."""
    modes = modes or {}
    if not (modes.get("automation") or modes.get("test_case")):
        return json.dumps({"error": "No modes selected."})

    llm = ChatOpenAI(model=DEFAULT_MODEL).with_structured_output(
        Artifacts, method="function_calling"
    )
    out: Artifacts = (GENERATE_ARTIFACTS_TOOL_PROMPT | llm).invoke(
        {"json": spec_json, "modes": modes}
    )

    result = {}
    if modes.get("automation"):
        result["tests_spec_js"] = out.tests_spec_js.strip()
    if modes.get("test_case"):
        result["test_cases_txt"] = out.test_cases_txt.strip()

    return json.dumps(result)


@tool("save_automation_artifact")
def save_automation_artifact(content: str, outdir: str = "output") -> str:
    """Save JavaScript test specs to 'output/tests.spec.js'."""
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "tests.spec.js")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return json.dumps({"path": path})


@tool("save_test_case_artifact")
def save_test_case_artifact(content: str, outdir: str = "output") -> str:
    """Save plain-text test cases to 'output/test_cases.txt'."""
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "test_cases.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return json.dumps({"path": path})
