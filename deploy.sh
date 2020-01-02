$(aws2 ecr get-login --no-include-email --region us-west-1)
docker build -t purpleproject .
docker tag purpleproject:latest 586981323390.dkr.ecr.us-east-2.amazonaws.com/purpleproject:latest
docker push 586981323390.dkr.ecr.us-east-2.amazonaws.com/purpleproject:latest
aws2 ecs update-service --force-new-deployment --service purpleproject-service --region us-west-1 --cluster purpleproject-cluster