# Task Breakdown: Todo Console Application

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Ready for Implementation

## Task Organization

Tasks are organized by component and include acceptance criteria, test cases, and dependencies.

---

## Phase 1: Project Setup

### Task 1.1: Initialize Project Structure
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: None

**Description**:
Set up the project with UV, create directory structure, and configure development tools.

**Acceptance Criteria**:
- [ ] Project initialized with UV
- [ ] Python 3.13 specified in `.python-version`
- [ ] Directory structure created (`src/`, `tests/`, subdirectories)
- [ ] All `__init__.py` files created
- [ ] `pyproject.toml` configured
- [ ] Dev dependencies installed (pytest, black, ruff, mypy, pytest-cov)

**Implementation Steps**:
1. Run `uv init` in project directory
2. Create `.python-version` with "3.13"
3. Create directory structure
4. Create `pyproject.toml` with project metadata
5. Add dev dependencies
6. Create empty `__init__.py` files

**Test Cases**:
- Verify `uv run python --version` shows Python 3.13+
- Verify all directories exist
- Verify `uv run pytest --version` works

---

## Phase 2: Data Model Layer

### Task 2.1: Implement Task Model
**Priority**: P0 (Blocker)  
**Estimated Time**: 1 hour  
**Dependencies**: Task 1.1

**Description**:
Create the Task data model with validation and helper methods.

**Acceptance Criteria**:
- [ ] Task class created as dataclass
- [ ] Fields: id (int), title (str), description (str), completed (bool), created_at (datetime)
- [ ] Title validation (1-200 chars, non-empty)
- [ ] Description validation (max 1000 chars)
- [ ] `to_dict()` method for serialization
- [ ] `__str__()` method for display
- [ ] Type hints on all methods
- [ ] Comprehensive docstrings

**Implementation Steps**:
1. Create `src/models/task.py`
2. Import dataclass and datetime
3. Define Task dataclass with all fields
4. Add `__post_init__` for validation
5. Implement `to_dict()` method
6. Implement `__str__()` method
7. Add docstrings

**Test Cases**:
```python
# test_task.py
def test_task_creation_valid()
def test_task_creation_empty_title_raises_error()
def test_task_creation_title_too_long_raises_error()
def test_task_creation_description_too_long_raises_error()
def test_task_to_dict()
def test_task_str_representation()
def test_task_defaults()
```

**Files to Create**:
- `src/models/task.py`
- `tests/test_task.py`

---

## Phase 3: Validation Layer

### Task 3.1: Implement Input Validators
**Priority**: P0 (Blocker)  
**Estimated Time**: 1 hour  
**Dependencies**: None

**Description**:
Create validation functions for user input.

**Acceptance Criteria**:
- [ ] `validate_title()` function
- [ ] `validate_description()` function
- [ ] `validate_task_id()` function
- [ ] `validate_menu_choice()` function
- [ ] All functions return tuple (is_valid, value/None, error_message)
- [ ] Type hints on all functions
- [ ] Comprehensive docstrings

**Implementation Steps**:
1. Create `src/utils/validators.py`
2. Implement `validate_title()`
3. Implement `validate_description()`
4. Implement `validate_task_id()`
5. Implement `validate_menu_choice()`
6. Add error message constants
7. Add docstrings

**Test Cases**:
```python
# test_validators.py
def test_validate_title_valid()
def test_validate_title_empty()
def test_validate_title_too_long()
def test_validate_title_whitespace_only()
def test_validate_description_valid()
def test_validate_description_empty_allowed()
def test_validate_description_too_long()
def test_validate_task_id_valid()
def test_validate_task_id_invalid_string()
def test_validate_task_id_negative()
def test_validate_menu_choice_valid()
def test_validate_menu_choice_invalid()
def test_validate_menu_choice_out_of_range()
```

**Files to Create**:
- `src/utils/validators.py`
- `tests/test_validators.py`

---

## Phase 4: Business Logic Layer

### Task 4.1: Implement Task Service - Core Structure
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 2.1

**Description**:
Create TaskService class with initialization and storage.

**Acceptance Criteria**:
- [ ] TaskService class created
- [ ] `__init__()` method initializes empty dict and ID counter
- [ ] Private `_tasks` dictionary
- [ ] Private `_next_id` counter
- [ ] Type hints on all attributes
- [ ] Comprehensive docstrings

**Implementation Steps**:
1. Create `src/services/task_service.py`
2. Define TaskService class
3. Add `__init__()` method
4. Initialize `_tasks: dict[int, Task]`
5. Initialize `_next_id: int = 1`
6. Add class docstring

