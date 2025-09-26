pipeline {
    agent any
    
    environment {
        // SonarQube project key for the analysis report
        SONAR_PROJECT_KEY = 'simple-banking-app'
        
        // Credentials ID for connecting to ServiceNow (ensure this ID exists in Jenkins Credentials Manager)
        SN_CREDS_ID = 'servicenow-api-creds' // Placeholder for your actual credential ID
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
                // Create a simulated JUnit report file for later steps (like qTest)
                sh 'mkdir -p target/surefire-reports && echo "<testsuite/>" > target/surefire-reports/TEST-Simulated.xml'
            }
        }
        
        // --- SONARQUBE ANALYSIS ---
        stage('SonarQube Analysis') {
            steps {
                echo 'Starting SonarQube Code Analysis...'
                // The 'withSonarQubeEnv' step injects the URL and credentials for 'SonarQube Local'.
                // You MUST configure a SonarQube server named 'SonarQube Local' in Manage Jenkins > Configure System.
                withSonarQubeEnv('SonarQube Local') { 
                    // This runs the SonarQube Scanner executable (Name: SonarScanner in Global Tool Config)
                    sh "sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=."
                }
            }
        }
        // --- END SONARQUBE ANALYSIS ---
        
        // --- QTEST / TEST PUBLISHING (Conceptual) ---
        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results to external QM tool (e.g., qTest)...'
                // You would typically use the official qTest plugin step here:
                // qTestUploader credentialsId: 'qtest-creds', results: 'target/surefire-reports/*.xml'
                sh 'echo "Simulated: Uploaded test results to qTest"'
            }
        }
        
        stage('Deploy to Dev (Simulated)') {
            steps {
                echo 'Simulating Deployment to Dev.....'
                sh 'echo "Deployment successful"'
            }
        }
    }
    

}