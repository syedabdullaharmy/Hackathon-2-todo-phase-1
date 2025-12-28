from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id: Unique identifier for the task.
        title: Short summary of the task.
        description: Detailed information about the task.
        completed: Status indicating if the task is finished.
        created_at: Timestamp when the task was created.
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Validates the task data after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty.")
        if len(self.title) > 200:
            raise ValueError("Title must be 200 characters or less.")
        if len(self.description) > 1000:
            raise ValueError("Description must be 1000 characters or less.")

    def to_dict(self) -> dict[str, Any]:
        """Converts the task object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
        }

    def __str__(self) -> str:
        """Returns a string representation of the task."""
        status = "✓" if self.completed else "✗"
        return f"[{status}] ID: {self.id} | {self.title}"
