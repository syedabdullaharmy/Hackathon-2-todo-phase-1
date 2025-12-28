from unittest.mock import MagicMock, patch

import pytest

from src.models.task import Task
from src.services.task_service import TaskService
from src.ui.cli import TodoCLI


@pytest.fixture
def mock_service() -> MagicMock:
    return MagicMock(spec=TaskService)


@pytest.fixture
def cli(mock_service: MagicMock) -> TodoCLI:
    return TodoCLI(mock_service)


def test_cli_initialization(cli: TodoCLI) -> None:
    assert isinstance(cli.task_service, MagicMock)


def test_display_menu(cli: TodoCLI, capsys: pytest.CaptureFixture[str]) -> None:
    cli.display_menu()
    captured = capsys.readouterr()
    assert "=== Todo Application ===" in captured.out
    assert "1. Add Task" in captured.out
    assert "6. Exit" in captured.out


def test_display_tasks_empty(cli: TodoCLI, capsys: pytest.CaptureFixture[str]) -> None:
    cli.display_tasks([])
    captured = capsys.readouterr()
    assert "No tasks found." in captured.out


def test_display_tasks_not_empty(
    cli: TodoCLI, capsys: pytest.CaptureFixture[str]
) -> None:
    task = Task(id=1, title="Test Task")
    cli.display_tasks([task])
    captured = capsys.readouterr()
    assert "[✗] ID: 1 | Test Task" in captured.out


@patch("builtins.input", side_effect=["My Task", "My Description"])
def test_handle_add_task_success(
    mock_input: MagicMock,
    cli: TodoCLI,
    mock_service: MagicMock,
    capsys: pytest.CaptureFixture[str],
) -> None:
    mock_service.add_task.return_value = Task(
        id=1, title="My Task", description="My Description"
    )
    cli.handle_add_task()
    captured = capsys.readouterr()
    assert "Success: Task added with ID 1" in captured.out
    mock_service.add_task.assert_called_once_with("My Task", "My Description")


@patch("builtins.input", side_effect=["1"])
def test_handle_view_tasks(
    mock_input: MagicMock,
    cli: TodoCLI,
    mock_service: MagicMock,
    capsys: pytest.CaptureFixture[str],
) -> None:
    task = Task(id=1, title="View Me")
    mock_service.get_all_tasks.return_value = [task]
    cli.handle_view_tasks()
    captured = capsys.readouterr()
    assert "View Me" in captured.out
    mock_service.get_all_tasks.assert_called_once()
