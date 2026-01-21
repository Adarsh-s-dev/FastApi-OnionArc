from fastapi import APIRouter

router = APIRouter(tags=["test"], prefix="/test")


@router.get("/get")
def get():
    return {"Message": "Test Success"}
