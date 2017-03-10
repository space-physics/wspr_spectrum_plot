====================
WSPR Spectrum Plots
====================

Analysis of WSPR spectrum, in the face of fading and audio glitches.

Assumes you or a friend has the `.wav files saved by WSPR Save>Save All <https://www.scivision.co/wspr-save-raw-wav-data/>`_.


.. image:: glitch_spectrum.png

Glitches in spectrum (broadband hash) caused by dropouts on a UDP link. 
Interference is about -25 dB down by edge of WSPR.
That means if you're transmitting with 1 Watt (30 dBm) than the WSPR band gets pulses of hash with several milliwatts of power.

Correspondingly, if one was transmitting with 100 Watt (50dBm), the WSPR band is getting intermittant splashes of 1 Watt of power.

Here's what the dropouts looks like in the time domain:

.. image:: time.png
   
