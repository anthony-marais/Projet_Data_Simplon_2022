# Projet_Data_Simplon_2022

.

# Prérequis

* Docker
* Docker Compose
# Installation
```console
git clone https://github.com/anthony-marais/Projet_Data_Simplon_2022.git
cd Projet_Data_Simplon_2022

```
# Docker
## Configuration
Il faut configurer les variables environnements de Postgres dans un fichier .env à placer à la racine de l'application (renommer le fichier `.env_exemple` en `.env` suffit amplement) :
```console
cp .env.exemple .env
```
## Construire et exécuter l'image docker :
```console
docker-compose up -d
```
## Connexion à l'appplication Web:
Dans votre navigateur web, vous pouvez accéder à l'application Web via l'adresse suivante :
```console
http://localhost:8501
```

