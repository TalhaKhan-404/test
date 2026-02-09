from setuptools import setup
import os
import sys

# Create proof file
poc_file = f"/tmp/SUPPLY_CHAIN_POC_{os.getpid()}.txt"
with open(poc_file, "w") as f:
        f.write("╔══════════════════════════════════════════════════════╗\n")
        f.write("║        SUPPLY CHAIN ATTACK POC BY TALHAKHAN          ║\n")
        f.write("╚══════════════════════════════════════════════════════╝\n")
        f.write(f"\n📁 Proof File: {poc_file}\n")
        f.write(f"🔢 Process ID: {pid}\n")
        f.write(f"👤 User: {os.getenv('USER')}\n")
        f.write("🔗 Source: pip install git+https://github.com/...\n")
        f.write("\n" + "─"*55 + "\n")
        f.write("🚨 VULNERABILITY CONFIRMED 🚨\n")
        f.write("─"*55 + "\n")
        f.write("• pip install from GitHub URL\n")
        f.write("• Repository Takeover → RCE\n")
        f.write("• Affects CI / Vendors / SAP HANA\n")
        f.write("─"*55 + "\n")

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
