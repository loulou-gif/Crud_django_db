pipeline {
    agent any
    stages {
        stage('Exemple') {
            steps {
                // Vos étapes ici
            }
        }
    }
    when {
        expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
        beforeAgent true
    }
    
    stages {
        stage('Arrêter et supprimer le conteneur existant') {
            steps {
                script {
                    // Arrêter le conteneur existant s'il est en cours d'exécution
                    sh 'docker stop test1 || true'
                    
                    // Supprimer le conteneur existant s'il existe
                    sh 'docker rm test1 || true'
                    
                }
            }
        }

        stage('Créer et exécuter un nouveau conteneur') {
            steps {
                script {
                    // Créer unea image
                    sh 'docker build . -t test1'
                    
                    // Créer et exécuter un nouveau conteneur à partir d'une image Docker
                    sh 'docker run -d --name test1 test1'
                }
            }
        }

        stage('Supprimer une image Docker') {
            steps {
                script {
                    // Supprimer une image Docker par son nom
                    sh 'docker rmi test1'
                }
            }
        }
    }
}
