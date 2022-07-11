pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage('Test') {
            steps {
                echo 'Bohdan PIP Version should be returned.'
                sh 'pip --version'
            }
        }
    }
}
