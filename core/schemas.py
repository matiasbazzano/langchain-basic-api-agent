from pydantic import BaseModel
from typing import Optional


class Artifacts(BaseModel):
    tests_spec_js: Optional[str] = None
    test_cases_txt: Optional[str] = None
