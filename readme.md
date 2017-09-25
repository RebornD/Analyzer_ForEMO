概要
----

このスクリプト群はEMOアルゴリズムの分析用です．

具体的には，mtdファイル生成，IGD計算，HyperVolume計算などを行うスクリプトとなります．

start.pyとtoolboxディレクトリは同じディレクトリに入れてくれないと実行できません．

	-mtdファイル生成のため，numpy

	-並列実行のため multiprocessing

がそれぞれ必要となります．

なのでAnacondaを入れることを推奨します．

インストールしていなければして，インストールしたけどpathが通っていない場合は，バッチファイルやシェルを使用して，パスを通すようにしてください

set PATH = (Anacondaへのパス);%PATH% バッチファイル

PATH = (Anacondaへのパス):$PATH シェルスクリプト

でパスを通せるはず


注意事項
--------

	1.ファイルのデミリタはcsvファイルや，tsvファイルなど特例を除きデミリタはタブである．
	
	2.個体群データファイルは，各行に個体群の各個体の目的関数値が記載されているが，各行，デミリタで終了しないことを推奨する．正しく計算されない恐れがある．

	3.mtdファイルを生成する際に，指定したディレクトリからFinalFUNディレクトリまでのディレクトリに，OBJがある場合( result/NSGAII/DTLZ1/2OBJ/FinalFUN/)，そのOBJと/で囲まれた数字が目的関数地だと判断される（例なら2OBJなので2目的)
	
	4.mtdファイルを作成する際，同名のファイルを消してから出力される．

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
	