from Domain.Entities.test_entity import TestEntity
from Infrastructure.Repositories.test_repo import TestRepo


class TestService:
    @staticmethod
    def create_test(name: str) -> str:
        entity = TestEntity.new({"Name": name})
        return TestRepo.create(entity)

    @staticmethod
    def get_item(id: str):
        return TestRepo.get_item(id)

    @staticmethod
    def get_all():
        return TestRepo.get_all()
