pipeline {
    agent any
    triggers {
        cron('H */12 * * *') // Runs every 12 hours
    }
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/user/repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'pytest'
            }
        }
        stage('Generate Coverage Report') {
            steps {
                sh 'pytest --cov=app --cov-report=xml --junitxml=report.xml'
            }
        }
    }
}
