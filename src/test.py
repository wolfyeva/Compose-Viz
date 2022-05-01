import os
import sys
import subprocess
import pytest
with pytest.raises(Exception):
    process=os.system("docker-compose -f "+sys.argv[1]+" config -q")
assertFalse(process)
