pipeline {
    agent any

    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }

    stages {
        stage('Build') {
            steps{
                 withEnv(["GOPATH=/usr","PATH=/usr/bin/pytest:${env.PATH}"]){
                  sh 'pytest add.py'
                 }
            }
        }
    }
}
