from abaqusGui import getAFXApp, Activator, AFXMode
from abaqusConstants import ALL
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='RandomFiberRVE', 
    object=Activator(os.path.join(thisDir, 'randomFiberRVEDB.py')),
    kernelInitString='import rve',
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