**Test Cases**:
```python
# test_task_service.py
def test_task_service_initialization()
def test_task_service_empty_on_start()
```

**Files to Create**:
- `src/services/task_service.py`
- `tests/test_task_service.py`

---

### Task 4.2: Implement Add Task Operation
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 4.1

**Description**:
Implement the add_task method in TaskService.

**Acceptance Criteria**:
- [ ] `add_task(title, description="")` method created
- [ ] Auto-generates task ID
- [ ] Creates Task object with current timestamp
- [ ] Stores task in dictionary
- [ ] Increments ID counter
- [ ] Returns created Task
- [ ] Validates title and description
- [ ] Type hints and docstring

**Implementation Steps**:
1. Add `add_task()` method to TaskService
2. Validate title using validators
3. Validate description using validators
4. Create Task with next ID
5. Store in `_tasks` dictionary
6. Increment `_next_id`
7. Return Task

**Test Cases**:
```python
def test_add_task_valid()
def test_add_task_increments_id()
def test_add_task_with_description()
def test_add_task_without_description()
def test_add_task_invalid_title_raises_error()
def test_add_task_stores_in_dict()
```

---

### Task 4.3: Implement Get Task Operations
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 4.2

**Description**:
Implement get_task and get_all_tasks methods.

**Acceptance Criteria**:
- [ ] `get_task(task_id)` method created
- [ ] Returns Task if found, None otherwise
- [ ] `get_all_tasks()` method created
- [ ] Returns list of all tasks sorted by ID
- [ ] Returns copies to prevent external modification
- [ ] Type hints and docstrings

**Implementation Steps**:
1. Add `get_task()` method
2. Look up task in dictionary
3. Return copy of task or None
4. Add `get_all_tasks()` method
5. Get all tasks from dictionary
6. Sort by ID
7. Return list of copies

**Test Cases**:
```python
def test_get_task_existing()
def test_get_task_non_existing()
def test_get_all_tasks_empty()
def test_get_all_tasks_multiple()
def test_get_all_tasks_sorted_by_id()
def test_get_task_returns_copy()
```

---

### Task 4.4: Implement Update Task Operation
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 4.3

**Description**:
Implement update_task method.

**Acceptance Criteria**:
- [ ] `update_task(task_id, title=None, description=None)` method created
- [ ] Updates title if provided
- [ ] Updates description if provided
- [ ] Validates new values
- [ ] Raises error if task not found
- [ ] Returns updated Task
- [ ] Type hints and docstring

**Implementation Steps**:
1. Add `update_task()` method
2. Check if task exists
3. Validate new title if provided
4. Validate new description if provided
5. Update task fields
6. Return updated task

**Test Cases**:
```python
def test_update_task_title()
def test_update_task_description()
def test_update_task_both()
def test_update_task_not_found()
def test_update_task_invalid_title()
def test_update_task_invalid_description()
```

---

### Task 4.5: Implement Delete Task Operation
**Priority**: P0 (Blocker)  
**Estimated Time**: 20 minutes  
**Dependencies**: Task 4.3

**Description**:
Implement delete_task method.

**Acceptance Criteria**:
- [ ] `delete_task(task_id)` method created
- [ ] Removes task from dictionary
- [ ] Returns True if deleted, False if not found
- [ ] Type hints and docstring

**Implementation Steps**:
1. Add `delete_task()` method
2. Check if task exists
3. Remove from dictionary if exists
4. Return boolean result

**Test Cases**:
```python
def test_delete_task_existing()
def test_delete_task_non_existing()
def test_delete_task_removes_from_storage()
def test_delete_task_multiple_operations()
```

---

### Task 4.6: Implement Toggle Status Operation
**Priority**: P0 (Blocker)  
**Estimated Time**: 20 minutes  
**Dependencies**: Task 4.3

**Description**:
Implement toggle_status method.

**Acceptance Criteria**:
- [ ] `toggle_status(task_id)` method created
- [ ] Toggles completed field
- [ ] Raises error if task not found
- [ ] Returns updated Task
- [ ] Type hints and docstring

**Implementation Steps**:
1. Add `toggle_status()` method
2. Get task by ID
3. Raise error if not found
4. Toggle completed field
5. Return updated task

**Test Cases**:
```python
def test_toggle_status_incomplete_to_complete()
def test_toggle_status_complete_to_incomplete()
def test_toggle_status_not_found()
def test_toggle_status_multiple_times()
```

---

## Phase 5: User Interface Layer

