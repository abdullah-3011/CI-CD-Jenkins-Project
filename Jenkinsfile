pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python Application'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests'
                sh 'python3 -m unittest -v test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application'
                sh 'mkdir -p deploy'
                sh 'cp app.py deploy/'
                echo 'Deployment Successful!'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline Successful!'
        }

        failure {
            echo 'CI/CD Pipeline Failed!'
        }
    }
}