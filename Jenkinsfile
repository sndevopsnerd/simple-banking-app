pipeline {
    agent any
    
    environment {
        // --- SonarQube Configuration ---
        SONAR_PROJECT_KEY = 'simple-banking-app'
        SN_TOKEN_ID = 'servicenow-api-token'
        SN_API_URL = 'https://dev197804.service-now.com/api/sn_devops/v2/devops/tool/orchestration?toolId=5c1dd70cc3d0f6108ce8fc0ed40131fd'
    }
    
    stages {
        // ... (Skipping initial stages for brevity, assume Checkout works) ...
        
        stage('SonarQube Analysis') {
            steps {
                echo 'Starting SonarQube Code Analysis...'
                // The 'tool' step ensures the executable is on the PATH for this block
                // Replace 'SonarScanner' with the exact name used in Global Tool Configuration
                withSonarQubeEnv('SonarQube Local') { 
                    tool 'SonarScanner' // Inject the tool into the PATH
                    sh "sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=."
                }
            }
        }
        
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
            withCredentials([string(credentialsId: SN_TOKEN_ID, variable: 'SN_TOKEN')]) {
                // Secure and correct way to execute sh with secrets: 
                // 1. Use triple single quotes (''') for the shell script block.
                // 2. Encapsulate the entire Authorization header, including the Bearer token, in double quotes inside the shell script.
                sh '''
                    curl -X POST \
                    -H "Authorization: Bearer ${SN_TOKEN}" \
                    "${SN_API_URL}"
                '''
            }
        }
    }
}
