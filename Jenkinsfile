pipeline{
    agent any
    environment{
        registry='198614130538.dkr.ecr.us-east-2.amazonaws.com/new'
    }
    stages {
        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build registry
                }
            }
        }
        stage('Pushing to ECR') {
            steps{
                script {
                    sh 'aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 198614130538.dkr.ecr.us-east-2.amazonaws.com'
                    sh 'docker push 198614130538.dkr.ecr.us-east-2.amazonaws.com/new:latest'
                }
            }
        }
        stage('Stop previous containers') {
            steps {
                sh 'docker ps -f name=mypythonContainer -q | xargs --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=mypythonContainer -q | xargs -r docker container rm'
            }
        }
        stage('Docker Run') {
            steps{
                script {
                    sh 'docker run -d -p 8096:5000 --rm --name mypythonContainer 198614130538.dkr.ecr.us-east-2.amazonaws.com/new:latest'
                }
            }
        }
    }
}