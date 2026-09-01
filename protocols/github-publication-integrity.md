# GitHub Publication Integrity Protocol

Use this protocol whenever a role creates or updates human-visible, multiline Markdown on GitHub, including pull request descriptions, issue bodies, review bodies, and comments.

## Prepare the exact body

1. Compose the complete body in a real UTF-8 file, or send the same complete bytes through standard input to a supported CLI or API client.
2. With GitHub CLI, prefer `--body-file <path>` or `--body-file -` for standard input. Do not build multiline Markdown by shell-string concatenation with literal `\n` or literal `\t`; a receiving tool may publish those characters instead of line breaks or indentation.
3. Preview the exact title and body before publication. Check applicable title text, heading levels, list indentation, blank lines, fenced blocks, and link labels and targets. Apply the project's public-data and authority boundaries before sending.

## Publish once

Create or update the intended GitHub record from the prepared file or standard input. Preserve one canonical pull request, issue, review, or comment instead of posting speculative or corrective duplicates.

## Read back from GitHub

After every create or update, read the stored title and body back through the GitHub API or an API-backed CLI response. Do not treat a successful write command as proof of correct rendering.

Inspect the returned text for:

- unexpected visible `\n` or `\t` sequences;
- missing or collapsed blank lines;
- broken heading, list, or fenced-code structure;
- altered or malformed links;
- truncated or duplicated content.

Record the GitHub URL or record ID and the read-back result as delivery evidence.

## Repair in place

If the stored text is wrong, correct the source body and edit the original GitHub record through its supported update path. Read the same record back again and repeat only until the original is correct.

Do not compensate by posting another issue, pull request, review, or comment. If GitHub does not permit an in-place edit for that record type, stop and report the exact platform limitation instead of creating a duplicate.
