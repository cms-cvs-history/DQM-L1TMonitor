import FWCore.ParameterSet.Config as cms
import sys

#
# cfg file to run L1GtHwValidation 
#
# V M Ghete 2009-10-09 initial version

###################### user choices ######################

# data type
dataType = 'RAW'
#dataType = 'StreamFile'
  
useGlobalTag = 'GR_R_38X_V9'
 
# runNumber for RAW only 
runNumber = 143657
#runNumber = 137028

# change to True to use local files
#     the type of file should match the choice of useGlobalTag
useLocalFiles = False 

###################### end user choices ###################


process = cms.Process("DQM")

#  DQM SERVICES
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

#  DQM SOURCES
process.load("CondCore.DBCommon.CondDBSetup_cfi")

#
# load and configure modules via Global Tag
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions

process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag = useGlobalTag+'::All'



process.load("DQM/L1TMonitor/L1TEmulatorMonitor_cff")


# number of events to be processed and source file
process.maxEvents = cms.untracked.PSet(
    input=cms.untracked.int32(1000)
)

# for RAW data, run first the RAWTODIGI 
if dataType == 'StreamFile' :
    readFiles = cms.untracked.vstring()
    process.source = cms.Source("NewEventStreamFileReader", fileNames=readFiles)
else :        
    readFiles = cms.untracked.vstring()
    secFiles = cms.untracked.vstring() 
    process.source = cms.Source ('PoolSource', fileNames=readFiles, secondaryFileNames=secFiles)


if dataType == 'RAW' : 

    if runNumber == 137028: 
        # data POOL
        dataset = '/Run2010A/ZeroBias/RAW'
        print '   Running on RAW dataset:', dataset, 'run', runNumber, 'with global tag', useGlobalTag 
    
        readFiles.extend( [
            '/store/data/Run2010A/ZeroBias/RAW/v1/000/137/028/0C88B386-3971-DF11-A163-000423D99896.root' 
            ] );

        secFiles.extend([
            ])    
    
    elif runNumber == 143657 : 
        # data POOL
        dataset = '/Run2010A/MinimumBias/RAW'
        print '   Running on RAW dataset:', dataset, 'run', runNumber, 'with global tag', useGlobalTag 
    
        readFiles.extend( [
            '/store/data/Run2010A/MinimumBias/RAW/v1/000/143/657/00FB1636-91AE-DF11-B177-001D09F248F8.root',
            '/store/data/Run2010A/MinimumBias/RAW/v1/000/143/657/023EB128-51AE-DF11-96D3-001D09F24682.root'
            ] );

        secFiles.extend([
            ])    
   
elif dataType == 'FileStream' : 

    # data dat
    print '   Running on FileStream with global tag', useGlobalTag 
    readFiles.extend( [
        'file:/lookarea_SM/MWGR_29.00105760.0001.A.storageManager.00.0000.dat'        
        ] );

process.valGtDigis.AlternativeNrBxBoardDaq = 0x101
process.valGtDigis.AlternativeNrBxBoardEvm = 0x2

if useLocalFiles :
    readFiles = 'file:/afs/cern.ch/user/g/ghete/scratch0/CmsswTestFiles/l1GtHwValidation_source.root'

process.l1demon.disableROOToutput = False
process.valGtDigis.RecordLength = cms.vint32(3, 5)

# Message Logger
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.debugModules = ['l1GtHwValidation']
process.MessageLogger.categories.append('L1GtHwValidation')

process.MessageLogger.cerr.default.limit = 0
process.MessageLogger.cerr.FwkJob.limit = 0
process.MessageLogger.cerr.FwkReport.limit = 0
process.MessageLogger.cerr.FwkSummary.limit = 0

process.MessageLogger.debugs = cms.untracked.PSet( 
        threshold = cms.untracked.string('DEBUG'),
        DEBUG = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
        INFO = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
        WARNING = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
        ERROR = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
        L1GtHwValidation = cms.untracked.PSet( limit = cms.untracked.int32(-1) ) 
        )

process.MessageLogger.warnings = cms.untracked.PSet( 
        threshold = cms.untracked.string('WARNING'),
        WARNING = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
        ERROR = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
        L1GtHwValidation = cms.untracked.PSet( limit = cms.untracked.int32(-1) ) 
        )

process.MessageLogger.errors = cms.untracked.PSet( 
        threshold = cms.untracked.string('ERROR'),
        ERROR = cms.untracked.PSet( limit = cms.untracked.int32(-1) ),
        L1GtHwValidation = cms.untracked.PSet( limit = cms.untracked.int32(-1) ) 
        )

process.DQMStore.verbose = 0
process.dqmSaver.convention = 'Online'
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'DQM'
process.dqmEnv.subSystemFolder = 'L1TEMU'
process.dqmSaver.saveByRun = 1
process.dqmSaver.saveAtJobEnd = True
