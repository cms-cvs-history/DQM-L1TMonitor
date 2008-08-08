import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQM/L1TMonitor/L1TEmulatorMonitor_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/GlobalCruzet1/A/000/000/000/RAW/0003/00ECEA7A-901B-DD11-A23C-000423D98868.root')
)

process.outputEvents = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('testdemon.root')
)

process.ep = cms.EndPath(process.outputEvents)
