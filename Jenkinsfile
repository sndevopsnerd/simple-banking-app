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
                
                // 1. Install the scanner tool and add its /bin directory to the PATH for this block
                def scannerHome = tool 'SonarScanner' 
                
                // 2. Inject environment variables and run the scanner
                withSonarQubeEnv('SonarQube Local') { 
                    // This command uses the scanner located via the 'tool' step
                    sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=."
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
