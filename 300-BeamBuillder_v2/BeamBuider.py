# -*- coding: mbcs -*-
# Do not delete the following import lines
# version：v1.0
from abaqus import *
from symbolicConstants import *
from abaqusConstants import *
import __main__

def BeamBuilder(BeamBuilderEnable,ModelName,PartName,MergeType,Meshable,Points,Rods):
    # create a model
    mdb.Model(name=ModelName,modelType=STANDARD_EXPLICIT)
    mymodel=mdb.models[ModelName]
    # create a blank part
    p=BlankPart(mymodel,PartName)

    meshable=SymbolicConstant(name=Meshable.upper())
    mergetype=SymbolicConstant(name=MergeType.upper())
    
    nodes=Points
    beams=Rods
    print('point numbers='+str(len(nodes)))
    print('rods numbers='+str(len(beams)))
    
    nodesDict={}
    for i in range(len(nodes)):
        node_index=nodes[i]
        nodesDict[node_index[0]]=node_index[1:4]
    lines=[]
    for i in range(len(beams)):
        line_index=beams[i]
        line=(nodesDict[line_index[1]],nodesDict[line_index[2]])
        lines.append(line)
    
    
    p.WirePolyLine(points=tuple(lines), mergeType=mergetype, meshable=meshable)
    
# create a balnk part object
def BlankPart(Model,PartName): 
    # return sketch
    s = Model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
    # view setting
    s.setPrimaryObject(option=STANDALONE)
    s.ArcByStartEndTangent(point1=(-36.25, 13.75), point2=(-17.5, 7.5), vector=(1.0, 0.0))
    # create a part according to the sketch
    p = Model.Part(name=PartName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = Model.parts[PartName]
    p.BaseWire(sketch=s)
    s.unsetPrimaryObject()
    del Model.sketches['__profile__']
    temp=p.features.keys()
    del p.features[temp[0]]
    return p




# p = mdb.models['Model-1'].parts['Part-1']
# p.WirePolyLine(points=(((0.0, 0.0, 0.0), (10.0, 0.0, 0.0)), ((10.0, 0.0, 0.0), 
#     (0.0, 100.0, 0.0))), mergeType=IMPRINT, meshable=ON)
# p = mdb.models['Model-1'].parts['Part-1']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#3 ]', ), )
# p.Set(edges=edges, name='Wire-1-Set-1')



# p = mdb.models['Model-1'].parts['Part-1']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#13 ]', ), )
# p.Set(edges=edges, name='Wire-2-Set-1')


# p = mdb.models['Model-1'].parts['Part-1']
# p.WirePolyLine(points=(((-15.0, 0.0, 0.0), (8.0, 45.0, 2.0)), ((8.0, 45.0, 
#     2.0), (89.0, 20.0, 5.0))), mergeType=IMPRINT, meshable=ON)
# p = mdb.models['Model-1'].parts['Part-1']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#60 ]', ), )
# p.Set(edges=edges, name='Wire-3-Set-1')