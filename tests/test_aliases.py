import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from normalize_m3u import compact,lookup,normalize
class Aliases(unittest.TestCase):
 def test_alias(self):self.assertEqual(lookup[compact('央视一套')],'CCTV-1 综合')
 def test_five_plus(self):self.assertEqual(lookup[compact('CCTV-5+')],'CCTV-5+ 体育赛事')
 def test_preserve_id_url(self):
  value='#EXTM3U\n#EXTINF:-1 tvg-id="provider_id" tvg-name="央视一套",央视一套\nhttps://example.invalid/a.m3u8\n'
  result=normalize(value)
  self.assertIn('tvg-id="provider_id"',result)
  self.assertIn('tvg-name="CCTV-1 综合"',result)
  self.assertIn('https://example.invalid/a.m3u8',result)
if __name__=='__main__':unittest.main()
