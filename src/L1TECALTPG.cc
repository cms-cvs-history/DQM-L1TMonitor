/*
 * \file L1TECALTPG.cc
 *
 * $Date: 2007/08/29 14:02:47 $
 * $Revision: 1.6 $
 * \author J. Berryhill
 *
 * - initial version stolen from GCTMonnitor (thanks!) (wittich 02/07)
 *
 * $Log: L1TECALTPG.cc,v $
 * Revision 1.6  2007/08/29 14:02:47  wittich
 * split into barrel and endcap
 *
 * Revision 1.5  2007/05/25 15:45:48  berryhil
 *
 *
 *
 * added exception handling for each edm Handle
 * updated cfg and cff to reflect recent usage at point 5
 *
 * Revision 1.4  2007/02/22 19:43:53  berryhil
 *
 *
 *
 * InputTag parameters added for all modules
 *
 * Revision 1.3  2007/02/20 22:49:00  wittich
 * - change from getByType to getByLabel in ECAL TPG,
 *   and make it configurable.
 * - fix problem in the GCT with incorrect labels. Not the ultimate
 *   solution - will probably have to go to many labels.
 *
 * Revision 1.2  2007/02/19 22:07:26  wittich
 * - Added three monitorables to the ECAL TPG monitoring (from GCTMonitor)
 * - other minor tweaks in GCT, etc
 *
 */

#include "DQM/L1TMonitor/interface/L1TECALTPG.h"

#include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"

// end of header files 
using namespace edm;

// Local definitions for the limits of the histograms
const unsigned int RTPBINS = 101;
const float RTPMIN = -0.5;
const float RTPMAX = 100.5;

const unsigned int TPPHIBINS = 72;
const float TPPHIMIN = 0.5;
const float TPPHIMAX = 72.5;

const unsigned int TPETABINS = 65;
const float TPETAMIN = -32.5;
const float TPETAMAX = 32.5;


L1TECALTPG::L1TECALTPG(const ParameterSet & ps):
  ecaltpgSourceB_(ps.getParameter<edm::InputTag>("ecaltpgSourceB")),
  ecaltpgSourceE_(ps.getParameter<edm::InputTag>("ecaltpgSourceE"))
{

  // verbosity switch
  verbose_ = ps.getUntrackedParameter < bool > ("verbose", false);

  if (verbose_)
    std::cout << "L1TECALTPG: constructor...." << std::endl;

  logFile_.open("L1TECALTPG.log");

  dbe = NULL;
  if (ps.getUntrackedParameter < bool > ("DaqMonitorBEInterface", false)) {
    dbe = Service < DaqMonitorBEInterface > ().operator->();
    dbe->setVerbose(0);
  }

  monitorDaemon_ = false;
  if (ps.getUntrackedParameter < bool > ("MonitorDaemon", false)) {
    Service < MonitorDaemon > daemon;
    daemon.operator->();
    monitorDaemon_ = true;
  }

  outputFile_ =
      ps.getUntrackedParameter < std::string > ("outputFile", "");
  if (outputFile_.size() != 0) {
    std::cout << "L1T Monitoring histograms will be saved to " 
	      << outputFile_ << std::endl;
  }
  else {
    outputFile_ = "L1TDQM.root";
  }

  bool disable =
      ps.getUntrackedParameter < bool > ("disableROOToutput", false);
  if (disable) {
    outputFile_ = "";
  }


  if (dbe != NULL) {
    dbe->setCurrentFolder("L1T/L1TECALTPG");
  }


}

L1TECALTPG::~L1TECALTPG()
{
}

