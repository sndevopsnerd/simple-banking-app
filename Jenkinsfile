pipeline {
    agent any

    environment {
        DEV_SERVER = 'dev-server-placeholder'
        TEST_SERVER = 'test-server-placeholder'
        PROD_SERVER = 'prod-server-placeholder'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'echo "Simulated: pip install -r requirements.txt"'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'echo "Simulated: Running tests (e.g., pytest)"'
                }
            }
        }

        stage('Deploy to Dev') {
            steps {
                script {
                    echo "Simulating deployment to DEV environment at ${DEV_SERVER}..."
                    sh 'echo "Simulated: Deploying to Dev environment"'
                }
            }
        }

        stage('Deploy to Test') {
            steps {
                script {
                    echo "Simulating deployment to TEST environment at ${TEST_SERVER}..."
                    sh 'echo "Simulated: Deploying to Test environment"'
                }
            }
        }

        stage('ServiceNow Change Request') {
            steps {
                script {
                    echo 'Creating and waiting for ServiceNow change request approval...'
                    snDevOpsChange(changeRequestDetails: '''
                    {
                      "attributes": {
                        "requested_by": {
                          "name": "Test User"
                        },
                        "assignment_group": {
                          "name": "Change Approval Team"
                        },
                        "priority": "2",
                        "comments": "Requesting approval before Prod deployment.",
                        "work_notes": "Auto-generated from Jenkins pipeline.",
                        "start_date": "2025-04-27 11:00:00",
                        "end_date": "2025-04-27 23:59:59"
                      }
                    }
                    ''')
                }
            }
        }

        stage('Deploy to Prod') {
            steps {
                script {
                    echo "Simulating deployment to PROD environment at ${PROD_SERVER}..."
                    sh 'echo "Simulated: Deploying to Prod environment"'
                }
            }
        }
    }

    post {
        success {
            echo 'Simulated deployment successful!'
        }
        failure {
            echo 'Simulated deployment failed!'
        }
    }
}
