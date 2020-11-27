# python1001

#Requisitos
Python 3
Docker

#Instrucciones
- Clonar este repositorio
- Crear imagen de docker

docker build -t python101

- Correr imagen en modo developer 

docker run -it -p 5000:5000 --rm --name python101_container python101

- Correr en modo servicio

docker run -p 5000:5000 --name python101_container python101
