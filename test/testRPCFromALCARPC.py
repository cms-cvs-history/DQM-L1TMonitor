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

process.load("DQM.L1TMonitor.L1TRPCTF_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#process.source = cms.Source("NewEventStreamFileReader",
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
            '/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/0A64AAD0-63A6-DD11-820B-00304879FA4C.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/14E95623-71A6-DD11-BAC4-000423D8F63C.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/2C1221C0-7DA6-DD11-B129-000423D6AF24.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/5695BC59-96A6-DD11-B0C8-0030487C608C.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/5E2B5A7F-85A6-DD11-9A4F-001D09F24D4E.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/626A2CAB-53A6-DD11-829D-0016177CA778.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/668B1454-75A6-DD11-A7B2-000423D986C4.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/A2CDC39C-6DA6-DD11-B5D8-000423D98B6C.root'
            ,'/store/data/Commissioning08/Cosmics/ALCARECO/CRAFT_V3P_StreamALCARECORpcCalHLT_v10/0019/D412463C-A7A6-DD11-9901-0019B9F705A3.root'
    )
)

process.l1trpctf.rpctfSource = cms.InputTag("gtDigis")
process.l1trpctf.rateUpdateTime = cms.int32(-1) # update at end of run



# include this later - contains path with rpc unpacker
#process.load("DQM.L1TMonitor.L1TRPCTPG_offline_cff")
#process.l1trpctpg.rpctpgSource = cms.InputTag("rpcunpacker")
#process.l1trpctpg.rpctfSource = cms.InputTag("gtUnpack")

process.a = cms.Path(process.l1trpctf*process.l1trpctfqTester*process.l1trpctfClient*process.dqmEnv*process.dqmSaver)

process.MessageLogger.destinations = ['log.txt']
process.dqmSaver.convention = 'Online'
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'DQM'
process.dqmEnv.subSystemFolder = 'L1T'
process.l1trpctfClient.verbose = True


