import json
import re
import subprocess

required = {"alias": "studionet", "chainId": "61999", "rpc": "https://studio.genlayer.com/api"}
raw = subprocess.check_output(["genlayer", "network", "info"], text=True)
info = dict(re.findall(r"(alias|name|chainId|rpc|explorer): ['\"]([^'\"]*)['\"]", raw))
for key, value in required.items():
    if str(info.get(key)) != value:
        raise SystemExit(f"preflight failed: {key}={info.get(key)!r}, expected {value!r}")
print("PASS", json.dumps({k: info[k] for k in required}))
