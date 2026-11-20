#!/usr/bin/env python3
"""Render STL geometry previews and BOM thumbnails; numpy and Pillow.

Run with --bom-only for thumbnails or --animate to also build a rotating GIF. Independent display scales;
source geometry is never edited. English figure labels avoid font dependencies.
"""
import argparse, io, struct
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'
BG='#f2f5f7'; INK='#18313f'; MUTED='#647b88'
FONTS=Path('/usr/share/fonts/truetype/dejavu')
PARTS=[
 dict(id='01',slug='sensor-base',title='Sensor base',subtitle='Adapted for a thicker camera PCB',filename='sensor_base_adapt_for_thick_PCB.STL',color='#3983ad'),
 dict(id='02',slug='isolation-ring',title='Camera isolation ring',subtitle='Revised light isolation geometry',filename='isolation_ring_out_11.4_in_10.3.STL',color='#208e89'),
 dict(id='03',slug='leap-fingertip',title='LEAP fingertip mount',subtitle='Tactile attachment with chip holder',filename='finger_tip_tactile_with_chip_holder.STL',color='#b17d40')]
def label(draw,xy,value,size=22,fill=INK,bold=False,mono=False):
 name='DejaVuSansMono.ttf' if mono else 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
 draw.text(xy,value,font=ImageFont.truetype(str(FONTS/name),size),fill=fill)
def read_mesh(part,path=None):
 raw=(Path(path) if path is not None else ROOT/'hardware/mesh'/part['filename']).read_bytes(); count=struct.unpack_from('<I',raw,80)[0]
 if len(raw)!=84+50*count: raise ValueError('Invalid binary STL size')
 mesh=np.array([struct.unpack_from('<9f',raw,84+50*i+12) for i in range(count)]).reshape(-1,3,3)
 part['triangles']=count; part['extents']=mesh.max(axis=(0,1))-mesh.min(axis=(0,1))
 # Rigid display rotation only: X remains X, Z becomes -Y, Y becomes Z.
 shown=mesh[:,:,[0,2,1]].copy(); shown[:,:,1]*=-1
 return shown
def draw_mesh(mesh,color,size,elevation=35,azimuth=-55):
 # Orthographic triangle rasterization with a depth buffer avoids painter-order
 # artifacts on nested holes, thin walls and coplanar triangulations.
 from PIL import ImageColor
 width,height=size; ss=2; w,h=width*ss,height*ss
 el,az=np.radians([elevation,azimuth])
 camera=np.array([np.cos(el)*np.cos(az),np.cos(el)*np.sin(az),np.sin(el)])
 right=np.array([-np.sin(az),np.cos(az),0.]); up=np.cross(camera,right)
 center=(mesh.min(axis=(0,1))+mesh.max(axis=(0,1)))/2
 points=mesh-center
 px=points@right; py=points@up; depth=points@camera
 # Fixed scale for a complete turntable, computed from source spatial bounds.
 radius_xy=np.sqrt(np.max(np.sum(points[:,:,:2]**2,axis=2)))
 zhalf=np.max(np.abs(points[:,:,2]))
 maxwidth=2*radius_xy
 maxheight=2*(radius_xy*abs(np.sin(el))+zhalf*abs(np.cos(el)))
 scale=min(.9*w/max(maxwidth,1e-9),.84*h/max(maxheight,1e-9))
 # Static plate face/edge views retain generous margins but show all geometry.
 sx=px*scale+w/2; sy=-py*scale+h/2
 projected=np.stack([sx,sy,depth],axis=2)
 normals=np.cross(mesh[:,1]-mesh[:,0],mesh[:,2]-mesh[:,0])
 normals/=np.maximum(np.linalg.norm(normals,axis=1,keepdims=True),1e-12)
 normals*=np.where(normals@camera<0,-1.,1.)[:,None]
 light=camera*.65+up*.8-right*.45; light/=np.linalg.norm(light)
 diffuse=np.maximum(normals@light,0)
 rgb=np.array(ImageColor.getrgb(color))/255
 colors=np.clip((.31+.69*diffuse[:,None])*rgb+.045,0,1)*255
 bg=np.array(ImageColor.getrgb(BG),dtype=np.uint8)
 canvas=np.broadcast_to(bg,(h,w,3)).copy(); zbuffer=np.full((h,w),-np.inf)
 for tri,shade in zip(projected,colors):
  a,b,c=tri
  den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
  if abs(den)<1e-9: continue
  xmin=max(int(np.floor(tri[:,0].min())),0); xmax=min(int(np.ceil(tri[:,0].max())),w-1)
  ymin=max(int(np.floor(tri[:,1].min())),0); ymax=min(int(np.ceil(tri[:,1].max())),h-1)
  if xmin>xmax or ymin>ymax: continue
  x,y=np.meshgrid(np.arange(xmin,xmax+1)+.5,np.arange(ymin,ymax+1)+.5)
  wa=((b[1]-c[1])*(x-c[0])+(c[0]-b[0])*(y-c[1]))/den
  wb=((c[1]-a[1])*(x-c[0])+(a[0]-c[0])*(y-c[1]))/den
  wc=1-wa-wb
  z=wa*a[2]+wb*b[2]+wc*c[2]
  sub=zbuffer[ymin:ymax+1,xmin:xmax+1]
  inside=(wa>=-1e-8)&(wb>=-1e-8)&(wc>=-1e-8)&(z>sub)
  sub[inside]=z[inside]
  canvas[ymin:ymax+1,xmin:xmax+1][inside]=shade.astype(np.uint8)
 return Image.fromarray(canvas).resize((width,height),Image.Resampling.LANCZOS)
