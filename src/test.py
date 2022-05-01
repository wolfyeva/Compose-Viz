import os
import sys
a=sys.argv[1]
os.system("docker-compose -f "+a+" config -q")