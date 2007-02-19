/*
 * \file L1TCSCTPG.cc
 *
 * $Date: 2007/02/02 06:01:40 $
 * $Revision: 1.00 $
 * \author J. Berryhill
 *
 */

#include "DQM/L1TMonitor/interface/L1TCSCTPG.h"

using namespace std;
using namespace edm;

L1TCSCTPG::L1TCSCTPG(const ParameterSet& ps)
{

  // verbosity switch
  verbose_ = ps.getUntrackedParameter<bool>("verbose", false);

  if(verbose_) cout << "L1TCSCTPG: constructor...." << endl;

  logFile_.open("L1TCSCTPG.log");

  dbe = NULL;
  if ( ps.getUntrackedParameter<bool>("DaqMonitorBEInterface", false) ) 
  {
    dbe = Service<DaqMonitorBEInterface>().operator->();
    dbe->setVerbose(0);
  }

  monitorDaemon_ = false;
  if ( ps.getUntrackedParameter<bool>("MonitorDaemon", false) ) {
    Service<MonitorDaemon> daemon;
    daemon.operator->();
    monitorDaemon_ = true;
  }

  outputFile_ = ps.getUntrackedParameter<string>("outputFile", "");
  if ( outputFile_.size() != 0 ) {
    cout << "L1T Monitoring histograms will be saved to " << outputFile_.c_str() << endl;
  }
  else{
    outputFile_ = "L1TDQM.root";
  }

  bool disable = ps.getUntrackedParameter<bool>("disableROOToutput", false);
  if(disable){
    outputFile_="";
  }


  if ( dbe !=NULL ) {
    dbe->setCurrentFolder("L1TMonitor/L1TCSCTPG");
  }


}

L1TCSCTPG::~L1TCSCTPG()
{
}

void L1TCSCTPG::beginJob(const EventSetup& c)
{

  nev_ = 0;

  // get hold of back-end interface
  DaqMonitorBEInterface* dbe = 0;
  dbe = Service<DaqMonitorBEInterface>().operator->();

  if ( dbe ) {
    dbe->setCurrentFolder("L1TMonitor/L1TCSCTPG");
    dbe->rmdir("L1TMonitor/L1TCSCTPG");
  }


  if ( dbe ) 
  {
    dbe->setCurrentFolder("L1TMonitor/L1TCSCTPG");
    
    csctpgpattern = dbe->book1D("CSC TPG hit pattern", 
       "CSC TPG hit pattern", 8, -0.5, 7.5 ) ;
    csctpgquality = dbe->book1D("CSC TPG quality", 
       "CSC TPG quality", 16, 0.5, 16.5 ) ;
    csctpgwg = dbe->book1D("CSC TPG wire group", 
       "CSC TPG wire group", 116, -0.5, 115.5 ) ;
    csctpgstrip = dbe->book1D("CSC TPG strip", 
       "CSC TPG strip", 160, -0.5, 159.5 ) ;
    csctpgstriptype = dbe->book1D("CSC TPG strip type", 
       "CSC TPG strip type", 2, 0.5, 1.5 ) ;
    csctpgbend = dbe->book1D("CSC TPG bend", 
       "CSC TPG bend", 3, 0.5, 2.5 ) ;
    csctpgbx = dbe->book1D("CSC TPG bx", 
       "CSC TPG bx", 20, -0.5, 19.5 ) ;


  }  
}


void L1TCSCTPG::endJob(void)
{
  if(verbose_) cout << "L1TCSCTPG: end job...." << endl;
  LogInfo("L1TCSCTPG") << "analyzed " << nev_ << " events"; 

 if ( outputFile_.size() != 0  && dbe ) dbe->save(outputFile_);

 return;
}

void L1TCSCTPG::analyze(const Event& e, const EventSetup& c)
{
  nev_++; 
  if(verbose_) cout << "L1TCSCTPG: analyze...." << endl;


  Handle<CSCCorrelatedLCTDigiCollection> pCSCTPGcorrlcts;
  e.getByLabel("lctproducer","MPCSORTED",pCSCTPGcorrlcts);
  const CSCCorrelatedLCTDigiCollection* myCSCTPGcorrlcts =
    pCSCTPGcorrlcts.product();
  for (CSCCorrelatedLCTDigiCollection::DigiRangeIterator cscItr1 = myCSCTPGcorrlcts->begin();
       cscItr1 != myCSCTPGcorrlcts->end();
       cscItr1++)
    {
     CSCCorrelatedLCTDigiCollection::Range range1 = myCSCTPGcorrlcts->get((*cscItr1).first);
     for (CSCCorrelatedLCTDigiCollection::const_iterator lctItr1 = range1.first;
	   lctItr1 != range1.second;
	   lctItr1++) 
        {


     csctpgpattern->Fill(lctItr1->getCLCTPattern());
    if (verbose_)
       {     
     std::cout << "CSC TPG CLCT pattern " << lctItr1->getCLCTPattern()  
   	    << std::endl;
       }

     csctpgquality->Fill(lctItr1->getQuality());     
     if (verbose_)
       {
     std::cout << "CSC LCT quality " << lctItr1->getQuality()  
   	    << std::endl;
       }

     csctpgwg->Fill(lctItr1->getKeyWG());     
     if (verbose_)
        {
     std::cout << "CSC LCT wire group " << lctItr1->getKeyWG()  
   	    << std::endl;
	}

     csctpgstrip->Fill(lctItr1->getStrip());     
     if (verbose_)
        {     
     std::cout << "CSC LCT strip " << lctItr1->getStrip()  
   	    << std::endl;
	}

     csctpgstriptype->Fill(lctItr1->getStripType());    
     if (verbose_)
       { 
     std::cout << "CSC LCT strip type" << lctItr1->getStripType()  
   	    << std::endl;
       }

     csctpgbend->Fill(lctItr1->getBend());     
     if (verbose_)
       {
     std::cout << "CSC LCT bend " << lctItr1->getBend()  
   	    << std::endl;
       }

     csctpgbx->Fill(lctItr1->getBX());
     if (verbose_)
        {     
     std::cout << "CSC LCT bx " << lctItr1->getBX()  
   	    << std::endl;
	}

     }
    }

   
 
}
