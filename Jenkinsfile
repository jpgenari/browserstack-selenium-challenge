pipeline {
    agent any

    environment {
        // Use updated Python from Homebrew
        PATH = "/opt/homebrew/bin:$PATH"
        
        // Jenkins credentials
        BROWSERSTACK_CREDENTIALS = credentials('browserstack-credentials')
        DEMO_CREDENTIALS = credentials('bstack-demo-credentials')
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run All Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export BROWSERSTACK_USERNAME=$BROWSERSTACK_CREDENTIALS_USR
                    export BROWSERSTACK_ACCESS_KEY=$BROWSERSTACK_CREDENTIALS_PSW
                    export DEMO_USERNAME=$DEMO_CREDENTIALS_USR
                    export DEMO_PASSWORD=$DEMO_CREDENTIALS_PSW
                    python3 -m pytest test_bstack_demo.py -n 3 -v
                '''
            }
        }

        stage('Report') {
            steps {
                echo 'Test execution completed'
                // Add steps to publish reports if needed
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace'
            cleanWs()
        }
        success {
            echo 'Tests executed successfully!'
        }
        failure {
            echo 'Test execution failed!'
        }
    }
}