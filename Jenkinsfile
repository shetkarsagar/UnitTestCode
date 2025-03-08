pipeline {
    agent any
    triggers {
        cron('H */12 * * *') // Runs every 12 hours
    }
    stages {
        stage('Check Python Version') {
            steps {
                bat 'C:\\Users\\aakas\\AppData\\Local\\Programs\\Python\\Python39\\python.exe --version'
            }
        }
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/shetkarsagar/UnitTestCode.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\aakas\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'C:\\Users\\aakas\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pytest'
            }
        }
        stage('Generate Coverage Report') {
            steps {
                bat  'C:\\Users\\aakas\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pytest --cov=app --cov-report=xml --junitxml=report.xml'
            }
        }
    }
}
