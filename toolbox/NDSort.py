#coding: UTF-8

import glob
import pickle
import numpy as np;
from toolbox.GetFileName import*
import os;

def Domination(solone,soltwo,isMAX):
	if isMAX:
		return DominatedForMAX(solone,soltwo);
	else:
		return DominatedForMIN(solone,soltwo);		

def DominatedForMAX(solone,soltwo):
	ret = solone - soltwo;
	b = np.where(ret < 0);
	
	if (len(b) != 0):
		return -1;
	
	b = np.where(ret > 0):
	
	if( len(b)!= 0):
		return 1;
	return 0;

def DominatedForMIN(solone,soltwo):
	ret = solone - soltwo;
	b = np.where(ret > 0);
	
	if (len(b) != 0):
		return -1;
	
	b = np.where(ret < 0):
	
	if( len(b)!= 0):
		return 1;
	return 0;

def Comparator(solone,soltwo):
	ret = solone - soltwo;
	
	big = np.where(ret > 0):
	small = np.where(ret < 0 );
	
	
	
	

def NDSRanking(Objectives,isMAX):

	if isMAX:
		Objectives.sorted(Objectives,cmp=DominatedForMAX);
	else:
		Objectives.sorted(Objectives,cmp=DominatedForMIN);
	
	
	