def static_assets(parts):
 (OUT/'parts').mkdir(parents=True,exist_ok=True)
 hero=Image.new('RGB',(1800,800),BG); d=ImageDraw.Draw(hero)
 label(d,(70,44),'9DTact–HashimotoLab',48,bold=True); label(d,(72,116),'THREE KEY PARTS  /  ACTUAL STL GEOMETRY',20,MUTED)
 for i,(part,mesh) in enumerate(parts):
  x=50+i*580
  hero.paste(draw_mesh(mesh,part['color'],(560,420)),(x,185))
  d.rounded_rectangle((x+24,174,x+83,219),radius=10,fill=part['color']); label(d,(x+34,179),part['id'],24,'#ffffff',True)
  label(d,(x+24,609),part['title'],29,bold=True); label(d,(x+24,655),part['subtitle'],18,MUTED)
 d.line((72,721,1728,721),fill='#d6e1e6',width=2)
 label(d,(72,747),'Separate parts at independent scales. Print orientation and physical fit are not established by this rendering.',18,MUTED)
 hero.save(OUT/'mesh-preview.png'); print('Rendered three-part overview',flush=True)
 for part,mesh in parts:
  sheet=Image.new('RGB',(1800,880),BG); d=ImageDraw.Draw(sheet)
  label(d,(65,40),part['id']+'  '+part['title'],43,bold=True); label(d,(68,108),part['filename'],19,MUTED,mono=True)
  sheet.paste(draw_mesh(mesh,part['color'],(810,550),38,-55),(45,190))
  sheet.paste(draw_mesh(mesh,part['color'],(550,380),-35,125),(810,205))
  sheet.paste(draw_mesh(mesh,part['color'],(330,300),90,-90),(1410,180))
  sheet.paste(draw_mesh(mesh,part['color'],(330,230),0,-90),(1410,490))
  label(d,(82,712),'PERSPECTIVE',18,MUTED); label(d,(880,610),'OPPOSITE SIDE',18,MUTED)
  label(d,(1450,454),'FACE VIEW',17,MUTED); label(d,(1450,714),'EDGE VIEW',17,MUTED)
  d.line((67,766,1733,766),fill='#d6e1e6',width=2); ext=' × '.join(f'{n:.3f}' for n in part['extents'])
  label(d,(68,793),f'Source XYZ bounds: {ext}  |  {part["triangles"]:,} triangles',19,MUTED)
  label(d,(68,829),'Coordinate units: mm assumed; verify in slicer. Display views do not specify the print orientation.',17,MUTED)
  sheet.save(OUT/'parts'/(part['slug']+'.png')); print('Rendered '+part['slug']+' detail sheet',flush=True)
def bom_assets(parts):
 (OUT/'bom').mkdir(parents=True,exist_ok=True)
 for part,mesh in parts:
  draw_mesh(mesh,part['color'],(480,360),38,-55).save(OUT/'bom'/(part['slug']+'.png'))
  print('Rendered BOM image: '+part['slug'],flush=True)
def animate(parts):
 frames=[]
 for frame in range(32):
  canvas=Image.new('RGB',(1200,530),BG); d=ImageDraw.Draw(canvas); label(d,(28,20),'Explore the three supplied STL parts',28,bold=True)
  for i,(part,mesh) in enumerate(parts):
   canvas.paste(draw_mesh(mesh,part['color'],(390,350),35,-55+frame*360/32),(i*400+5,82))
   label(d,(i*400+25,438),part['id']+'  '+part['title'],20,bold=True)
  label(d,(29,493),'Independent scales • Geometry preview, not assembly or physical validation',16,MUTED); frames.append(canvas)
  if frame%8==0: print(f'Rotating preview: {frame+1}/32',flush=True)
 palette=frames[0].quantize(colors=128)
 frames=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
 frames[0].save(OUT/'parts-turntable.gif',save_all=True,append_images=frames[1:],duration=110,loop=0,optimize=True,disposal=2)
 print('Rendered rotating GIF',flush=True)
def main():
 parser=argparse.ArgumentParser(); parser.add_argument('--animate',action='store_true'); parser.add_argument('--bom-only',action='store_true')
 parser.add_argument('--stl',type=Path); parser.add_argument('--output',type=Path); args=parser.parse_args()
 if (args.stl is None)!=(args.output is None): parser.error('--stl and --output must be supplied together')
 if args.stl is not None:
  mesh=read_mesh({'filename':args.stl.name},args.stl)
  args.output.parent.mkdir(parents=True,exist_ok=True)
  draw_mesh(mesh,'#3983ad',(480,360),38,-55).save(args.output)
  print('Rendered '+str(args.output),flush=True); return
 parts=[(part,read_mesh(part)) for part in PARTS]; bom_assets(parts)
 if args.bom_only: return
 static_assets(parts)
 if args.animate: animate(parts)
if __name__=='__main__': main()
