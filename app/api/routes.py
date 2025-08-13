from fastapi import APIRouter, status

from app.controllers.service import answer_question
from .schemas import AskRequest, AskResponse

router = APIRouter(prefix="", tags=["RAG"])


@router.post(
    path="/ask",
    response_model=AskResponse,
    status_code=status.HTTP_200_OK,
    description="Answer question",
)
async def ask(req: AskRequest):
    answer = await answer_question(req.question)

    return AskResponse(answer=answer)
