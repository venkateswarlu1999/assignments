pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Perform build steps here
                sh 'npm install'  // Example command using shell step
            }
        }

        stage('Test') {
            steps {
                // Perform test steps here
                sh 'npm test'  // Example command using shell step
            }
        }

        stage('Deploy') {
            steps {
                // Perform deployment steps here
                sh 'npm run deploy'  // Example command using shell step
            }
        }
    }

    post {
        success {
            // Actions to perform when the pipeline succeeds
            echo 'Pipeline successful!'
        }

        failure {
            // Actions to perform when the pipeline fails
            echo 'Pipeline failed!'
        }

        always {
            // Actions to perform always, regardless of success or failure
            echo 'Pipeline completed!'
        }
    }
}
