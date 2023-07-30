



import xml.etree.ElementTree as XMLElement

#Below are the input values for GenerateXML function. The default value is set to None. Checking for the value of None will then allow some self checks to occur.
def output2ADES2017( 
        d_output_filename       = None, 
        d_mpc_code              = None, 
        d_observatoryName       = None,
        d_submitter             = None, 
        d_observers             = None, 
        d_measurers             = None, 
        d_telescope_design      = None, 
        d_telescope_aperture    = None,
        d_telescope_detector    = None, 
        d_fundingSource         = None, 
        d_comment               = None, 
        d_permID                = None, 
        d_provID                = None, 
        d_trkSub                = None, 
        d_mode                  = None, 
        d_stn                   = None, 
        d_prog                  = None, 
        d_obsTime               = None, 
        d_ra                    = None, 
        d_dec                   = None, 
        d_rmsRA                 = None, 
        d_rmsDec                = None, 
        d_rmsCorr               = None, 
        d_astCat                = None, 
        d_mag                   = None, 
        d_rmsMag                = None, 
        d_band                  = None, 
        d_photCat               = None, 
        d_photAp                = None, 
        d_logSNR                = None, 
        d_seeing                = None, 
        d_exp                   = None, 
        d_notes                 = None, 
        d_remarks               = None
        ):
    
    #print (d_output_filename)
    #print (d_mpc_code)
    #stop
    
    ades = XMLElement.Element('ades', version="2017")
    

    obsBlock = XMLElement.SubElement( ades, "obsBlock")

    #obsBlock Information Section to the next #--
    #---------------------------------------------------------
    obsContext = XMLElement.SubElement( obsBlock, "obsContext" )

    #Observatory Information section to the next ####
    ##############################################################
    observatory = XMLElement.SubElement( obsContext, "observatory")

    #set obsContext/observatory values
    mpcCode = XMLElement.SubElement( observatory, "mpcCode")
    if d_mpc_code == None:
        raise NameError('output2ADES2017 value -> mpc_code -> must be provided')
    else:
        mpcCode.text = d_mpc_code 

    name = XMLElement.SubElement( observatory, "name")
    name.text = d_observatoryName 
    ##############################################################

    #data obsContext/submitter
    submitter = XMLElement.SubElement( obsContext, "submitter")
    submitter_name = XMLElement.SubElement( submitter, "name")
    submitter_name.text = d_submitter

    #data obsContext/observers
    observers = XMLElement.SubElement( obsContext, "observers")
    observers_name = XMLElement.SubElement( observers, "name")
    observers_name.text = d_observers

    #data obsContext/measures
    measurers = XMLElement.SubElement( obsContext, "measurers")
    measurers_name = XMLElement.SubElement( measurers, "name")
    measurers_name.text = d_measurers

    #data obsContext/telescope
    telescope = XMLElement.SubElement( obsContext, "telescope")
    design = XMLElement.SubElement( telescope, "design")
    design.text = d_telescope_design
    aperture = XMLElement.SubElement( telescope, "aperture")
    aperture.text = d_telescope_aperture
    detector = XMLElement.SubElement( telescope, "detector")
    detector.text = d_telescope_detector

    #data obsContext/fundingSource
    fundingSource = XMLElement.SubElement( obsContext, "fundingSource")
    fundingSource.text = d_fundingSource

    #data obsContext/comment
    comment = XMLElement.SubElement( obsContext, "comment")
    comment_line = XMLElement.SubElement( comment, "line")
    comment_line.text = d_comment
    #---------------------------------------------------------




    

    #obsData Information to the next #$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    obsData = XMLElement.SubElement( obsBlock, "obsData" )

    optical = XMLElement.SubElement( obsData, "optical" )

    #optical Information to the next #@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    permID = XMLElement.SubElement( optical, "permID" )
    permID.text = d_permID

    provID = XMLElement.SubElement( optical, "provID" )
    provID.text = d_provID

    trkSub = XMLElement.SubElement( optical, "trkSub" )
    trkSub.text = d_trkSub

    mode = XMLElement.SubElement( optical, "mode" )
    mode.text = d_mode

    stn = XMLElement.SubElement( optical, "stn" )
    stn.text = d_stn

    #prog = XMLElement.SubElement( optical, "prog" )
    #prog.text = d_prog

    obsTime = XMLElement.SubElement( optical, "obsTime" )
    obsTime.text = d_obsTime

    ra = XMLElement.SubElement( optical, "ra" )
    ra.text = d_ra

    dec = XMLElement.SubElement( optical, "dec" )
    dec.text = d_dec

    rmsRA = XMLElement.SubElement( optical, "rmsRA" )
    rmsRA.text = d_rmsRA

    rmsDec = XMLElement.SubElement( optical, "rmsDec" )
    rmsDec.text = d_rmsDec

    rmsCorr = XMLElement.SubElement( optical, "rmsCorr" )
    rmsCorr.text = d_rmsCorr

    astCat = XMLElement.SubElement( optical, "astCat" )
    astCat.text = d_astCat

    mag = XMLElement.SubElement( optical, "mag" )
    mag.text = d_mag

    rmsMag = XMLElement.SubElement( optical, "rmsMag" )
    rmsMag.text = d_rmsMag

    band = XMLElement.SubElement( optical, "band" )
    band.text = d_band

    photCat = XMLElement.SubElement( optical, "photCat" )
    photCat.text = d_photCat

    photAp = XMLElement.SubElement( optical, "photAp" )
    photAp.text = d_photAp

    logSNR = XMLElement.SubElement( optical, "logSNR" )
    logSNR.text = d_logSNR

    seeing = XMLElement.SubElement( optical, "seeing" )
    seeing.text = d_seeing

    exp = XMLElement.SubElement( optical, "exp" )
    exp.text = d_exp

    #notes = XMLElement.SubElement( optical, "notes" )
    #notes.text = d_notes

    remarks = XMLElement.SubElement( optical, "remarks" )
    remarks.text = d_remarks

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


    tree = XMLElement.ElementTree( ades )

    if d_output_filename == None:
        raise NameError('output2ADES2017 value -> output_filename -> must be provided')
    else:
        with open( d_output_filename, 'wb') as files:
            tree.write(files, encoding="UTF-8", xml_declaration=True)

