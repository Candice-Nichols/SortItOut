import sys
import os.path
from chimera import runCommand # opens chimera without visual interface
from chimera import replyobj # emits status message
from chimera.tkgui import saveReplyLog

fn=("3j98_chainK.pdb") # change to file name 

replyobj.status('Processing ' + fn) # shows the file that is being worked on
runCommand('open ' + fn)
runCommand('surf #0 grid 0.5')
runCommand('measure volume #all')
runCommand('close all')
