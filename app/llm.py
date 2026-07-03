from functools import lru_cache

from langchain_openai import ChatOpenAI
from app.config import get_settings


@lru_cache(maxsize=1)
def get_llm() -> ChatOpenAI:
    settings = get_settings()

    return ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
        temperature=0,
        timeout=30,
        max_retries=2,
    )