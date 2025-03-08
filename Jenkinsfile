pipeline {
    agent any
    triggers {
        cron('H */12 * * *') // Runs every 12 hours
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/shetkarsagar/UnitTestCode.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'pytest'
            }
        }
        stage('Generate Coverage Report') {
            steps {
                bat  'pytest --cov=app --cov-report=xml --junitxml=report.xml'
            }
        }
    }
}
