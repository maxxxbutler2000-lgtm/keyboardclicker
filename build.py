"""Build the single-file GitHub Pages app from the editable source/ folder."""
from pathlib import Path
import base64,json,mimetypes,re
root=Path(__file__).resolve().parent
src=root/'source'
if not src.exists():
 raise SystemExit('Unzip editable-source.zip here first to create source/.')
assets={}
for p in (src/'assets').rglob('*'):
 if p.is_file():
  mime=mimetypes.guess_type(str(p))[0] or 'application/octet-stream'
  assets[p.relative_to(src).as_posix()]='data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()
html=(src/'index.html').read_text()
for name in ['style.css','clicker.css','skins.css']:
 html=html.replace('<link rel="stylesheet" href="'+name+'">','<style>\n'+(src/name).read_text()+'\n</style>')
app=(src/'app.js').read_text().replace('fetch(url)','fetch(assetURL(url))')
for key in ['board','b']:
 app=app.replace('`url("assets/skins/${'+key+'.id}.webp")`','`url("${assetURL(\'assets/skins/\'+'+key+'.id+\'.webp\')}")`')
bootstrap='const KEYDRIFT_ASSETS='+json.dumps(assets,separators=(',',':'))+';\nconst assetURL=path=>KEYDRIFT_ASSETS[decodeURIComponent(path)]||path;\n'
html=html.replace('<script src="game.js"></script>','<script>\n'+bootstrap+(src/'game.js').read_text()+'\n</script>')
html=html.replace('<script src="app.js"></script>','<script>\n'+app+'\n</script>')
(root/'index.html').write_text(html)
print('Built index.html:',len(html.encode()),'bytes;',len(assets),'embedded assets.')
