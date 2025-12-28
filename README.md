# Todo In-Memory Console Application

A robust, spec-driven command-line task manager built with Python 3.13 and UV.

## Features

- **Add Task**: Create new tasks with a title and optional description.
- **View All Tasks**: List all tasks with their current status (Complete/Incomplete).
- **Update Task**: Modify existing task titles or descriptions.
- **Delete Task**: Remove tasks by their ID.
- **Tick Status**: Easily toggle between complete and incomplete.
- **Input Validation**: Robust handling of menu choices, titles, and IDs.
- **In-Memory Storage**: Fast performance for sessions (resets on close).

## Requirements

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

1. Clone or download this project.
2. Ensure you have `uv` installed.
3. Sync the virtual environment and install dependencies:
   ```bash
   uv sync
   ```

## Usage

Start the interactive console application:

```bash
uv run python -m src.main
```

### Menu Options:
1. **Add Task**: Prompts for title (required) and description (optional).
2. **View All Tasks**: Shows a summarized list of ID, Status, and Title.
3. **Update Task**: Opens a submenu to modify specific fields of a task.
4. **Delete Task**: Permanently removes a task (requires confirmation).
5. **Mark Complete/Incomplete**: Toggles a task's status.
6. **Exit**: Gracefully shuts down the application.

## Development

### Setup Environment
```bash
uv sync --all-extras
```

### Running Tests
Execute the full test suite with coverage:
```bash
uv run pytest
```

### Linting and Formatting
Check code style and potential issues:
```bash
uv run black src tests
uv run ruff check src tests
uv run mypy src
```

## Project Structure

```
/
├── src/
│   ├── models/       # Data structures (Task)
│   ├── services/     # Business logic (TaskService)
│   ├── ui/           # User Interface (CLI)
│   ├── utils/        # Shared helpers (Validators)
│   └── main.py       # Entry point
├── tests/            # Full test suite
├── specs_history/    # Specification and planning docs
└── pyproject.toml    # Dependencies and tool configuration
```

## License
MIT
