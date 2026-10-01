[![Python CI](https://github.com/KonstantinGus/python-devops-assignment/actions/workflows/worky.yml/badge.svg)]
(https://github.com/KonstantinGus/python-devops-assignment/actions/workflows/worky.yml)

# Python DevOps Assignment

This repository contains a Python project with automated checks run through
GitHub Actions.

## Prerequisites

- Git
- Python 3.10 or newer (use the version required by the project files if it
	differs)
- `pip`

Check your installed versions:

```bash
python --version
python -m pip --version
```

On some systems, use `python3` instead of `python`.

## Clone the repository

```bash
git clone https://github.com/KonstantinGus/python-devops-assignment.git
cd python-devops-assignment
```

## Create a virtual environment

Using a virtual environment keeps project dependencies separate from your
system Python installation.

### Linux and macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

Upgrade `pip` after activating the environment:

```bash
python -m pip install --upgrade pip
```

## Install dependencies

If the repository provides a dependency file, install it with the matching
command:

```bash
python -m pip install -r requirements.txt
```

If development dependencies are defined in `pyproject.toml`, install the
project in editable mode instead:

```bash
python -m pip install -e ".[dev]"
```

Skip commands for files that are not present in the repository.

## Run the project

Run the project using its documented entry point. Common examples are:

```bash
python main.py
```

or:

```bash
python -m <package_name>
```

Replace the example with the entry point defined by the project.

## Run tests and checks

Run the test suite with the test runner configured by the project. For a
pytest-based project:

```bash
python -m pytest
```

If linting or formatting tools are configured, run them before committing.
For example:

```bash
python -m ruff check .
python -m black --check .
```

The exact commands should match the configuration in the repository.

## Continuous integration

The workflow in `.github/workflows/worky.yml` runs automatically for the
configured branches and pull requests. You can view its status by selecting
the badge at the top of this page or opening the repository's **Actions** tab.

Before opening a pull request:

1. Activate the virtual environment.
2. Install the project dependencies.
3. Run the tests and configured quality checks locally.
4. Commit your changes and push the branch.
5. Confirm that the GitHub Actions workflow completes successfully.

## Deactivate the virtual environment

When finished, run:

```bash
deactivate
```

## Troubleshooting

- If a command is not found, confirm that the virtual environment is active.
- If dependencies are missing, reinstall them using the repository's dependency
	file.
- If Windows blocks PowerShell activation, review the local execution-policy
	settings or use Command Prompt instead.
- Use the workflow logs in GitHub Actions to investigate CI failures.

