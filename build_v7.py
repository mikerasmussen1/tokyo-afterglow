from pathlib import Path
import base64,json
P=Path(__file__).parent
def data(path):return 'data:image/png;base64,'+base64.b64encode(path.read_bytes()).decode()
levels=[]
for id,title,sub in [('tokyo','Tokyo','Afterglow'),('kyoto','Kyoto','Autumn paths')]:
 items=json.loads((P/f'{id}-items.json').read_text())
 for it in items:
  it['sceneSrc']=data(P/'assets'/it['sceneAsset']);it['src']=data(P/'assets'/it['canonicalAsset'])
 levels.append(dict(id=id,title=title,subtitle=sub,background=data(P/f'assets/v7/{id}-clean-plate.png'),items=items))
t=(P/'game-v7-template.html').read_text().replace('CSS_DATA',(P/'game-v7.css').read_text()).replace('LEVELS_DATA','const LEVELS='+json.dumps(levels)+';').replace('RUNTIME_DATA',(P/'game-v7.js').read_text())
(P/'index.html').write_text(t);print('Built v7:',[(l['id'],len(l['items'])) for l in levels],len(t),'bytes')
