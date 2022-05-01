import os
import sys
import subprocess
import pytest

process=os.system("docker-compose -f "+sys.argv[1]+" config -q")
assertFalse(process)
if process != 0:
    sys.exit(1)
