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

det getAllSubDirectoryName(str):
	