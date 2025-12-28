# Implementation Plan: Todo Console Application

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Approved

## 1. Technology Stack

### Core Technologies
- **Language**: Python 3.13+
- **Package Manager**: UV (for fast, reliable dependency management)
- **Runtime**: CPython 3.13

### Development Tools
- **Formatter**: Black (code formatting)
- **Linter**: Ruff (fast Python linter)
- **Type Checker**: mypy (static type checking)
- **Testing**: pytest (unit and integration testing)
- **Coverage**: pytest-cov (code coverage reporting)

### Dependencies
```toml
[project]
name = "todo-console-app"
version = "0.1.0"
description = "A command-line todo application with in-memory storage"
requires-python = ">=3.13"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",
    "black>=24.0.0",
    "ruff>=0.1.0",
    "mypy>=1.8.0",
]
```

## 2. Architecture Overview

### 2.1 Layered Architecture

```
┌─────────────────────────────────────┐
│         CLI Interface Layer         │
│     (User Interaction & Display)    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       Business Logic Layer          │
│      (Task Service & Operations)    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│         Data Model Layer            │
│    (Task Model & Validation)        │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       In-Memory Storage Layer       │
│      (Dictionary-based Store)       │
└─────────────────────────────────────┘
```

### 2.2 Module Structure

```
src/
├── __init__.py
├── main.py                 # Application entry point
├── models/
│   ├── __init__.py
│   └── task.py            # Task data model
├── services/
│   ├── __init__.py
│   └── task_service.py    # Business logic for task operations
├── ui/
│   ├── __init__.py
│   └── cli.py             # Command-line interface
└── utils/
    ├── __init__.py
    └── validators.py      # Input validation utilities
```

## 3. Component Design

### 3.1 Task Model (`models/task.py`)

**Purpose**: Represent a single task with all its properties

**Responsibilities**:
- Define task data structure
- Validate task data
- Provide task representation methods

**Design**:
```python
@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    
    def __post_init__(self):
        # Validation logic
        
    def to_dict(self) -> dict:
        # Serialization
        
    def __str__(self) -> str:
        # String representation
```

### 3.2 Task Service (`services/task_service.py`)

**Purpose**: Manage all task operations and in-memory storage

**Responsibilities**:
- CRUD operations (Create, Read, Update, Delete)
- Task status management
- ID generation
- Data storage management

**Design**:
```python
class TaskService:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Task
    def get_task(self, task_id: int) -> Task | None
    def get_all_tasks(self) -> list[Task]
    def update_task(self, task_id: int, title: str | None, description: str | None) -> Task
    def delete_task(self, task_id: int) -> bool
    def toggle_status(self, task_id: int) -> Task
```

**Storage Strategy**:
- Use dictionary with task ID as key for O(1) lookups
- Maintain counter for auto-incrementing IDs
- Return copies to prevent external modification

### 3.3 CLI Interface (`ui/cli.py`)

**Purpose**: Handle user interaction and display

**Responsibilities**:
- Display menu
- Get user input
- Format output
- Handle user commands
- Display errors

**Design**:
```python
class TodoCLI:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service
    
    def run(self) -> None
    def display_menu(self) -> None
    def handle_add_task(self) -> None
    def handle_view_tasks(self) -> None
    def handle_update_task(self) -> None
    def handle_delete_task(self) -> None
    def handle_toggle_status(self) -> None
    def get_input(self, prompt: str) -> str
    def display_task(self, task: Task) -> None
    def display_tasks(self, tasks: list[Task]) -> None
```

### 3.4 Validators (`utils/validators.py`)

**Purpose**: Validate user input

**Responsibilities**:
- Validate task title
- Validate task description
- Validate task ID
- Validate menu choices

**Design**:
```python
def validate_title(title: str) -> tuple[bool, str]
def validate_description(description: str) -> tuple[bool, str]
def validate_task_id(task_id_str: str) -> tuple[bool, int | None, str]
def validate_menu_choice(choice: str, max_choice: int) -> tuple[bool, int | None, str]
```

## 4. Data Flow

### 4.1 Add Task Flow
```
User Input → CLI.handle_add_task()
    → Validate title
    → TaskService.add_task()
    → Create Task object
    → Store in dictionary
    → Return Task
    → Display success message
```

### 4.2 View Tasks Flow
```
User selects view → CLI.handle_view_tasks()
    → TaskService.get_all_tasks()
    → Retrieve all tasks from dictionary
    → Sort by ID
    → CLI.display_tasks()
    → Format and print each task
```

### 4.3 Update Task Flow
```
User Input → CLI.handle_update_task()
    → Get task ID
    → Validate ID
    → TaskService.get_task()
    → Display current values
    → Get new values
    → Validate new values
    → TaskService.update_task()
    → Update task in dictionary
    → Display success message
```

### 4.4 Delete Task Flow
```
User Input → CLI.handle_delete_task()
    → Get task ID
    → Validate ID
    → TaskService.get_task()
    → Display task
    → Confirm deletion
    → TaskService.delete_task()
    → Remove from dictionary
    → Display success message
```

### 4.5 Toggle Status Flow
```
User Input → CLI.handle_toggle_status()
    → Get task ID
    → Validate ID
    → TaskService.toggle_status()
    → Update task.completed
    → Display success message
```

