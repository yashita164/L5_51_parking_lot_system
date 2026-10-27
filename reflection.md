# Lab 5: Static Code Analysis — Reflection

## 1. What is the importance of static code analysis?

Static code analysis helps identify potential bugs, security vulnerabilities, and code-quality problems without executing the program. In this lab, Pylint, Bandit, and Flake8 helped identify issues that could affect the reliability, security, readability, and maintainability of the Parking Lot System.

## 2. What issues were identified in the original program?

The original program had several issues, including unsafe use of `eval()`, shell command execution through `os.system()`, weak MD5 hashing, insecure random PIN generation, a mutable default argument, and a bare `except` block. Pylint and Flake8 also identified unused imports and variables, naming violations, missing docstrings, and formatting problems.

## 3. How did the static analysis tools help improve the program?

Pylint helped improve naming conventions, documentation, and code quality. Bandit identified potentially unsafe operations and security-related coding patterns. Flake8 identified formatting and style violations. By reviewing the reports and correcting the identified issues, I improved the code's readability and reduced avoidable security risks while retaining the parking system's main functionality.

## 4. What did you learn from this lab?

I learned that a program can run successfully and still contain security, reliability, and maintainability problems. Static analysis tools provide complementary perspectives, so using multiple tools is more useful than relying on only one. I also learned to compare before-and-after reports to verify that fixes address the reported findings. The final version achieved a Pylint score of 10.00/10, and the final Bandit and Flake8 runs reported no issues.
