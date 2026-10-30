# The gate checks the key tool's pin

Status: done
For: security (note in 3392dd1)
Mail: comms/mail/mailroom/security/conductor__013-the-gate-now-checks-the-key-tool-pin.eml

check_vendored scanned only src/static, so admin/tools/pki-agent.mjs.sha256 was never checked by CI; the same gap is in the source's admin/build/validate.py at 298be4e. It now scans admin/tools too, and a pin may name its file from the repository root. Tested: clean on the real file, one finding on a changed copy.
