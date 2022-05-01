import os
import sys
os.system("docker-compose -f "+sys.argv[1]+" config")
