# BrowserStack Demo Test Suite
---

## Index
- [Updates](#updates)
- [Test Scenario](#test-scenario)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Local Setup](#local-setup)
  - [Jenkins Setup](#jenkins-setup)
- [Running Tests Manually](#running-tests-manually)
- [Screenshots](#screenshots)
- [Notes](#notes)

## Updates
- Updated `conftest.py` to simplify browser execution by parametrizing the `browser_config` fixture directly with three browsers (`windows_chrome`, `mac_firefox`, `galaxy_s22`), removing the need to pass `--browser` manually each time. Also updated `pytest_addoption` action from `store` to `append` to support multiple browsers if needed dynamically.
- Updated `Jenkinsfile` to run all browser tests at once with a single command `python3 -m pytest test_bstack_demo.py -n 3 -v`, simplifying the pipeline by removing unnecessary parallel stages and avoiding multiple executions.
- Updated project structure by removing the `browserstack_test/` folder and moving `test_bstack_demo.py` to the root directory to simplify script execution both locally and on Jenkins.

## Test Scenario

The test suite performs the following actions:
1. Logs into [bstackdemo.com](https://www.bstackdemo.com) using dummy credentials
2. Filters the product view to show "Samsung" devices only
3. Favorites the "Galaxy S20+" device by clicking the yellow heart icon
4. Verifies that the Galaxy S20+ is listed on the Favorites page

These tests are run in parallel on the following browsers:
- Windows 10 Chrome
- macOS Ventura Firefox
- Samsung Galaxy S22

## Prerequisites

- Python 3.8 or higher
- A BrowserStack account (free trial works)
- Jenkins (for CI/CD integration)

## Project Structure

```
|
|-- conftest.py
|-- test_bstack_demo.py
|-- utils/
|   |-- __init__.py
|   |-- config.py
|-- requirements.txt
|-- Jenkinsfile
|-- README.md
```

## Setup Instructions

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/browserstack-demo-tests.git
   cd browserstack-demo-tests
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your BrowserStack credentials:
   ```env
   BROWSERSTACK_USERNAME=your_username
   BROWSERSTACK_ACCESS_KEY=your_access_key
   DEMO_USERNAME=demouser
   DEMO_PASSWORD=testingisfun99
   ```

4. Run the tests locally:
   ```bash
   python3 -m pytest test_bstack_demo.py -n 3 -v
   ```

### Jenkins Setup

1. Create a new Pipeline job in Jenkins.

2. Configure the pipeline to use your Git repository:
   - Under "Pipeline", select "Pipeline script from SCM"
   - Select "Git" as the SCM
   - Enter your repository URL
   - Specify the branch to build (e.g., `main` or `master`)
   - Script Path: `Jenkinsfile`

3. Create the following credentials in Jenkins:
   - `browserstack-credentials`: Username/password credential with your BrowserStack username and access key
   - `bstack-demo-credentials`: Username/password credential with the demo site login (`demouser` / `testingisfun99`)

4. Run the Jenkins job.

## Running Tests Locally

You can run the tests on all three browsers together locally:

```bash
python3 -m pytest test_bstack_demo.py -n 3 -v
```

## Screenshots

Screenshots from a successful build:

| **Page** | **Screenshot** |
|:---------|:---------------|
| Manual Deploy - VS Code Terminal | ![VS Code Terminal](/documents/screenshots/vs_code_terminal.png) |
| Jenkins Deploy | ![Jenkins Console](/documents/screenshots/jenkins_console.png) |

## Notes

- Sensitive data is not hardcoded and is referenced as environment variables.
- The tests run in parallel across three different browser configurations.
- The Jenkins pipeline is configured to run all browser configurations in parallel.