### Task 5.1: Implement CLI Core Structure
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 4.6

**Description**:
Create TodoCLI class with menu display and main loop.

**Acceptance Criteria**:
- [ ] TodoCLI class created
- [ ] `__init__()` accepts TaskService
- [ ] `run()` method with main loop
- [ ] `display_menu()` method
- [ ] `get_input()` helper method
- [ ] Graceful exit on option 6
- [ ] Type hints and docstrings

**Implementation Steps**:
1. Create `src/ui/cli.py`
2. Define TodoCLI class
3. Add `__init__()` with TaskService parameter
4. Implement `display_menu()`
5. Implement `get_input()`
6. Implement `run()` with while loop
7. Handle menu selection

**Test Cases**:
```python
# test_cli.py
def test_cli_initialization()
def test_display_menu(capsys)
def test_get_input(monkeypatch)
def test_run_exit_immediately(monkeypatch)
```

**Files to Create**:
- `src/ui/cli.py`
- `tests/test_cli.py`

---

### Task 5.2: Implement Add Task UI
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 5.1

**Description**:
Implement handle_add_task method in CLI.

**Acceptance Criteria**:
- [ ] `handle_add_task()` method created
- [ ] Prompts for title
- [ ] Prompts for description (optional)
- [ ] Validates inputs
- [ ] Calls TaskService.add_task()
- [ ] Displays success message with task ID
- [ ] Handles errors gracefully
- [ ] Type hints and docstring

**Implementation Steps**:
1. Add `handle_add_task()` method
2. Prompt for title
3. Validate title
4. Prompt for description
5. Call service.add_task()
6. Display success message
7. Handle validation errors

**Test Cases**:
```python
def test_handle_add_task_success(monkeypatch, capsys)
def test_handle_add_task_with_description(monkeypatch, capsys)
def test_handle_add_task_invalid_title(monkeypatch, capsys)
```

---

### Task 5.3: Implement View Tasks UI
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 5.1

**Description**:
Implement handle_view_tasks and display methods.

**Acceptance Criteria**:
- [ ] `handle_view_tasks()` method created
- [ ] `display_task()` method for single task
- [ ] `display_tasks()` method for list
- [ ] Shows task ID, title, description, status
- [ ] Visual indicator for completed tasks (✓/✗)
- [ ] Handles empty list gracefully
- [ ] Type hints and docstrings

**Implementation Steps**:
1. Add `display_task()` method
2. Format task with ID, title, description, status
3. Add `display_tasks()` method
4. Loop through tasks and display each
5. Add `handle_view_tasks()` method
6. Get all tasks from service
7. Display tasks or empty message

**Test Cases**:
```python
def test_display_task(capsys)
def test_display_tasks_multiple(capsys)
def test_display_tasks_empty(capsys)
def test_handle_view_tasks(capsys)
```

---

### Task 5.4: Implement Update Task UI
**Priority**: P0 (Blocker)  
**Estimated Time**: 40 minutes  
**Dependencies**: Task 5.1, Task 5.3

**Description**:
Implement handle_update_task method.

**Acceptance Criteria**:
- [ ] `handle_update_task()` method created
- [ ] Prompts for task ID
- [ ] Displays current task
- [ ] Prompts for new title (optional)
- [ ] Prompts for new description (optional)
- [ ] Validates inputs
- [ ] Calls TaskService.update_task()
- [ ] Displays success message
- [ ] Handles errors (task not found, validation)

**Implementation Steps**:
1. Add `handle_update_task()` method
2. Prompt for task ID
3. Validate and get task
4. Display current task
5. Prompt for new title (allow skip)
6. Prompt for new description (allow skip)
7. Call service.update_task()
8. Display success message
9. Handle errors

**Test Cases**:
```python
def test_handle_update_task_title(monkeypatch, capsys)
def test_handle_update_task_description(monkeypatch, capsys)
def test_handle_update_task_both(monkeypatch, capsys)
def test_handle_update_task_not_found(monkeypatch, capsys)
```

---

### Task 5.5: Implement Delete Task UI
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 5.1, Task 5.3

**Description**:
Implement handle_delete_task method.

**Acceptance Criteria**:
- [ ] `handle_delete_task()` method created
- [ ] Prompts for task ID
- [ ] Displays task to be deleted
- [ ] Asks for confirmation
- [ ] Calls TaskService.delete_task()
- [ ] Displays success message
- [ ] Handles errors (task not found)
- [ ] Allows cancellation

