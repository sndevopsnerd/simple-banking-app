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
                echo "Simulating deployment to PROD environment at ${PROD_SERVER}..."
                sh 'echo "Simulated: Deploying to Prod environment"'
            }
        }
    }
    post {
        always {
            // This runs at the end of the build regardless of the outcome.
            echo 'Pipeline finished. Cleanup...'
        }
        success {
            // This runs only if the build succeeds.
            echo 'Pipeline succeeded. Notifying external service...'
            // Replace with your actual webhook URL
            sh 'curl -X POST \'https://dev197804.service-now.com/api/sn_devops/v2/devops/tool/{code | plan | artifact | orchestration | test | softwarequality }?toolId=5c1dd70cc3d0f6108ce8fc0ed40131fd/success\''
        }
        failure {
            // This runs only if the build fails.
            echo 'Pipeline failed. Notifying external service about the failure...'
            // Replace with your actual webhook URL
            sh 'curl -X POST \'https://dev197804.service-now.com/api/sn_devops/v2/devops/tool/{code | plan | artifact | orchestration | test | softwarequality }?toolId=5c1dd70cc3d0f6108ce8fc0ed40131fd/failure\''
        }
    }
}