# L1 Emulator DQM sequence
#
#   authors previous versions - see CVS
#
#   V.M. Ghete 2010-10-22 revised version of L1 emulator DQM


import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TEmuDQMlive")


#----------------------------
# Event Source
#

process.load("DQM.Integration.test.inputsource_cfi")
#
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("*")
    )
process.EventStreamHttpReader.consumerName = 'L1TEMU DQM Consumer'


#----------------------------
# DQM Environment
#
 
#
process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")
process.dqmEnv.subSystemFolder = 'L1TEMU'

#
process.load("DQM.Integration.test.environment_cfi")
#
# no references needed
# replace DQMStore.referenceFileName = "L1TEMU_reference.root"

#
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
process.GlobalTag.RefreshEachRun = cms.untracked.bool(True)

#
process.load("Configuration.StandardSequences.Geometry_cff")

#-------------------------------------
# sequences needed for L1 emulator DQM
#

# standard unpacking sequence 
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")    

# L1 data - emulator sequences 
process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    

#-------------------------------------
# paths & schedule for L1 emulator DQM
#

# TODO define a L1 trigger L1TriggerRawToDigi in the standard sequence 
# to avoid all these remove
process.rawToDigiPath = cms.Path(process.RawToDigi)
#
process.RawToDigi.remove("siPixelDigis")
process.RawToDigi.remove("siStripDigis")
process.RawToDigi.remove("scalersRawToDigi")
process.RawToDigi.remove("castorDigis")

# L1HvVal + emulator monitoring path
process.l1HwValEmulatorMonitorPath = cms.Path(process.l1HwValEmulatorMonitor)

#
process.l1EmulatorMonitorClientPath = cms.Path(process.l1EmulatorMonitorClient)

#
process.l1EmulatorMonitorEndPath = cms.EndPath(process.dqmEnv*process.dqmSaver)

#

#
process.schedule = cms.Schedule(process.rawToDigiPath,
                                process.l1HwValEmulatorMonitorPath,
                                process.l1EmulatorMonitorClientPath,
                                process.l1EmulatorMonitorEndPath)

#---------------------------------------------

# examples for quick fixes in case of troubles 
#    please do not modify the commented lines
#
# remove a module from hardware validation
# cff file: L1Trigger.HardwareValidation.L1HardwareValidation_cff
#
# process.L1HardwareValidation.remove("deCsctf")
#


#
# remove a L1 trigger system from the comparator integrated in hardware validation
# cfi file: L1Trigger.HardwareValidation.L1Comparator_cfi
#
# process.l1compare.COMPARE_COLLS = [1, 1, 1, 1,  1, 1, 1, 1, 1, 0, 1, 1]
#


#
# remove an expert module for L1 trigger system
# cff file: DQM.L1TMonitor.L1TEmulatorMonitor_cff
#
# process.l1ExpertDataVsEmulator.remove(process.l1GtHwValidation)
#

#process.l1ExpertDataVsEmulator.remove(process.l1TdeCSCTF)

#
# remove a module / sequence from l1EmulatorMonitorClient
# cff file: DQM.L1TMonitorClient.L1TEmulatorMonitorClient_cff
#
# process.l1EmulatorMonitorClient.remove(process.l1EmulatorErrorFlagClient)
#


#
# fast over-mask a system in L1TEMUEventInfoClient: 
#   if the name of the system is in the list, the system will be masked
#   (the default mask value is given in L1Systems VPSet)             
#
# names are case sensitive, order is irrelevant
# "ECAL", "HCAL", "RCT", "GCT", "DTTF", "DTTPG", "CSCTF", "CSCTPG", "RPC", "GMT", "GT"
#
# process.l1temuEventInfoClient.MaskL1Systems = cms.vstring("ECAL")
#


#
# fast over-mask an object in L1TEMUEventInfoClient:
#   if the name of the object is in the list, the object will be masked
#   (the default mask value is given in L1Objects VPSet)             
#
# names are case sensitive, order is irrelevant
# 
# "Mu", "NoIsoEG", "IsoEG", "CenJet", "ForJet", "TauJet", "ETM", "ETT", "HTT", "HTM", 
# "HfBitCounts", "HfRingEtSums", "TechTrig", "GtExternal
#
# process.l1temuEventInfoClient.MaskL1Objects =  cms.vstring("ETM")   
#


#
# turn on verbosity in L1TEMUEventInfoClient
#
# process.l1EmulatorEventInfoClient.verbose = cms.untracked.bool(True)
