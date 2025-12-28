import sys

from src.models.task import Task
from src.services.task_service import TaskService
from src.utils.validators import validate_menu_choice, validate_task_id


class TodoCLI:
    """
    Handles user interaction via a command-line interface.
    """

    def __init__(self, task_service: TaskService) -> None:
        """Initializes the CLI with a task service instance."""
        self.task_service = task_service
        self.max_choice = 6

    def display_menu(self) -> None:
        """Prints the main menu to the console."""
        print("\n=== Todo Application ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")

    def get_input(self, prompt: str) -> str:
        """Gets trimmed input from the user."""
        return input(prompt).strip()

    def display_task(self, task: Task) -> None:
        """Displays formatted details of a single task."""
        status = "✓" if task.completed else "✗"
        print(f"\nID: {task.id}")
        print(f"Title: {task.title}")
        print(f"Status: {status} ({'Completed' if task.completed else 'Incomplete'})")
        if task.description:
            print(f"Description: {task.description}")
        print(f"Created: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

    def display_tasks(self, tasks: list[Task]) -> None:
        """Displays a list of all tasks."""
        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n--- Task List ---")
        for task in tasks:
            print(str(task))

    def handle_add_task(self) -> None:
        """Interactive flow to add a new task."""
        print("\n--- Add New Task ---")
        title = self.get_input("Enter title: ")
        description = self.get_input("Enter description (optional): ")

        try:
            task = self.task_service.add_task(title, description)
            print(f"\nSuccess: Task added with ID {task.id}")
        except ValueError as e:
            print(f"\nError: {e}")

    def handle_view_tasks(self) -> None:
        """Displays all tasks."""
        tasks = self.task_service.get_all_tasks()
        self.display_tasks(tasks)

    def handle_update_task(self) -> None:
        """Interactive flow to update an existing task."""
        print("\n--- Update Task ---")
        id_str = self.get_input("Enter task ID to update: ")
        valid_id, task_id, err = validate_task_id(id_str)

        if not valid_id or task_id is None:
            print(f"\nError: {err}")
            return

        task = self.task_service.get_task(task_id)
        if not task:
            print(f"\nError: Task with ID {task_id} not found.")
            return

        print("\nCurrent task details:")
        self.display_task(task)

        print("\nEnter new details (leave empty to keep current):")
        new_title = self.get_input("New title: ") or None
        new_description = self.get_input("New description: ") or None

        try:
            self.task_service.update_task(task_id, new_title, new_description)
            print("\nSuccess: Task updated successfully.")
        except ValueError as e:
            print(f"\nError: {e}")

    def handle_delete_task(self) -> None:
        """Interactive flow to delete a task."""
        print("\n--- Delete Task ---")
        id_str = self.get_input("Enter task ID to delete: ")
        valid_id, task_id, err = validate_task_id(id_str)

        if not valid_id or task_id is None:
            print(f"\nError: {err}")
            return

        task = self.task_service.get_task(task_id)
        if not task:
            print(f"\nError: Task with ID {task_id} not found.")
            return

        self.display_task(task)
        confirm = self.get_input("Are you sure you want to delete this task? (y/n): ")

        if confirm.lower() == "y":
            if self.task_service.delete_task(task_id):
                print("\nSuccess: Task deleted successfully.")
            else:
                print("\nError: Could not delete task.")
        else:
            print("\nDeletion cancelled.")

    def handle_toggle_status(self) -> None:
        """Interactive flow to toggle task completion status."""
        print("\n--- Toggle Task Completion ---")
        id_str = self.get_input("Enter task ID: ")
        valid_id, task_id, err = validate_task_id(id_str)

        if not valid_id or task_id is None:
            print(f"\nError: {err}")
            return

        try:
            task = self.task_service.toggle_status(task_id)
            status_text = "Completed" if task.completed else "Incomplete"
            print(f"\nSuccess: Task {task_id} marked as {status_text}.")
        except ValueError as e:
            print(f"\nError: {e}")

    def run(self) -> None:
        """Main application loop."""
        while True:
            try:
                self.display_menu()
                choice = self.get_input("Enter your choice (1-6): ")

                is_valid, choice_int, err = validate_menu_choice(
                    choice, self.max_choice
                )
                if not is_valid or choice_int is None:
                    print(f"\nError: {err}")
                    continue

                if choice_int == 1:
                    self.handle_add_task()
                elif choice_int == 2:
                    self.handle_view_tasks()
                elif choice_int == 3:
                    self.handle_update_task()
                elif choice_int == 4:
                    self.handle_delete_task()
                elif choice_int == 5:
                    self.handle_toggle_status()
                elif choice_int == 6:
                    print("\nExiting. Goodbye!")
                    break

            except KeyboardInterrupt:
                print("\n\nExiting. Goodbye!")
                sys.exit(0)
            except Exception as e:
                print(f"\nAn unhandled error occurred: {e}")
