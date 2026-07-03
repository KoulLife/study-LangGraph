import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()

@dataclass(frozen=True)
class Settings:
    llm_base_url: str
    llm_model: str
    llm_api_key: str


def get_settings() -> Settings:
    llm_base_url = os.getenv("LLM_BASE_URL")
    llm_model = os.getenv("LLM_MODEL")
    llm_api_key = os.getenv("LLM_API_KEY")

    if not llm_base_url:
        raise ValueError("LLM_BASE_URL is missing")

    if not llm_model:
        raise ValueError("LLM_MODEL is missing")

    if not llm_api_key:
        raise ValueError("LLM_API_KEY is missing")

    return Settings(
        llm_base_url=llm_base_url,
        llm_model=llm_model,
        llm_api_key=llm_api_key,
    )

