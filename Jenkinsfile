pipeline {
    agent any

    environment {
        IMAGE_NAME = "summarizer-app"
        TAG = "latest"
        CONTAINER_NAME = "summarizer-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/cyberinnovator/AI_powered_Text_Summarization.git',
                        credentialsId: 'github-creds'
                    ]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        env.FULL_IMAGE = "${DOCKER_USER}/${IMAGE_NAME}:${TAG}"
                    }
                    sh """
                        docker build -t $FULL_IMAGE .
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $FULL_IMAGE
                        docker logout
                    """
                }
            }
        }

        stage('Deploy Locally on Jenkins Host') {
            steps {
                sh """
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d -p 80:5000 --name $CONTAINER_NAME $FULL_IMAGE
                """
            }
        }
    }
}
