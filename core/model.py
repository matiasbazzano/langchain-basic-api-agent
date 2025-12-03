from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from core.model_versions import DEFAULT_MODEL_VERSION

load_dotenv()

LLM = ChatOpenAI(model=DEFAULT_MODEL_VERSION)
