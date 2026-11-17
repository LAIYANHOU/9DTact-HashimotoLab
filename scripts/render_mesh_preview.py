#!/usr/bin/env python3
"""Render actual supplied meshes; requires numpy and matplotlib.

This is a separate-parts preview, not an assembly or fit check.
"""
from pathlib import Path
import numpy as np
import struct
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.colors import LightSource
root=Path(__file__).resolve().parents[1]
fig=plt.figure(figsize=(15,10),facecolor='#f2f5f7')
fig.text(.045,.952,'9DTact–HashimotoLab',fontsize=26,fontweight='bold',color='#152a38')
fig.text(.045,.914,'SUPPLIED MESHES  /  HARDWARE HANDOVER',fontsize=11,color='#607683')
files=[('isolation_ring_out_11.4_in_10.3.STL','01  Camera isolation ring','#268b93'),('finger_tip_tactile_with_chip_holder.STL','02  LEAP fingertip with chip holder','#397cba')]
views=[(25,-55,'PERSPECTIVE'),(90,-90,'TOP'),(0,-90,'FRONT')]
for row,(name,title,color) in enumerate(files):
 raw=(root/'hardware/mesh'/name).read_bytes();n=struct.unpack_from('<I',raw,80)[0]
 tris=np.array([struct.unpack_from('<9f',raw,84+50*i+12) for i in range(n)]).reshape(-1,3,3)
 lower=tris.min(axis=(0,1));upper=tris.max(axis=(0,1));center=(lower+upper)/2
 span=max(upper-lower)*.58
 yy=.853 if row==0 else .466
 fig.text(.045,yy,title,fontsize=17,fontweight='bold',color='#152a38')
 fig.text(.045,yy-.027,name,fontsize=9,color='#607683',fontfamily='monospace')
 normals=np.cross(tris[:,1]-tris[:,0],tris[:,2]-tris[:,0]);normals=normals/np.maximum(np.linalg.norm(normals,axis=1,keepdims=True),1e-12)
 light=np.array([-.5,-.4,.8]);light/=np.linalg.norm(light)
 shade=.55+.4*np.maximum(normals@light,0)
 rgb=np.array(matplotlib.colors.to_rgb(color));colors=np.clip(shade[:,None]*rgb+.06,0,1)
 for col,(elev,azim,label) in enumerate(views):
  ax=fig.add_axes([.04+.32*col,.51-.385*row,.29,.30],projection='3d',facecolor='#f2f5f7')
  pc=Poly3DCollection(tris,facecolors=colors,edgecolors=(.05,.15,.2,.15),linewidths=.1)
  ax.add_collection3d(pc)
  ax.set_xlim(center[0]-span,center[0]+span);ax.set_ylim(center[1]-span,center[1]+span);ax.set_zlim(center[2]-span,center[2]+span)
  ax.set_box_aspect((1,1,1));ax.set_proj_type('ortho');ax.view_init(elev,azim);ax.set_axis_off()
  ax.text2D(.02,.02,label,transform=ax.transAxes,fontsize=9,color='#607683')
fig.text(.045,.06,'Actual STL geometry • Separate parts, independent display scales • No physical fit validation',fontsize=10,color='#607683')
fig.text(.045,.034,'SolidWorks-only base is not rendered. CAD source and mesh variants are not assumed to match.',fontsize=9,color='#607683')
fig.savefig(root/'assets/mesh-preview.png',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
print('Rendered assets/mesh-preview.png')
