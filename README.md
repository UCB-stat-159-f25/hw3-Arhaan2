# Stats 159/259 — Homework 3  
### From Notebooks to Research Packages (Fall 2025)

This repository contains my submission for **HW3**, which focuses on converting the LIGO Gravitational Wave Detection tutorial into a complete, installable, testable, and documented research-style Python package following modern reproducible research standards.

---

## 🚀 Launch on Binder

Click below to run the notebook interactively in your browser:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-Arhaan2.git/main?urlpath=%2Fdoc%2Ftree%2Fhttps%3A%2F%2Fgithub.com%2FUCB-stat-159-f25%2Fhw3-Arhaan2%2Fblob%2Fmain%2FLOSC_Event_tutorial.ipynb)

---

## 📘 Project Overview

This assignment transforms the original **LOSC LIGO tutorial** into a structured, reproducible project with:

- A proper **Python package** (`ligotools/`)
- Support for **editable installation** via `pyproject.toml`
- **Unit tests** using `pytest`
- A clean **repository structure** (`data/`, `figures/`, `audio/`)
- Utility functions factored into `ligotools/utils.py`
- A **MyST website** (local + GitHub Pages deployment)
- A **Makefile** with `env`, `html`, and `clean` targets

The notebook has been modified to load data from `data/`, save figures to `figures/`, and save audio to `audio/`.  
All LIGO helper functions have been moved into the `ligotools` Python package.


