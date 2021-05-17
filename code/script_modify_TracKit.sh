#!/bin/sh

# git clone https://github.com/researchmm/TracKit.git

echo "******* Copying modified files... *******"
cp modified_TracKit/boundingbox.py TracKit/tracking/
cp modified_TracKit/nfov.py TracKit/tracking/
cp modified_TracKit/parser.py TracKit/tracking/
cp modified_TracKit/ocean_360_default.py TracKit/tracking/
cp modified_TracKit/ocean_360_border.py TracKit/tracking/
cp modified_TracKit/ocean_360_nfov.py TracKit/tracking/
cp modified_TracKit/siamdw_360_default.py TracKit/tracking/
cp modified_TracKit/siamdw_360_border.py TracKit/tracking/
cp modified_TracKit/siamdw_360_nfov.py TracKit/tracking/
cp modified_TracKit/run_video_360.py TracKit/tracking/

echo "******* Installing gdown... *******"
pip install gdown

mkdir TracKit/snapshot
echo "******* Downloading SiamDW model... *******"
gdown https://drive.google.com/u/0/uc\?id\=1SzIql02jJ6Id1k0M6f-zjUA3RgAm6E5U -O TracKit/snapshot/siamdw_res22w.pth

echo "******* Downloading Ocean VOT19 online model... *******"
gdown https://drive.google.com/u/0/uc\?id\=1JAg22EYUpH_ODns-w-EN1hRhqk4d78Oz -O TracKit/snapshot/OceanV19on.pth


echo "******* If models have not been downloaded, you need get access - see https://github.com/researchmm/TracKit ... *******"
