#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:00:28 2022

@author: gavinkoma
"""
import csv
import os
import sys 
import glob
import math
import numpy as np
import pandas as pd
from pandas import *
from matplotlib import pyplot as plt


#%%
#okay lets recall our inhib stuff:
inhib = pd.read_csv("Rupert_week2_cam2_Inhibitory Rat 5_2021-08-10_11_28_34_fr_wbgam_h264_nearlossless_safeDLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000.csv",index_col=0,header=[0,1,2])

idx = pd.IndexSlice

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
##the rest below is gonna be for excite & control, we dont have more inhib

er1_1 = pd.read_csv("grantprelim_week1_cam3_ratER1Excitatory_2022-01-31_11_53_24_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er1_2 = pd.read_csv("grantprelim_week1_cam3_ratER1Excitatory_2022-01-31_11_57_27_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er1_3 = pd.read_csv("grantprelim_week1_cam3_ratER1Excitatory_2022-01-31_12_04_21_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er1_1_cno = pd.read_csv("grantprelim_week1_cam3_ratER1ExcitatorywithCNO_2022-02-09_11_56_41_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er1_2_cno = pd.read_csv("grantprelim_week1_cam3_ratER1ExcitatorywithCNO_2022-02-09_11_59_00_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er1_3_cno = pd.read_csv("grantprelim_week1_cam3_ratER1ExcitatorywithCNO_2022-02-09_12_00_12_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er1_4_cno = pd.read_csv("grantprelim_week1_cam3_ratER1ExcitatorywithCNO_2022-02-09_12_01_14_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er1_5_cno = pd.read_csv("grantprelim_week1_cam3_ratER1ExcitatorywithCNO_2022-02-09_12_02_34_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er3_1 = pd.read_csv("grantprelim_week1_cam3_ratER1ExcitatorywithCNO_2022-02-09_12_02_34_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er3_2 = pd.read_csv("grantprelim_week1_cam3_ratER3Excitatory_2022-01-31_12_18_03_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er3_3 = pd.read_csv("grantprelim_week1_cam3_ratER3Excitatory_2022-01-31_12_22_19_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er3_1_cno = pd.read_csv("grantprelim_week1_cam3_ratER3ExcitatorywithCNO_2022-02-09_11_43_39_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er3_2_cno = pd.read_csv("grantprelim_week1_cam3_ratER3ExcitatorywithCNO_2022-02-09_11_45_38_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er3_3_cno = pd.read_csv("grantprelim_week1_cam3_ratER3ExcitatorywithCNO_2022-02-09_11_47_42_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er6_1 = pd.read_csv("grantprelim_week1_cam3_ratER6Control_2022-01-31_12_42_21_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er6_2 = pd.read_csv("grantprelim_week1_cam3_ratER6Control_2022-01-31_12_45_28_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er6_3 = pd.read_csv("grantprelim_week1_cam3_ratER6Control_2022-01-31_12_48_10_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er6_4 = pd.read_csv("grantprelim_week1_cam3_ratER6Control_2022-01-31_12_51_23_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er6_1_cno = pd.read_csv("grantprelim_week1_cam3_ratER6ControlwithCNO_2022-02-09_12_07_27_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er6_2_cno = pd.read_csv("grantprelim_week1_cam3_ratER6ControlwithCNO_2022-02-09_12_12_13_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])
er6_3_cno = pd.read_csv("grantprelim_week1_cam3_ratER6ControlwithCNO_2022-02-09_12_16_44_fr_wbgam_h264_nearlossless_safeDLC_resnet50_rupertgrantsubFeb16shuffle1_200000.csv",index_col=0,header=[0,1,2])

#%%
#okay so now we need to compile & average these things
#we can index them like we did before, and then we need to average them going across 

# inhibitoryshoulderx = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000','shoulder','x']]
# inhibitoryshouldery = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000','shoulder','y']]
# inhibitoryelbowx = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000','elbow','x']]
# inhibitoryelbowy = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000','elbow','y']]
# inhibitorywristx = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000','wrist','x']]
# inhibitorywristy = inhib.loc[:,idx['DLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000','wrist','y']]

#maybe there is an easier way to parse through these with a loop?
#im still not really sure how to do this but lets just make it messy

path = '/Users/gavinkoma/Documents/spencepython/rupertcoordinate/normalization/rupertreaching/newdata'
files = glob.glob(path + '/*.csv')

li = []

# loop through list of files and read each one into a dataframe and append to list
for f in files:
    # read in csv
    temp_df = pd.read_csv(f)
    # append df to list
    li.append(temp_df)
    print(f'Successfully created dataframe for {f} with shape {temp_df.shape}')

# concatenate our list of dataframes into one!
df = pd.concat(li, axis=0)
print(df.shape)
df.head()









