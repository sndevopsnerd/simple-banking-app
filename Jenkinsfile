pipeline {
    agent any
    environment {
        DEV_SERVER = 'dev-server-placeholder'
        TEST_SERVER = 'test-server-placeholder'
        PROD_SERVER = 'prod-server-placeholder'
        REPO_URL = 'https://github.com/sndevopsnerd/simple-banking-app' // Replace with your actual repository URL
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository using Jenkins' SCM configuration
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'echo "Simulated: pip install -r requirements.txt"'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'echo "Simulated: Running tests (e.g., pytest)"'
            }
        }

        stage('Deploy to Dev') {
            steps {
                echo "Simulating deployment to DEV environment at ${DEV_SERVER}..."
                sh 'echo "Simulated: Deploying to Dev environment"'
            }
        }

        stage('Deploy to Test') {
            steps {
                echo "Simulating deploy to TEST environment at ${TEST_SERVER}..."
                sh 'echo "Simulated: Deploying to Test environment"'
            }
        }

        stage('Deploy to Prod') {
            steps {
                script {
                    snDevOpsChange(
                        changeRequestDetails: '''{
                            "attributes": {
                                "short_description": "Deploy to Prod",
                                "priority": "1",
                                "start_date": "2025-04-27 08:00:00",
                                "end_date": "2025-04-27 18:00:00",
                                "justification": "Deploying new features to production environment",
                                "description": "Deploying new features to production environment",
                                "cab_required": true,
                                "comments": "This update is from Jenkins pipeline",
                                "work_notes": "Deploying to Prod environment",
                                "assignment_group": "a715cd759f2002002920bde8132e7018"
                            },
                            "setCloseCode": false,
                            "autoCloseChange": true
                        }''',
                        changeCreationTimeOut: 3600,
                        changeStepTimeOut: 18000,
                        pollingInterval: 60
                    )
                }
                echo "Simulating deployment to PROD environment at ${PROD_SERVER}..."
                sh 'echo "Simulated: Deploying to Prod environment"'
            }
        }
    }
}