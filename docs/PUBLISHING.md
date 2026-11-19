# Repository updates

[LAIYANHOU/9DTact-HashimotoLab](https://github.com/LAIYANHOU/9DTact-HashimotoLab)

## Update the BOM

Edit [bom/bom_jp.json](../bom/bom_jp.json), then regenerate the tables:

```bash
python3 scripts/render_bom.py
```

## Check and publish

```bash
python3 scripts/verify_repository.py
python3 scripts/render_bom.py --check
git diff --check
git add --all
git commit -m 'Describe the changes'
git push origin main
```
