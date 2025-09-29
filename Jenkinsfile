pipeline {
    agent any
    
    environment {
        // --- SonarQube Configuration ---
        SONAR_PROJECT_KEY = 'simple-banking-app'
        
        // --- ServiceNow Credentials & API ---
        // Credential ID for the Secret Token (ensure this ID exists in Jenkins Credentials Manager)
        SN_TOKEN_ID = 'sn-api-token'
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
                // Creates a simulated JUnit report file for later stages if needed
                sh 'mkdir -p target/surefire-reports && echo "<testsuite/>" > target/surefire-reports/TEST-Simulated.xml'
            }
        }
        stage('Diagnostic Check') {
            steps {
                echo 'Checking workspace contents before SonarScanner execution...'
                // This command lists all files and permissions in the workspace
                sh 'ls -la' 
                // This command specifically checks the permissions and existence of the downloaded scanner
                sh 'ls -la /usr/local/bin/sonar-scanner || echo "Sonar-scanner not in /usr/local/bin"'
            }
        }
        // --- SONARQUBE ANALYSIS ---
        stage('SonarQube Analysis') {
            steps {
                echo 'Starting SonarQube Code Analysis...'
                // The 'withSonarQubeEnv' step injects the configured SonarQube server details.
                // You MUST configure a SonarQube server named 'SonarQube Local' in Manage Jenkins > Configure System.
                withSonarQubeEnv('SonarQube Local') { 
                    // This runs the SonarQube Scanner executable (Name: SonarScanner in Global Tool Config)
                    sh "sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=."
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
            withCredentials([string(credentialsId: SN_TOKEN_ID, variable: 'SN_TOKEN')]) {
                // Correctly format the Authorization header value with the variable
                sh "curl -X POST -H \"Authorization: Bearer ${SN_TOKEN}\" \"${SN_API_URL}\""
            }
        }
    }
}
