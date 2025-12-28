hr
==

.. image:: https://github.com/flyck/LA_hr/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/flyck/LA_hr/actions/workflows/tests.yml
   :alt: Build Status

.. image:: https://img.shields.io/badge/dynamic/toml?url=https://raw.githubusercontent.com/flyck/LA_hr/master/pyproject.toml&query=$.project.requires-python&label=python
   :target: https://www.python.org/downloads/
   :alt: Python Version
|
CLI for local user management. Based on a Linux Academy training module to get acquainted with TDD.

Getting Started
---------------

1. Ensure ``uv`` is [installed](https://docs.astral.sh/uv/getting-started/installation/)
2. Fetch development dependencies ``uv sync``
3. Create the virtualenv: ``uv venv``

Usage
-----

``uv run hr <path-to-json>``

Running Tests
-------------

Run tests locally using ``uv run pytest``