**Implementation Steps**:
1. Add `handle_delete_task()` method
2. Prompt for task ID
3. Validate and get task
4. Display task
5. Ask for confirmation
6. Call service.delete_task() if confirmed
7. Display appropriate message
8. Handle errors

**Test Cases**:
```python
def test_handle_delete_task_confirmed(monkeypatch, capsys)
def test_handle_delete_task_cancelled(monkeypatch, capsys)
def test_handle_delete_task_not_found(monkeypatch, capsys)
```

---

### Task 5.6: Implement Toggle Status UI
**Priority**: P0 (Blocker)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 5.1

**Description**:
Implement handle_toggle_status method.

**Acceptance Criteria**:
- [ ] `handle_toggle_status()` method created
- [ ] Prompts for task ID
- [ ] Calls TaskService.toggle_status()
- [ ] Displays success message with new status
- [ ] Handles errors (task not found)

**Implementation Steps**:
1. Add `handle_toggle_status()` method
2. Prompt for task ID
3. Validate ID
4. Call service.toggle_status()
5. Display success with new status
6. Handle errors

**Test Cases**:
```python
def test_handle_toggle_status_success(monkeypatch, capsys)
def test_handle_toggle_status_not_found(monkeypatch, capsys)
```

---

## Phase 6: Application Entry Point

### Task 6.1: Implement Main Entry Point
**Priority**: P0 (Blocker)  
**Estimated Time**: 20 minutes  
**Dependencies**: Task 5.6

**Description**:
Create main.py with application entry point.

**Acceptance Criteria**:
- [ ] `main.py` created
- [ ] `main()` function defined
- [ ] Creates TaskService instance
- [ ] Creates TodoCLI instance
- [ ] Runs CLI
- [ ] Handles keyboard interrupt gracefully
- [ ] `if __name__ == "__main__"` block
- [ ] Type hints and docstring

**Implementation Steps**:
1. Create `src/main.py`
2. Import TaskService and TodoCLI
3. Define `main()` function
4. Instantiate TaskService
5. Instantiate TodoCLI with service
6. Call cli.run()
7. Add try-except for KeyboardInterrupt
8. Add `if __name__ == "__main__"` block

**Test Cases**:
```python
# test_main.py
def test_main_runs_without_error(monkeypatch)
def test_main_handles_keyboard_interrupt(monkeypatch)
```

**Files to Create**:
- `src/main.py`
- `tests/test_main.py`

---

## Phase 7: Documentation

### Task 7.1: Create README.md
**Priority**: P1 (High)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 6.1

**Description**:
Write comprehensive README with setup and usage instructions.

**Acceptance Criteria**:
- [ ] Project description
- [ ] Features list
- [ ] Requirements section
- [ ] Installation instructions
- [ ] Usage instructions with examples
- [ ] Development setup
- [ ] Running tests
- [ ] Project structure overview
- [ ] License information

**Implementation Steps**:
1. Create `README.md`
2. Add project overview
3. List features
4. Document installation steps
5. Document usage with examples
6. Add development section
7. Add testing instructions
8. Document project structure

**Files to Create**:
- `README.md`

---

### Task 7.2: Update CLAUDE.md
**Priority**: P1 (High)  
**Estimated Time**: 20 minutes  
**Dependencies**: Task 6.1

**Description**:
Update CLAUDE.md with Phase I specific instructions.

**Acceptance Criteria**:
- [ ] Phase I overview added
- [ ] Specification file references
- [ ] Implementation approach documented
- [ ] Testing approach documented
- [ ] Links to all spec files

**Implementation Steps**:
1. Add Phase I section to CLAUDE.md
2. Link to specification
3. Link to implementation plan
4. Link to task breakdown
5. Document key decisions

**Files to Update**:
- `CLAUDE.md`

---

## Phase 8: Quality Assurance

### Task 8.1: Code Formatting and Linting
**Priority**: P1 (High)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 6.1

**Description**:
Format all code and fix linting issues.

**Acceptance Criteria**:
- [ ] All code formatted with Black
- [ ] Zero Ruff linting errors
- [ ] Zero mypy type errors
- [ ] Consistent code style throughout

**Implementation Steps**:
1. Run `uv run black src tests`
2. Run `uv run ruff check src tests --fix`
3. Run `uv run mypy src`
4. Fix any remaining issues

**Verification**:
```bash
uv run black src tests --check
uv run ruff check src tests
uv run mypy src
```

---

### Task 8.2: Test Coverage Review
**Priority**: P1 (High)  
**Estimated Time**: 30 minutes  
**Dependencies**: Task 8.1

