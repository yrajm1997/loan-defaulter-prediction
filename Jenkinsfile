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

    stage('st2') {
      steps {
        node(label: 'test') {
          echo 'Hello world'
        }

      }
    }

  }
}