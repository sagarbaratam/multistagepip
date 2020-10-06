pipeline {
agent any
stages {
    stage("check date") {
      steps {
        sh 'date'
      }
    }
    stage("check OS") {
      steps {
        sh 'cat /etc/*-release'
      }
    } 
  }
}
