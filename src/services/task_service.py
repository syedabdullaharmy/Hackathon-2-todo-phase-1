from copy import deepcopy

from src.models.task import Task
from src.utils.validators import validate_description, validate_title


class TaskService:
    """
    Manages the business logic and in-memory storage for tasks.
    """

    def __init__(self) -> None:
        """Initializes an empty task storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Creates and stores a new task.

        Args:
            title: The title of the task.
            description: Optional description of the task.

        Returns:
            The newly created Task object.

        Raises:
            ValueError: If the title or description is invalid.
        """
        is_valid_title, title_err = validate_title(title)
        if not is_valid_title:
            raise ValueError(title_err)

        is_valid_desc, desc_err = validate_description(description)
        if not is_valid_desc:
            raise ValueError(desc_err)

        task = Task(
            id=self._next_id, title=title.strip(), description=description.strip()
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return deepcopy(task)

    def get_task(self, task_id: int) -> Task | None:
        """
        Retrieves a task by its ID.

        Returns a copy to prevent external modification of internal storage.
        """
        task = self._tasks.get(task_id)
        return deepcopy(task) if task else None

    def get_all_tasks(self) -> list[Task]:
        """
        Retrieves all stored tasks, sorted by their ID.

        Returns a list of task copies.
        """
        tasks = sorted(self._tasks.values(), key=lambda t: t.id)
        return [deepcopy(task) for task in tasks]

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        description: str | None = None,
    ) -> Task:
        """
        Updates an existing task's title and/or description.

        Returns:
            The updated Task object.

        Raises:
            ValueError: If the task is not found or new data is invalid.
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} not found.")

        task = self._tasks[task_id]

        if title is not None:
            is_valid_title, title_err = validate_title(title)
            if not is_valid_title:
                raise ValueError(title_err)
            task.title = title.strip()

        if description is not None:
            is_valid_desc, desc_err = validate_description(description)
            if not is_valid_desc:
                raise ValueError(desc_err)
            task.description = description.strip()

        return deepcopy(task)

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by its ID.

        Returns:
            True if the task was deleted, False if it was not found.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_status(self, task_id: int) -> Task:
        """
        Toggles the completion status of a task.

        Returns:
            The updated Task object.

        Raises:
            ValueError: If the task is not found.
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} not found.")

        task = self._tasks[task_id]
        task.completed = not task.completed
        return deepcopy(task)
