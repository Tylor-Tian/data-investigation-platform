from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

class Investigation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    created_by: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "active"
    tags: List[str] = []
