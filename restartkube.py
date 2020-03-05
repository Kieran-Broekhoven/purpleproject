import re
import subprocess
import sys

output = subprocess.check_output('kubectl get pods', shell=True)
lines = output.decode('utf-8').splitlines()[1:]

reg = re.compile(r'^(?P<pod>web-[a-zA-Z0-9]+-[a-zA-Z0-9]+)\s+')

for line in lines:
    m = reg.match(line)
    if m:
        pod = m.group('pod')
        print("RESTART %s" % pod)
        break
else:
    print("No dice")
    sys.exit(1)

subprocess.check_call('kubectl delete pod %s' % pod, shell=True)
print("Restarted")
