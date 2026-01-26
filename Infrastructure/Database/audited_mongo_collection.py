from pymongo.collection import Collection

from Domain.Core.entity import AuditedEntity
from Infrastructure.Database.audit_item import MongoAuditItem


class AuditedMongoCollection:

    def __init__(self, collection: Collection, audited_collection: Collection) -> None:
        self.collection = collection
        self.audited_collection = audited_collection

    def insert(self, entity: AuditedEntity):
        audit = MongoAuditItem.create_insert_audit(entity)
        self.collection.insert_one(entity.to_dict())
        self.audited_collection.insert_one(audit.to_dict())
        pass

    def insert_many(self, entities: list[AuditedEntity]):
        pass

    def update(self, entity: AuditedEntity):
        pass

    def update_may(self, entities: list[AuditedEntity]):
        pass

    def delete(self, id: str):
        pass

    def delete_many(self, flter: dict):
        pass

    def get(self):
        pass
