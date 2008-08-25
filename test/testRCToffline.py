import FWCore.ParameterSet.Config as cms

process = cms.Process("RCTofflineTEST")

#process.load("DQMServices.Core.DQM_cfg")
process.DQMStore = cms.Service("DQMStore")

process.load("DQM/L1TMonitor/L1TRCToffline_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Commissioning08/Cosmics/RAW/CRUZET4_v1/000/057/774/2260AF5F-356E-DD11-99F3-000423D6C8E6.root')
)


