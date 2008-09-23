import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQM/L1TMonitor/L1TEmulatorMonitor_cff")
process.GlobalTag.globaltag = 'CRUZET4_V5P::All'
process.GlobalTag.connect = 'frontier://FrontierProd/CMS_COND_21X_GLOBALTAG'
# ETP,HTP,RCT,GCT, DTP,DTF,CTP,CTF,RPC, LTC,GMT,GLT 
#process.l1compare.COMPARE_COLLS = [0,0,0,0, 0,0,1,0,0, 0,0,0]
#process.l1compare.DumpMode = -1
#process.l1compare.VerboseFlag = 1
#process.l1demon.VerboseFlag = -1
#process.l1demonecal.VerboseFlag = -1
#process.l1demongct.VerboseFlag = -1
process.l1tderct.verbose = False
process.l1demon.disableROOToutput = False
process.l1demonecal.disableROOToutput = False
#process.l1demongct.disableROOToutput = False
#process.l1tderct.disableROOToutput = False

#process.l1demon.RunInFilterFarm=True

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/data/BeamCommissioning08/Cosmics/RAW/v1/000/063/136/A444AFCA-6085-DD11-87F3-000423D987E0.root'
    )
)

process.outputEvents = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('testdemon.root')
)

process.ep = cms.EndPath(process.outputEvents)
