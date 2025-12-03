from langchain_openai import ChatOpenAI
from core.model_versions import DEFAULT_MODEL_VERSION

LLM = ChatOpenAI(model=DEFAULT_MODEL_VERSION)
