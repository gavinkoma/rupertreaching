#!/usr/bin/env python3# -*- coding: utf-8 -*-"""@author: aspenceconda environment = spyder-env (on AJS mac)"""# %% importsimport matplotlib.pyplot as pltimport pandas as pdimport seaborn as snsidx = pd.IndexSliceplt.rc('legend',fontsize=6)# frame per second for conversion to timefps=250# %% load file and metadata databasemd=pd.read_csv('reachfiles.csv')fn='Rupert_week2_cam2_Inhibitory Rat 5_2021-08-10_11_28_34_fr_wbgam_h264_nearlossless_safeDLC_resnet50_Rupert Reaching Videos_sampleOct3shuffle1_200000.csv'# %% function that loads and plots one filedef plotreachkinfile(fn,xwall):  df=pd.read_csv(fn,index_col=0,header=[0,1,2])  # plot the x coords and  # get x and y coordinates  xco = df.loc[:,idx[:,:,'x']]  yco = df.loc[:,idx[:,:,'y']]  # plot it up:  fig, axes = plt.subplots(nrows=2, ncols=1)  xco.plot(ax=axes[0])  yco.plot(ax=axes[1])  fig.suptitle(fn,fontsize=4)  axes[0].set_ylabel('x coord')  axes[1].set_xlabel('frame')  axes[1].set_ylabel('y coord')  # save it  axes[0].axhline(xwall)  fig.savefig(fn.split('.')[0]+'.png')  #plt.show()plotreachkinfile(fn,md.loc[0,'plexi_x'])for ind in range(len(md)):  plotreachkinfile(md.loc[ind,'file'],md.loc[ind,'plexi_x'])# %% okay laod them on to same timedfs=[]for ind in range(len(md)):  dfs.append(pd.read_csv(md.loc[ind,'file'],index_col=0,header=[0,1,2]))md=pd.read_csv('reachfiles.csv')# %% Okay use peaks to overlay excite in red, control is blue.f=plt.figure(2)f.clf()cols={'inhib':'green','control':'blue','excite':'red'}subs=[]# create mapping of unique treatments to themselveslegendlabs = dict(zip(md.loc[:,'type'].unique(),md.loc[:,'type'].unique()))for ind in range(len(md)):  rng=range(round((md.loc[ind,'peakframe']-(md.loc[ind,'aroundpeakframes']/2))), \      round((md.loc[ind,'peakframe']+(md.loc[ind,'aroundpeakframes']/2))))  xco=dfs[ind].loc[:,idx[:,md.loc[ind,'marker'],'x']]  if md.loc[ind,'goodbad']=='good':    repdf=md.loc[[ind]*len(rng)].reset_index() # repeated meta entries of md    repdf['frame']=repdf.index    newdf=dfs[ind].loc[rng,idx[:,md.loc[ind,'marker'],'x']].reset_index()    newdf.columns=newdf.columns.droplevel([0,1])    newdf['frame']=newdf.index    outdf=newdf.join(repdf,on='frame',rsuffix='_md').rename({'type':'treatment'},axis='columns')    outdf['time']=(outdf['frame']-md.loc[ind,'aroundpeakframes']/2)/fps    subs.append(outdf)    #plt.plot( outdf['time'], outdf['time'], c=cols[md.loc[ind,'type']], label=legendlabs[md.loc[ind,'type']] )    plt.plot( outdf['time'], np.array(xco.iloc[rng].droplevel([0,1],axis='columns')), c=cols[md.loc[ind,'type']], label=legendlabs[md.loc[ind,'type']] )    legendlabs[md.loc[ind,'type']]='_'+legendlabs[md.loc[ind,'type']]#    plt.plot( range(md.loc[ind,'aroundpeakframes']), \#      xco.loc[ round((md.loc[ind,'peakframe']-(md.loc[ind,'aroundpeakframes']/2))): \#      round((md.loc[ind,'peakframe']+(md.loc[ind,'aroundpeakframes']/2))-1) ], c=cols[md.loc[ind,'type']])plt.axhline(md.loc[1,'plexi_x'])plt.xlabel('time (s)')plt.ylabel('wrist x (pix)')plt.legend(title='treatment')plt.title('Individual reaches by treatment')plt.annotate('Wall', xy=(-0.2, 1715),  xycoords='data',            xytext=(-0.2, 1800), textcoords='data',            arrowprops=dict(facecolor='black', shrink=0.05),            horizontalalignment='center', verticalalignment='top',            )ad = pd.concat(subs).reset_index()plt.savefig('indivreach_x.pdf')# %% plot with shaded errors# Plot the responses for different events and regionsf3=plt.figure(3)f3.clf()sns.lineplot(x="time", y="x",ci="sd",hue="treatment",palette=cols,data=ad)plt.axhline(md.loc[1,'plexi_x'])plt.xlabel('time (s)')plt.ylabel('wrist x (pix)')plt.title('Mean $\pm$ S.D. reaches by treatment')plt.annotate('Wall', xy=(-0.3, 1715),  xycoords='data',            xytext=(-0.3, 1800), textcoords='data',            arrowprops=dict(facecolor='black', shrink=0.05),            horizontalalignment='center', verticalalignment='top',            )plt.savefig('meansdreach_x.pdf')# %% lets see what y looks like, the bad coding waymd=pd.read_csv('reachfiles.csv')# %% Okay use peaks to overlay excite in red, control is blue.f4=plt.figure(4)f4.clf()cols={'inhib':'green','control':'blue','excite':'red'}subs=[]# create mapping of unique treatments to themselveslegendlabs = dict(zip(md.loc[:,'type'].unique(),md.loc[:,'type'].unique()))for ind in range(len(md)):  rng=range(round((md.loc[ind,'peakframe']-(md.loc[ind,'aroundpeakframes']/2))), \      round((md.loc[ind,'peakframe']+(md.loc[ind,'aroundpeakframes']/2))))  yco=700-dfs[ind].loc[:,idx[:,md.loc[ind,'marker'],'y']]  if md.loc[ind,'goodbad']=='good':    repdf=md.loc[[ind]*len(rng)].reset_index() # repeated meta entries of md    repdf['frame']=repdf.index    newdf=700-dfs[ind].loc[rng,idx[:,md.loc[ind,'marker'],'y']].reset_index()    newdf.columns=newdf.columns.droplevel([0,1])    newdf['frame']=newdf.index    outdf=newdf.join(repdf,on='frame',rsuffix='_md').rename({'type':'treatment'},axis='columns')    outdf['time']=(outdf['frame']-md.loc[ind,'aroundpeakframes']/2)/fps    subs.append(outdf)    plt.plot( outdf['time'], np.array(yco.loc[ rng ]), c=cols[md.loc[ind,'type']], label=legendlabs[md.loc[ind,'type']] )    legendlabs[md.loc[ind,'type']]='_'+legendlabs[md.loc[ind,'type']]plt.xlabel('time (s)')plt.ylabel('wrist y (pix)')plt.legend(title='treatment')plt.title('Individual reaches by treatment')ady = pd.concat(subs).reset_index()plt.savefig('indivreach_y.pdf')# %% plot with shaded errors# Plot the responses for different events and regionsf5=plt.figure(5)f5.clf()sns.lineplot(x="time", y="y",ci="sd",hue="treatment",palette=cols,data=ady)#plt.axhline(md.loc[1,'plexi_x'])plt.xlabel('time (s)')plt.ylabel('wrist y (pix)')plt.title('Mean $\pm$ S.D. reaches by treatment')#plt.annotate('Wall', xy=(-0.3, 1715),  xycoords='data',#            xytext=(-0.3, 1800), textcoords='data',#            arrowprops=dict(facecolor='black', shrink=0.05),#            horizontalalignment='center', verticalalignment='top',#            )plt.savefig('meansdreach_y.pdf')