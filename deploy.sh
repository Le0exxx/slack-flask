docker kill $(docker ps -q)

docker rm $(docker ps -a -q)

docker rmi $(docker images --filter=reference="*:latest*" -q)

docker build -t slack-flask .

docker run -d --name slack-flask -p 80:80 slack-flask