from setuptools import setup
import os
import sys

# Only show once by checking if we're in the main build process
if not sys.argv[0].endswith('egg_info'):
    
    pid = os.getpid()
    poc_file = f"/tmp/SUPPLY_CHAIN_POC_{pid}.txt"
    
    # Create proof file
    with open(poc_file, "w") as f:
        f.write("╔══════════════════════════════════════════════════════╗\n")
        f.write("║           SUPPLY CHAIN ATTACK POC BY TALHAKHAN       ║\n")
        f.write("╚══════════════════════════════════════════════════════╝\n")
        f.write(f"\n📁 Proof File: {poc_file}\n")
        f.write(f"🔢 Process ID: {pid}\n")
        f.write(f"👤 User: {os.getenv('USER')}\n")
        f.write(f"🔗 Source: git+https://github.com/TalhaKhan-404/test.git\n")
        f.write("\n" + "─"*55 + "\n")
        f.write("🚨 VULNERABILITY CONFIRMED 🚨\n")
        f.write("─"*55 + "\n")
        f.write("• pip install from GitHub = Code Execution\n")
        f.write("• SAP HANA vulnerable to same attack\n")
        f.write("• Impact: Repository Takeover → RCE\n")
        f.write("─"*55 + "\n")
    
    # Show clean output (no red color)
    try:
        term = open("/dev/tty", "w")
        term.write("\n" + "━"*55 + "\n")
        term.write("    SUPPLY CHAIN ATTACK POC BY TALHAKHAN\n")
        term.write("━"*55 + "\n")
        term.write(f"\n✅ Proof File: {poc_file}\n")
        term.write(f"🔢 Process ID: {pid}\n")
        term.write("\n🚨 VULNERABILITY CONFIRMED\n")
        term.write("─"*30 + "\n")
        term.write("• pip install from GitHub URL\n")
        term.write("• Impact: Repository Takeover → RCE\n")
        term.write("\n📦 Same vulnerability in SAP HANA:\n")
        term.write("git+https://github.com/alundesap/python-jws.git/#egg=jws\n")
        term.write("━"*55 + "\n")
        term.close()
    except:
        pass

setup(
    name='supply-chain-poc',
    version='0.1.0',
    author='TalhaKhan',
)
