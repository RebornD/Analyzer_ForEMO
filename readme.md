Overview
----

This repository has python scripts analysing EMO algorithms.

you must put toolbox folder and start.py script in the same directory.  
moreover, you need to install numpy modules and multiprocessing module to utilize all of these scripts.

Notion
------

	1.Except for specific files (i.e., csv and tsv), the delimiter of files is tab.
	
	2. In the objective data file (i.e., .mtd file),   each column is about each objective function value, and each row is the objective vectors of each solutions. In each row, you prefer to NOT end with delimiter (i.e., tab). this script may miscalclate.

	3 .mtdファイルを生成する際に，指定したディレクトリからFinalFUNディレクトリまでのディレクトリに，OBJがある場合( result/NSGAII/DTLZ1/2OBJ/FinalFUN/)，そのOBJと/で囲まれた数字が目的関数地だと判断される（例なら2OBJなので2目的)
	
	4 .mtdファイルを作成する際，同名のファイルを消してから出力される．

	5.HpyerVolumeやIGD計算スクリプトは別途作成する必要がある．

実装思想
--------

一つのメイスクリプトを実行すると，全ての実行が行えるようにする．
多数目的にも対応できるように，並列で行う必要あり．

各スクリプト説明
-----------------

start.py
	メインスクリプト

toolbox/CalcHV.py:

	toolbox/Calclator/hv.batを起動してHyperVolume計算を行う関数がある．個体群の形式は現在mtdファイルのみサポート

	パイプライン出力によりファイルに書き込む．ディレクトリは個体群ファイルがあるディレクトリに出力．

toolbox/CalcIGD.py
	
	toolbox/Calclator/igd.batを起動してIGDを計算する．基本的にCalcHV.py のIGDバージョン；
	
	参照点はtoolbox/RefFilesに保管予定
	
toolbox/CommandLine.py
	
	コマンドライン解析クラス
	
	-h true などを行うことにより行いたい実行や設定の指定を行う．
	
toolbox/ErrorMassage.py
	
	Assertionなどの役割を行う関数を扱うスクリプト
	
	ErroMassageを使用．
	
toolbox/NDSort.py
	
	非劣解ソートを行うスクリプト．これとmtdファイルを合わせる予定
	
toolbox/Normalization.py

	FinalFUディレクトリの兄弟ディレクトリとしてNFinalFUNを作成し，FinalFUNのMaxPoint と MinPointを使用して正規化を行い，NFianlFUNに出力する．
	正規化を行うスクリプト
	
toolbox/GetFileName.py	

	指定したディレクトリの子，子孫ディレクトリを探索し，特定のファイルまたは，ディレクトリを探索する．
	
toolbox/MakeMTDFile/py
	
	指定したディレクトリの子，子孫ディレクトリを探索し，FinalFUNディレクトリを探索しmtdファイルを生成する．
	
	
今後の予定
----------

	・並列化処理
	
	・コマンドの充実
	
	・グラフプロットスクリプトの追加
	
version
-------

2017/09/25
	
