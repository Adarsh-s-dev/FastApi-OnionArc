from typing import Optional
from Domain.Core.entity import Entity, IdempotentMixin


class TestEntity(Entity, IdempotentMixin):
    Name: str
