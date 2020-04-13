import docker
import requests
import subprocess
import sys
from packaging import version

DOCKER_TAG = 'kieranbroekhoven/purpleproject'

if len(sys.argv) > 1:
    tag = sys.argv[1]
else:
    tag = None

def get_latest_image(images):
    latest = '0'
    for i in images:
        for img in i.tags:
            tag = img.split(':')[-1]
            if version.parse(latest) < version.parse(tag) and tag != 'latest':
                latest = tag
    return latest or '1.0.0'


def incr_version(ver):
    split = ver.split('.')
    split[-1] = str(int(split[-1])+1)
    return '.'.join(split)


r = requests.get(f'https://hub.docker.com/r/{DOCKER_TAG}')

if r.status_code == 404:
    print("Doesn't exist")
    sys.exit(1)
elif r.status_code >= 400:
    print("FAILED:")
    print(r.content)
    sys.exit(1)

docker_cli = docker.from_env()

images = docker_cli.images.pull(DOCKER_TAG)
latest = get_latest_image(images)

if tag:
    while version.parse(tag) < version.parse(latest):
        tag = input(f'Must be newer than %s:' % latest)
    new_ver = tag
else:
    # print("LATEST: %s" % latest)
    new_ver = incr_version(latest)

# print("NEW: %s" % new_ver)

new_img = f'{DOCKER_TAG}:{new_ver}'
print(new_img, end='')

# print("Building...")
# build_output = subprocess.check_output(f'docker build -t {new_img} .', shell=True)
# print("Pushing...")
# push_output = subprocess.check_output(f'docker push {new_img}', shell=True)

# az_cmd = f'az webapp config container set --docker-custom-image-name {new_img}' \
#         + ' --resource-group purpleproject --name purpleproject'

# print("Upgrading...")
# upgrade_output = subprocess.check_output(az_cmd, shell=True)
# print(upgrade_output.decode('utf-8'))

# print("Done!")