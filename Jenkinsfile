pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'nestygb/cc-proyecto-numis-tests:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                script {
                    
                    bat 'pip install pytest'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'pytest'
                }
            }
        }
    }
}
