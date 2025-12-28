import sys

from src.services.task_service import TaskService
from src.ui.cli import TodoCLI


def main() -> None:
    """
    Principal entry point of the application.
    Initializes components and starts the user interface loop.
    """
    service = TaskService()
    cli = TodoCLI(service)

    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nA fatal error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
