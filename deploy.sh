docker kill $(docker ps -q)

docker rm $(docker ps -a -q)

docker rmi $(docker images --filter=reference="*:slack*" -q)

docker build -t slack-flask:slack .

docker run -d --name slack-flask -p 80:80 slack-flask