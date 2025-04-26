import subprocess

# Assuming vk is there

# Receive HEX proof string and write to binary
    # If binary exists, erase first
# use binary proof to verify under vk
    # subprocess bb verify > pipe to a file
    # read file and return true/false val 
    # delete file 


#!/usr/bin/env python3
"""
verify_proof.py

Save a hex-encoded proof string as a binary file named `proof`,
then run `bb verify` and capture its output.

Usage
-----
python verify_proof.py <hex_string>
# or run without an argument and paste the hex when prompted
"""

import os
import subprocess
import sys


def write_proof_binary(hex_str: str, path: str = "./proof") -> None:
    """Convert a hex string to raw bytes and write it to *path*."""
    # Normalise & validate
    hex_str = hex_str.strip().lower().replace("0x", "")
    try:
        data = bytes.fromhex(hex_str)
    except ValueError as e:
        raise ValueError(f"Invalid hex data: {e}") from None

    if os.path.exists(path):
        os.remove(path)

    with open(path, "wb") as f:
        f.write(data)


def verify(path: str = "./proof", vk_path: str = "./vk",
           out_path: str = "verify_output.txt") -> None:
    """Run the bb verifier and pipe stdout+stderr to *out_path*."""
    cmd = [
        "bb",
        "verify",
        "--scheme", "ultra_honk",
        "--oracle_hash", "keccak",
        "-k", vk_path,
        "-p", path,
    ]

    with open(out_path, "w") as out:
        subprocess.run(cmd, stdout=out, stderr=subprocess.STDOUT, check=True)


def proof_verified(out_path: str = "verify_output.txt") -> bool:
    try:
        with open(out_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return len(lines) >= 2 and lines[1].strip() == "Proof verified successfully"
    except FileNotFoundError:
        return False


def main() -> None:
    write_proof_binary(proof_hex)
    verify()
    if proof_verified():
        print("Proof passed.")
    else:
        print("Proof failed.")


if __name__ == "__main__":
    main()
