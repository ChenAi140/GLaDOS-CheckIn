@echo off

git remote add upstream https://github.com/ChenAi140/GLaDOS-CheckIn.git
git fetch upstream
echo ��ȡ������ɣ�

echo ��ʼ�ϲ�...
git checkout main
git merge upstream/main

echo �ϲ���ɣ�

git push
echo push���!

pause