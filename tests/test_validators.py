from src.utils.validators import (
    validate_description,
    validate_menu_choice,
    validate_task_id,
    validate_title,
)


def test_validate_title_valid() -> None:
    is_valid, msg = validate_title("My Task")
    assert is_valid is True
    assert msg == ""


def test_validate_title_empty() -> None:
    is_valid, msg = validate_title("")
    assert is_valid is False
    assert msg == "Title cannot be empty."

    is_valid, msg = validate_title("   ")
    assert is_valid is False
    assert msg == "Title cannot be empty."


def test_validate_title_too_long() -> None:
    is_valid, msg = validate_title("a" * 201)
    assert is_valid is False
    assert msg == "Title must be 200 characters or less."


def test_validate_description_valid() -> None:
    is_valid, msg = validate_description("Some description")
    assert is_valid is True
    assert msg == ""

    is_valid, msg = validate_description("")
    assert is_valid is True
    assert msg == ""


def test_validate_description_too_long() -> None:
    is_valid, msg = validate_description("a" * 1001)
    assert is_valid is False
    assert msg == "Description must be 1000 characters or less."


def test_validate_task_id_valid() -> None:
    is_valid, task_id, msg = validate_task_id("10")
    assert is_valid is True
    assert task_id == 10
    assert msg == ""


def test_validate_task_id_invalid_string() -> None:
    is_valid, task_id, msg = validate_task_id("abc")
    assert is_valid is False
    assert task_id is None
    assert msg == "Please enter a valid numeric task ID."


def test_validate_task_id_negative() -> None:
    is_valid, task_id, msg = validate_task_id("-5")
    assert is_valid is False
    assert task_id is None
    assert msg == "Please enter a valid positive task ID."


def test_validate_menu_choice_valid() -> None:
    is_valid, choice, msg = validate_menu_choice("3", 6)
    assert is_valid is True
    assert choice == 3
    assert msg == ""


def test_validate_menu_choice_invalid() -> None:
    is_valid, choice, msg = validate_menu_choice("xyz", 6)
    assert is_valid is False
    assert choice is None
    assert msg == "Invalid input. Please enter a number between 1 and 6."


def test_validate_menu_choice_out_of_range() -> None:
    is_valid, choice, msg = validate_menu_choice("7", 6)
    assert is_valid is False
    assert choice is None
    assert msg == "Invalid choice. Please enter a number between 1 and 6."
