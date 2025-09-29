pipeline {
    agent any
    
    environment {
        // --- SonarQube Configuration ---
        SONAR_PROJECT_KEY = 'simple-banking-app'
        
        // --- ServiceNow Credentials & API ---
        // Credential ID for the Secret Token (ensure this ID exists as 'Secret text' in Jenkins)
        SN_TOKEN_ID = 'servicenow-api-token'
        // ServiceNow DevOps API URL
        SN_API_URL = 'https://dev197804.service-now.com/api/sn_devops/v2/devops/tool/orchestration?toolId=5c1dd70cc3d0f6108ce8fc0ed40131fd'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        
        stage('Install Dependencies (Simulated)') {
            steps {
                echo 'Installing dependencies...'
                sh 'echo "Simulated: pip install -r requirements.txt"'
            }
        }
        
        stage('Run Tests (Simulated)') {
            steps {
                echo 'Running tests...'
                // Creates a simulated JUnit report file
                sh 'mkdir -p target/surefire-reports && echo "<testsuite/>" > target/surefire-reports/TEST-Simulated.xml'
            }
        }
        
        // --- SONARQUBE ANALYSIS ---
        stage('SonarQube Analysis') {
            steps {
                echo 'Starting SonarQube Code Analysis...'
                
                // FIX: Wrap Groovy variable declaration in a script block
                script {
                    def scannerHome = tool 'SonarScanner' 
                    env.SONAR_SCANNER_HOME = scannerHome
                }
                
                // The withSonarQubeEnv step implicitly adds the tool to the path for its block, 
                // but we also ensure the path is set via env for safety.
                withSonarQubeEnv('SonarQube Local') { 
                    // This command now uses the environment variable or the tool step's influence
                    // to find the scanner executable.
                    sh "${env.SONAR_SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=."
                }
            }
        }
        // --- END SONARQUBE ANALYSIS ---

        stage('Deploy to Dev (Simulated)') {
            steps {
                echo 'Simulating Deployment to Dev...'
                sh 'echo "Deployment successful"'
            }
        }
    }
    
    post {
        failure {
            echo 'Pipeline failed. Notifying ServiceNow about the failure...'
            // Use withCredentials to securely access the token
            withCredentials([string(credentialsId: SN_TOKEN_ID, variable: 'SN_TOKEN')]) {
                // Use triple single quotes (''') and double quotes inside the shell command
                // This ensures the Authorization header is treated as one complete string, fixing the 403 error.
                sh '''
                    curl -X POST \
                    -H "Authorization: Bearer ${SN_TOKEN}" \
                    "${SN_API_URL}"
                '''
            }
        }
    }
}
