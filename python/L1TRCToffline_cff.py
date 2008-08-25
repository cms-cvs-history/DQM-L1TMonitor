import FWCore.ParameterSet.Config as cms


#global configuration
from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *
es_prefer_GlobalTag = cms.ESPrefer("PoolDBESSource","GlobalTag")
#off-line
GlobalTag.globaltag = 'CRUZET4_V1::All'
GlobalTag.connect = 'frontier://FrontierProd/CMS_COND_21X_GLOBALTAG'
#on-line
#GlobalTag.globaltag = 'CRZT210_V1H::All'
#GlobalTag.connect = 'frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG'

#add'n
from Configuration.StandardSequences.Geometry_cff import *

#unpacking
from Configuration.StandardSequences.RawToDigi_Data_cff import *

#emulator/comparator
from L1Trigger.HardwareValidation.L1HardwareValidationGR_cff import *
from L1Trigger.Configuration.L1Config_cff import *

#for LUTs
from DQM.L1TMonitor.Rct_LUTconfiguration_cff import *


#dqm
rctEmulDigis = cms.EDProducer("L1RCTProducer",
    hcalDigisLabel = cms.InputTag("hcalTriggerPrimitiveDigis"),
    useDebugTpgScales = cms.bool(True),
    useEcalCosmicTiming = cms.bool(False),
    postSamples = cms.uint32(0),
    preSamples = cms.uint32(0),
    useHcalCosmicTiming = cms.bool(False),
    useEcal = cms.bool(False),
    useHcal = cms.bool(True),
    ecalDigisLabel = cms.InputTag("ecalTriggerPrimitiveDigis"),
    useCorrectionsLindsey = cms.bool(False)
)

rctEmulDigis.hcalDigisLabel='hcalDigis'
rctEmulDigis.ecalDigisLabel='ecalEBunpacker'

l1tderct = cms.EDFilter("L1TdeRCT",
    rctSourceData = cms.InputTag("l1GctHwDigis"),
    HistFolder = cms.untracked.string('L1TEMU/L1TdeRCT/'),
    outputFile = cms.untracked.string('./L1TDQM.root'),
    verbose = cms.untracked.bool(True),
    DQMStore = cms.untracked.bool(True),
    singlechannelhistos = cms.untracked.bool(False),
    ecalTPGData = cms.InputTag("",""),
    rctSourceEmul = cms.InputTag("rctDigis"),
    disableROOToutput = cms.untracked.bool(False),
    hcalTPGData = cms.InputTag("")
)

l1tderct.rctSourceData = 'gctDigis'
l1tderct.rctSourceEmul = 'rctEmulDigis'
l1tderct.ecalTPGData = 'ecalEBunpacker'
l1tderct.hcalTPGData = 'hcalDigis'

l1trct = cms.EDFilter("L1TRCT",
    DQMStore = cms.untracked.bool(True),
    disableROOToutput = cms.untracked.bool(False),
    outputFile = cms.untracked.string('./L1TDQM.root'),
    rctSource = cms.InputTag("l1GctHwDigis","","DQM"),
    verbose = cms.untracked.bool(False)
)

l1trct.rctSource = 'gctDigis'

p = cms.Path(
    cms.SequencePlaceholder("RawToDigi")
    *cms.SequencePlaceholder("rctEmulDigis")
    *cms.SequencePlaceholder("l1trct")
    *cms.SequencePlaceholder("l1tderct")
    )



