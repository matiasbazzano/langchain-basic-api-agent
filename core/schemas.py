from pydantic import BaseModel


class Artifacts(BaseModel):
    tests_spec_js: str
    test_cases_txt: str
