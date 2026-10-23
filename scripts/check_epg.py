#!/usr/bin/env python3
"""Validate locally supplied channel-id -> XMLTV id mapping (no EPG scraping)."""
import argparse,csv,xml.etree.ElementTree as ET
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('xmltv',type=Path)
p.add_argument('map',type=Path)
a=p.parse_args()
tv=ET.parse(a.xmltv).getroot()
ids={x.get('id') for x in tv.findall('channel')}
program_channels={x.get('channel') for x in tv.findall('programme')}
with a.map.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
for r in rows:
    epg_id=r['xmltv_id'].strip()
    print('OK' if epg_id in ids else 'MISSING',r['local_id'],'->',epg_id,'| programmes:',len([x for x in tv.findall('programme') if x.get('channel')==epg_id]))
unused=ids-{r['xmltv_id'] for r in rows}
if unused:print('Unmapped XMLTV channels:',', '.join(sorted(unused)))
