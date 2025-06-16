from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Project(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True, nullable=False)
    repo_path: str
    current_version: Optional[uuid.UUID] = Field(default=None)  # References document_versions
    project_metadata: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    created_by: str = Field(nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_by: str = Field(nullable=False)
