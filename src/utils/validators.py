def validate_title(title: str) -> tuple[bool, str]:
    """
    Validates the task title.

    Returns:
        A tuple of (is_valid, error_message).
    """
    stripped_title = title.strip()
    if not stripped_title:
        return False, "Title cannot be empty."
    if len(stripped_title) > 200:
        return False, "Title must be 200 characters or less."
    return True, ""


def validate_description(description: str) -> tuple[bool, str]:
    """
    Validates the task description.

    Returns:
        A tuple of (is_valid, error_message).
    """
    if len(description) > 1000:
        return False, "Description must be 1000 characters or less."
    return True, ""


def validate_task_id(task_id_str: str) -> tuple[bool, int | None, str]:
    """
    Validates the task ID string from user input.

    Returns:
        A tuple of (is_valid, parsed_id, error_message).
    """
    try:
        task_id = int(task_id_str)
        if task_id <= 0:
            return False, None, "Please enter a valid positive task ID."
        return True, task_id, ""
    except ValueError:
        return False, None, "Please enter a valid numeric task ID."


def validate_menu_choice(choice: str, max_choice: int) -> tuple[bool, int | None, str]:
    """
    Validates the user's menu choice.

    Returns:
        A tuple of (is_valid, parsed_choice, error_message).
    """
    try:
        choice_int = int(choice)
        if 1 <= choice_int <= max_choice:
            return True, choice_int, ""
        return (
            False,
            None,
            f"Invalid choice. Please enter a number between 1 and {max_choice}.",
        )
    except ValueError:
        return (
            False,
            None,
            f"Invalid input. Please enter a number between 1 and {max_choice}.",
        )
