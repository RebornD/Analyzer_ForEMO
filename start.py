#coding: UTF-8
import glob;
import sys;

from toolbox.CommandLine import*
from toolbox.ErrorMassage import*
from toolbox.GetFileName import*
from toolbox.MakeMTDFile import*
from toolbox.CalcHV		 import*

if __name__ == "__main__":
	argv = sys.argv; 
	
	
	setting = CommandLineSetting(argv);
	d = 0;
#	max = setting.getAsBool("max");
#	Assertion(d ==1 , "str");
	#files = getAllDirectoryName("toolbox")
	MakeMTDFileNormalize( "test/2OBJ/FinalFUN",max,'\t');
#	MakeMTDFile( "test/2OBJ/FinalFUN",max,'\t');
	CalcHVSTDFile("test/2OBJ/FinalFUN/FUN.mtd","5.0");
		
	input();
	