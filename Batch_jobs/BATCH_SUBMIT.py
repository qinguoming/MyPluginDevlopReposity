# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
from symbolicConstants import *

#  main funtion
def SubmitTask(DefaultMode,UserMode,InpFilePath,pureINP,notRUN,jobtype,multiprocessMode,reFormat,CpuNumber,numDomain,Paramode):
    if DefaultMode:
        for jobName in mdb.jobs.keys(): 
            mdb.jobs[jobName].submit(consistencyChecking=OFF) #提交计算 
            mdb.jobs[jobName].waitForCompletion() #等待计算完成 
            print(jobName+" is completed")
    if UserMode:
        import os
        # return inpfiles' dir name
        InpDir=os.path.dirname(InpFilePath)
        tuple_inp_job=getInpList(InpDir,pureINP)
        inplist=tuple_inp_job[0]
        JobNamelist=tuple_inp_job[1]
        # options
        Jobtype=SymbolicConstant(name=jobtype)
        multiprocessMode=SymbolicConstant(name=multiprocessMode)
        rFormat=SymbolicConstant(name=reFormat)
        
        # create jobs from inp file
        for index in range(len(inplist)):
            mdb.JobFromInputFile(name=JobNamelist[index], inputFileName=inplist[index], 
                                 type=Jobtype, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
                                 memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,  explicitPrecision=SINGLE, 
                                 nodalOutputPrecision=SINGLE, userSubroutine='', scratch='', 
                                 resultsFormat=rFormat,  multiprocessingMode=multiprocessMode, numCpus=CpuNumber, numDomains=CpuNumber, numGPUs=0)
        if not notRUN:
            # loop submit
            for job in JobNamelist:
                mdb.jobs[job].submit(consistencyChecking=OFF) #提交计算 
                mdb.jobs[job].waitForCompletion() #等待计算完成 
                print(job+"is completed")

def getInpList(InpDir,pureINP):
    import os
    inpfiles=[]
    jobNames=[]
    objs= os.listdir(InpDir) #得到InpDir文件夹下的所有文件和子目录名称
    # if the dir only have inp file
    if pureINP:
        # objs is list include inp filename 
        for i in objs:
            inpfiles.append(os.path.join(InpDir,i))
            jobNames.append(os.path.splitext(i)[0])
        return (inpfiles,jobNames)
    # IF the dir have other format file
    else:
        for file in objs:
            path=os.path.join(InpDir,file)
            # IS file then return TRUE
            if os.path.isfile(path):
                # if inp  format ?
                if os.path.splitext(file)[1]=='.inp':
                    inpfiles.append(path)
                    jobNames.append(os.path.splitext(file)[0])
        return (inpfiles,jobNames)
# import os

# # test function getInpList()
# InpFilePath='G:/SIMULIA/workspace/06-CMA study/QUICK_START/simpleModel/Job-SIMPLE_MODEL.dat'
# InpDir=os.path.dirname(InpFilePath)
# tuple_inp_job=getInpList(pureINP=0,InpDir=InpDir)
# print(tuple_inp_job[0])

# print(tuple_inp_job[1])