import FWCore.ParameterSet.Config as cms

# L1 Emulator DQM sequence
#
# used by DQM GUI: DQM/Integration/python/test/l1temulator_dqm_sourceclient-*_cfg.py
#
# N. Leonardo 2008-02-XX initial version
#
# V.M. Ghete 2010-10-22 revised version of L1 emulator DQM
#                       proper definition of sequences

# hardware validation sequence - it runs also the L1 emulator
from L1Trigger.HardwareValidation.L1HardwareValidation_cff import *

# temporary fix for L1 GT emulator configuration in hardware validation
valGtDigis.RecordLength = cms.vint32(3, 5)
valGtDigis.AlternativeNrBxBoardDaq = 0x101
valGtDigis.AlternativeNrBxBoardEvm = 0x2

# DQM modules
from DQM.L1TMonitor.L1TDEMON_cfi import *

from DQM.L1TMonitor.L1TdeECAL_cfi import *

from DQM.L1TMonitor.L1TdeGCT_cfi import *

from DQM.L1TMonitor.L1TdeRCT_cfi import *
l1TdeRCT.rctSourceData = 'gctDigis'
l1TdeRCT.rctSourceEmul = 'valRctDigis'

from DQM.L1TMonitor.L1TdeCSCTF_cfi import *

from DQM.L1TMonitor.l1GtHwValidation_cfi import *

# filter to select "real events"
from HLTrigger.special.HLTTriggerTypeFilter_cfi import *
hltTriggerTypeFilter.SelectedTriggerType = 1


# sequence for expert modules for data - emulator comparison
# the modules are independent, so uses "+"

# l1TdeRCT requires separate definition due to the filter
#
# must be at the end of expert sequence to avoid having the filter 
# in all modules
#
# must be removed in offline sequence
#
# TODO ask RCT if really needed - filter are forbidden in DQM

l1TdeRCTSeq = cms.Sequence(
                    hltTriggerTypeFilter * 
                    l1TdeRCT
                    )

l1ExpertDataVsEmulator = cms.Sequence(
                                l1TdeECAL + 
                                l1TdeGCT + 
                                l1TdeCSCTF + 
                                l1GtHwValidation + 
                                l1TdeRCTSeq                 
                                )


l1EmulatorMonitor = cms.Sequence(
                            l1demon+
                            l1ExpertDataVsEmulator             
                            )

# for use in processes where hardware validation is not run
l1HwValEmulatorMonitor = cms.Sequence(
                                L1HardwareValidation*
                                l1EmulatorMonitor
                                )
