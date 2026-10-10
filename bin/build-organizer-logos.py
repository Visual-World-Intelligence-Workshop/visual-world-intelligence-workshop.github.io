"""Assemble official affiliation artwork without stretching the source logos."""
from pathlib import Path
import base64,re
root=Path(__file__).resolve().parents[1]/'assets/img';assets=root/'affiliation-logos'
p=assets/'meta.svg';s=p.read_text()
if 'viewBox=' not in s:s=re.sub(r'<svg\b','<svg viewBox="0 0 948 191"',s,count=1);p.write_text(s)
items=[('Anates Labs','anates.png',40,30,500,100),('Mila','mila.svg',600,30,250,100),('Meta','meta.svg',930,30,290,100),('CNRS','cnrs.svg',1360,30,100,100),('TUM','tum.svg',80,195,290,105),('AMI Labs — Advanced Machine Intelligence','ami.svg',475,190,380,115),('Black Forest Labs','black-forest-labs.svg',1030,205,440,90),('Université de Montréal','udem.svg',135,365,340,120),('École Polytechnique','polytechnique.svg',625,365,350,120),('McGill University','mcgill.png',1090,365,460,120)]
s=['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1550" height="495" viewBox="20 10 1550 495" role="img"><title>Organizer affiliations: '+', '.join(i[0] for i in items)+'</title><rect width="1600" height="540" fill="white"/>']
for label,name,x,y,w,h in items:
 data=(assets/name).read_bytes();mime='image/svg+xml' if name.endswith('.svg') else 'image/png'
 s.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" xlink:href="data:{mime};base64,{base64.b64encode(data).decode()}"/>')
s.append('</svg>');(root/'organizer-logos-2027.svg').write_text(''.join(s))
