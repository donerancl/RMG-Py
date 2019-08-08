#!/usr/bin/env python
# -*- coding: utf-8 -*-

energy = {
    'CBS-QB3': Log('TolueneEnergy.log')
}

geometry = Log('TolueneFreq.log')

frequencies = Log('TolueneFreq.log')

rotors = [HinderedRotorClassicalND(calcPath='TolueneRot1.log', pivots=[[3,12]], tops=[[12,13,14,15]], sigmas=[6], semiclassical=True)]
