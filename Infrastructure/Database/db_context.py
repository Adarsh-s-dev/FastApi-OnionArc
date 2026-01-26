from pymongo import MongoClient, collection
from Infrastructure.Database.audited_mongo_collection import AuditedMongoCollection
from config import CONFIG
from Domain.Core.entity import AuditedEntity
# from typing import Type


class DbContext:
    _client: MongoClient | None = None

    @classmethod
    def _get_client(cls) -> MongoClient:
        if cls._client is None:
            connection_string = CONFIG["DataBase"]["MongoConnectionString"]
            cls._client = MongoClient(connection_string)
        return cls._client

    @classmethod
    def get_database(cls):
        db_name = CONFIG["DataBase"]["DatabaseName"]
        return cls._get_client()[db_name]

    @classmethod
    def get_collection(cls, name: str) -> collection.Collection:
        """
        Avoid Using This No Audit No Check etc

        :param cls: Description
        :param name: Description
        :type name: str
        """
        collection = cls.get_database()[name]
        return collection

    @classmethod
    def get_audited_collection(cls, entity_cls: type[AuditedEntity]) -> AuditedMongoCollection:
        audit_collection = cls.get_collection("Audit")
        collection = cls.get_collection(entity_cls.__name__)
        audited_collection = AuditedMongoCollection(
            collection, audit_collection)
        return audited_collection
