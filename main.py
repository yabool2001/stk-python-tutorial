# The STK Python API is packaged as a wheel file that can be installed using pip.
# The wheel file is included with the STK install in the bin/AgPythonAPI directory.
# python -m pip install "<STK installation directory>/bin/AgPythonAPI/agi.stk12-12.8.0-py3-none-any.whl"


# PS C:\Users\mzeml> python -m pip install "C:/Program Files/AGI/STK 12/bin/AgPythonAPI/agi.stk12-12.8.0-py3-none-any.whl"
# Processing c:\program files\agi\stk 12\bin\agpythonapi\agi.stk12-12.8.0-py3-none-any.whl
# Installing collected packages: agi.stk12
# Successfully installed agi.stk12-12.8.0
# PS C:\Users\mzeml>

# https://help.agi.com/stkdevkit/index.htm#python/pythonGettingStarted.htm
from agi.stk12.stkengine import STKEngine

# https://help.agi.com/stkdevkit/index.htm#python/pythonProgrammingGuide.htm
from agi.stk12.stkdesktop import STKDesktop
from agi.stk12.stkobjects import *

# stk = STKEngine.StartApplication ( noGraphics = True )
# stk = STKDesktop.StartApplication ( visible = True ) #using optional visible argument
stk = STKDesktop.AttachToApplication ()

stk.ShutDown ()