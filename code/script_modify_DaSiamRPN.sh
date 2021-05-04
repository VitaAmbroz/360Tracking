#!/bin/sh

# git clone https://github.com/foolwood/DaSiamRPN.git

# bash DaSiamRPN/run_install.sh

echo "******* Copying modified files... *******"
cp modified_DaSiamRPN/boundingbox.py DaSiamRPN/code/
cp modified_DaSiamRPN/nfov.py DaSiamRPN/code/
cp modified_DaSiamRPN/parser.py DaSiamRPN/code/
cp modified_DaSiamRPN/run_video_360.py DaSiamRPN/code/
cp modified_DaSiamRPN/tracker_360_default.py DaSiamRPN/code/
cp modified_DaSiamRPN/tracker_360_border.py DaSiamRPN/code/
cp modified_DaSiamRPN/tracker_360_nfov.py DaSiamRPN/code/

echo "******* Installing gdown... *******"
pip install gdown

echo "******* Downloading model... *******"
gdown https://drive.google.com/u/0/uc\?id\=1-vNVZxfbIplXHrqMHiJJYWXYWsOIvGsf -O DaSiamRPN/code/SiamRPNBIG.model

echo "******* Downloading VOT model... *******"
gdown https://drive.google.com/u/0/uc\?id\=1G9GtKpF36-AwjyRXVLH_gHvrfVSCZMa7 -O DaSiamRPN/code/SiamRPNVOT.model