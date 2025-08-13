from app.api.schemas import AskResponse
from app.utils.pdf_loader import load_document
from app.utils.llm import call_llm




async def answer_question(input: str) -> AskResponse:
    """Run LLM for `question` using RAG.

    Parameters
    ----------
    question
        query question

    Returns
    -------
    result
        LLM response for `question`
    """
    vector_store = await load_document()
    context = vector_store.similarity_search(input, k=2)
    response = await call_llm(input, context)
    print(response)
    return response.content


    