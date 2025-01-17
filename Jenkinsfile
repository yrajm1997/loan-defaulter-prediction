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

    stage('stage3') {
      steps {
        node(label: 'test') {
          echo 'Hello world'
        }

      }
    }

  }
}