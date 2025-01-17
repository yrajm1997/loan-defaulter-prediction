pipeline {
  agent any
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

  }
}