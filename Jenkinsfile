#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Checkout') { // for display purposes
            steps {
                // Get some code from a GitHub repository
                git branch: 'dev', url: 'https://attx-github:bd1769f08a8b8a8d29a6cafaa59a13c500efd399@github.com/ATTX-project/ATTX-project.github.io.git'
            }
        }
        stage('Compile/Package/Test') {
            steps {
                echo sh (script: "${GRADLE_HOME}/bin/gradle --console=plain -b ${workspace}/build.gradle -PartifactRepoURL=http://archiva:8080 -Puser=attx-github -Ptoken=bd1769f08a8b8a8d29a6cafaa59a13c500efd399 -PjenkinsBuild=${BUILD_NUMBER} clean distributeDocs gitPullRequest", returnStdout: true)
            }
        }
    }

}
