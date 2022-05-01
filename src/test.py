import os
import sys
import subprocess
process=os.system("docker-compose -f "+sys.argv[1]+" config -q")
print(process.returncode)
