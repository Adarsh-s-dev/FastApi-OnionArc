from datetime import datetime, timezone
from typing import Optional, TypeVar, Type
from pydantic import Field
from Domain.Core.entity import AuditedEntity, Entity

MAI = TypeVar("MAI", bound="MongoAuditItem")


class MongoAuditItem(Entity):
    CreatedAt: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc))
    CreatedBy: str = Field(default="Not Set")
    TableName: Optional[str] = None
    OldValue: Optional[dict] = Field(default=None)
    NewValue: Optional[dict] = Field(default=None)
    EntityId: Optional[str] = None
    Action: Optional[str] = None

    @classmethod
    def create_insert_audit(cls: Type[MAI], new_value: AuditedEntity) -> MAI:
        audit_item = cls.new({})
        audit_item.TableName = new_value.__class__.__name__
        audit_item.EntityId = new_value.id
        audit_item.NewValue = new_value.to_dict()
        audit_item.Action = "Insert"
        return audit_item

    @classmethod
    def create_update_audit(cls: Type[MAI], new_value: AuditedEntity, old_value: AuditedEntity) -> MAI:
        audit_item = cls.new({})
        audit_item.TableName = new_value.__class__.__name__
        audit_item.EntityId = new_value.id
        audit_item.NewValue = new_value.to_dict()
        audit_item.OldValue = old_value.to_dict()
        audit_item.Action = "Update"
        return audit_item

    @classmethod
    def create_delete_audit(cls: Type[MAI], old_value: AuditedEntity) -> MAI:
        audit_item = cls.new({})
        audit_item.TableName = old_value.__class__.__name__
        audit_item.EntityId = old_value.id
        audit_item.NewValue = None
        audit_item.OldValue = old_value.to_dict()
        audit_item.Action = "Update"
        return audit_item
