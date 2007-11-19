#include "DQM/L1TMonitor/interface/L1TDEMON.h"
#include <bitset>

using namespace dedefs;

L1TDEMON::L1TDEMON(const edm::ParameterSet& iConfig) {

  verbose_ = iConfig.getUntrackedParameter<int>("VerboseFlag",0);

  if(verbose())
    std::cout << "L1TDEMON::L1TDEMON()...\n" << std::flush;
  
  DEsource_ = iConfig.getParameter<edm::InputTag>("DataEmulCompareSource");
  histFile_ = iConfig.getUntrackedParameter<std::string>("HistFile", "");
  
  nEvt_     = 0;
  for(int i=0; i<DEnsys; i++)
    deSysCount[i]=0;
  
  dbe = NULL;
  if (iConfig.getUntrackedParameter<bool>("DaqMonitorBEInterface", false)) { 
    dbe = edm::Service<DaqMonitorBEInterface>().operator->();
    dbe->setVerbose(0);
  }
  
  monitorDaemon_ = false;
  if(iConfig.getUntrackedParameter<bool>("MonitorDaemon", false)) {
    edm::Service<MonitorDaemon> daemon;
    daemon.operator->();
    monitorDaemon_ = true;
  }
  
  if(dbe!=NULL)
    dbe->setCurrentFolder("L1DEMon");
  
  if(verbose())
    std::cout << "L1TDEMON::L1TDEMON()...done.\n" << std::flush;
}

L1TDEMON::~L1TDEMON() {}

