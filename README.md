# AI Parser Project

A Python-based application for parsing and processing data using OpenAI integration.

## Project Structure

```
aiparser/
├── app/
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── ai_handler.py
│   │   └── file_handler.py
│   ├── view/
│   │   └── ui.py
│   ├── models/
│   └── config.py
├── resources/
│   └── config.toml
└── requirements.txt
```

## How It Works

The application operates through several key components:

1. **File Handler**: Manages file operations and text processing
2. **AI Handler**: Interfaces with OpenAI API for text generation
3. **UI Component**: Provides a PyQt5-based user interface
4. **Configuration**: Uses TOML for application settings

## Features

- OpenAI integration for text processing
- Excel file support through openpyxl
- Progress tracking and error handling
- Configurable settings via TOML

## Installation

```bash
pip install uv
uv venv
uv pip install PyQt5
```

## How to run

```bash
uv run main.py
```

## Requirements

- Python 3.10+
- Dependencies:
  - openai
  - pandas
  - openpyxl
  - dynaconf
  - PyQt5
