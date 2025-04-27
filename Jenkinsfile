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
                    // Simulating the installation of dependencies
                    sh 'echo "Simulated: pip install -r requirements.txt"'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'
                    // Simulate running tests
                    sh 'echo "Simulated: Running tests (e.g., pytest)"'
                }
            }
        }

        stage('Deploy to Dev') {
            steps {
                script {
                    echo "Simulating deployment to DEV environment at ${DEV_SERVER}..."
                    // Simulate deployment process
                    sh 'echo "Simulated: Deploying to Dev environment"'
                }
            }
        }

        stage('Approval for Test') {
            steps {
                input message: 'Approve deployment to TEST?', ok: 'Deploy to Test'
            }
        }

        stage('Deploy to Test') {
            steps {
                script {
                    echo "Simulating deployment to TEST environment at ${TEST_SERVER}..."
                    // Simulate deployment process
                    sh 'echo "Simulated: Deploying to Test environment"'
                }
            }
        }

        stage('Approval for Prod') {
            steps {
                input message: 'Approve deployment to PROD?', ok: 'Deploy to Prod'
            }
        }

        stage('Deploy to Prod') {
            steps {
                script {
                    echo "Simulating deployment to PROD environment at ${PROD_SERVER}..."
                    // Simulate deployment process
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
git status
