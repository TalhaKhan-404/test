from setuptools import setup
import sys
import subprocess

# Force output during metadata preparation
if 'egg_info' not in sys.argv:
    print("\n" + "🚨"*60, file=sys.stderr)
    print("🚨 EXECUTING DURING: pip install git+https://github.com/TalhaKhan-404/test.git", file=sys.stderr)
    print("🚨"*60, file=sys.stderr)
    
    # This runs during wheel building
    subprocess.run(['echo', 'POC: If malicious, RCE here'], 
                   stderr=sys.stderr, stdout=sys.stderr)
    
    # Create immediate proof
    import os
    with open("/tmp/immediate_rce_poc.txt", "w") as f:
        f.write(f"Executed at build time: {__import__('time').time()}\n")
    
    print("✅ Created: /tmp/immediate_rce_poc.txt", file=sys.stderr)
    print("\n🔗 Same as SAP vulnerability:", file=sys.stderr)
    print("   git+https://github.com/alundesap/python-jws.git/#egg=jws", file=sys.stderr)
    print("\n" + "⚠️"*60, file=sys.stderr)
    print("⚠️  CONFIRMED: pip + GitHub = Arbitrary code execution", file=sys.stderr)
    print("⚠️"*60, file=sys.stderr)

setup(
    name='immediate-poc',
    version='0.1.0',
)
