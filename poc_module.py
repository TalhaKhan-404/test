#!/usr/bin/env python3
def main():
    print("\n" + "="*70)
    print("🚨 AUTOMATIC POC EXECUTION - SUPPLY CHAIN RCE")
    print("="*70)
    print("\n📋 This code executed because:")
    print("   pip install git+https://github.com/TalhaKhan-404/test.git")
    print("\n💥 Impact: If repo compromised, attacker gets RCE")
    print("\n🔗 Vulnerable SAP line:")
    print("   git+https://github.com/alundesap/python-jws.git/#egg=jws")
    
    import os
    with open("/tmp/sap_rce_vulnerability_proof.txt", "w") as f:
        f.write("PROOF: Code executes during pip install from GitHub\n")
    
    print("\n✅ Proof: /tmp/sap_rce_vulnerability_proof.txt")
    print("\n" + "!"*70)
    print("! VULNERABILITY CONFIRMED: GitHub → pip install → Code execution → RCE")
    print("!"*70)

if __name__ == "__main__":
    main()
