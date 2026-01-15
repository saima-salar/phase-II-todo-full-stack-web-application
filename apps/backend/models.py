from sqlmodel import SQLModel, Field, Column, DateTime
from sqlalchemy import Integer, String
from typing import Optional, List
from datetime import datetime
from enum import Enum

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(sa_column=Column(Integer, nullable=False))
    title: str = Field(nullable=False)
    description: Optional[str] = Field(default=None)
    completed: bool = Field(default=False)
    priority: str = Field(default="medium", sa_column=Column(String, nullable=False))  # low, medium, high
    tags: Optional[str] = Field(default=None, sa_column=Column(String))  # JSON string of tags
    due_date: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=None)
    )
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    )
    # Advanced features
    is_recurring: bool = Field(default=False)
    recurrence_pattern: Optional[str] = Field(default=None, sa_column=Column(String))  # daily, weekly, monthly, yearly
    parent_task_id: Optional[int] = Field(default=None, foreign_key="task.id")  # For task dependencies
    estimated_duration: Optional[int] = Field(default=None)  # Estimated time in minutes
    actual_duration: Optional[int] = Field(default=None)  # Actual time spent in minutes
    reminder_enabled: bool = Field(default=False)
    reminder_time: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=None)
    )
    shared_with: Optional[str] = Field(default=None, sa_column=Column(String))  # JSON string of user IDs

# User model for authentication
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    )