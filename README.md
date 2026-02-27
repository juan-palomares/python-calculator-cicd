# Python Calculator with CI/CD

![CI/CD Pipeline](https://github.com/juan-palomares/python-calculator-cicd/actions/workflows/ci.yml/badge.svg)

A simple Python calculator demonstrating **automated testing** and **CI/CD best practices** using GitHub Actions.

## 🚀 Features

- Basic arithmetic operations (add, subtract, multiply, divide, power)
- Comprehensive unit test suite
- Automated CI/CD pipeline with GitHub Actions
- Tests run on Python 3.9, 3.10, and 3.11
- Code quality checks with flake8

## 🛠️ Technologies

- **Python 3.9+**
- **unittest** (Python's built-in testing framework)
- **GitHub Actions** (CI/CD automation)
- **flake8** (code linting)

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/juan-palomares/python-calculator-cicd.git
cd python-calculator-cicd

# Run the calculator
python calculator.py

# Run tests
python -m unittest test_calculator.py -v

🧪 Running Tests

Bash

python test_calculator.py

Expected output:

text

test_add (__main__.TestCalculator) ... ok
test_divide (__main__.TestCalculator) ... ok
test_divide_by_zero (__main__.TestCalculator) ... ok
test_multiply (__main__.TestCalculator) ... ok
test_power (__main__.TestCalculator) ... ok
test_subtract (__main__.TestCalculator) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK

🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:

    Runs unit tests on every push and pull request
    Tests across multiple Python versions (3.9, 3.10, 3.11)
    Performs code quality checks using flake8
    Displays build status with a badge

Pipeline Configuration

See .github/workflows/ci.yml for the complete workflow.
📚 What I Learned

    Setting up automated testing with GitHub Actions
    Writing unit tests with Python's unittest framework
    Implementing CI/CD best practices
    Multi-version testing strategies
    Code quality automation with linting tools

🎯 Purpose

This project demonstrates my understanding of:

    DevOps principles (automation, testing, continuous integration)
    Python development (clean code, documentation, error handling)
    Quality assurance (unit testing, test coverage, edge cases)
    Version control workflows (Git, GitHub, CI/CD pipelines)

Built as part of my DevOps engineering learning journey.
📧 Contact

Juan Palomares
GitHub: @juan-palomares