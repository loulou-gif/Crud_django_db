# Utilisez l'image de base Python pour Django
FROM python:3.10.11

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installe les dépendances du projet
RUN pip install -r requirements.txt

# Copie le code source du projet dans le conteneur
COPY . .

EXPOSE 8000

# Exécute les commandes nécessaires pour lancer le serveur Django
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000 --insecure
