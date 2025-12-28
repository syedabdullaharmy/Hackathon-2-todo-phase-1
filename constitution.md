# Project Constitution: Todo Console Application

## Project Overview
A command-line todo application that stores tasks in memory, built with Python 3.13+ and UV package manager, following spec-driven development principles.

## Core Principles

### 1. Code Quality
- **Clean Code**: Follow PEP 8 style guidelines
- **Type Safety**: Use Python type hints throughout
- **Documentation**: Docstrings for all public functions and classes
- **Simplicity**: Prefer simple, readable solutions over clever code
- **DRY Principle**: Don't Repeat Yourself - extract common logic

### 2. Architecture
- **Separation of Concerns**: Clear boundaries between UI, business logic, and data
- **Single Responsibility**: Each module/class has one clear purpose
- **Dependency Injection**: Pass dependencies explicitly
- **Immutability**: Prefer immutable data structures where possible

### 3. Testing
- **Test Coverage**: Aim for 80%+ code coverage
- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **Test-Driven Development**: Write tests before implementation when possible

### 4. Project Structure
```
/
├── .specify/
│   └── memory/
│       └── constitution.md
├── specs_history/
│   ├── 01-specification.md
│   ├── 02-implementation-plan.md
│   └── 03-tasks.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── cli.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_task_service.py
│   └── test_cli.py
├── README.md
├── CLAUDE.md
├── pyproject.toml
└── .python-version
```

### 5. Development Workflow
- **Spec-Driven**: All features start with specifications
- **Iterative**: Build incrementally, test continuously
- **Version Control**: Commit early, commit often
- **Documentation**: Update docs with code changes

### 6. Python Standards
- **Version**: Python 3.13+
- **Package Manager**: UV for dependency management
- **Formatting**: Black for code formatting
- **Linting**: Ruff for fast linting
- **Type Checking**: mypy for static type checking

### 7. Error Handling
- **Explicit Errors**: Use specific exception types
- **User-Friendly Messages**: Clear error messages for CLI users
- **Graceful Degradation**: Handle errors without crashing
- **Logging**: Log errors for debugging

### 8. Performance
- **Efficiency**: O(1) lookups for task retrieval by ID
- **Memory**: Reasonable memory usage for in-memory storage
- **Responsiveness**: Instant CLI responses

### 9. Security
- **Input Validation**: Validate all user inputs
- **No Injection**: Prevent command injection
- **Safe Defaults**: Secure by default

### 10. Maintainability
- **Readable Code**: Code should be self-documenting
- **Consistent Style**: Follow established patterns
- **Modular Design**: Easy to extend and modify
- **Clear Dependencies**: Explicit dependency declarations

## Non-Goals
- Persistent storage (Phase I is in-memory only)
- Multi-user support
- Network features
- GUI interface
- Complex task relationships

## Success Criteria
- All 5 basic features implemented and working
- Clean, well-structured codebase
- Comprehensive test coverage
- Clear documentation
- Easy to run and use
