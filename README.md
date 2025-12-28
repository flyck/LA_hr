# hr

[![Build Status](https://github.com/flyck/LA_hr/actions/workflows/tests.yml/badge.svg)](https://github.com/flyck/LA_hr/actions/workflows/tests.yml)
[![Python Version](https://img.shields.io/badge/dynamic/toml?url=https://raw.githubusercontent.com/flyck/LA_hr/master/pyproject.toml&query=$.project.requires-python&label=python)](https://www.python.org/downloads/)

CLI for local user management. Based on a Linux Academy training module to get acquainted with TDD.

## Getting Started

1. Ensure `uv` is [installed](https://docs.astral.sh/uv/getting-started/installation/)
2. Fetch development dependencies `uv sync`
3. Create the virtualenv: `uv venv`

## Usage

`uv run hr <path-to-json>`

## Running Tests

Run tests locally using `uv run pytest`
