# BrowserStack Demo Test Suite

This repository contains a Selenium test suite that runs on BrowserStack to test the functionality of the [BStackDemo](https://www.bstackdemo.com) website.

## Test Scenario

The test suite performs the following actions:
1. Logs into www.bstackdemo.com using dummy credentials
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
|-- browserstack_test/
|   |-- conftest.py
|   |-- test_bstack_demo.py
|   |-- utils/
|       |-- __init__.py
|       |-- config.py
|-- requirements.txt
|-- Jenkinsfile
|-- README.md
```

## Setup Instructions

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/browserstack-demo-tests.git
   cd browserstack-demo-tests
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your BrowserStack credentials:
   ```
   BROWSERSTACK_USERNAME=your_username
   BROWSERSTACK_ACCESS_KEY=your_access_key
   DEMO_USERNAME=demouser
   DEMO_PASSWORD=testingisfun99
   ```

4. Run the tests locally:
   ```
   cd browserstack_test
   pytest test_bstack_demo.py --browser=windows_chrome -v
   ```

### Jenkins Setup

1. Create a new Pipeline job in Jenkins

2. Configure the pipeline to use your Git repository:
   - Under "Pipeline", select "Pipeline script from SCM"
   - Select "Git" as the SCM
   - Enter your repository URL
   - Specify the branch to build (e.g., "main" or "master")
   - Script Path: `Jenkinsfile`

3. Create the following credentials in Jenkins:
   - `browserstack-credentials`: Username/password credential with your BrowserStack username and access key
   - `bstack-demo-credentials`: Username/password credential with the demo site login (demouser/testingisfun99)

4. Run the Jenkins job

## Running Tests Manually

You can run the tests on different browsers by specifying the browser configuration:

```
# For Windows 10 Chrome
pytest test_bstack_demo.py --browser=windows_chrome -v

# For macOS Ventura Firefox
pytest test_bstack_demo.py --browser=mac_firefox -v

# For Samsung Galaxy S22
pytest test_bstack_demo.py --browser=galaxy_s22 -v
```

## Screenshots

Screenshots of successful build #9

**PAGE**|**SCREENSHOT**
----------|----------
Pipeline Overview|![pipeline-overview](/screenshots/pipeline_overview.png)
Pipeline Console Parallel|![pipeline-parallel](/screenshots/pipeline_console_paarallel.png)
Pipeline Post Actions|![pipeline-post-actions](/screenshots/pipeline_console_post_actions.png)
Console Output|![console-output](/screenshots/console_output.png)
Pipeline Configure|![configure](/screenshots/configure.png)

## Notes

- Sensitive data is not hardcoded and is referenced as environment variables
- The tests run in parallel across three different browser configurations
- The Jenkins pipeline is configured to run all browser configurations in parallel