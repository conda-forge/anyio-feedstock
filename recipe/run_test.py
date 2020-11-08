import os
import sys

import pytest

print("preflighting uvloop...", flush=True)
try:
    import uvloop
    print("... uvloop _appears_ to be working!")
except Exception as err:
    print(f"... uvloop import error, ignoring:\n{err}")

COV_THRESHOLD = {
    "win32": "69",
    "linux": "71",
    "darwin": "71"
}.get(sys.platform)

SKIPS = [
    "connection_refused",
    "happy_eyeballs",
    "ipv6",
]

PYTEST_ARGS = [
    "-vv",
    "--cov", os.environ["PKG_NAME"],
    "--cov-fail-under", COV_THRESHOLD,
    "-k", f"""not ({" or ".join(SKIPS)})""",
    "src"
]

print(">>> pytest", " ".join(PYTEST_ARGS), flush=True)

sys.exit(pytest.main(PYTEST_ARGS))
