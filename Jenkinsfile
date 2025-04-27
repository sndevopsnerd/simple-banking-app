node {
    def DEV_SERVER = 'dev-server-placeholder'
    def TEST_SERVER = 'test-server-placeholder'
    def PROD_SERVER = 'prod-server-placeholder'

    stage('Checkout') {
        checkout scm
    }

    stage('Install Dependencies') {
        echo 'Installing dependencies...'
        sh 'echo "Simulated: pip install -r requirements.txt"'
    }

    stage('Run Tests') {
        echo 'Running tests...'
        sh 'echo "Simulated: Running tests (e.g., pytest)"'
    }

    stage('Deploy to Dev') {
        echo "Simulating deployment to DEV environment at ${DEV_SERVER}..."
        sh 'echo "Simulated: Deploying to Dev environment"'
    }

    stage('Deploy to Test') {
        echo "Simulating deployment to TEST environment at ${TEST_SERVER}..."
        sh 'echo "Simulated: Deploying to Test environment"'
    }

    stage('Deploy to Prod') {
        echo "Requesting ServiceNow change request approval before PROD deployment..."
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

        echo "Simulating deployment to PROD environment at ${PROD_SERVER}..."
        sh 'echo "Simulated: Deploying to Prod environment"'
    }

    echo 'Simulated deployment completed!'
}
