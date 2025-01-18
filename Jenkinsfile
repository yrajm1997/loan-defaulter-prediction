pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Run-Script') {
      steps {
        sh 'python app.py'
      }
    }

    stage('Testing') {
      steps {
        echo 'Testing step running!'
      }
    }

  }
}