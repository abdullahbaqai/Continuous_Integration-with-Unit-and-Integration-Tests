# 🚀 Continuous Integration Test Automation

This project sets up a **Continuous Integration (CI)** pipeline that automatically runs **unit** and **integration** tests using tools like **PyTest**, **JUnit**, and **Selenium** whenever new code is pushed to the repository.

## 📌 Features

- ✅ Runs tests on every `git push` and `pull request`
- 🧪 Supports Unit & Integration Testing
- 🌐 Browser-based testing with Selenium WebDriver
- ⚙️ GitHub Actions as the CI engine
- 📊 Clear test logs and failure traces

---

## 🛠️ Tech Stack

- **GitHub Actions** – CI/CD platform
- **Selenium** – Browser automation
- **JUnit** – Unit testing framework for Java
- **PyTest** – Unit testing framework for Python
- **Python / Java** – Supported languages

## Project Structure

ci-cd/
│

├── app/                    # Application code

├── test_app.py             # Unit tests

├── requirements.txt        # Python dependencies

├── .github/workflows/

│   └── python-ci.yml       # CI workflow configuration

└── coverage.xml            # Auto-generated coverage report
