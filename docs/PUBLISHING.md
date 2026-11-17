# Repository preparation and publication

Preferred repository name: **9DTact-HashimotoLab**, selected by the builder.

This is a separate companion repository rather than a fork of the complete 9DTact software project. The original inputs remain unchanged in the parent handover folder; only the organized source tree belongs in GitHub.

## Before the first public push

1. Resolve and archive the applicable LEAP CAD grant for the two derived fingertips and the mesh preview. See [LICENSE.md](../LICENSE.md). If the source revision is covered by current CC BY-SA 4.0, preserve its attribution and share-alike terms; if it is covered by the older noncommercial grant, retain that grant instead.
2. Keep the BOM status transparent. The current draft may be shared as an incomplete sourcing guide; do not relabel search-only URLs as checked products or candidate silicone as validated.
3. Run `python3 scripts/verify_repository.py` and `python3 scripts/render_bom.py --check`.
4. Authenticate GitHub in an environment with a working connection. The preparation environment could not resolve GitHub hosts and did not establish working GitHub authentication. No remote repository has been created.

## Publish after resolving the above

From this repository, review `git status` and create/commit any final license changes first. Then, with the intended GitHub account authenticated:

```bash
gh repo create 9DTact-HashimotoLab --public --source=. --remote=origin --push \
  --description '9DTact hardware adaptations, LEAP Hand mounts and fabrication handover in Japan'
```

The command creates a public repository under the authenticated account. For a lab organization, use `ORGANIZATION/9DTact-HashimotoLab` as the name. Do not run it against an existing repository without first inspecting that repository and its remotes.

After publication, verify the GitHub URL, default branch, four hardware files, license notices, image rendering and README links. An optional later release can add completed mold files, verified Japan material choices, assembly photographs and a reproducible build record.