**Description**:
Ensure test coverage meets 80% threshold.

**Acceptance Criteria**:
- [ ] Overall coverage >= 80%
- [ ] Business logic coverage >= 90%
- [ ] All critical paths tested
- [ ] Coverage report generated

**Implementation Steps**:
1. Run `uv run pytest --cov=src --cov-report=html`
2. Review coverage report
3. Identify untested code
4. Add missing tests
5. Re-run coverage

**Verification**:
```bash
uv run pytest --cov=src --cov-report=term-missing
```

---

### Task 8.3: Integration Testing
**Priority**: P1 (High)  
**Estimated Time**: 1 hour  
**Dependencies**: Task 8.2

**Description**:
Test complete user workflows end-to-end.

**Acceptance Criteria**:
- [ ] Test complete add-view-update-delete flow
- [ ] Test toggle status workflow
- [ ] Test error handling workflows
- [ ] Test edge cases
- [ ] All integration tests passing

**Implementation Steps**:
1. Create `tests/test_integration.py`
2. Write test for complete CRUD workflow
3. Write test for status toggle workflow
4. Write test for error scenarios
5. Run all tests

**Test Cases**:
```python
# test_integration.py
def test_complete_task_lifecycle()
def test_multiple_tasks_workflow()
def test_error_handling_workflow()
def test_empty_state_workflow()
```

**Files to Create**:
- `tests/test_integration.py`

---

## Task Summary

### By Priority
- **P0 (Blocker)**: 16 tasks - Must complete for Phase I
- **P1 (High)**: 5 tasks - Quality and documentation

### By Phase
- Phase 1 (Setup): 1 task
- Phase 2 (Model): 1 task
- Phase 3 (Validation): 1 task
- Phase 4 (Service): 6 tasks
- Phase 5 (UI): 6 tasks
- Phase 6 (Main): 1 task
- Phase 7 (Docs): 2 tasks
- Phase 8 (QA): 3 tasks

### Total Estimated Time
- **Development**: ~8 hours
- **Testing**: ~2 hours
- **Documentation**: ~1 hour
- **QA**: ~2 hours
- **Total**: ~13 hours

### Dependencies Graph
```
1.1 (Setup)
  ├─→ 2.1 (Task Model)
  │     ├─→ 4.1 (Service Core)
  │     │     ├─→ 4.2 (Add Task)
  │     │     │     ├─→ 4.3 (Get Tasks)
  │     │     │     │     ├─→ 4.4 (Update)
  │     │     │     │     ├─→ 4.5 (Delete)
  │     │     │     │     └─→ 4.6 (Toggle)
  │     │     │     │           └─→ 5.1 (CLI Core)
  │     │     │     │                 ├─→ 5.2 (Add UI)
  │     │     │     │                 ├─→ 5.3 (View UI)
  │     │     │     │                 ├─→ 5.4 (Update UI)
  │     │     │     │                 ├─→ 5.5 (Delete UI)
  │     │     │     │                 └─→ 5.6 (Toggle UI)
  │     │     │     │                       └─→ 6.1 (Main)
  │     │     │     │                             ├─→ 7.1 (README)
  │     │     │     │                             ├─→ 7.2 (CLAUDE.md)
  │     │     │     │                             └─→ 8.1 (Format)
  │     │     │     │                                   └─→ 8.2 (Coverage)
  │     │     │     │                                         └─→ 8.3 (Integration)
  └─→ 3.1 (Validators)
```

## Implementation Order

Execute tasks in this order for optimal workflow:

1. Task 1.1 - Project Setup
2. Task 2.1 - Task Model
3. Task 3.1 - Validators
4. Task 4.1 - Service Core
5. Task 4.2 - Add Task
6. Task 4.3 - Get Tasks
7. Task 4.4 - Update Task
8. Task 4.5 - Delete Task
9. Task 4.6 - Toggle Status
10. Task 5.1 - CLI Core
11. Task 5.2 - Add Task UI
12. Task 5.3 - View Tasks UI
13. Task 5.4 - Update Task UI
14. Task 5.5 - Delete Task UI
15. Task 5.6 - Toggle Status UI
16. Task 6.1 - Main Entry Point
17. Task 7.1 - README
18. Task 7.2 - CLAUDE.md
19. Task 8.1 - Formatting/Linting
20. Task 8.2 - Coverage Review
21. Task 8.3 - Integration Testing

---

**Ready for Implementation**: All tasks defined with clear acceptance criteria and test cases. Proceed with `/sp.implement` to execute all tasks.
