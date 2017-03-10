#!/usr/bin/env python
"""
plot spectrum and time of WSPR signals

./PlotWSPRspectrum.py ~/data/170309_2210.wav -f 1400 1700 -t 40 46
"""
from pathlib import Path
from datetime import datetime,timedelta
from pytz import UTC
from numpy import arange
from scipy.io import wavfile
from matplotlib.pyplot import figure,show
import seaborn
#
from piradar.plots import spec

FTICK = (1400,1600) # limit of WSPR audio frequency [Hz]

def wspr_spectrum(wavfn,flim=None,tlim=None):
    wavfn = Path(wavfn).expanduser()
#%% get absolute time
    t0 = datetime.strptime(wavfn.stem[:11],'%y%m%d_%H%M').replace(tzinfo=UTC)
    
    fs,dat = wavfile.read(wavfn)
    
    if tlim:
        i = slice(int(tlim[0]*fs), int(tlim[1]*fs))
        dat = dat[i]
        t0 += timedelta(seconds=tlim[0])
    else:
        tlim = [0]
        
    t = [t0 + timedelta(seconds=T) for T in arange(0,dat.size//fs,1/fs)]
    
    spec(dat,fs,flim,t0,FTICK)
    
    fg = figure()
    ax = fg.gca()
    ax.plot(t,dat)
    ax.set_xlabel('time [UTC]')
    ax.set_ylabel('amplitude [raw]')
    ax.set_title(t0.strftime('%Y-%m-%d'))
    ax.autoscale(True,tight=True)

    
if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('wavfn',help='WSPR recorded wave file, 12kHz')
    p.add_argument('-t','--tlim',help='plot between these seconds of the 110 second file',nargs=2,type=float)
    p.add_argument('-f','--flim',help='plot between these frequencies Hz',nargs=2,type=float)
    p = p.parse_args()
    
    wspr_spectrum(p.wavfn,p.flim,p.tlim)

    show()