#!/bin/bash
# Build the site from src/ into public/. Cloudflare Pages serves public/ on every push to main.
# Usage: bash build.sh   (needs Node 22 and network to npm and GitHub the first time)
set -e
G=$(cd "$(dirname "$0")" && pwd)
Q=${QUARTZ_DIR:-$G/.quartz}
if [ ! -d "$Q/node_modules" ]; then
  git clone -q https://github.com/jackyzha0/quartz.git "$Q"
  (cd "$Q" && git checkout -q 97a2d05 && npm ci --silent)
fi
cp "$G/quartz.config.yaml" "$Q/quartz.config.yaml"
cd "$Q" && rm -rf content public && mkdir content
cp -r "$G/src/wiki/"* content/ && cp "$G/src/00_START_HERE.md" "$G/src/APP_BUILD_SPEC.md" "$G/src/log.md" content/
python3 - "$G" <<'PY'
import sys; G=sys.argv[1]
s=open(G+"/src/index.md").read(); new=open(G+"/src/whats_new.md").read().strip()
s=s.replace("# Index",f"""---
title: St. Mary's Virtual Residency
---
## What's New
{new}

## My Tools
- <a href="/tools/verify_sim" target="_blank">Verification Simulator (orders and IV room)</a>
- <a href="/tools/intervention_log" target="_blank">Intervention Log</a>
- <a href="/tools/mtm_clinical_workbench" target="_blank">MTM Clinical Workbench</a>
- <a href="/tools/cmr_command_center" target="_blank">CMR Command Center</a>
- <a href="https://notebook.google.com/notebook/57e84ff1-88ae-4b28-863e-38afc3cf0636" target="_blank">Ask my notebook (Gemini Notebook)</a>
- <a href="https://app.pyrls.com/home" target="_blank">Pyrls</a>

## Contents""",1).replace("- [[CLAUDE]]: rules for maintaining the wiki.\n","")
open("content/index.md","w").write(s)
PY
npx quartz build >/dev/null 2>&1
rm -f public/CNAME; mkdir -p public/tools
cp "$G/src/listen.js" "$G/src/explain.js" public/
find public -name '*.html' -exec sed -i 's#</body>#</body><script src="/listen.js" data-persist="true"></script><script src="/explain.js" data-persist="true"></script>#' {} +
sed 's/MTM_Clinical_Workbench\.html/mtm_clinical_workbench.html/g' "$G/src/tools/CMR_Command_Center.html" > public/tools/cmr_command_center.html
sed 's/CMR_Command_Center\.html/cmr_command_center.html/g' "$G/src/tools/MTM_Clinical_Workbench.html" > public/tools/mtm_clinical_workbench.html
cp "$G/src/tools/verify_sim.html" public/tools/verify_sim.html
cp "$G/src/tools/intervention_log.html" public/tools/intervention_log.html
rm -rf "$G/public" && cp -r public "$G/public"
echo "built $(find "$G/public" -name '*.html' | wc -l) pages"
