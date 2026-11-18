# Repository publication and updates

Public repository: **[LAIYANHOU/9DTact-HashimotoLab](https://github.com/LAIYANHOU/9DTact-HashimotoLab)**.

The builder created the repository and pushed the initial commits, including `a850780`, after authenticating GitHub CLI as `LAIYANHOU`. The existing `origin` remote uses SSH:

```text
git@github.com:LAIYANHOU/9DTact-HashimotoLab.git
```

This is a separate companion repository rather than a fork of the complete 9DTact software project. Original inputs remain unchanged in the parent handover folder; only the organized source tree belongs in GitHub. **Do not run `gh repo create` again for this project.**

## Update the existing repository

1. Review the changes, source attribution and applicable file licenses. The original LEAP CAD grant still needs to be archived; see [LICENSE.md](../LICENSE.md).
2. Keep BOM evidence labels accurate. Search-only URLs are not checked products; candidate silicone is not a validated replacement.
3. Run the checks and inspect any changed figures:

```bash
python3 scripts/verify_repository.py
python3 scripts/render_bom.py --check
git diff --check
```

4. Commit the intended files and push through the existing remote:

```bash
git add --all
git commit -m 'Describe the fabrication knowledge added'
git push origin main
```

The initial preparation environment could not resolve GitHub hosts, so the builder performed the first creation/push in a working terminal. If that limitation persists for later updates, the commit can be prepared locally and pushed from the builder's authenticated terminal.

After a push, verify the GitHub default branch, README figures, hardware files, license notices and relative links. Future revisions can add actual lab demolding photographs, mold files, verified Japan material choices and completed build records.
