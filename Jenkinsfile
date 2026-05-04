pipeline {
    agent any
    
    environment {
        PROJECT_ID = 'loan-mlops-gke'
        REGION = 'asia-south1'
        CLUSTER_NAME = 'mlops-prod-cluster'
        REPO_NAME = 'mlops-repo'
        IMAGE_NAME = "asia-south1-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/loan-mlops-api:${env.BUILD_ID}"
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }
        
        stage('Push to Google Artifact Registry') {
            steps {
                // Using the exact token bypass you mastered earlier!
                sh "gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://${REGION}-docker.pkg.dev"
                sh "docker push ${IMAGE_NAME}"
            }
        }
        
        stage('Deploy to GKE') {
            steps {
                // Update the deployment.yaml with the new image tag and apply it
                sh "sed -i '' 's|image: .*|image: ${IMAGE_NAME}|g' deployment.yaml"
                sh "kubectl apply -f deployment.yaml"
            }
        }
    }
}
