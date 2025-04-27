        stage('Deploy to Prod') {
            steps {
                script {
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
            }
        }
