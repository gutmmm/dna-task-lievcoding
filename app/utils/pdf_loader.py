import asyncio

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

from app.utils.config import settings


async def load_document(file_path: str = "data/documents/document1.pdf"):
    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings(openai_api_key=settings.openai_api_key))