void L1TECALTPG::beginJob(const EventSetup & c)
{

  nev_ = 0;

  // get hold of back-end interface
  DaqMonitorBEInterface *dbe = 0;
  dbe = Service < DaqMonitorBEInterface > ().operator->();

  if (dbe) {
    dbe->setCurrentFolder("L1T/L1TECALTPG");
    dbe->rmdir("L1T/L1TECALTPG");
  }


  if (dbe) {
    dbe->setCurrentFolder("L1T/L1TECALTPG");
    ecalTpEtEtaPhiB_ = 
      dbe->book2D("EcalTpEtEtaPhiB", "ECAL TP E_{T} Barrel", TPPHIBINS, 
		  TPPHIMIN, TPPHIMAX, TPETABINS, TPETAMIN, TPETAMAX);
    ecalTpOccEtaPhiB_ =
	dbe->book2D("EcalTpOccEtaPhiB", "ECAL TP OCCUPANCY Barrel", TPPHIBINS,
		    TPPHIMIN, TPPHIMAX, TPETABINS, TPETAMIN, TPETAMAX);
    ecalTpRankB_ =
      dbe->book1D("EcalTpRankB", "ECAL TP RANK Barrel", RTPBINS, RTPMIN,
		  RTPMAX);

    ecalTpEtEtaPhiE_ = 
      dbe->book2D("EcalTpEtEtaPhiE", "ECAL TP E_{T} Endcap", TPPHIBINS, 
		  TPPHIMIN, TPPHIMAX, TPETABINS, TPETAMIN, TPETAMAX);
    ecalTpOccEtaPhiE_ =
	dbe->book2D("EcalTpOccEtaPhiE", "ECAL TP OCCUPANCY Endcap", TPPHIBINS,
		    TPPHIMIN, TPPHIMAX, TPETABINS, TPETAMIN, TPETAMAX);
    ecalTpRankE_ =
      dbe->book1D("EcalTpRankE", "ECAL TP RANK Endcap", RTPBINS, RTPMIN,
		  RTPMAX);

  }
}


void L1TECALTPG::endJob(void)
{
  if (verbose_)
    std::cout << "L1TECALTPG: end job...." << std::endl;
  LogInfo("L1TECALTPG") << "analyzed " << nev_ << " events";

  if (outputFile_.size() != 0 && dbe)
    dbe->save(outputFile_);

  return;
}

void L1TECALTPG::analyze(const Event & e, const EventSetup & c)
{
  nev_++;
  if (verbose_) {
    std::cout << "L1TECALTPG: analyze...." << std::endl;
  }

  // Get the ECAL TPGs
  edm::Handle < EcalTrigPrimDigiCollection > eeTP;
  edm::Handle < EcalTrigPrimDigiCollection > ebTP;

  try {
    e.getByLabel(ecaltpgSourceE_,ebTP);
  }
  catch (...) {
    edm::LogInfo("L1TECALTPG") << "can't find EcalTrigPrimCollection with "
      " endcap label " << ecaltpgSourceE_.label() ;
    return;
  }
  try {
    e.getByLabel(ecaltpgSourceE_,eeTP);
  }
  catch (...) {
    edm::LogInfo("L1TECALTPG") << "can't find EcalTrigPrimCollection with "
      " barrel label " << ecaltpgSourceB_.label() ;
    return;
  }

  // Fill the ECAL TPG histograms
  if ( verbose_ ) {
    std::cout << "L1TECALTPG: barrel size is " << ebTP->size() << std::endl;
    std::cout << "L1TECALTPG: endcap size is " << eeTP->size() << std::endl;
  }
  for (EcalTrigPrimDigiCollection::const_iterator iebTP = ebTP->begin();
       iebTP != ebTP->end(); iebTP++) {
    if ( verbose_ ) {
      std::cout << "barrel: " << iebTP->id().iphi() << ", " 
		<< iebTP->id().ieta()
		<< std::endl;
    }
    ecalTpEtEtaPhiB_->Fill(iebTP->id().iphi(), iebTP->id().ieta(),
			  iebTP->compressedEt());
    ecalTpOccEtaPhiB_->Fill(iebTP->id().iphi(), iebTP->id().ieta());
    ecalTpRankB_->Fill(iebTP->compressedEt());

  }
  // endcap
  for (EcalTrigPrimDigiCollection::const_iterator ieeTP = eeTP->begin();
       ieeTP != eeTP->end(); ieeTP++) {
    if ( verbose_ ) {
      std::cout << "endcap: " << ieeTP->id().iphi() << ", " 
		<< ieeTP->id().ieta()
		<< std::endl;
    }
    ecalTpEtEtaPhiE_->Fill(ieeTP->id().iphi(), ieeTP->id().ieta(),
			  ieeTP->compressedEt());
    ecalTpOccEtaPhiE_->Fill(ieeTP->id().iphi(), ieeTP->id().ieta());
    ecalTpRankE_->Fill(ieeTP->compressedEt());

  }


}
