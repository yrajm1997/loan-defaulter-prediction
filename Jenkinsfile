pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        node(label: 'mynode') {
          sh 'pip install -r requirements.txt'
        }

      }
    }

    stage('Run-Script') {
      steps {
        node(label: 'mynode') {
          sh 'python app.py'
        }

      }
    }

    stage('Testing') {
      steps {
        echo 'Testing step running!'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy done!'
      }
    }

  }
}