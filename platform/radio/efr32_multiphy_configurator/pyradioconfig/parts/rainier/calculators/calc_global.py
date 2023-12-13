from pyradioconfig.parts.bobcat.calculators.calc_global import Calc_Global_Bobcat
from pycalcmodel.core.variable import ModelVariableFormat


class CalcGlobalRainier(Calc_Global_Bobcat):
   def buildVariables(self, model):
      # Build variables from the Ocelot calculations
      super().buildVariables(model)
      self._add_SYNTH_S3_regs(model)

      self._addModelRegister(model, 'MODEM.TXCORR.TXDGAIN6DB', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXCORR.TXDGAIN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXCORR.TXGAINIMB', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXCORR.TXPHSIMB', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.TXFREQCORR.TXFREQCORR', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.TXMISC.FORCECLKEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXIQIMBEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXINTPEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXDSEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXIQSWAP', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXDACFORMAT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXDCI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXDCQ', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.BR2M', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXMOD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXDOFORCEI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXMISC.TXDOFORCEQ', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.TXDACVAL.TXFORCEDI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXDACVAL.TXFORCEDQ', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXDACVAL.TXIDLEI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TXDACVAL.TXIDLEQ', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.DIGMIXCTRL.BLEORZB', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DIGMIXCTRL.MULTIPHYHOP', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DIGMIXCTRL.HOPPINGSRC', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DIGMIXCTRL.RXBRINTSHIFT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DIGMIXCTRL.DSSSCFECOMBO', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.DSSSPMTIMEOUT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.DSSSFRMTIMEOUT', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.COCURRMODE.DSSSDSACHK', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.COCURRMODE.TRECSDSACHK', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.COCURRMODE.CORRCHKMUTE', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.SYNCBITS2TH', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.SYNC0ERRORS', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.SYNC1ERRORS', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.SYNC2ERRORS', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.SYNC3ERRORS', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.DUALSYNC', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.DUALSYNC2TH', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.SYNCDET2TH', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNCWORDCTRL.SYNCSWFEC', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNC2.SYNC2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SYNC3.SYNC3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.SYMIDENTDIS', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.SISTARTDELAY', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'RAC.CLKMULTEN0.CLKMULTLDFNIB', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.CLKMULTEN0.CLKMULTLDMNIB', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.CLKMULTEN0.CLKMULTRDNIBBLE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.CLKMULTEN0.CLKMULTLDCNIB', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'RAC.CLKMULTEN1.CLKMULTBWCAL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.CLKMULTEN1.CLKMULTFREQCAL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.CLKMULTEN1.CLKMULTDIVN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.CLKMULTEN1.CLKMULTDIVR', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.CLKMULTEN1.CLKMULTDIVX', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'RAC.ADCCTRL1.ADCENHALFMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.ADCCTRL0.ADCCLKSEL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.ADCTRIM0.ADCSIDETONEAMP', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.ADCEN0.ADCENNEGRES', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.LNAMIXCTRL1.LNAMIXRFPKDTHRESHSELHI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.LNAMIXCTRL1.LNAMIXRFPKDTHRESHSELLO', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.TIACTRL0.TIATHRPKDHISEL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.TIACTRL0.TIATHRPKDLOSEL', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.EXPECTPATTDUAL.EXPECTPATTDUAL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DUALTIM.DUALTIMEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DUALTIM.MINCOSTTHD2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DUALTIM.SYNCACQWIN2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.COCURRMODE.DSSSCONCURRENT', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.EHDSSSEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.DSSSTIMEACQUTHD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.FOEBIAS', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.FREQCORREN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.DSSSFRQLIM', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.DSSSDSATHD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCTRL.DUALDSA', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.EHDSSSCFG0.DSSSPATT', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.EHDSSSCFG1.DSSSEXPSYNCLEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG1.DSSSCORRTHD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG1.DSSSDSAQTHD', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.EHDSSSCFG2.DSSSTIMCORRTHD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG2.DSSSFRTCORRTHD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG2.DSSSTRACKINGWIN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG2.DSSSCORRSCHWIN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG2.ONESYMBOLMBDD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG2.MAXSCHMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG2.DSSSDSAQUALEN', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.EHDSSSCFG3.DSSSDASMAXTHD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG3.DSSSFOETRACKGEAR', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG3.OPMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.EHDSSSCFG3.DSSSINITIMLEN', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.CMD.HOPPINGSTART', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.CTRL3.ANTDIVMODE', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.SICTRL0.SIMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL0.NDFOCAL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL0.PEAKNUMTHRESHLW', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL0.FREQNOMINAL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL0.PEAKNUMADJ', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL0.NOISETHRESH', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL0.NOISETHRESHADJ', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.SICTRL1.TWOSYMBEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.SMALLSAMPLETHRESH', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.SUPERCHIPTOLERANCE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.FASTMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.PEAKNUMP2ADJ', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.ZCEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.ZCSAMPLETHRESH', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.SOFTCLIPBYPASS', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL1.SOFTCLIPTHRESH', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.SICTRL2.SIRSTAGCMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.SIRSTPRSMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.SIRSTCCAMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.DISSIFRAMEDET', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.AGCRSTUPONSI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.SUPERCHIPNUM', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.CORRNUM', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.SHFTWIN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.NARROWPULSETHRESH', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICTRL2.PEAKNUMADJEN', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.SICORR.CORRTHRESH', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICORR.CORRTHRESHLOW', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICORR.CORRTHRESHUP', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.SICORR.CORRTHRESH2SYMB', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'RAC.AUXADCCTRL2.ADCENHALFMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.IFADCTRIM0.ADCCLKSEL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.IFADCTRIM1.ADCSIDETONEAMP', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.AUXADCEN.ADCENNEGRES', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.RX.LNAMIXRFPKDTHRESHSELHI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.RX.LNAMIXRFPKDTHRESHSELLO', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.TIAEN.TIAENLATCHI', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.TIAEN.TIAENLATCHQ', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.TIAEN.TIATHRPKDHISEL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'RAC.TIAEN.TIATHRPKDLOSEL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TRECSCFG.SOFTD', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.TRECSCFG.SDSCALE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.DIGMIXCTRL.FWHOPPING', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.PHDMODCTRL.FASTHOPPINGEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'MODEM.PHDMODCTRL.CHPWRQUAL', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'MODEM.SRCCHF.CHMUTETIMER', int, ModelVariableFormat.HEX)

   #################################
   # Update for Series 3 SYIF
   #################################
   def _add_SYNTH_LPFCTRL_regs(self, model):
      self._addModelRegister(model, 'SYNTH.DLFCTRL.LOCKLPFBWGEAR0', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRL.LOCKLPFBWGEAR1', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR4', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR5', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR6', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR7', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR8', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLRX.RXLOCKLPFBWGEAR9', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR4', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR5', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR6', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR7', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR8', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRLTX.TXLOCKLPFBWGEAR9', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'SYNTH.DLFCTRL.LOCKLPFBWGEARSLOT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRL.LPFBWLOADDEL', int, ModelVariableFormat.HEX)

   def _add_SYNTH_DSMCTRL_regs(self, model):
      self._addModelRegister(model, 'SYNTH.DSMCTRLRX.LSBFORCERX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DSMCTRLRX.DITHERDACRX', int,
                             ModelVariableFormat.HEX)  # QNC need for RX HOP
      self._addModelRegister(model, 'SYNTH.DSMCTRLRX.DEMMODERX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DSMCTRLRX.REQORDERRX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DSMCTRLTX.LSBFORCETX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DSMCTRLTX.DITHERDACTX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DSMCTRLTX.PHISELTX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DSMCTRLTX.DEMMODETX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DSMCTRLTX.REQORDERTX', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.QNCCTRL.QNCMODE', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.QNCCTRL.QNCOFFSET', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.QNCCTRL.ENABLEDQNCTIME', int, ModelVariableFormat.HEX)

   def _add_SYNTH_DENOMINIT_regs(self, model):
      self._addModelRegister(model, 'SYNTH.MMDDENOMINIT.DENOMINIT0', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.MMDDENOMINIT.DENOMINIT1', int, ModelVariableFormat.HEX)

   def _add_SYNTH_S3_regs(self, model):
      ## Hopping
      self._addModelRegister(model, 'SYNTH.HOPPING.HOPLPFBWGEARSLOT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.HOPPING.HOPHCAPDELAY', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.HOPPING.HCAPRETIMEEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.HOPPING.HCAPRETIMESEL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRL.LPFBWDURINGHOP', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.DLFCTRL.LPFBWAFTERHOP', int, ModelVariableFormat.HEX)
      ## LMS
      self._addModelRegister(model, 'SYNTH.GLMS.GLMSENABLEDELAY', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.GLMS.GLMSGEAR0', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.GLMS.GLMSGEAR1', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.GLMS.GLMSGEAR2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.GLMS.GLMSGEAR3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.GLMS.GLMSGEAR4', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.GLMS.GLMSGEARSLOT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.PLMS.PLMSENABLEDELAY', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.PLMS.PLMSGEAR0', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.PLMS.PLMSGEAR1', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.PLMS.PLMSGEAR2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.PLMS.PLMSGEAR3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.PLMS.PLMSGEAR4', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.PLMS.PLMSGEARSLOT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LMSOVERRIDE.GLMSOVERRIDEEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LMSOVERRIDE.GLMSOVERRIDEVAL', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LMSOVERRIDE.PLMSOVERRIDEEN', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LMSOVERRIDE.PLMSOVERRIDEVAL', int, ModelVariableFormat.HEX)
      ## FCAL HW
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION0', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION1', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION4', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION5', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION6', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.COMPANION.COMPANION7', int, ModelVariableFormat.HEX)

      # self._addModelRegister(model, 'SYNTH.LOCNTCTRL.NUMCYCLE', int, ModelVariableFormat.HEX) #already defined
      self._addModelRegister(model, 'SYNTH.LOCNTCTRL.NUMCYCLE1', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LOCNTCTRL.NUMCYCLE2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LOCNTCTRL.NUMCYCLE3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LOCNTCTRL.NUMCYCLE4', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.LOCNTCTRL.NUMCYCLE5', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALCTRL.NUMCYCLE6', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALCTRL.NUMCYCLE7', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALCTRL.NUMCYCLE8', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALCTRL.NUMCYCLE9', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALCTRL.NUMCYCLE10', int, ModelVariableFormat.HEX)

      self._addModelRegister(model, 'SYNTH.FCALCTRL.STEPWAIT', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT1', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT2', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT3', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT4', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT5', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT6', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT7', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT8', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT9', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALSTEPWAIT.STEPWAIT10', int, ModelVariableFormat.HEX)
      self._addModelRegister(model, 'SYNTH.FCALCTRL.FCALMODE', int, ModelVariableFormat.HEX)