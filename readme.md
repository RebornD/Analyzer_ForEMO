�T�v
----

���̃X�N���v�g�Q��EMO�A���S���Y���̕��͗p�ł��D

��̓I�ɂ́Cmtd�t�@�C�������CIGD�v�Z�CHyperVolume�v�Z�Ȃǂ��s���X�N���v�g�ƂȂ�܂��D

start.py��toolbox�f�B���N�g���͓����f�B���N�g���ɓ���Ă���Ȃ��Ǝ��s�ł��܂���D

	-mtd�t�@�C�������̂��߁Cnumpy

	-������s�̂��� multiprocessing

�����ꂼ��K�v�ƂȂ�܂��D

�Ȃ̂�Anaconda�����邱�Ƃ𐄏����܂��D

�C���X�g�[�����Ă��Ȃ���΂��āC�C���X�g�[����������path���ʂ��Ă��Ȃ��ꍇ�́C�o�b�`�t�@�C����V�F�����g�p���āC�p�X��ʂ��悤�ɂ��Ă�������

set PATH = (Anaconda�ւ̃p�X);%PATH% �o�b�`�t�@�C��

PATH = (Anaconda�ւ̃p�X):$PATH �V�F���X�N���v�g

�Ńp�X��ʂ���͂�


���ӎ���
--------

	1.�t�@�C���̃f�~���^��csv�t�@�C����Ctsv�t�@�C���ȂǓ���������f�~���^�̓^�u�ł���D
	
	2.�̌Q�f�[�^�t�@�C���́C�e�s�Ɍ̌Q�̊e�̖̂ړI�֐��l���L�ڂ���Ă��邪�C�e�s�C�f�~���^�ŏI�����Ȃ����Ƃ𐄏�����D�������v�Z����Ȃ����ꂪ����D

	3.mtd�t�@�C���𐶐�����ۂɁC�w�肵���f�B���N�g������FinalFUN�f�B���N�g���܂ł̃f�B���N�g���ɁCOBJ������ꍇ( result/NSGAII/DTLZ1/2OBJ/FinalFUN/)�C����OBJ��/�ň͂܂ꂽ�������ړI�֐��n���Ɣ��f�����i��Ȃ�2OBJ�Ȃ̂�2�ړI)
	
	4.mtd�t�@�C�����쐬����ہC�����̃t�@�C���������Ă���o�͂����D

	5.HpyerVolume��IGD�v�Z�X�N���v�g�͕ʓr�쐬����K�v������D

�����v�z
--------

��̃��C�X�N���v�g�����s����ƁC�S�Ă̎��s���s����悤�ɂ���D
�����ړI�ɂ��Ή��ł���悤�ɁC����ōs���K�v����D

�e�X�N���v�g����
-----------------

start.py
	���C���X�N���v�g

toolbox/CalcHV.py:

	toolbox/Calclator/hv.bat���N������HyperVolume�v�Z���s���֐�������D�̌Q�̌`���͌���mtd�t�@�C���̂݃T�|�[�g

	�p�C�v���C���o�͂ɂ��t�@�C���ɏ������ށD�f�B���N�g���͌̌Q�t�@�C��������f�B���N�g���ɏo�́D

toolbox/CalcIGD.py
	
	toolbox/Calclator/igd.bat���N������IGD���v�Z����D��{�I��CalcHV.py ��IGD�o�[�W�����G
	
	�Q�Ɠ_��toolbox/RefFiles�ɕۊǗ\��
	
toolbox/CommandLine.py
	
	�R�}���h���C����̓N���X
	
	-h true �Ȃǂ��s�����Ƃɂ��s���������s��ݒ�̎w����s���D
	
toolbox/ErrorMassage.py
	
	Assertion�Ȃǂ̖������s���֐��������X�N���v�g
	
	ErroMassage���g�p�D
	
toolbox/NDSort.py
	
	�����\�[�g���s���X�N���v�g�D�����mtd�t�@�C�������킹��\��
	
toolbox/Normalization.py

	FinalFU�f�B���N�g���̌Z��f�B���N�g���Ƃ���NFinalFUN���쐬���CFinalFUN��MaxPoint �� MinPoint���g�p���Đ��K�����s���CNFianlFUN�ɏo�͂���D
	���K�����s���X�N���v�g
	
toolbox/GetFileName.py	

	�w�肵���f�B���N�g���̎q�C�q���f�B���N�g����T�����C����̃t�@�C���܂��́C�f�B���N�g����T������D
	
toolbox/MakeMTDFile/py
	
	�w�肵���f�B���N�g���̎q�C�q���f�B���N�g����T�����CFinalFUN�f�B���N�g����T����mtd�t�@�C���𐶐�����D
	
	
����̗\��
----------

	�E���񉻏���
	
	�E�R�}���h�̏[��
	
	�E�O���t�v���b�g�X�N���v�g�̒ǉ�
	
version
-------

2017/09/25
	