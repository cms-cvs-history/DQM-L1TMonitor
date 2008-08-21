import FWCore.ParameterSet.Config as cms

process = cms.Process("ecalde")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.test.dqm_onlineEnv_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")

process.load("L1TriggerConfig.GMTConfigProducers.L1MuGMTParametersConfig_cff")

process.load("L1TriggerConfig.L1ScalesProducers.L1MuTriggerScalesConfig_cff")

process.load("L1TriggerConfig.L1ScalesProducers.L1MuTriggerPtScaleConfig_cff")

process.load("L1TriggerConfig.L1ScalesProducers.L1MuGMTScalesConfig_cff")

process.load("DQM.L1TMonitorClient.L1TRPCTFClient_cff")


#process.load("EventFilter.RPCRawToDigi.RPCSQLiteCabling_cfi")
#process.load("EventFilter.RPCRawToDigi.rpcUnpacker_cfi")


process.load("DQM.L1TMonitor.L1TRPCTF_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

process.source = cms.Source("NewEventStreamFileReader",
#process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

            '/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0001.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0001.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0001.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0001.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0002.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0001.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0001.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0002.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0003.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0002.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0002.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0003.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0002.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0002.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0003.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0003.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0003.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0003.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0004.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0004.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0004.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0004.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0004.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0004.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0005.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0005.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0005.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0005.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0005.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0005.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0006.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0006.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0006.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0006.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0006.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0006.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0007.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0007.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0007.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0007.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0007.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0007.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0008.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0008.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0008.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0008.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0008.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0008.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0009.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0009.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0009.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0009.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0009.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0009.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0010.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0010.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0010.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0010.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0010.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0011.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0011.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0011.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0011.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0011.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0011.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0012.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0012.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0012.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0012.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0012.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0012.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0013.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0013.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0013.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0013.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0013.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0013.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0014.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0014.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0014.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0014.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0014.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0014.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0015.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0015.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0015.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0015.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0015.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0015.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0016.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0016.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0016.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0017.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0017.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0017.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0018.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0018.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0018.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0018.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0018.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0018.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0019.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0019.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0019.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0019.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0020.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0020.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0020.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0020.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0020.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0020.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0021.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0021.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0021.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0022.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0022.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0022.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0022.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0022.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0022.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0023.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0023.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0023.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0023.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0023.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0023.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0024.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0024.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0024.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0025.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0025.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0025.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0026.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0026.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0026.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0027.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0027.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0027.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0028.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0028.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0028.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0028.A.storageManager.3.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0028.A.storageManager.0.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0028.A.storageManager.1.0001.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0029.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0029.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0029.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0030.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0030.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0030.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0031.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0031.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0031.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0032.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0032.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0032.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0033.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0033.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0033.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0034.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0034.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0034.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0035.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0035.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0035.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0036.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0036.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0036.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0037.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0037.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0037.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0038.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0038.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0038.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0039.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0039.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0039.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0040.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0040.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0040.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0041.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0041.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0041.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0042.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0042.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0042.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0043.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0043.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0043.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0044.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0044.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0044.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0045.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0045.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0045.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0046.A.storageManager.1.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0046.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0046.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0047.A.storageManager.0.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0047.A.storageManager.3.0000.dat'
            ,'/store/data/GlobalCruzet4/A/000/057/620/GlobalCruzet4.00057620.0047.A.storageManager.1.0000.dat'
    )
)

process.gtUnpack = cms.EDFilter("L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32(813),
    DaqGtInputTag = cms.InputTag("source"),
    UnpackBxInEvent = cms.int32(-1),
    ActiveBoardsMask = cms.uint32(65535)
)

#process.l1trpctf = cms.EDFilter("L1TRPCTF",
#    rpctfRPCDigiSource = cms.InputTag("rpcunpacker"),
#    outputFile = cms.untracked.string(''),
#    verbose = cms.untracked.bool(False),
#    rpctfSource = cms.InputTag("gtUnpack"),
#    MonitorDaemon = cms.untracked.bool(True),
#    DaqMonitorBEInterface = cms.untracked.bool(True)
#)

#process.l1trpctpg = cms.EDFilter("L1TRPCTPG",
#    outputFile = cms.untracked.string(''),
#    verbose = cms.untracked.bool(False),
#    rpctpgSource = cms.InputTag("rpcunpacker"),
#    rpctfSource = cms.InputTag("gtUnpack"),
#    MonitorDaemon = cms.untracked.bool(True),
#    DaqMonitorBEInterface = cms.untracked.bool(True)
#)

#process.l1trpctpg.rpctpgSource = cms.InputTag("rpcunpacker")
#process.l1trpctpg.rpctfSource = cms.InputTag("gtUnpack")



process.l1trpctf.rpctfSource = cms.InputTag("gtUnpack")

process.b = cms.Path(process.gtUnpack)

process.load("DQM.L1TMonitor.L1TRPCTPG_offline_cff")
process.l1trpctpg.rpctpgSource = cms.InputTag("rpcunpacker")
process.l1trpctpg.rpctfSource = cms.InputTag("gtUnpack")

process.a = cms.Path(process.l1trpctf*process.l1trpctfqTester*process.l1trpctfClient*process.dqmEnv*process.dqmSaver)

process.MessageLogger.destinations = ['log.txt']
process.dqmSaver.convention = 'Online'
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'DQM'
process.dqmEnv.subSystemFolder = 'L1T'
process.l1trpctfClient.verbose = True


