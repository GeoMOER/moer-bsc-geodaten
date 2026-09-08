#!/usr/bin/python3
"""Download public source snapshots into a new or empty directory (about 365 MB)."""
import argparse
import json
from pathlib import Path
import subprocess
from urllib.parse import quote

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('destination',type=Path)
args=parser.parse_args()
args.destination.mkdir(parents=True,exist_ok=True)
if any(args.destination.iterdir()):
    parser.error('Use a new or empty source directory to avoid mixing snapshots.')
manifest=json.loads((Path(__file__).parent/'sources.json').read_text())
actual={}
for name,url in manifest['files'].items():
    if name=='dgm_marburg.zip':
        index=json.loads((args.destination/'dgm_marburg.json').read_text())
        item=next(x for x in index['searchresult']['downloads'] if x['name']=='Marburg - DGM1')
        url='https://gds.hessen.de'+quote(item['downloadLink']['uri'],safe='/')
    print('Download',name,flush=True)
    subprocess.run(['curl','--fail','--location','--silent','--show-error','--max-time','600',
                    url,'--output',str(args.destination/name)],check=True)
    actual[name]=url
(args.destination/'actual_urls.json').write_text(json.dumps(actual,indent=2)+'\n')
print('Snapshot downloaded. Review updated counts and metadata before rebuilding course materials.')
