from datetime import datetime, timezone
import uuid
from pydantic import BaseModel, Field
from typing import Optional, TypeVar, Type
T = TypeVar("T", bound="BaseEntity")
E = TypeVar("E", bound="Entity")
AE = TypeVar("AE", bound="AuditedEntity")


class BaseEntity(BaseModel):
    @classmethod
    def from_dict(cls: Type[T], v: dict) -> T:
        return cls.model_validate(v)

    def to_dict(self):
        return self.model_dump(by_alias=True)


class Entity(BaseEntity):
    id: Optional[str] = Field(alias="_id", default=None)

    @classmethod
    def new(cls: Type[E], v: dict) -> E:
        data = cls.from_dict(v)
        data.id = str(uuid.uuid4())
        return data


class IdempotentMixin:
    IdempotentKey: Optional[str] = None


class AuditedEntity(Entity):

    # These Fields Are Marked as Optional, But Will and Should be
    # Auto Asigned During Insert/Update Operation to DB
    CreatedUser: Optional[str] = None
    CreatedAt: Optional[datetime] = None

    LastModifiedBy: Optional[str] = None
    LastModifiedAt: Optional[datetime] = None

    def set_create_audit(self):
        self.CreatedAt = datetime.now(tz=timezone.utc)
        self.CreatedUser = "Not set"

    def set_update_audit(self, old_entity: Type[AE]):
        self.CreatedAt = old_entity.CreatedAt
        self.CreatedUser = old_entity.CreatedUser

        self.LastModifiedAt = datetime.now(tz=timezone.utc)
        self.LastModifiedBy = "Not Set"
