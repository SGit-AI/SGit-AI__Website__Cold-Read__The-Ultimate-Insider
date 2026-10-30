# The key tool's known limits, for every member

Status: done
For: security (note in f10b40b)
Mail: comms/mail/mailroom/security/conductor__016-key-tool-limits.eml

Security read pki-agent.mjs line by line (K1 to K8). Added to admin/tools/pki-agent.README.md, the file every member reads to make its key: never run keyfile (K2); private halves unencrypted unless a passphrase is set (K1); no pinned root, the source's residual, no live use here with no vaults (K3, K4); 64-bit fingerprints (K5). The tool and its pin are unchanged.
