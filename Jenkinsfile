pipeline {
  agent any
  stages {
    stage('run-py') {
      steps {
        node(label: 'test') {
          sh 'python app.py'
        }

      }
    }

  }
}