# Specification: Todo Console Application (Phase I)

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Approved

## 1. Overview

Build a command-line todo application that stores tasks in memory. This is Phase I of a multi-phase project that will eventually evolve into a full-stack web application with AI capabilities.

## 2. Objectives

- Create a functional command-line interface for task management
- Implement in-memory storage for tasks
- Provide all 5 basic CRUD operations
- Follow clean code principles and proper Python project structure
- Use spec-driven development methodology

## 3. User Stories

### US-1: Add Task
**As a** user  
**I want to** add a new task with a title and description  
**So that** I can track things I need to do

**Acceptance Criteria**:
- User can provide a task title (required)
- User can provide a task description (optional)
- Task is assigned a unique ID automatically
- Task is created with "incomplete" status by default
- Success message is displayed with the task ID

### US-2: View All Tasks
**As a** user  
**I want to** see a list of all my tasks  
**So that** I can review what needs to be done

**Acceptance Criteria**:
- Display all tasks in a readable format
- Show task ID, title, description, and status
- Indicate which tasks are complete vs incomplete
- Handle empty task list gracefully

### US-3: Update Task
**As a** user  
**I want to** update a task's title or description  
**So that** I can correct or clarify task details

**Acceptance Criteria**:
- User can select a task by ID
- User can update the title
- User can update the description
- User can update both or just one field
- Changes are reflected immediately
- Error message if task ID doesn't exist

### US-4: Delete Task
**As a** user  
**I want to** delete a task  
**So that** I can remove tasks I no longer need

**Acceptance Criteria**:
- User can select a task by ID to delete
- Confirmation message before deletion
- Task is removed from the list
- Success message after deletion
- Error message if task ID doesn't exist

### US-5: Mark Task Complete/Incomplete
**As a** user  
**I want to** mark tasks as complete or incomplete  
**So that** I can track my progress

**Acceptance Criteria**:
- User can toggle task status by ID
- Status changes from incomplete to complete or vice versa
- Visual indicator shows current status
- Success message after status change
- Error message if task ID doesn't exist

## 4. Functional Requirements

### FR-1: Task Data Model
- **Task ID**: Auto-generated unique integer
- **Title**: String, required, max 200 characters
- **Description**: String, optional, max 1000 characters
- **Status**: Boolean (complete/incomplete)
- **Created At**: Timestamp (auto-generated)

### FR-2: Command-Line Interface
- Interactive menu-driven interface
- Clear prompts for user input
- Numbered menu options
- Option to exit the application
- Input validation with error messages

### FR-3: In-Memory Storage
- Tasks stored in Python data structure (dictionary/list)
- Data persists only during application runtime
- No file or database storage in Phase I

### FR-4: Operations
1. **Add Task**: Create new task with title and optional description
2. **List Tasks**: Display all tasks with formatting
3. **Update Task**: Modify existing task details
4. **Delete Task**: Remove task from storage
5. **Toggle Status**: Mark task as complete/incomplete
6. **Exit**: Close the application

## 5. Non-Functional Requirements

### NFR-1: Performance
- Instant response time for all operations
- Support for up to 1000 tasks in memory

### NFR-2: Usability
- Clear, intuitive menu structure
- Helpful error messages
- Consistent command format

### NFR-3: Code Quality
- Follow PEP 8 style guidelines
- Type hints on all functions
- Comprehensive docstrings
- 80%+ test coverage

### NFR-4: Maintainability
- Modular code structure
- Separation of concerns
- Easy to extend for future phases

## 6. Technical Constraints

- **Language**: Python 3.13+
- **Package Manager**: UV
- **Storage**: In-memory only (no persistence)
- **Interface**: Command-line only
- **Dependencies**: Minimal (standard library preferred)

## 7. User Interface Flow

```
=== Todo Application ===

1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Enter your choice (1-6): _
```

## 8. Data Validation Rules

- **Title**: 
  - Required
  - 1-200 characters
  - Non-empty after stripping whitespace
  
- **Description**: 
  - Optional
  - Max 1000 characters
  
- **Task ID**: 
  - Must exist in storage for update/delete/toggle operations
  - Must be a valid integer

## 9. Error Handling

- Invalid menu choice: "Invalid choice. Please enter a number between 1-6."
- Task not found: "Task with ID {id} not found."
- Invalid input: "Invalid input. Please try again."
- Empty title: "Title cannot be empty."

## 10. Success Criteria

- ✅ All 5 basic operations implemented
- ✅ Clean, modular code structure
- ✅ Comprehensive test coverage
- ✅ Clear user interface
- ✅ Proper error handling
- ✅ Documentation complete

## 11. Out of Scope (Future Phases)

- Persistent storage (database/files)
- Multi-user support
- Web interface
- API endpoints
- Authentication
- Task categories/tags
- Due dates
- Priority levels
- Search/filter functionality

## 12. Deliverables

1. Source code in `/src` directory
2. Test suite in `/tests` directory
3. README.md with setup and usage instructions
4. CLAUDE.md with development guidelines
5. Constitution file
6. This specification document
7. Implementation plan
8. Task breakdown
