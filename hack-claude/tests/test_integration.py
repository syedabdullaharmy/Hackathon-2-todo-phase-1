import pytest

from src.services.task_service import TaskService


def test_complete_task_lifecycle() -> None:
    """Tests a full workflow from creation to deletion."""
    service = TaskService()

    # 1. Add Task
    task = service.add_task("Life Cycle Task", "Testing full flow")
    assert task.id == 1
    assert task.title == "Life Cycle Task"

    # 2. View Task
    retrieved = service.get_task(1)
    assert retrieved is not None
    assert retrieved.title == "Life Cycle Task"

    # 3. Update Task
    updated = service.update_task(1, title="Updated Task")
    assert updated.title == "Updated Task"
    assert updated.description == "Testing full flow"

    # 4. Toggle Status
    toggled = service.toggle_status(1)
    assert toggled.completed is True

    # 5. Delete Task
    deleted = service.delete_task(1)
    assert deleted is True
    assert service.get_task(1) is None


def test_multiple_tasks_workflow() -> None:
    """Tests managing multiple tasks simultaneously."""
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")
    service.add_task("Task 3")

    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 3
    assert all_tasks[0].id == 1
    assert all_tasks[1].id == 2
    assert all_tasks[2].id == 3

    service.delete_task(2)
    remaining = service.get_all_tasks()
    assert len(remaining) == 2
    assert remaining[0].id == 1
    assert remaining[1].id == 3


def test_error_handling_workflow() -> None:
    """Tests service responses to invalid requests."""
    service = TaskService()
    service.add_task("Valid Task")

    with pytest.raises(ValueError, match="Task with ID 99 not found."):
        service.update_task(99, title="Broken")

    with pytest.raises(ValueError, match="Task with ID 99 not found."):
        service.toggle_status(99)

    assert service.delete_task(99) is False


def test_empty_state_workflow() -> None:
    """Tests the service behavior with no data."""
    service = TaskService()
    assert len(service.get_all_tasks()) == 0
    assert service.get_task(1) is None
