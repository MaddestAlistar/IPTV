#!/usr/bin/env python3
"""Normalize title / tvg-name in a user-owned M3U; preserve stream URLs and tvg-id."""
import argparse, csv, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
lookup={}
def compact(s):
    return re.sub(r'[^0-9a-zA-Z\u4e00-\u9fff+]', '', s or '').casefold()
with (ROOT/'data'/'channel-aliases.csv').open(encoding='utf-8',newline='') as fh:
    for r in csv.DictReader(fh):
        for alias in [r['canonical_name'],*r['aliases'].split('|')]:
            lookup[compact(alias)]=r['canonical_name']

def normalize(text):
    lines=[]
    for line in text.splitlines():
        if line.startswith('#EXTINF:') and ',' in line:
            head,title=line.split(',',1)
            name_match=re.search(r'tvg-name="([^"]*)"',head)
            raw=title.strip() or (name_match.group(1) if name_match else '')
            canonical=lookup.get(compact(raw)) or lookup.get(compact(name_match.group(1))) if name_match else lookup.get(compact(raw))
            if canonical:
                if name_match:
                    head=head[:name_match.start(1)]+canonical+head[name_match.end(1):]
                else:
                    head+=' tvg-name="'+canonical+'"'
                line=head+','+canonical
        lines.append(line)
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser()
    p.add_argument('input',type=Path)
    p.add_argument('output',type=Path)
    a=p.parse_args()
    if a.input.resolve()==a.output.resolve(): p.error('output must differ from input')
    a.output.write_text(normalize(a.input.read_text(encoding='utf-8-sig')),encoding='utf-8')
    print('Written',a.output)
if __name__=='__main__': main()
