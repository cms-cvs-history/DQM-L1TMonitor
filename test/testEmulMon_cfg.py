import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQM/L1TMonitor/L1TEmulatorMonitor_cff")

process.load("Configuration.StandardSequences.Geometry_cff")
#process.load("L1Trigger.Configuration.L1Config_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#off-line
process.GlobalTag.globaltag = 'GR09_P_V1::All'
#process.GlobalTag.globaltag = 'GR09_31X_V6P::All'
#process.GlobalTag.connect = 'frontier://FrontierProd/CMS_COND_21X_GLOBALTAG'
#process.GlobalTag.globaltag = "GR09_P_V1::All"


#ETP,HTP,RCT,GCT, DTP,DTF,CTP,CTF,RPC, LTC,GMT,GLT 
process.l1compare.COMPARE_COLLS = [0,0,0,0, 0,0,0,1,0, 0,0,0]
process.l1compare.DumpMode = -1
process.l1compare.VerboseFlag = 1
process.l1demon.VerboseFlag = 1
#process.l1demonecal.VerboseFlag = 1
#process.l1demongct.VerboseFlag = 1
#process.l1tderct.verbose = False
process.l1demon.disableROOToutput = False
process.l1demonecal.disableROOToutput = False
process.l1demongct.disableROOToutput = False
process.l1tderct.disableROOToutput = False
#process.l1demon.RunInFilterFarm=True

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'file:file_craft09_fevt_110998.root'
    '/store/express/CRAFT09/ExpressMuon/FEVT/v1/000/110/998/FEF63450-1B8A-DE11-8102-000423D987FC.root'
    )
)

process.outputEvents = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('testdemon.root')
)
process.ep = cms.EndPath(process.outputEvents)
