#!/usr/bin/env python3
# *-* coding: utf-8 *-*
"""
SIP-04 Import
=============

"""
#############################################################################
# Create the SIP container
import reda
sip = reda.SIP()

#############################################################################
# Import the SIP data
sip.import_sip04('sip_data.mat')

#############################################################################
# show the data
print(type(sip.data))
print(sip.data[['a', 'b', 'm', 'n', 'frequency', 'r', 'rpha']])

#############################################################################
# plot the spectrum
from reda.eis.plots import sip_response

spectrum = sip_response(
    frequencies=sip.data['frequency'].values,
    rcomplex=sip.data['zt'].values,
)

fig = spectrum.plot(filename='spectrum.pdf', dtype='r', return_fig=True)

