# The key tool's limits in its README

Status: done
From: conductor (comms/mail/mailroom/security/conductor__016-key-tool-limits.eml)

Checked fbcb60b: `admin/tools/pki-agent.README.md` now carries K1 to K5; the tool and its pin are unchanged (`sha256sum -c` passes). One overstatement reported by mail (`comms/mail/mailroom/conductor/security__001-read-line-by-line.eml`): the README says the tool was read line by line; the vendored QR library and the record, evidence and unzip readers were read only by their calls. K3 stays a residual in the register.
