import pytest

from src.services.task_service import TaskService


@pytest.fixture
def service() -> TaskService:
    return TaskService()


def test_task_service_initialization(service: TaskService) -> None:
    assert len(service.get_all_tasks()) == 0


def test_add_task_valid(service: TaskService) -> None:
    task = service.add_task("Buy groceries", "Milk, Eggs, Bread")
    assert task.id == 1
    assert task.title == "Buy groceries"
    assert task.description == "Milk, Eggs, Bread"
    assert task.completed is False
    assert len(service.get_all_tasks()) == 1


def test_add_task_increments_id(service: TaskService) -> None:
    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2")
    assert task1.id == 1
    assert task2.id == 2


def test_get_task_existing(service: TaskService) -> None:
    service.add_task("Test")
    task = service.get_task(1)
    assert task is not None
    assert task.id == 1


def test_get_task_non_existing(service: TaskService) -> None:
    assert service.get_task(99) is None


def test_get_all_tasks_sorted_by_id(service: TaskService) -> None:
    service.add_task("Task B")
    service.add_task("Task A")
    tasks = service.get_all_tasks()
    assert tasks[0].id == 1
    assert tasks[1].id == 2


def test_update_task_success(service: TaskService) -> None:
    service.add_task("Old Title", "Old Desc")
    updated_task = service.update_task(1, title="New Title", description="New Desc")
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Desc"

    # Verify in storage
    stored_task = service.get_task(1)
    assert stored_task.title == "New Title"


def test_update_task_partial(service: TaskService) -> None:
    service.add_task("Title", "Desc")
    updated_task = service.update_task(1, title="Newer Title")
    assert updated_task.title == "Newer Title"
    assert updated_task.description == "Desc"


def test_update_task_not_found(service: TaskService) -> None:
    with pytest.raises(ValueError, match="Task with ID 99 not found."):
        service.update_task(99, title="Whatever")


def test_delete_task_success(service: TaskService) -> None:
    service.add_task("To Delete")
    assert service.delete_task(1) is True
    assert len(service.get_all_tasks()) == 0


def test_delete_task_not_found(service: TaskService) -> None:
    assert service.delete_task(1) is False


def test_toggle_status(service: TaskService) -> None:
    service.add_task("Incomplete Task")
    task = service.toggle_status(1)
    assert task.completed is True

    task = service.toggle_status(1)
    assert task.completed is False


def test_toggle_status_not_found(service: TaskService) -> None:
    with pytest.raises(ValueError, match="Task with ID 99 not found."):
        service.toggle_status(99)
