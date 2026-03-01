from fastapi import APIRouter, Header

from Application.Services.test_service import TestService

router = APIRouter(tags=["test"], prefix="/test")


@router.post("/create")
def create(name: str):
    return TestService.create_test(name)


@router.get("/get")
def get(id: str):
    return TestService.get_item(id)


@router.get("/getall")
def get_all():
    return TestService.get_all()


@router.get("/test")
def test(x: str):
    return {"message": f"Received  value: {x}"}
