# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_14-01.49.31 163176
# Run by Administrator on Tue Sep 12 11:43:34 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=107.947914123535, 
    height=128.435195922852)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
from dxf2abq import importdxf
importdxf(fileName='F:/MyPluginDevlopReposity/20230813.dxf')
#: Importing DXF file to model Model-1 as sketch '20230813' ...
#: Total sketch entities translated: 123
#:   X bounding values range from -5.196152 to 57.157677
#:   Y bounding values range from -6.000000 to 51.000000
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.sketchOptions.setValues(gridOrigin=(25.9807622432709, 22.5))
#: Warning: Grid center was moved to the sketch center.
s1.retrieveSketch(sketch=mdb.models['Model-1'].sketches['20230813'])
session.viewports['Viewport: 1'].view.fitView()
#: Info: 123 entities copied from 20230813.
session.viewports['Viewport: 1'].view.setValues(width=159.488, height=76.7308, 
    cameraPosition=(40.1394, 23.3263, 168.962), cameraTarget=(40.1394, 23.3263, 
    0))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.sketchOptions.setValues(gridOrigin=(25.9807622432709, 22.5))
#: Warning: Grid center was moved to the sketch center.
s.retrieveSketch(sketch=mdb.models['Model-1'].sketches['20230813'])
session.viewports['Viewport: 1'].view.fitView()
#: Info: 123 entities copied from 20230813.
session.viewports['Viewport: 1'].view.setValues(nearPlane=139.779, 
    farPlane=198.144, width=159.488, height=76.7308, cameraPosition=(38.3528, 
    26.0286, 168.962), cameraTarget=(38.3528, 26.0286, 0))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShellExtrude(sketch=s, depth=20.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Face']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=118.305, 
    farPlane=247.017, width=113.345, height=54.5311, viewOffsetX=5.79307, 
    viewOffsetY=0.457115)
session.viewports['Viewport: 1'].view.setValues(nearPlane=129.49, 
    farPlane=219.247, width=124.062, height=59.6868, cameraPosition=(-11.0874, 
    102.691, 160.384), cameraUpVector=(0.145183, 0.695245, -0.703957), 
    cameraTarget=(25.1218, 21.2612, 0.93819), viewOffsetX=6.34079, 
    viewOffsetY=0.500333)
session.viewports['Viewport: 1'].view.setValues(nearPlane=124.702, 
    farPlane=216.897, width=119.474, height=57.4799, cameraPosition=(-56.1848, 
    -7.91731, 156.668), cameraUpVector=(0.0675847, 0.988768, -0.133304), 
    cameraTarget=(28.2358, 26.5524, -1.60354), viewOffsetX=6.10632, 
    viewOffsetY=0.481832)
session.viewports['Viewport: 1'].view.setValues(nearPlane=140.433, 
    farPlane=205.331, width=134.546, height=64.731, cameraPosition=(3.48486, 
    11.9667, 181.147), cameraUpVector=(0.0292705, 0.964479, -0.262533), 
    cameraTarget=(23.0285, 25.1985, 0.017518), viewOffsetX=6.87663, 
    viewOffsetY=0.542615)
session.viewports['Viewport: 1'].view.setValues(nearPlane=141.333, 
    farPlane=206.146, width=135.409, height=65.1459, cameraPosition=(34.2208, 
    16.1538, 183.484), cameraUpVector=(-0.0588902, 0.956411, -0.286025), 
    cameraTarget=(21.2888, 24.5877, 1.47717), viewOffsetX=6.9207, 
    viewOffsetY=0.546093)
session.viewports['Viewport: 1'].view.setValues(nearPlane=133.778, 
    farPlane=216.731, width=128.171, height=61.6637, cameraPosition=(80.0374, 
    39.305, 175.923), cameraUpVector=(-0.16764, 0.909824, -0.379627), 
    cameraTarget=(19.4477, 23.4659, 4.33412), viewOffsetX=6.55075, 
    viewOffsetY=0.516901)
session.viewports['Viewport: 1'].view.setValues(nearPlane=139.288, 
    farPlane=209.768, width=133.45, height=64.2036, cameraPosition=(58.0278, 
    27.717, 181.547), cameraUpVector=(-0.0770618, 0.936235, -0.342819), 
    cameraTarget=(20.0132, 24.2139, 2.92079), viewOffsetX=6.82056, 
    viewOffsetY=0.538191)
session.viewports['Viewport: 1'].view.setValues(nearPlane=136.935, 
    farPlane=212.471, width=131.196, height=63.1189, cameraPosition=(56.5266, 
    41.499, 181.022), cameraUpVector=(-0.121027, 0.904133, -0.409751), 
    cameraTarget=(20.1169, 23.2693, 2.95796), viewOffsetX=6.70533, 
    viewOffsetY=0.529099)
session.viewports['Viewport: 1'].view.setValues(nearPlane=135.097, 
    farPlane=214.639, width=129.435, height=62.2719, cameraPosition=(47.5127, 
    65.7957, 178.114), cameraUpVector=(-0.117214, 0.835446, -0.536927), 
    cameraTarget=(20.4646, 22.2109, 2.80402), viewOffsetX=6.61532, 
    viewOffsetY=0.521997)
session.viewports['Viewport: 1'].view.setValues(nearPlane=134.474, 
    farPlane=215.646, width=128.838, height=61.9846, cameraPosition=(59.6436, 
    59.6038, 177.803), cameraUpVector=(-0.126581, 0.855882, -0.501441), 
    cameraTarget=(20.02, 22.6787, 3.35762), viewOffsetX=6.58479, 
    viewOffsetY=0.519588)
session.viewports['Viewport: 1'].view.setValues(nearPlane=128.132, 
    farPlane=224.051, width=122.762, height=59.0616, cameraPosition=(85.2202, 
    82.9064, 164.494), cameraUpVector=(-0.329499, 0.769313, -0.547346), 
    cameraTarget=(19.635, 20.9589, 5.6677), viewOffsetX=6.27426, 
    viewOffsetY=0.495085)
session.viewports['Viewport: 1'].view.setValues(nearPlane=124.345, 
    farPlane=229.487, width=119.134, height=57.316, cameraPosition=(92.0704, 
    116.947, 144.277), cameraUpVector=(-0.389993, 0.623664, -0.677458), 
    cameraTarget=(19.6835, 20.3743, 7.16902), viewOffsetX=6.08882, 
    viewOffsetY=0.480452)
session.viewports['Viewport: 1'].view.setValues(nearPlane=127.059, 
    farPlane=225.857, width=121.734, height=58.5669, cameraPosition=(81.4698, 
    108.034, 154.091), cameraUpVector=(-0.335671, 0.666141, -0.666019), 
    cameraTarget=(19.6934, 20.4328, 6.19077), viewOffsetX=6.2217, 
    viewOffsetY=0.490937)
