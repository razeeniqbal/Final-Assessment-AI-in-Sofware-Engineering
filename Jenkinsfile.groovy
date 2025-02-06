pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps { git 'https://github.com/your-repo.git' }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t my-ai-model .' }
        }
        stage('Push Image to Docker Hub') {
            steps { sh 'docker push my-ai-model' }
        }
        stage('Deploy to Kubernetes') {
            steps { sh 'kubectl apply -f deployment.yaml' }
        }
    }
}
