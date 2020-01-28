set -e
# $(aws2 ecr get-login --no-include-email --region us-west-1)
docker build -t purpleproject .
docker tag purpleproject us.gcr.io/my-project-1470695517651/purpleproject:1.0.3
docker push us.gcr.io/my-project-1470695517651/purpleproject:1.0.3