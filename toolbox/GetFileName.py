#coding: UTF-8

import glob;
from toolbox.ErrorMassage import *
import os;

def getDatFileName(str):
	Assertion(os.path.exists(str), "there are not " + str+" Directory ");	
	return glob.glob(str+"/*.dat");
def getCSVFileName(str):
	Assertion(os.path.exists(str), "there are not " + str+" Directory ");	
	return glob.glob(str+"/*.csv");
def getMTDFileName(str):
	Assertion(os.path.exists(str), "there are not " + str+" Directory ");	
	return glob.glob(str+"/*.mtd");	
def getTSVFileName(str):
	Assertion(os.path.exists(str), "there are not " + str+" Directory ");	
	return glob.glob(str+"/*.tsv");

def getALLFileName(str):
	Assertion(os.path.exists(str), "there are not " + str+" Directory ");	
	return glob.glob(str+"/*");


# true maens variables'str' is file name, false means variables'str' is DirectoryName  
def FileJudge(str):
	if str.find(".") != -1:
		return True;
	else:
		return False;

def getSubDirectoryName(str):
	Assertion(os.path.exists(str), "there are not " + str+" Directory ");	
	Files = glob.glob(str+"/*");
	ret = [];
	if len(Files) == 0:
		return ret;

	for file in Files:
		if not FileJudge(file):
			ret.append(file);

	return ret;

def getAllDirectoryName(str):
	Files = getSubDirectoryName(str);

	print(str)
	if (len(Files) == 0):
		return Files;
		
	ret = [];
	for file in Files:
		d = getAllDirectoryName(file);
		if ( not (len(d) == 0)):
			ret.append(d);
	
	


	return ret;

