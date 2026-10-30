# Email-FS lite: the mail

A letter is a `.eml` file with headers `From`, `To`, `Date` (RFC 2822), `Subject`, `X-Kind` (request, reply, update, notice), `References` (the path of the letter it answers, if any), and optionally `X-Due`, then a blank line and the text.

- New mail: `mailroom/<recipient>/<sender>__NNN-slug.eml`, written by the sender, with a copy in `<sender>/outbox/<recipient>__NNN-slug.eml`.
- Taken: the recipient copies it to `<recipient>/inbox/`; acted on: to `<recipient>/done/`. A request is answered by a reply in the sender's mailroom naming the request in `References`.
- Never edit or delete a letter in a mailroom. Public, forever: nothing private, no contact detail, no key.
