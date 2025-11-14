# SauceDemo E2E Tests with Playwright + pytest

This project demonstrates **end-to-end UI testing** of the [SauceDemo](https://www.saucedemo.com/) website,
validating key user workflows and page features using **Playwright + pytest**.  

While individual features are tested separately, the suite collectively ensures full application coverage across login, 
shopping, and checkout flows.  

A [separate project of mine](https://github.com/ukk0/saucedemo-playwright-behave) 
utilizes instead **Playwright + Behave** to explore **BDD workflows** for the same web app. Both serve as a comparison 
of different frameworks and approaches to test design.

---

## Project overview
The goal of this project is to provide not 100% thorough, but high **functional test coverage** of the SauceDemo site using a **scalable, modular, and reusable framework** built with pytest.

It emphasizes:
- The use of **fixtures** and **parametrization** for reusability and maintainability  
- Clean separation of concerns using the **Page Object Model (POM)**  
- Consistent code quality enforced through **pre-commit hooks**

---

## Project structure

saucedemo-playwright-pytest/  
├── pages/ # Page Object Models (POMs)  
├── tests/ # Test files  
├── conftest.py # Shared fixtures and test setup  
├── requirements.txt  
├── pytest.ini  
└── .pre-commit-config.yaml  
└── .github/workflows/playwright-pytest-html.yml  

---

## Setup

This project was developed using **Python 3.13**.  
It’s recommended to use the same version to ensure compatibility.

Install dependencies and Playwright browsers:
```bash
pip install -r requirements.txt
playwright install
```

Enabling pre-commit hooks:

```bash
pre-commit install
```

---

## Running tests

Run all tests:

```bash
pytest
```

Run specific tests:

```
pytest <path_to_test_file>
```

Run tests in parallel with the help of pytest-xdist:

```bash
pytest -n auto
```
(the 'auto' option will automatically distribute test execution across all available CPUs, you can also
replace it with a specific number you would like to utilize, f.e. ```pytest -n 4```)

By default, tests are configured to run in headless mode using Chromium browser and without delay (as defined in ```pytest.ini```)  
You can override these options from the command line:

| Option            | Description                                         | Example                         |
|------------------|-----------------------------------------------------|---------------------------------|
| `--browser`       | Choose browser engine (`chromium`, `firefox`, `webkit`) | `pytest --browser=firefox`      |
| `--headed`        | Run tests with browser UI (not headless)           | `pytest --headed`                |
| `--slowmo <ms>`   | Add delay between actions in milliseconds          | `pytest --slowmo 200`            |

Example: Override defaults and run login tests in headed Firefox, with a 300ms action delay:
```bash
pytest tests/test_login_page.py --browser=firefox --headed --slowmo 300
```

---

## Code quality

Pre-commit hooks automatically ensure clean and consistent code using:
- ruff — linting and formatting
- isort — import sorting

Hooks will automatically run during commits for changed files.  
They can also be run manually for all files with:
```bash
pre-commit run --all-files
```

---

## Test reports and CI/CD

This project uses pytest-html for generating HTML test reports, available locally and in CI. A simple GitHub Actions 
workflow (manual trigger) runs the test suite, produces an HTML report, and uploads an artifact kept for 1 day
(workflow defined in .github/workflows/playwright-pytest-html.yml).

To run tests locally with report created:

```bash
pytest --html=reports/report.html --self-contained-html
```

In CI, the report is triggered via Actions > 'Playwright pytest-html' > Run workflow. The report can then be downloaded
through the 'Upload report' step of the workflow.
