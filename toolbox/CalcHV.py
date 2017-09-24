#coding: UTF-8

import glob;
from toolbox.ErrorMassage import *
from subprocess import call

import os;



def CalcHVALLFile(FileName:str,ref:str):
	if (not FileName.endswith(".mtd")):
		ErrorMassage("in CalcHVMTDFile, argment file is not MTD file");
	
	outname = FileName.split("/");
	fileoutname ="";
	outname.pop();
	for namepart in outname:
			fileoutname += namepart + "/";
	fileoutname += "Hv.hv";
	if (os.path.exists("toolbox")):
		print("OK");
	print(fileoutname)
	call(["toolbox\\Calclator\\hv.bat","-r","-a",ref,FileName,">>",fileoutname])
	#, ,,] )

def CalcHVSTDFile(FileName:str,ref:str):
	if (not FileName.endswith(".mtd")):
		ErrorMassage("in CalcHVMTDFile, argment file is not MTD file");
	
	outname = FileName.split("/");
	fileoutname ="";
	outname.pop();
	for namepart in outname:
			fileoutname += namepart + "/";
	fileoutname += "Hv.hv";
	if (os.path.exists("toolbox")):
		print("OK");
	print(fileoutname)
	call(["toolbox\\Calclator\\hv.bat","-r",ref,"-v",FileName,">>",fileoutname])
	#, ,,] )

	
def CalcHVAVERAGEFile(FileName:str,ref:str):
	if (not FileName.endswith(".mtd")):
		ErrorMassage("in CalcHVMTDFile, argment file is not MTD file");
	
	outname = FileName.split("/");
	fileoutname ="";
	outname.pop();
	for namepart in outname:
			fileoutname += namepart + "/";
	fileoutname += "Hv.hv";
	if (os.path.exists("toolbox")):
		print("OK");
	print(fileoutname)
	call(["toolbox\\Calclator\\hv.bat","-r",ref,FileName,">>",fileoutname])
	#, ,,] )
