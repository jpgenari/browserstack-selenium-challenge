pipeline {
    agent any
    
    environment {
        // Define credential IDs (to be configured in Jenkins)
        BROWSERSTACK_CREDENTIALS = credentials('browserstack-credentials')
        DEMO_CREDENTIALS = credentials('bstack-demo-credentials')
    }
    
    stages {
        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests in Parallel') {
            parallel {
                stage('Windows 10 Chrome') {
                    steps {
                        sh '''
                            export BROWSERSTACK_USERNAME=$BROWSERSTACK_CREDENTIALS_USR
                            export BROWSERSTACK_ACCESS_KEY=$BROWSERSTACK_CREDENTIALS_PSW
                            export DEMO_USERNAME=$DEMO_CREDENTIALS_USR
                            export DEMO_PASSWORD=$DEMO_CREDENTIALS_PSW
                            cd browserstack_test
                            python3 -m pytest test_bstack_demo.py --browser=windows_chrome -v
                        '''
                    }
                }
                
                stage('macOS Ventura Firefox') {
                    steps {
                        sh '''
                            export BROWSERSTACK_USERNAME=$BROWSERSTACK_CREDENTIALS_USR
                            export BROWSERSTACK_ACCESS_KEY=$BROWSERSTACK_CREDENTIALS_PSW
                            export DEMO_USERNAME=$DEMO_CREDENTIALS_USR
                            export DEMO_PASSWORD=$DEMO_CREDENTIALS_PSW
                            cd browserstack_test
                            python3 -m pytest test_bstack_demo.py --browser=mac_firefox -v
                        '''
                    }
                }
                
                stage('Samsung Galaxy S22') {
                    steps {
                        sh '''
                            export BROWSERSTACK_USERNAME=$BROWSERSTACK_CREDENTIALS_USR
                            export BROWSERSTACK_ACCESS_KEY=$BROWSERSTACK_CREDENTIALS_PSW
                            export DEMO_USERNAME=$DEMO_CREDENTIALS_USR
                            export DEMO_PASSWORD=$DEMO_CREDENTIALS_PSW
                            cd browserstack_test
                            python3 -m pytest test_bstack_demo.py --browser=galaxy_s22 -v
                        '''
                    }
                }
            }
        }
        
        stage('Report') {
            steps {
                echo 'Test execution completed'
                // Here you could add steps to generate and publish test reports
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