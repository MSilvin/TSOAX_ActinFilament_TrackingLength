# TSOAX_ActinFilament_TrackingLength.py
Calcul of Actin Filament Length based on TSOAX text file output.
author: Marine SILVIN, silvinm@igbmc.fr
with the help of : Matthieu BASTO (https://github.com/matthieu66100), Bryan SIENA and Baptiste SION


## TSOAX
_source: https://github.com/tix209/TSOAX_

"TSOAX is an open source software to extract and track the growth and deformation of biopolymer networks from 2D and 3D time-lapse sequences. It tracks each filament or network branch from complex network dynamics and works well even if filaments disappear or reappear.

TSOAX is an extension of SOAX (for network extraction in static images) to network extraction and tracking in time lapse movies."

## Problematic
The goal is to allow a user to obtain a final table containing each length per filament at each frame.
For now, this code results in the creation of a "Results" text file with the ordered data. This then allows the import into Excel in order to perform calculations, graphs or others.

The basic problem posed by the tracking file extracted directly from TSOAX was its complexity of analysis. Indeed, the file was then composed of three main parts:
- segmentation + tracking parameters
- filament IDs with the coordinates of points created during the segmentation
- Tracking results

In addition, the software associated for each filament a different ID to each frame.

For more information, you can consult the SOAX user manual: https://www.lehigh.edu/~div206/tsoax/documentation.html

## Transformation of datas




## How to use this repository
This repository contains the code to transform TSOAX text file output and an example of a TSOAX output named "tracking_snakes.txt".
