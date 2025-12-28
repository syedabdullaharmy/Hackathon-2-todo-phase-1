# Claude Code Rules

The current project is a Spec-Driven Development (SDD) project. Use the following guidelines to maintain consistency.

## Phase I: Todo Console Application

### Project Structure
- Source code is in `/src`.
- Modular layout: `models/`, `services/`, `ui/`, `utils/`.
- Entry point: `src/main.py`.

### Specification Documents
- **Constitution**: `.specify/memory/constitution.md`
- **Spec**: `specs_history/01-specification.md`
- **Plan**: `specs_history/02-implementation-plan.md`
- **Tasks**: `specs_history/03-tasks.md`

### Tech Stack
- **Language**: Python 3.13+
- **Manager**: UV
- **Testing**: pytest (aim for 80%+ coverage)
- **Quality**: black (formatting), ruff (linting), mypy (typing)

### Key Architectural Decisions
- **In-Memory Storage**: Uses a dictionary in `TaskService` for O(1) ID-based operations.
- **Layered approach**: CLI handles inputs, Service handles logic, Model handles data integrity.
- **Deepcopy on retrieval**: Service returns copies of data to prevent mutation of internal state by UI.

### Development Commands
- Run App: `uv run python -m src.main`
- Run Tests: `uv run pytest`
- Check Quality: `uv run black . && uv run ruff check . && uv run mypy src`