void 
L1TDEMON::beginJob(const edm::EventSetup&) {

  if(verbose())
    std::cout << "L1TDEMON::beginJob()  start\n";

  DaqMonitorBEInterface* dbe = 0;
  dbe = edm::Service<DaqMonitorBEInterface>().operator->();
  if(dbe) {
    dbe->setCurrentFolder("L1DEMon");
    dbe->rmdir("L1DEMon");
  }

  if(dbe) {

    dbe->setCurrentFolder("L1DEMon");
    
    for(int j=0; j<2; j++) {
      std::string lbl("sysncand"); 
      lbl += (j==0?"Data":"Emul");
      sysncand[j] = dbe->book1D(lbl.data(),lbl.data(),DEnsys, 0, DEnsys );
    }

    sysrates = dbe->book1D("sysrates","sysrates",DEnsys, 0, DEnsys );
    const int nerr = 5; 
    errordist = dbe->book1D("errorflag","errorflag",nerr, 0, nerr);

    const double tpi = 6.2832;
    const double amin=   -0.5;
    const double amax=tpi+0.5;

    //                           ETP,  HTP,  RCT, GCT, DTP, DTF,  CTP, CTF, RPC,LTC, GMT,GLT
    int    phiNBins[DEnsys] = { 71  , 71  , 18  ,18  ,  12, 100,   12, 100, 100,  0, 100,0};
    double phiMinim[DEnsys] = {  0.5,  0.5,- 0.5,-0.5,-0.5,amin, -0.5,amin,amin,  0,amin,0};
    double phiMaxim[DEnsys] = { 71.5, 71.5, 17.5,17.5,11.5,amax, 11.5,amax,amax,  0,amax,0};
				     	       	      		    
    int    etaNBins[DEnsys] = { 35  , 35  , 22  ,22  ,   5,  20,    4,  20,  20,  0, 100,0};
    double etaMinim[DEnsys] = {-17.5,-17.5,- 0.5,-0.5,-2.5,-2.5, -0.5,-2.5,-2.5,  0,-2.5,0};
    double etaMaxim[DEnsys] = { 17.5, 17.5, 21.5,21.5, 2.5, 2.5,  3.5, 2.5, 2.5,  0, 2.5,0};
					       	   
    int    x3NBins [DEnsys] = {    0,    0,    0,   0,   4,   0,    0,   0,   0,  0,   0,0};
    double x3Minim [DEnsys] = {    0,    0,    0,   0, 0.5,   0,    0,   0,   0,  0,   0,0};
    double x3Maxim [DEnsys] = {    0,    0,    0,   0, 4.5,   0,    0,   0,   0,  0,   0,0};

    int    rnkNBins[DEnsys] = {    0,    0,    0,   0,   0,   0,    0,   0,   0,  0,   0,0};
    double rnkMinim[DEnsys] = {    0,    0,    0,   0,   0,   0,    0,   0,   0,  0,   0,0};
    double rnkMaxim[DEnsys] = {    0,    0,    0,   0,   0,   0,    0,   0,   0,  0,   0,0};
    //assume for 
    for(int i=0; i<DEnsys; i++) {rnkNBins[i]=63;rnkMinim[i]=0.5;rnkMaxim[i]=63.5;}//rank 0x3f->63
    rnkNBins[DTP]=7;rnkMinim[DTP]=-0.5;rnkMaxim[DTP]=6.5; //rank 0-6

    /*--notes 
      RCT: global index ieta (0-21)=[22,-0.5,21.5] , iphi (0-17)=[18,-0.5,17.5]; crate (18) card (7)
      GCT: phi index (0-17); eta = -6 to -0, +0 to +6. Sign is bit 3, 1 means -ve Z, 0 means +ve Z -> 0.17
      DTP  usc 0..11; uwh -2..2; ust 1..4; 
    */

    for(int j=0; j<DEnsys; j++) {

      dbe->setCurrentFolder(std::string("L1DEMon/"+SystLabelExt[j]));

      std::string lbl("");
      lbl.clear();
      lbl+=SystLabel[j];lbl+="ErrorFlag"; 
      errortype[j] = dbe->book1D(lbl.data(),lbl.data(), nerr, 0, nerr);

      //
      lbl.clear();
      lbl+=SystLabel[j];lbl+="eta"; 
      eta[j] = dbe->book1D(lbl.data(),lbl.data(),
			   etaNBins[j], etaMinim[j], etaMaxim[j]);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="phi"; 
      phi[j] = dbe->book1D(lbl.data(),lbl.data(),
			   phiNBins[j], phiMinim[j], phiMaxim[j]);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="x3"; 
      x3[j] = dbe->book1D(lbl.data(),lbl.data(),
			   x3NBins[j], x3Minim[j], x3Maxim[j]);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="etaphi"; 
      etaphi[j] = dbe->book2D(lbl.data(),lbl.data(), 
			      etaNBins[j], etaMinim[j], etaMaxim[j],
			      phiNBins[j], phiMinim[j], phiMaxim[j]
			      );
      //
      lbl.clear();
      lbl+=SystLabel[j];lbl+="eta"; lbl+="Data";
      etaData[j] = dbe->book1D(lbl.data(),lbl.data(),
			       etaNBins[j], etaMinim[j], etaMaxim[j]);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="phi";  lbl+="Data";
      phiData[j] = dbe->book1D(lbl.data(),lbl.data(),
			       phiNBins[j], phiMinim[j], phiMaxim[j]);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="x3";  lbl+="Data";
      x3Data[j] = dbe->book1D(lbl.data(),lbl.data(),
			      x3NBins[j], x3Minim[j], x3Maxim[j]);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="rank";  lbl+="Data";
      rnkData[j] = dbe->book1D(lbl.data(),lbl.data(),
			       rnkNBins[j], rnkMinim[j], rnkMaxim[j]);
      
      const int nbit = 32;
      lbl.clear();
      lbl+=SystLabel[j];lbl+="dword"; 
      dword[j] = dbe->book1D(lbl.data(),lbl.data(),nbit,0,nbit);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="eword"; 
      eword[j] = dbe->book1D(lbl.data(),lbl.data(),nbit,0,nbit);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="deword"; 
      deword[j] = dbe->book1D(lbl.data(),lbl.data(),nbit,0,nbit);
      lbl.clear();
      lbl+=SystLabel[j];lbl+="masked"; 
      masked[j] = dbe->book1D(lbl.data(),lbl.data(),nbit,0,nbit);
    }

    ///correlation
    dbe->setCurrentFolder("L1DEMon/CORR");
    const int ncorr = 3;
    std::string corrl[ncorr] = {"phi","eta","rank"};
    for(int i=0; i<DEnsys; i++) {
      for(int j=0; j<DEnsys; j++) {
	if(i>j) continue;
	std::string lbl("");
	lbl.clear(); lbl+=SystLabel[i]; lbl+=SystLabel[j]; lbl+=corrl[0]; 
	CORR[i][j][0]= dbe->book2D(lbl.data(),lbl.data(), 
				   phiNBins[i], phiMinim[i], phiMaxim[i],
				   phiNBins[j], phiMinim[j], phiMaxim[j]
				   );
	lbl.clear(); lbl+=SystLabel[i]; lbl+=SystLabel[j]; lbl+=corrl[1]; 
	CORR[i][j][1]= dbe->book2D(lbl.data(),lbl.data(), 
				   etaNBins[i], etaMinim[i], etaMaxim[i],
				   etaNBins[j], etaMinim[j], etaMaxim[j]
				   );
	lbl.clear(); lbl+=SystLabel[i]; lbl+=SystLabel[j]; lbl+=corrl[2]; 
	CORR[i][j][2]= dbe->book2D(lbl.data(),lbl.data(), 
				   rnkNBins[i], rnkMinim[i], rnkMaxim[i],
				   rnkNBins[j], rnkMinim[j], rnkMaxim[j]
				   );
      }
    }
    
  }
  
  /// labeling (temporary cosmetics added here)
  for(int i=0; i<DEnsys; i++) {
    sysrates   ->setBinLabel(i+1,SystLabel[i]);
    sysncand[0]->setBinLabel(i+1,SystLabel[i]);
    sysncand[1]->setBinLabel(i+1,SystLabel[i]);
  }
  const int nerr=5;
  std::string errLabel[nerr]= {
    "Agree", "Loc. Agree", "L.Disagree", "Data only", "Emul only"
  };
  for(int j=0; j<nerr; j++) {
    errordist->setBinLabel(j+1,errLabel[j]);
  }
  for(int i=0; i<DEnsys; i++) {
    for(int j=0; j<nerr; j++) {
      errortype[i]->setBinLabel(j+1,errLabel[j]);
    }
  }
  for(int i=0; i<DEnsys; i++) {
    etaphi [i]->setAxisTitle("eta",1);
    etaphi [i]->setAxisTitle("phi",2);
    eta    [i]->setAxisTitle("eta");
    phi    [i]->setAxisTitle("phi");
    x3     [i]->setAxisTitle("x3");
    etaData[i]->setAxisTitle("eta");
    phiData[i]->setAxisTitle("phi");
    x3Data [i]->setAxisTitle("x3");
    rnkData[i]->setAxisTitle("rank");
    dword  [i]->setAxisTitle("trigger data word bit");
    eword  [i]->setAxisTitle("trigger data word bit");
    deword [i]->setAxisTitle("trigger data word bit");
    masked [i]->setAxisTitle("trigger data word bit");
  }
  for(int i=0; i<DEnsys; i++) {
    for(int j=0; j<DEnsys; j++) {
      if(i>j) continue;
      for(int k=0; k<3; k++) {
	CORR[i][j][k]->setAxisTitle(SystLabel[i],1);
	CORR[i][j][k]->setAxisTitle(SystLabel[j],2);
      }
    }
  }

  ///assertions/temporary
  assert(ETP==0); assert(HTP==1); assert(RCT== 2); assert(GCT== 3);
  assert(DTP==4); assert(DTF==5); assert(CTP== 6); assert(CTF== 7);
  assert(RPC==8); assert(LTC==9); assert(GMT==10); assert(GLT==11);
  
  if(verbose())
    std::cout << "L1TDEMON::beginJob()  end.\n" << std::flush;
}

