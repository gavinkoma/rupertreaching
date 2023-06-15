#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: aspence

conda environment = spyder-env (on AJS mac)

on spence new M1 mac: launch iterm2-x64! then do conda activate dog
dog environment has what's needed... and arm64 version conda iffy.

"""
# 2023-06-15 Adding more control rats
# 
#
# 2023-05-31 AJS 
# finished adding 2 more trials from that rat... good reaches in last vid 43, too bad one at 1 sec goes before vid start! could fix.
# 2023-05-31 AJS and GK adding one new inhibitory rat from 2023-05-03
# this one added and worked: dd_inhib_female_2023_05_03_10_23_27DLC_resnet50_Please_use_this_oneMay20shuffle1_200000.csv
# this one the reach was supposed to be at 25 sec and didn't track well. can switch to manual coords... DDinhib_05_03_10_31_56DLC_resnet50_Please_use_this_oneMay20shuffle1_200000.csv
# 
# 2022-12-12 AJS adding two new inhibitory rats.
# found manually labelled videos. make excel file with notes, see that.
# copied csv of coordinates. how to roll into this?
# the scale looks similar! 38 pixels wide for the 1/4 inch plexi.
# however the origin is different. just need to click/measure, and enter into the sheet.
# what do i do that with? GIMP? photoshop?
# OKAY I JUST WROTE AN IMAGEJ MACRO PLUGIN TO DO THIS. spencelab/code/imagej. install it into image j, click A button on toolbar
# and it adds coords over a point selection and allows you to have the image.
#
# 2023-02-07 AJS removing inhib rat with no injury. either ihrGS2 or ihrMS1.
# ipython
# command enter from sublime ttext to run chunks...
# BINGO - it was ihrMS1 and putting 'bad' inthe column fixed it!
# running chunks of this script manually with teh bad columsn to recreate the data, then will do R.
#
# 2023-05-02 AJS George wants panels C and D only and control only...
# Ok I just did this in illustrator. here:
# '/Users/aspence/rupertreaching/newdata/reachkinematics_pa_sci_grant_r2_CDcontrolonly.ai'

# %% imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from scipy.signal import butter,filtfilt
import seaborn as sns
idx = pd.IndexSlice
plt.rc('legend',fontsize=8)
#plt.rcParams["figure.figsize"] = (6.4,4.8)

if 0:
  def butter_lowpass_filter(data, cutoff, fs=250, order=5):
      nyq = 0.5 * fs
      normal_cutoff = cutoff / nyq
      # Get the filter coefficients 
      b, a = butter(order, normal_cutoff, btype='low', analog=False)
      y = filtfilt(b, a, data)
      return y

# frame per second for conversion to time
fps=250
pixpermm=38/6.35 # the plexiglass is 1/4 inch thick which is 6.35 mm. So this must be 38 pixels wide as clicked.
# first inhib trial is more like 61 pix for the plexi... add column to reachfiles.csv

def fixtheindex(df):
  if isinstance(df.index[0],str):
    print("Fixing index.")
    df.index = range(0,len(df))
  return(df)

# %% load file and metadata database
md=pd.read_csv('reachfiles.csv')
# %% okay laod them on to same time
dfs=[]
for ind in range(len(md)):
  df=pd.read_csv(md.loc[ind,'file'],index_col=0,header=[0,1,2])
  df=fixtheindex(df)
  df.loc[:,idx[:,:,['x','y']]]=df.loc[:,idx[:,:,['x','y']]].rolling(6,center=True).mean()
  dfs.append(df)
fn='Rupert_week2_cam2_Inhibitory Rat 5_2021-08-10_11_28_34_fr_wbgam_h264_nearlossless_safeDLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000.csv'

# %% function that loads and plots one file
def plotreachkinfile(fn,xwall,ywall):
  df=pd.read_csv(fn,index_col=0,header=[0,1,2])
  # some files have file names as the index, manually annotated i think.
  # fix...
  #if isinstance(df.index[0],str):
  #  print("Fixing index.")
  #  df.index = range(0,len(df))
  df=fixtheindex(df)
  # plot the x coords and
  # get x and y coordinates
  xco = df.loc[:,idx[:,:,'x']]
  yco = df.loc[:,idx[:,:,'y']]
  # plot it up:
  fig, axes = plt.subplots(nrows=2, ncols=1)
  xco.plot(ax=axes[0])
  yco.plot(ax=axes[1])
  fig.suptitle(fn,fontsize=4)
  axes[0].set_ylabel('x coord')
  axes[1].set_xlabel('frame')
  axes[1].set_ylabel('y coord')
  axes[1].invert_yaxis()
  # save it
  axes[0].axhline(xwall)
  axes[1].axhline(700-ywall)
  fig.savefig(fn.split('.')[0]+'.png')
  #plt.show()

#plotreachkinfile(fn,md.loc[0,'plexi_x'],md.loc[0,'plexi_y'])

# Need to interact with individuall to find peak x. 
if 0:
  ind=0
  plotreachkinfile(md.iloc[ind]['file'],md.loc[ind,'plexi_x'],md.loc[ind,'plexi_y'])
  plt.show()
  fn=md.iloc[ind]['file']
  xwall=md.loc[ind,'plexi_x']
  ywall=md.loc[ind,'plexi_y']

for ind in range(len(md)):
  plotreachkinfile(md.loc[ind,'file'],md.loc[ind,'plexi_x'],md.loc[ind,'plexi_y'])

# just do new inhib ones i'm adding
for ind in range(22,len(md)):
  plotreachkinfile(md.loc[ind,'file'],md.loc[ind,'plexi_x'],md.loc[ind,'plexi_y'])

# just do new inhib w GK 2023-05-31
for ind in range(28,len(md)):
  plotreachkinfile(md.loc[ind,'file'],md.loc[ind,'plexi_x'],md.loc[ind,'plexi_y'])

# just do new controls 15-6-2023
for ind in range((len(md)-4),len(md)):
  plotreachkinfile(md.loc[ind,'file'],md.loc[ind,'plexi_x'],md.loc[ind,'plexi_y'])

#ok let's also export data needed for velocities analysis:
# want output file: type cno minframebef peakframe xmin ymin xpk ypk rchdur dx dy vely goodbad rat file
xmin,ymin,xpk,ypk,rchdur,dx,dy,velx,vely =[],[],[],[],[],[],[],[],[]
for ind in range(len(md)):
  print(md.loc[ind,'file'])
  df=pd.read_csv(md.loc[ind,'file'],index_col=0,header=[0,1,2])
  df=fixtheindex(df)
  df.columns=df.columns.droplevel('scorer')
  xmin.append(df.loc[md['minframebef'][ind],idx[md['marker'][ind],'x']]/pixpermm)
  ymin.append(df.loc[md['minframebef'][ind],idx[md['marker'][ind],'y']]/pixpermm)
  xpk.append(df.loc[md['peakframe'][ind],idx[md['marker'][ind],'x']]/pixpermm)
  ypk.append(df.loc[md['peakframe'][ind],idx[md['marker'][ind],'y']]/pixpermm)
  rchdur.append( (md['peakframe'][ind] - md['minframebef'][ind])/fps )
  dx.append( (xpk[-1]-xmin[-1])/pixpermm  )
  dy.append( (ypk[-1]-ymin[-1])/pixpermm )
  velx.append( dx[-1]/rchdur[-1] )
  vely.append( dy[-1]/rchdur[-1] )
mdwv=md.copy()
mdwv=mdwv.assign(xmin=xmin,ymin=ymin,xpk=xpk,ypk=ypk,rchdur=rchdur,dx=dx,dy=dy,velx=velx,vely=vely)
mdwv.to_csv('reachfiles_generated_wvelocities.csv')

# md=pd.read_csv('reachfiles.csv')
# Make a big plot of all reaches color by treatment.
# %% Okay use peaks to overlay excite in red, control is blue, inhib green.
f=plt.figure(2)
f.clf()
#f.set_figheight(1.32)
#f.set_figwidth(2.87)
#f=plt.figure(figsize=(2.87,1,32))
cols={'inhib':'green','control':'blue','excite':'red','norm':'black'}
subs=[]
# create mapping of unique treatments to themselves
legendlabs = dict(zip(md.loc[:,'type'].unique(),md.loc[:,'type'].unique()))
for ind in range(len(md)):
  rng=range(round((md.loc[ind,'peakframe']-(md.loc[ind,'aroundpeakframes']/2))), \
      round((md.loc[ind,'peakframe']+(md.loc[ind,'aroundpeakframes']/2))))
  xco=(dfs[ind].loc[:,idx[:,md.loc[ind,'marker'],'x']] - md.loc[ind,'plexi_x'])/md.loc[ind,'pixpermm']
  if md.loc[ind,'goodbad']=='good':
    repdf=md.loc[[ind]*len(rng)].reset_index() # repeated meta entries of md
    repdf['frame']=repdf.index
    newdf=(dfs[ind].loc[rng,idx[:,md.loc[ind,'marker'],'x']].reset_index() - md.loc[ind,'plexi_x'])/md.loc[ind,'pixpermm']
    newdf.columns=newdf.columns.droplevel([0,1])
    newdf['frame']=newdf.index
    outdf=newdf.join(repdf,on='frame',rsuffix='_md').rename({'type':'treatment'},axis='columns')
    #outdf['time']=(outdf['frame']-md.loc[ind,'aroundpeakframes']/2)/fps
    outdf['time']=(outdf['frame'])/fps
    subs.append(outdf)
    #plt.plot( outdf['time'], outdf['time'], c=cols[md.loc[ind,'type']], label=legendlabs[md.loc[ind,'type']] )
    plt.plot( outdf['time'], np.array(xco.iloc[rng].droplevel([0,1],axis='columns')), \
      c=cols[md.loc[ind,'type']], label=legendlabs[md.loc[ind,'type']] )
    legendlabs[md.loc[ind,'type']]='_'+legendlabs[md.loc[ind,'type']]
#    plt.plot( range(md.loc[ind,'aroundpeakframes']), \
#      xco.loc[ round((md.loc[ind,'peakframe']-(md.loc[ind,'aroundpeakframes']/2))): \
#      round((md.loc[ind,'peakframe']+(md.loc[ind,'aroundpeakframes']/2))-1) ], c=cols[md.loc[ind,'type']])
#plt.axhline(md.loc[1,'plexi_x'])
plt.axhline(0)
plt.xlabel('time (s)')
plt.ylabel('wrist x (mm)')
plt.legend(title='treatment')
plt.title('Individual reaches by treatment')
plt.annotate('Wall', xy=(0.2, 0),  xycoords='data',
            xytext=(0.2, 10), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='center',
            )
ad = pd.concat(subs).reset_index()
ad.to_csv('alldata_x.csv')
plt.savefig('indivreach_x.pdf')

# %% plot with shaded errors
# Plot the responses for different events and regions
f3=plt.figure(3)
f3.clf()
sns.lineplot(x="time", y="x",ci="sd",hue="treatment",palette=cols,data=ad)
plt.axhline(0)
plt.xlabel('time (s)')
plt.ylabel('wrist x (mm)')
plt.title('Mean $\pm$ S.D. reaches by treatment')
plt.annotate('Wall', xy=(0.2, 0),  xycoords='data',
            xytext=(0.2, 10), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='center',
            )
plt.savefig('meansdreach_x.pdf')

# %% lets see what y looks like, the bad coding way
#md=pd.read_csv('reachfiles.csv')
# %% Okay use peaks to overlay excite in red, control is blue.
f4=plt.figure(4)
f4.clf()
# USE ABOVE DEF! cols={'inhib':'green','control':'blue','excite':'red'}
subs=[]
# create mapping of unique treatments to themselves
legendlabs = dict(zip(md.loc[:,'type'].unique(),md.loc[:,'type'].unique()))
for ind in range(len(md)):
  rng=range(round((md.loc[ind,'peakframe']-(md.loc[ind,'aroundpeakframes']/2))), \
      round((md.loc[ind,'peakframe']+(md.loc[ind,'aroundpeakframes']/2))))
  yco=((700-dfs[ind].loc[:,idx[:,md.loc[ind,'marker'],'y']]) - md.loc[ind,'plexi_y'])/md.loc[ind,'pixpermm']
  if md.loc[ind,'goodbad']=='good':
    repdf=md.loc[[ind]*len(rng)].reset_index() # repeated meta entries of md
    repdf['frame']=repdf.index
    newdf=((700-dfs[ind].loc[rng,idx[:,md.loc[ind,'marker'],'y']].reset_index())-md.loc[ind,'plexi_y'])/md.loc[ind,'pixpermm']
    newdf.columns=newdf.columns.droplevel([0,1])
    newdf['frame']=newdf.index
    outdf=newdf.join(repdf,on='frame',rsuffix='_md').rename({'type':'treatment'},axis='columns')
    #outdf['time']=(outdf['frame']-md.loc[ind,'aroundpeakframes']/2)/fps
    outdf['time']=(outdf['frame'])/fps
    subs.append(outdf)
    plt.plot( outdf['time'], np.array(yco.loc[ rng ]), c=cols[md.loc[ind,'type']], label=legendlabs[md.loc[ind,'type']] )
    legendlabs[md.loc[ind,'type']]='_'+legendlabs[md.loc[ind,'type']]
plt.xlabel('time (s)')
plt.ylabel('wrist y (mm)')
plt.axhline(0)
plt.legend(title='treatment')
plt.title('Individual reaches by treatment')
plt.annotate('Slit min height', xy=(0.1, 0),  xycoords='data',
            xytext=(0.1, 20), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='center',
            )
ady = pd.concat(subs).reset_index()
ady.to_csv('alldata_y.csv')
plt.savefig('indivreach_y.pdf')

# %% plot with shaded errors
# Plot the responses for different events and regions
f5=plt.figure(5)
f5.clf()
sns.lineplot(x="time", y="y",ci="sd",hue="treatment",palette=cols,data=ady)
#plt.axhline(md.loc[1,'plexi_x'])
plt.xlabel('time (s)')
plt.ylabel('wrist y (mm)')
plt.title('Mean $\pm$ S.D. reaches by treatment')
plt.axhline(0)
#plt.annotate('Wall', xy=(-0.3, 1715),  xycoords='data',
#            xytext=(-0.3, 1800), textcoords='data',
#            arrowprops=dict(facecolor='black', shrink=0.05),
#            horizontalalignment='center', verticalalignment='top',
#            )
plt.annotate('Slit min height', xy=(0.1, 0),  xycoords='data',
            xytext=(0.1, 20), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='center',
            )
plt.savefig('meansdreach_y.pdf')


