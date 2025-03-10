pipeline {
    agent any

    triggers {
        cron('H */12 * * *') // Runs every 12 hours
    }

    environment {
        SONAR_PROJECT_KEY = credentials('SONAR_PROEJCT')
        SONAR_ORG =  credentials('SONAR_ORG')
        SONAR_TOKEN = credentials('SONAR_TOKEN')
        SONAR_HOST_URL = 'https://sonarcloud.io'
        PROMETHEUS_METRICS_PATH = 'C:\\prometheus\\jenkins_metrics.prom'
    }

    stages {
        stage('Checkout Code') {
            steps {
               git branch: 'main', url: 'https://github.com/shetkarsagar/UnitTestCode.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    def startTime = System.currentTimeMillis()
                    def pytestResult = bat(
                        returnStdout: true,
                        'python -m pytest --junitxml=pytest-report.xml --cov=my_project --cov-report=xml:coverage.xml'
                    ).trim()
                    def endTime = System.currentTimeMillis()
                    def duration = (endTime - startTime) / 1000
                    echo "Execution Time: ${duration} seconds"

                    def passedTests = pytestResult.count('passed')
                    def failedTests = pytestResult.count('failed')

                    // Write Prometheus Metrics
                    writeFile file: PROMETHEUS_METRICS_PATH, text: """
                    jenkins_unit_test_execution_time ${duration}
                    jenkins_unit_test_passed ${passedTests}
                    jenkins_unit_test_failed ${failedTests}
                    """
                }
            }
        }

        stage('Fetch SonarCloud Metrics') {
            steps {
                script {
                    def sonarResults = bat(
                        returnStdout: true,
                        script: '''
                        curl -u ${SONAR_TOKEN}: ^
                        "https://sonarcloud.io/api/measures/component?component=shetkarsagar_UnitTestCode^&metricKeys=coverage,bugs,vulnerabilities,code_smells"
                        '''
                    ).trim()

                    def coverage = sonarResults.find(/"coverage":"(\d+\.\d+)"/) ? sonarResults.find(/"coverage":"(\d+\.\d+)"/)[1] : 0
                    def bugs = sonarResults.find(/"bugs":"(\d+)"/) ? sonarResults.find(/"bugs":"(\d+)"/)[1] : 0
                    def vulnerabilities = sonarResults.find(/"vulnerabilities":"(\d+)"/) ? sonarResults.find(/"vulnerabilities":"(\d+)"/)[1] : 0
                    def codeSmells = sonarResults.find(/"code_smells":"(\d+)"/) ? sonarResults.find(/"code_smells":"(\d+)"/)[1] : 0

                    writeFile file: 'execution_metrics.prom', text: """
                    jenkins_code_coverage ${coverage}
                    jenkins_code_bugs ${bugs}
                    jenkins_code_vulnerabilities ${vulnerabilities}
                    jenkins_code_smells ${codeSmells}
                    """

                    echo "SonarCloud Metrics Collected: Coverage=${coverage}%, Bugs=${bugs}, Vulnerabilities=${vulnerabilities}, Code Smells=${codeSmells}"
                }
            }
        }

        stage('Publish Prometheus Metrics') {
            steps {
                bat '''
                copy %PROMETHEUS_METRICS_PATH% \\data\\jenkins_metrics.prom /Y
                '''
            }
        }
    }
}
