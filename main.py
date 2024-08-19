# The STK Python API is packaged as a wheel file that can be installed using pip.
# The wheel file is included with the STK install in the bin/AgPythonAPI directory.
# python -m pip install "<STK installation directory>/bin/AgPythonAPI/agi.stk12-12.8.0-py3-none-any.whl"
# or python -m pip install "agi.stk12-12.8.0-py3-none-any.whl"

# PS C:\Users\mzeml> python -m pip install "C:/Program Files/AGI/STK 12/bin/AgPythonAPI/agi.stk12-12.8.0-py3-none-any.whl"
# Processing c:\program files\agi\stk 12\bin\agpythonapi\agi.stk12-12.8.0-py3-none-any.whl
# Installing collected packages: agi.stk12
# Successfully installed agi.stk12-12.8.0
# PS C:\Users\mzeml>

from agi.stk12.stkobjects import *

import os
import platform
import time

mode = 'desktop'
# mode = 'engine'

if mode == 'engine' :
    # https://help.agi.com/stkdevkit/index.htm#python/pythonGettingStarted.htm
    from agi.stk12.stkengine import STKEngine
    stk = STKEngine.StartApplication ( noGraphics = True )
    print ( stk.Version )
    stkRoot = stk.NewObjectRoot ()
elif mode == 'desktop' :
    # https://help.agi.com/stkdevkit/index.htm#python/pythonProgrammingGuide.htm
    from agi.stk12.stkdesktop import STKDesktop
    # stk = STKDesktop.StartApplication ( visible = True , userControl = True )
    stk = STKDesktop.AttachToApplication ()
    stkRoot = stk.Root

stkRoot.UnitPreferences.SetCurrentUnit ( "DateFormat" , "UTCG" )

stkRoot.NewScenario ( "Mono_BLOS_16_python001" )
scenario = stkRoot.CurrentScenario
scenario.SetTimePeriod ( "1 Jan 2010 12:00:00", "1 Jan 2011 12:00:00" )


satellite = scenario.Children.New ( AgESTKObjectType.eSatellite , "POLMEO" )
satellite.SetPropagatorType ( AgEVePropagatorType.ePropagatorJ4Perturbation )
keplerian = satellite.Propagator.InitialState.Representation.ConvertTo ( AgEOrbitStateType.eOrbitStateClassical )

propagator = satellite.Propagator

orbitState = propagator.InitialState.Representation
orbitStateClassical = orbitState.InitialState.Representation.ConvertTo ( AgEOrbitStateType.eOrbitStateClassical )
# orbitStateClassical.SizeShapeType = AgEClassicalSizeShape.eSizeShapeSemimajorAxis
orbitStateClassical.SizeShapeType = AgEClassicalSizeShape.eSizeShapeAltitude
orbitStateClassical.LocationType = AgEClassicalLocation.eLocationTrueAnomaly
orientation = orbitStateClassical.Orientation
orientation.AscNodeType = AgEOrientationAscNode.eAscNodeRAAN

sizeShape = orbitStateClassical.SizeShape
sizeShape.PerigeeAltitude   = 12000
sizeShape.ApogeeAltitude    = 12000

orientation.Inclination = 90
orientation.ArgOfPerigee = 0

raan = orientation.AscNode
raan.Value = 0

trueAnomaly = orbitStateClassical.Location
trueAnomaly.Value = 0

orbitState.Assign ( orbitStateClassical )

propagator.Propagate()

stk.ShutDown ()
