# BrowserStack Demo Test Suite
---

## Index
- [Updates](#updates)
- [Test Scenario](#test-scenario)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [IDE (Local) Setup](#ide-local-setup)
  - [Jenkins Setup](#jenkins-setup)
- [Running Tests on IDE (Locally)](#running-tests-on-ide-locally)
- [Deployment Screenshots](#deployment-screenshots)
- [Notes](#notes)

## Updates
- Updated `conftest.py` to simplify browser execution by dynamically parametrizing the `browser_config` fixture based on the available browsers listed in `config.py`, removing hardcoded browser names. This ensures that adding or removing browsers only requires updating the config file.
- Updated `Jenkinsfile` to run all browser tests at once with a single command `python3 -m pytest test_bstack_demo.py -n 3 -v`, simplifying the pipeline and removing unnecessary parallel stages.
- Updated project structure by removing the `browserstack_test/` folder and moving all files and folders to the root directory to simplify script execution both locally and on Jenkins.

[Back to Top](#browserstack-demo-test-suite)

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

[Back to Top](#browserstack-demo-test-suite)

## Prerequisites

- Python 3.8 or higher
- A BrowserStack account (free trial works)
- Jenkins (for CI/CD integration)

[Back to Top](#browserstack-demo-test-suite)

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

[Back to Top](#browserstack-demo-test-suite)

## Setup Instructions

### IDE (Local) Setup

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

- `-n 3` specifies that pytest should run up to 3 tests in parallel using 3 workers (parallel processing improves speed).
- `-v` stands for verbose mode, which shows detailed information about each test being run.

[Back to Top](#browserstack-demo-test-suite)

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

[Back to Top](#browserstack-demo-test-suite)

## Running Tests on IDE (Locally)

You can run the tests on all available browsers dynamically in parallel:

```bash
python3 -m pytest test_bstack_demo.py -n 3 -v
```

- `-n 3`: Run tests with 3 parallel workers.
- `-v`: Enable verbose output to show each test execution step clearly.

[Back to Top](#browserstack-demo-test-suite)

## Deployment Screenshots

Screenshots and links from successful deployments and builds:

| **Deploy** | **Screenshot** | **Public Links** |
|:---------|:---------------|:---------------|
| VS Code Terminal | ![VS Code Terminal](/documents/screenshots/vs_code_terminal.png) | [Windows&nbsp;Chrome](https://automate.browserstack.com/builds/21f77926f4289fefb39b77e4e56debee0f963588/sessions/d42a94c3c04fc7ed2363a445b6258c13f7962c5d?auth_token=caeee2f04ad8087079310ae894e47ff441a72b4c0b513e68fb91ec4628f06331)<br>[MacOS&nbsp;Firefox](https://automate.browserstack.com/builds/21f77926f4289fefb39b77e4e56debee0f963588/sessions/f592de38d39a13bd4e69a81d676e8860b0df41c5?auth_token=eab009faaa8fdae9396a83be1bedf75e9404ca3bc01a5b98021ed15223b1e908)<br>[Galaxy&nbsp;S22](https://automate.browserstack.com/builds/21f77926f4289fefb39b77e4e56debee0f963588/sessions/daf1d3183add78faf9f9ac594e9fc8da33daae33?auth_token=a59f52fea86ec9c9551852029d40e74934500fd5438f653a51919def384bb430) |
| Jenkins | ![Jenkins Console](/documents/screenshots/jenkins_console.png) | [Windows&nbsp;Chrome](https://automate.browserstack.com/builds/21f77926f4289fefb39b77e4e56debee0f963588/sessions/5b7f98d46f78af50c5b5f724ed2e1f6b31bd9e8d?auth_token=f3a2b75281c17646a95dcc4508fe51bebcc2ca49144dfed712ec9d9982fb65ff)<br>[MacOS&nbsp;Firefox](https://automate.browserstack.com/builds/21f77926f4289fefb39b77e4e56debee0f963588/sessions/af87ce2946a688bede10541c214484cbf1348cba?auth_token=b655d3ae00ab04eb0a0cf114cd9b912f11d073a8e581b9b720bbfe1e817a24b2)<br>[Galaxy&nbsp;S22](https://automate.browserstack.com/builds/21f77926f4289fefb39b77e4e56debee0f963588/sessions/36e4a9342a3271e85951536634962c9f3393cf0d?auth_token=8edad13c5d43679e5c2828f85be882cfc42d1af71fe7ecbe2f4113c0d959f349) |

[Back to Top](#browserstack-demo-test-suite)

## Notes

- Sensitive data is not hardcoded and is referenced as environment variables.
- The tests run in parallel across all configured browser environments.
- The Jenkins pipeline is configured to trigger all browser configurations automatically.

[Back to Top](#browserstack-demo-test-suite)
