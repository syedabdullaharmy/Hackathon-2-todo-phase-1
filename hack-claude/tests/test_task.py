from datetime import datetime

import pytest

from src.models.task import Task


def test_task_creation_valid() -> None:
    """Tests creating a task with valid data."""
    now = datetime.now()
    task = Task(id=1, title="Test Task", description="Test Description", created_at=now)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False
    assert task.created_at == now


def test_task_creation_empty_title_raises_error() -> None:
    """Tests that an empty title raises a ValueError."""
    with pytest.raises(ValueError, match="Title cannot be empty."):
        Task(id=1, title="")
    with pytest.raises(ValueError, match="Title cannot be empty."):
        Task(id=1, title="   ")


def test_task_creation_title_too_long_raises_error() -> None:
    """Tests that a title longer than 200 characters raises a ValueError."""
    with pytest.raises(ValueError, match="Title must be 200 characters or less."):
        Task(id=1, title="a" * 201)


def test_task_creation_description_too_long_raises_error() -> None:
    """Tests that a description longer than 1000 characters raises a ValueError."""
    with pytest.raises(
        ValueError, match="Description must be 1000 characters or less."
    ):
        Task(id=1, title="Valid Title", description="a" * 1001)


def test_task_to_dict() -> None:
    """Tests the to_dict method."""
    now = datetime.now()
    task = Task(id=1, title="Test Task", created_at=now)
    task_dict = task.to_dict()
    assert task_dict["id"] == 1
    assert task_dict["title"] == "Test Task"
    assert task_dict["description"] == ""
    assert task_dict["completed"] is False
    assert task_dict["created_at"] == now.isoformat()


def test_task_str_representation() -> None:
    """Tests the __str__ representation."""
    task_incomplete = Task(id=1, title="Test Task", completed=False)
    assert str(task_incomplete) == "[✗] ID: 1 | Test Task"

    task_complete = Task(id=2, title="Completed Task", completed=True)
    assert str(task_complete) == "[✓] ID: 2 | Completed Task"


def test_task_defaults() -> None:
    """Tests the default values for description and completed status."""
    task = Task(id=1, title="Default Task")
    assert task.description == ""
    assert task.completed is False
    assert isinstance(task.created_at, datetime)
