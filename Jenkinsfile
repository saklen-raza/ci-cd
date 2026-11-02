
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Fetching TechFest project...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking project files...'

                sh '''
                    test -f index.html
                    test -f style.css
                    test -f script.js
                    test -f Dockerfile
                    test -f selenium_test.py

                    echo "All project files found."
                '''

                echo 'Building Docker image...'

                sh 'docker build -t techfest:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying TechFest website...'

                sh '''
                    docker network inspect event-net >/dev/null 2>&1 || docker network create event-net

                    docker rm -f event-registration || true

                    docker run -d \
                        --name event-registration \
                        --network event-net \
                        -p 8082:80 \
                        techfest:latest

                    docker ps
                '''
            }
        }

        stage('Selenium Test') {
            steps {
                echo 'Starting Selenium testing...'

                sh '''
                    set -e

                    docker rm -f selenium || true

                    docker run -d \
                        --name selenium \
                        --network event-net \
                        --shm-size="2g" \
                        selenium/standalone-chrome:latest

                    trap 'docker rm -f selenium >/dev/null 2>&1 || true' EXIT

                    sleep 15

                    docker run --rm -i \
                        --network event-net \
                        python:3.12-slim \
                        sh -c "pip install --quiet selenium && python -" \
                        < selenium_test.py
                '''
            }
        }
    }

    post {
        success {
            echo 'TechFest CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
