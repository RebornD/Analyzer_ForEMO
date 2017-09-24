#coding: UTF-8

import glob
import pickle
import numpy as np;
from toolbox.GetFileName import*
import os;

ZERODEVIDE = 1.0E-6;

def getObj(DirectoryName):
	directorys = DirectoryName.split("/");
	for dir in directorys:
		p = dir.find("OBJ");
		if (not (p == -1)):
			 return dir[0:p];
	return -1;


def MakeMTDFile(DirectoryName: str,isMAX: str,Demiliter:str):
	
	FILES = getDatFileName(DirectoryName);
	OUTPUTFILE = DirectoryName + "/FUN.mtd";
	max = "false";
	if (isMAX ==True):
		max = "true"
	obj = getObj(DirectoryName);
		
	if(os.path.exists(OUTPUTFILE)):
		os.remove(OUTPUTFILE);
	
	
	if (obj == -1):
		ErrorMassage("OBJ is not found , so you modify this source code at MakeMTDFileNormalize in  makeMTDFile.py")
	
	Reps = len(FILES);
	Datas = [];
	print()
	Data = [np.genfromtxt(file,delimiter = Demiliter, filling_values=(0, 0, 0)) for file in FILES];
	
	with open(OUTPUTFILE,"w") as fout:
		fout.write("#nObjectives: "+obj+"\n");
		fout.write("#nTrials:    "+str(len(Data))+"\n");
		fout.write("#isMaximize: " + max+"\n");
	
	for i in Data:
		with open(OUTPUTFILE,"a") as fout:
			fout.write("\n#nSols:	" +str(len(i)) + "\n")
		
		with open(OUTPUTFILE,"ab") as fout:
			np.savetxt(fout,i,delimiter="\t",fmt='%f');
	

def MakeMTDFileNormalize(DirectoryName: str,isMAX: str,Demiliter:str):
	
	FILES = getDatFileName(DirectoryName);
	OUTPUTFILE = DirectoryName + "/FUN.mtd";
	max = "false";
	if (isMAX ==True):
		max = "true"
	obj = getObj(DirectoryName);
		
	if(os.path.exists(OUTPUTFILE)):
		os.remove(OUTPUTFILE);
	
	
	if (obj == -1):
		ErrorMassage("OBJ is not found , so you modify this source code at MakeMTDFileNormalize in  makeMTDFile.py")
	
	Reps = len(FILES);
	Datas = [];
	Data = [np.genfromtxt(file,delimiter = Demiliter, filling_values=(0, 0, 0)) for file in FILES];
	
	with open(OUTPUTFILE,"w") as fout:
		fout.write("#nObjectives: "+obj+"\n");
		fout.write("#nTrials:    "+str(len(Data))+"\n");
		fout.write("#isMaximize: " + max+"\n");
	
	for i in Data:
		with open(OUTPUTFILE,"a") as fout:
			fout.write("\n#nSols:	" +str(len(i)) + "\n")
		
		max = np.ones(len(obj))*-1*1.0E100;
		min = np.ones(len(obj))*1.0E100;
		
		for z in i:
			max = (np.maximum(z,max));
			min = (np.minimum(z,min));
			
		bunbo = np.array(   [ma - mi if (ma - mi > ZERODEVIDE ) else ZERODEVIDE for ma,mi in zip(max,min)])
		i = np.array([ (z - min)/ (bunbo) for z in i]);
		
		with open(OUTPUTFILE,"ab") as fout:
			np.savetxt(fout,i,delimiter="\t",fmt='%f');
	
	