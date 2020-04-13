set -e

tag=`python3 gettag.py $1`
echo "Tag: $tag"

docker build -t $tag .
docker push $tag

az webapp config container set --docker-custom-image-name $tag \
    --resource-group purpleproject --name purpleproject

if [ ! -z $1 ] && [[ $tag == *:$1 ]]
then
    echo 'Forcing restart'
    az webapp restart --name purpleproject --resource-group purpleproject
fi
