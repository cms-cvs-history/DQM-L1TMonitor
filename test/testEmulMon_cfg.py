import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQM/L1TMonitor/L1TEmulatorMonitor_cff")

process.load("Configuration.StandardSequences.Geometry_cff")
#process.load("L1Trigger.Configuration.L1Config_cff")
 
#off-line
#process.GlobalTag.globaltag = 'CRAFT_V2P::All'
#process.GlobalTag.connect = 'frontier://FrontierProd/CMS_COND_21X_GLOBALTAG'
#on-line
#process.GlobalTag.globaltag = 'CRAFT_V2H::All'
#process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"   
process.GlobalTag.globaltag = 'GR09_31X_V3P::All' # or any other appropriate
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')


#ETP,HTP,RCT,GCT, DTP,DTF,CTP,CTF,RPC, LTC,GMT,GLT 
#process.l1compare.COMPARE_COLLS = [0,0,0,1, 0,0,0,0,0, 0,1,0]
process.l1compare.DumpMode = -1
process.l1compare.VerboseFlag = 1
process.l1demon.VerboseFlag = 1
#process.l1demonecal.VerboseFlag = 1
#process.l1demongct.VerboseFlag = 1
#process.l1tderct.verbose = False
process.l1demon.disableROOToutput = False
#process.l1demonecal.disableROOToutput = False
#process.l1demongct.disableROOToutput = False
#process.l1tderct.disableROOToutput = False
#process.l1demon.RunInFilterFarm=True

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
)
#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring(
#    '/store/data/Commissioning08/Monitor/RAW/v1/000/065/935/7E8E286F-6A99-DD11-8A15-000423D6B48C.root'
#    )
#)


process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring(
 '/store/streamer/MWGR_29/A/000/106/019/MWGR_29.00106019.0036.A.storageManager.07.0000.dat'
 ));


#process.outputEvents = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string('testdemon.root')
#)
#
#process.ep = cms.EndPath(process.outputEvents)
