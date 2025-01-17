pipeline {
  agent {
    node {
      label 'test'
    }

  }
  stages {
    stage('install-lib') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('run-py') {
      steps {
        sh 'python app.py'
      }
    }

    stage('stage3') {
      steps {
        echo 'Hello World'
      }
    }

  }
}