#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:18:35 2022

@author: gavinkoma
"""
# %%
#okay something about the previous data really just doesnt make any sense
#the math just isnt right, so were going to go through and double check and be safe
import sys
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#%%
#read in the data
#we can just use the control rat as the normalization point
idx = pd.IndexSlice
inhib = pd.read_csv("Rupert_week2_cam2_Inhibitory Rat 5_2021-08-10_11_28_34_fr_wbgam_h264_nearlossless_safeDLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000.csv",index_col=0,header=[0,1,2])
control = pd.read_csv("Rupert_week2_cam2_MG Control 2_2021-08-10_11_11_56_fr_wbgam_h264_nearlossless_safeDLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000.csv",index_col=0,header=[0,1,2])
ex = pd.read_csv("Rupert_week2_cam2_JI Excitatory 4_2021-08-10_11_02_23_fr_wbgam_h264_nearlossless_safeDLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000.csv",index_col=0,header=[0,1,2])

#%%
#read in the corner csv
corner = pd.read_csv("cornercoordinate_controlxypts.csv")
xval = corner.iloc[0][0]
float(xval)
yval = corner.iloc[0][1]
float(yval)
print(xval,yval)

#%%

inhibitoryshoulderx = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'shoulder','x']]

inhibitoryshouldery = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'shoulder','y']]
    
inhibitoryelbowx = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'elbow','x']]
    
inhibitoryelbowy = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'elbow','y']]
    
inhibitorywristx = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'wrist','x']]
    
inhibitorywristy = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'wrist','y']]
    

inhibitoryshoulderx = pd.DataFrame([float(x) for x in inhibitoryshoulderx]-xval)
inhibitoryshouldery = pd.DataFrame([float(x) for x in inhibitoryshouldery]-yval)

inhibitoryelbowx = pd.DataFrame([float(x) for x in inhibitoryelbowx]-xval)
inhibitoryelbowy = pd.DataFrame([float(x) for x in inhibitoryelbowy]-yval)

inhibitorywristx = pd.DataFrame([float(x) for x in inhibitorywristx]-xval)
inhibitorywristy = pd.DataFrame([float(x) for x in inhibitorywristy]-yval)

#make them into one pandas dataframe pls
inhibitoryresults = pd.concat([inhibitoryshoulderx, inhibitoryshouldery, inhibitoryelbowx, inhibitoryelbowy, inhibitorywristx, inhibitorywristy],axis = 1, join='inner')
inhibitoryresults.columns = ['inhibshoulderx','inhibshouldery','inhibelbowx','inhibelbowy','inhibwristx','inhibwristy']
display(inhibitoryresults)

plt.figure(1)
plt.clf()
plt.scatter(inhibitoryshoulderx,inhibitoryshouldery,label = "Inhib Shoulder",s=5)
plt.scatter(inhibitoryelbowx,inhibitoryelbowy,label = "Inhib Elbow",s=5)
plt.scatter(inhibitorywristx,inhibitorywristy,label = "Inhib Wrist",s=5)
plt.title("Inhibitory Rat")
plt.legend(loc = 2)

plt.savefig("inhibitoryratplot.jpg")

#%%
#control rat next

controlshoulderx = control.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'shoulder','x']]

controlshouldery = control.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'shoulder','y']]
    
controlelbowx = control.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'elbow','x']]
    
controlelbowy = control.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'elbow','y']]
    
controlwristx = control.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'wrist','x']]
    
controlwristy = control.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'wrist','y']]

controlshoulderx = pd.DataFrame([float(x) for x in controlshoulderx]-xval)
controlshouldery = pd.DataFrame([float(x) for x in controlshouldery]-yval)

controlelbowx = pd.DataFrame([float(x) for x in controlelbowx]-xval)
controlelbowy = pd.DataFrame([float(x) for x in controlelbowy]-yval)

controlwristx = pd.DataFrame([float(x) for x in controlwristx]-xval)
controlwristy = pd.DataFrame([float(x) for x in controlwristy]-yval)

#make data table
controlresult = pd.concat([controlshoulderx,controlshouldery,controlelbowx,controlelbowy,controlwristx,controlwristy],axis = 1, join='inner')
controlresult.columns = ['controlshoulderx','controlshouldery','controlelbowx','controlelbowy','controlwristx','controlwristy']
display(controlresult)

#graph
plt.figure(2)
plt.clf()
plt.scatter(controlshoulderx,controlshouldery,label = "Shoulder",s=5)
plt.scatter(controlelbowx,controlelbowy,label = "Elbow",s=5)
plt.scatter(controlwristx,controlwristy,label = "Wrist",s=5)
plt.title("Control Rat")
plt.legend(loc = 2)
plt.show()

plt.savefig("controlratplot.jpg")

#%%

#excitatory rat data
exciteshoulderx = ex.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'shoulder','x']]

exciteshouldery = ex.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'shoulder','y']]
    
exciteelbowx = ex.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'elbow','x']]
    
exciteelbowy = ex.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'elbow','y']]
    
excitewristx = ex.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'wrist','x']]
    
excitewristy = ex.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000', \
             'wrist','y']]

exciteshoulderx = pd.DataFrame([float(x) for x in exciteshoulderx]-xval)
exciteshouldery = pd.DataFrame([float(x) for x in exciteshouldery]-yval)

exciteelbowx = pd.DataFrame([float(x) for x in exciteelbowx]-xval)
exciteelbowy = pd.DataFrame([float(x) for x in exciteelbowy]-yval)

excitewristx = pd.DataFrame([float(x) for x in excitewristx]-xval)
excitewristy = pd.DataFrame([float(x) for x in excitewristy]-yval)

#graph em babe
exciteresult = pd.concat([exciteshoulderx, exciteshouldery,exciteelbowx,exciteelbowy,excitewristx,excitewristy],axis = 1, join='inner')
exciteresult.columns = ['exciteshoulderx','exciteshouldery','exciteelbowx','exciteelbowy','excitewristx','excitewristy']
display(exciteresult)


plt.figure(3)
plt.clf()
plt.scatter(exciteshoulderx,exciteshouldery,label = "Shoulder",s=5)
plt.scatter(exciteelbowx,exciteelbowy,label = "Elbow",s=5)
plt.scatter(excitewristx,excitewristy,label = "Wrist",s=5)
plt.title("Excitatory Rat")
plt.legend(loc = 2)
plt.show()

plt.savefig("excitatoryratplot.jpg")

#%%
#comparison graphs
plt.figure(4)
plt.clf()
plt.plot(inhibitoryshoulderx,label = "Inhibitory Shoulder")
plt.plot(controlshoulderx, label = "Control Shoulder")
plt.plot(exciteshoulderx, label = "Excitatory Shoulder")
plt.legend(loc = 2)
plt.title("Shoulder Comparison")
plt.savefig("shouldercomparison.jpg")

plt.figure(5)
plt.clf()
plt.plot(inhibitoryelbowx, label="Inhibitory Elbow")
plt.plot(controlelbowx, label = "Control Elbow")
plt.plot(exciteelbowx, label = "Excitatory Elbow")
plt.title("Elbow Comparison")
plt.legend(loc = 2)
plt.savefig("elbowcomparison.jpg")

plt.figure(6)
plt.clf()
plt.plot(inhibitorywristx, label = "Inhibitory Wrist")
plt.plot(controlwristx, label = "Control Wrist")
plt.plot(excitewristx, label = "Excitatory Wrist")
plt.legend(loc = 2)
plt.title("Wrist Comparison")
plt.savefig("wristcomparison.jpg")


#
