from Domain.Entities.test_entity import TestEntity
from Infrastructure.Database.db_context import DbContext


class TestRepo:

    @staticmethod
    def create(item: TestEntity) -> str:
        col = DbContext.get_collection("TestEntity")
        result = col.insert_one(item.to_dict())
        return result.inserted_id

    @staticmethod
    def get_item(id: str):
        col = DbContext.get_collection("TestEntity")
        result = col.find_one({"_id": id})
        return result

    @staticmethod
    def get_all():
        col = DbContext.get_collection("TestEntity")
        result = col.find({})
        return list(result)