if __name__ == "__main__":

    #below allows a user to call obs2xml.py and have the function create an xml file for testing the function

    #Below is for testing purposes
    output_filename     = "ADES2017.xml" 
    mpc_code            = '807'
    observatoryName     = 'Cerro Tololo Inter-American Observatory'
    submitter           = 'Who Not What'
    observers           = 'Abe Lincoln'
    measurers           = 'John Wayne'
    telescope_design    = 'reflector' 
    telescope_aperture  = '1.0' #do not include the m for meters
    telescope_detector  = 'CCD'
    fundingSource       = 'NASA'
    comment             = 'None'
    permID              = '04933'
    provID              = '2022 LB1'
    trkSub              = 'None'
    mode                = 'CCD'
    stn                 = '807'
    prog                = '|'
    obsTime             = '2016-08-29T12:23:34.12Z'
    ra                  = '215.10254'
    dec                 = '-12.547'
    rmsRA               = '0.015'
    rmsDec              = '0.015'
    rmsCorr             = '-0.214'
    astCat              = '2MASS'
    mag                 = '21.91'
    rmsMag              = '0.25'
    band                = 'r'
    photCat             = 'PPMXL'
    photAp              = '13.3'
    logSNR              = '0.78'
    seeing              = '0.8'
    exp                 = '30.0'
    notes               = 'Hello'
    remarks             = 'None'

    #call the function and pass the keyword arguments
    output2ADES2017(
        d_output_filename       =   output_filename,  
        d_mpc_code              =   mpc_code, 
        d_observatoryName       =   observatoryName, 
        d_submitter             =   submitter, 
        d_observers             =   observers, 
        d_measurers             =   measurers, 
        d_telescope_design      =   telescope_design, 
        d_telescope_aperture    =   telescope_aperture, 
        d_telescope_detector    =   telescope_detector, 
        d_fundingSource         =   fundingSource, 
        d_comment               =   comment, 
        d_permID                =   permID, 
        d_provID                =   provID, 
        d_trkSub                =   trkSub, 
        d_mode                  =   mode, 
        d_stn                   =   stn, 
        d_prog                  =   prog, 
        d_obsTime               =   obsTime, 
        d_ra                    =   ra, 
        d_dec                   =   dec, 
        d_rmsRA                 =   rmsRA, 
        d_rmsDec                =   rmsDec, 
        d_rmsCorr               =   rmsCorr, 
        d_astCat                =   astCat, 
        d_mag                   =   mag, 
        d_rmsMag                =   rmsMag, 
        d_band                  =   band, 
        d_photCat               =   photCat, 
        d_photAp                =   photAp, 
        d_logSNR                =   logSNR, 
        d_seeing                =   seeing, 
        d_exp                   =   exp, 
        d_notes                 =   notes, 
        d_remarks               =   remarks )


