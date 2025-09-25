pipeline {
    agent any
    environment {
        DEV_SERVER = 'dev-server-placeholder'
        TEST_SERVER = 'test-server-placeholder'
        PROD_SERVER = 'prod-server-placeholder'
        REPO_URL = 'https://github.com/sndevopsnerd/simple-banking-app'
    }
    stages {
        stage('Checkout') {
            steps {
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
                echo "Simulating deployment to PROD environment at ${PROD_SERVER}..."
                sh 'echo "Simulated: Deploying to Prod environment"'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished. Cleanup...'
        }
        success {
            echo 'Pipeline succeeded. Notifying external service...'
            sh 'curl -X POST -H "Authorization: Bearer cRldpw5y51IhSZH5MZMWqSvHZg6YVXh7" "https://dev197804.service-now.com/api/sn_devops/v2/devops/tool/orchestration?toolId=5c1dd70cc3d0f6108ce8fc0ed40131fd"'
        }
        failure {
            echo 'Pipeline failed. Notifying external service about the failure...'
            sh 'curl -X POST -H "Authorization: Bearer cRldpw5y51IhSZH5MZMWqSvHZg6YVXh7" "https://dev197804.service-now.com/api/sn_devops/v2/devops/tool/orchestration?toolId=5c1dd70cc3d0f6108ce8fc0ed40131fd"'
        }
    }
}