void 
L1TDEMON::endJob() {

  if(verbose())
    std::cout << "L1TDEMON::endJob Nevents: " << nEvt_ << "\n" << std::flush;

  for(int i=1; i<sysrates->getNbinsX(); i++) {
    double vali = sysrates->getBinContent(i)/nEvt_;
    sysrates->setBinContent(i,vali);
  }
  
  if(verbose()) {
    std::cout << "[L1TDEMON] verbose fill histo: ";
    for(int i=0; i<DEnsys; i++)
      std::cout <<  deSysCount[i] << " ";
    std::cout << std::endl;  
  }

  if(histFile_.size()!=0  && dbe) 
    dbe->save(histFile_);
  
  if(verbose())
    std::cout << "L1TDEMON::endJob()  end.\n" << std::flush;
}


// ------------ method called to for each event  ------------
void
L1TDEMON::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  
  if(verbose())
    std::cout << "L1TDEMON::analyze()  start\n" << std::flush;

  nEvt_++;

  /// get the comparison results
  edm::Handle<L1DataEmulRecord> deRecord;
  iEvent.getByLabel(DEsource_, deRecord);
  
  bool deMatch[DEnsys];
  deRecord->get_status(deMatch);  
  if(verbose()) {
    std::cout << "[L1TDEMON] verbose sys match?: ";
    for(int i=0; i<DEnsys; i++)
      std::cout << deMatch[i] << " ";
    std::cout << std::endl;
  }

  bool isComp[DEnsys];
  for(int i=0; i<DEnsys; i++)
    isComp[i] = deRecord->get_isComp(i);
  if(verbose()) {
    std::cout << "[L1TDEMON] verbose dosys?: ";
    for(int i=0; i<DEnsys; i++)
      std::cout << isComp[i];
    std::cout << std::endl;
  }

  int DEncand[DEnsys][2];
  for(int i=0; i<DEnsys; i++)
    for(int j=0; j<2; j++) 
      DEncand[i][j] = deRecord->getNCand(i,j);
  if(verbose()) {
    std::cout << "[L1TDEMON] ncands d: ";
    for(int i=0; i<DEnsys; i++)
      std::cout << DEncand[i][0] << " ";
    std::cout << std::endl;  
    std::cout << "[L1TDEMON] ncands e: ";
    for(int i=0; i<DEnsys; i++)
      std::cout << DEncand[i][1] << " ";
    std::cout << std::endl;
  }


  const int nullVal = L1DataEmulDigi().reset();

  /// get the de candidates
  L1DEDigiCollection deColl;
  deColl = deRecord->getColl();

  if(verbose()) {
    std::cout << "[L1TDEMON] digis: \n";
    for(L1DEDigiCollection::const_iterator it=deColl.begin(); it!=deColl.end(); it++)
      std::cout << "\t" << *it << std::endl;
  }
  

  /// --- Fill histograms(me) ---

  // global, sub-systems d|e match, ncands
  for(int i=0; i<DEnsys; i++) {
    if(!isComp[i]) continue;
    if(deMatch[i])
      deSysCount[i]++;
    sysrates->Fill(i,(int)!deMatch[i]);
    for(int j=0; j<2; j++) 
      sysncand[j]->Fill(i,DEncand[i][j]);
  }
  
  // container for subsystem's leading candidate
  const int ncorr = 3;
  float LeadCandVal[DEnsys][ncorr] = {{nullVal}};
  for(int i=0; i<DEnsys; i++) 
    for(int j=0; j<ncorr; j++)
      LeadCandVal[i][j]=nullVal;

  // d|e candidate loop
  for(L1DEDigiCollection::const_iterator it=deColl.begin(); it!=deColl.end(); it++) {

    int    sid = it->sid();
    int    cid = it->cid();

    if(it->empty())
      continue;
    assert(isComp[sid]);

    int type   = it->type();
    double phiv = it->x1();
    double etav = it->x2();
    double x3v  = it->x3();

    float rankarr[2]; 
    it->rank(rankarr);
    float rnkv = rankarr[0];

    double wei = 1.;

    unsigned int mask = (~0x0);

    if(sid==RCT) {
      if(cid!=RCTem)  continue;
      //if(cid!=RCTrgn) continue;
    }
    if(sid==GCT) { 
      if(cid!=GCTem ) continue;
      //if(cid!=GCTjet) continue;
    }      
    if(sid==DTP) {
      //tbd cols:th,ph; plots per wheel
      //if(it->x3()!=0) continue;
    }
    if(sid==GMT) { 
      //select gmt cands only for GMT sys 
      if(cid!=GMTcnd) continue;
      //masking: gres -- I.Mikulec: mask bits 0,5,16,21,22,23
      //mask = (~(0x0e10021));
    }
    if(sid==DTF || sid==RPC || sid==CTF || sid==RPC) { 
      //select mu regional cands only for dtf,ctf,rpc
      if(cid!=MUrtf) continue;
      //masking: gres dttf only -- I.Mikulec: lowest 16 bits only
      //if(sid==DTF) mask = 0xffff;
    }
    
    errordist     ->Fill(type);
    errortype[sid]->Fill(type);

    //exclude agreeing cands
    wei=1.; if(!type) wei=0.;
    if(etav!=nullVal && phiv!=nullVal)
      etaphi[sid]->Fill(etav,phiv,wei);
    if(etav!=nullVal)
      eta   [sid]->Fill(etav,wei);
    if(phiv!=nullVal)
      phi   [sid]->Fill(phiv,wei);
    if(sid==DTP)
      if(x3v!=nullVal)
	x3    [sid]->Fill( x3v,wei);
    
    unsigned int word[2];
    it->data(word);
    std::bitset<32> dbits(word[0]);
    std::bitset<32> ebits(word[1]);
    unsigned int dexor = ( (word[0]) ^ (word[1]) );
    //disagreeing bits
    std::bitset<32> debits(dexor);
    //disagreeing bits after masking
    std::bitset<32> dembits( ( (dexor) & (mask) ) );
    
    if(verbose())
      std::cout << "l1demon" 
		<< " sid:" << sid << " cid:" << cid << "\n"
		<< " data:0x" << std::hex << word[0] << std::dec
		<< " bitset:" << dbits
		<< "\n"
		<< " emul:0x" << std::hex << word[1] << std::dec
		<< " bitset:" << ebits
		<< "\n"
		<< "  xor:0x" << std::hex << dexor << std::dec
		<< " bitset:" << debits
		<< " bitset:" << ( (dbits) ^ (ebits) )
		<< "\n" << std::flush;

    ///bitset loop
    for(int ibit=0; ibit<32; ibit++) {
      wei=1.;
      //comparison gives no info if there's only 1 candidate
      if(type==3 || type==4) wei=0.; 
      if(dbits  [ibit]) dword[sid]->Fill(ibit,wei);
      if(ebits  [ibit]) eword[sid]->Fill(ibit,wei);
      if(debits [ibit])deword[sid]->Fill(ibit,wei);
      if(dembits[ibit])masked[sid]->Fill(ibit,wei);
    }

    //exclude e-only cands (only data)
    wei=1.;if(type==4) wei=0.;
    if(etav!=nullVal)
      etaData[sid]->Fill(etav,wei);
    if(phiv!=nullVal)
      phiData[sid]->Fill(phiv,wei);
    if(sid==DTP)
      if(x3v!=nullVal)
	x3Data [sid]->Fill( x3v,wei);
    rnkData[sid]->Fill(rnkv,wei);

    //correlations: store leading candidate
    if(type==4) continue; //exclude e-only cands
    if(rnkv>=LeadCandVal[sid][2]) {
      LeadCandVal[sid][0] = phiv;
      LeadCandVal[sid][1] = etav;
      LeadCandVal[sid][2] = rnkv;
    }
    
  }//close loop over dedigi-cands


  ///correlations: fill histograms
  double wei=1.;
  for(int i=0; i<DEnsys; i++) {
    for(int j=0; j<DEnsys; j++) {
      if(i>=j) continue;
      for(int k=0; k<ncorr; k++) {
	if(LeadCandVal[i][k]!=nullVal && LeadCandVal[j][k]!=nullVal)
	  CORR[i][j][k]->Fill(LeadCandVal[i][k],LeadCandVal[j][k],wei);
      }
    }
  }

  if(verbose())
    std::cout << "L1TDEMON::analyze() end.\n" << std::flush;

}