## 5. Error Handling Strategy

### 5.1 Error Types
- **ValidationError**: Invalid user input
- **TaskNotFoundError**: Task ID doesn't exist
- **ValueError**: Invalid data type

### 5.2 Error Handling Approach
- Validate early at the UI layer
- Return error messages to user
- Never crash the application
- Log errors for debugging
- Provide helpful error messages

### 5.3 Error Messages
```python
ERROR_MESSAGES = {
    "invalid_choice": "Invalid choice. Please enter a number between 1-6.",
    "task_not_found": "Task with ID {id} not found.",
    "empty_title": "Title cannot be empty.",
    "title_too_long": "Title must be 200 characters or less.",
    "description_too_long": "Description must be 1000 characters or less.",
    "invalid_id": "Please enter a valid task ID (number).",
}
```

## 6. Testing Strategy

### 6.1 Unit Tests

**Test Coverage**:
- `test_task.py`: Task model validation and methods
- `test_task_service.py`: All service operations
- `test_validators.py`: All validation functions
- `test_cli.py`: CLI display and input handling

**Test Approach**:
- Arrange-Act-Assert pattern
- Mock external dependencies
- Test edge cases
- Test error conditions

### 6.2 Integration Tests
- Test complete user flows
- Test CLI + Service integration
- Test error propagation

### 6.3 Coverage Goal
- Minimum 80% code coverage
- 100% coverage for business logic

## 7. Project Setup

### 7.1 Initialize Project
```bash
# Create project directory
mkdir todo-console-app
cd todo-console-app

# Initialize with UV
uv init

# Set Python version
echo "3.13" > .python-version

# Create project structure
mkdir -p src/{models,services,ui,utils}
mkdir -p tests
touch src/__init__.py
touch src/models/__init__.py
touch src/services/__init__.py
touch src/ui/__init__.py
touch src/utils/__init__.py
```

### 7.2 Install Dependencies
```bash
# Add dev dependencies
uv add --dev pytest pytest-cov black ruff mypy
```

### 7.3 Configuration Files

**pyproject.toml**:
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 88
target-version = ['py313']

[tool.ruff]
line-length = 88
target-version = "py313"

[tool.mypy]
python_version = "3.13"
strict = true
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--cov=src --cov-report=term-missing --cov-report=html"
```

## 8. Development Workflow

### 8.1 Development Process
1. Write specification for feature
2. Write tests (TDD approach)
3. Implement feature
4. Run tests
5. Format code with Black
6. Lint with Ruff
7. Type check with mypy
8. Commit changes

### 8.2 Commands
```bash
# Run application
uv run python -m src.main

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=term-missing

# Format code
uv run black src tests

# Lint code
uv run ruff check src tests

# Type check
uv run mypy src

# Run all checks
uv run black src tests && uv run ruff check src tests && uv run mypy src && uv run pytest
```

## 9. Performance Considerations

### 9.1 Time Complexity
- Add task: O(1)
- Get task by ID: O(1)
- Get all tasks: O(n)
- Update task: O(1)
- Delete task: O(1)
- Toggle status: O(1)

### 9.2 Space Complexity
- Storage: O(n) where n is number of tasks
- Expected max: 1000 tasks
- Memory footprint: ~100KB for 1000 tasks

## 10. Security Considerations

### 10.1 Input Validation
- Sanitize all user inputs
- Limit string lengths
- Validate data types
- Prevent injection attacks

### 10.2 Safe Defaults
- Tasks created as incomplete by default
- Empty description if not provided
- Auto-generated IDs (no user control)

## 11. Future Extensibility

### 11.1 Phase II Preparation
- Service layer ready for database integration
- Model can be serialized to JSON
- Clear separation allows API layer addition
- CLI can be replaced with web UI

### 11.2 Extension Points
- Storage backend (currently in-memory)
- Task properties (add tags, priority, due dates)
- Additional operations (search, filter, sort)
- Export/import functionality

## 12. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Data loss on exit | High | Document clearly; Phase II adds persistence |
| Memory overflow | Low | Limit to 1000 tasks; validate input |
| Invalid input crashes | Medium | Comprehensive validation and error handling |
| Poor UX | Medium | Clear prompts and helpful error messages |

## 13. Success Metrics

- ✅ All 5 operations working correctly
- ✅ 80%+ test coverage achieved
- ✅ Zero linting errors
- ✅ Zero type checking errors
- ✅ All tests passing
- ✅ Clean, readable code
- ✅ Complete documentation

## 14. Timeline Estimate

- Setup & Configuration: 30 minutes
- Task Model: 1 hour
- Task Service: 2 hours
- CLI Interface: 2 hours
- Validators: 1 hour
- Tests: 3 hours
- Documentation: 1 hour
- **Total**: ~10 hours

## 15. Deliverables Checklist

- [ ] Project initialized with UV
- [ ] All modules created
- [ ] Task model implemented
- [ ] Task service implemented
- [ ] CLI interface implemented
- [ ] Validators implemented
- [ ] Unit tests written
- [ ] Integration tests written
- [ ] README.md completed
- [ ] CLAUDE.md completed
- [ ] All code formatted
- [ ] All code linted
- [ ] All code type-checked
- [ ] All tests passing
- [ ] Coverage report generated
