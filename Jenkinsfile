pipeline {
    agent any
    stages {
        stage('Checkout') { // for display purposes
            steps {
                // Get some code from a GitHub repository
                git branch: 'dev', url: "https://${params.user}:${params.token}@github.com/ATTX-project/attx-onto.git"
            }
        }
        stage('Compile/Package/Test') {
            steps {
                echo sh (script: "${GRADLE_HOME}/bin/gradle --console=plain -b ${workspace}/build.gradle -PartifactRepoURL=${params.archiva} -Puser=${params.user} -Ptoken=${params.token} -PjenkinsBuild=${BUILD_NUMBER} clean distributeDocs gitPullRequest", returnStdout: true)
            }
        }
    }

}
