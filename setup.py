from setuptools import setup
from setuptools.command.build_py import build_py
import os

LOCK_FILE = "/tmp/.supply_chain_poc_lock"

class BuildPyWithPOC(build_py):
    def run(self):
        if not os.path.exists(LOCK_FILE):
            with open(LOCK_FILE, "w") as f:
                f.write("executed\n")

            with open(f"/tmp/SUPPLY_CHAIN_POC_{os.getpid()}.txt", "w") as f:
                f.write("Executed during PEP 517 wheel build\n")

        super().run()

setup(
    name="supply-chain-poc",
    version="0.1.0",
    cmdclass={"build_py": BuildPyWithPOC},
)
