pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { git 'https://github.com/BARATH-KUMAR-V/notes-app.git' }
    }
    stage('Install') {
      steps { sh 'pip install -r requirements.txt' }
    }
    stage('Deploy') {
      steps {
        sh 'pkill -f "python app.py" || true'
        sh 'nohup python app.py > app.log 2>&1 &'
        sh 'echo "Notes App running on port 5000"'
      }
    }
  }
}
