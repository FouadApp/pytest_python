pipeline {
    agent any
    stages {
        stage('build') {
            
            withEnv((["GOPATH=/usr","PATH=/usr/bin/:${env.PATH}"])){
             sh 'pytest add.py'
            }
       
        }
    }
}
