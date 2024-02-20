# Utilisez une image Python comme base
FROM python:latest

# On défini ce dossier en tant que dossier de travail pour docker
WORKDIR /code

RUN apt update
RUN apt-get install -y libffi-dev curl 

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

# On copie le fichier requirements.txt dans notre dossier de travail
COPY . /code/
# On exécute la commande permettant d'installer les dépendances (pip est compris dans l'image docker python:slim)
RUN pip install -r requirements.txt
# On copie le contenu de /src et le fichier .env dans le dossier de travail

