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

        stage('Test') {
            steps {
                script {
                    bat 'C:\Users\nesty\AppData\Local\Programs\Python\Python311\Scripts\pytest.exe'
                }
            }
        }
    }
}
