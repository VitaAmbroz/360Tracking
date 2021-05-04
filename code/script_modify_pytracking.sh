#!/bin/sh

# git clone https://github.com/visionml/pytracking.git
# cd pytracking
# git submodule update --init
# bash install.sh conda_install_path pytracking

echo "******* Copying modified files... *******"
cp modified_pytracking/__init__.py pytracking/pytracking/evaluation
cp modified_pytracking/boundingbox.py pytracking/pytracking/evaluation
cp modified_pytracking/nfov.py pytracking/pytracking/evaluation
cp modified_pytracking/parser.py pytracking/pytracking/evaluation
cp modified_pytracking/tracker_360_default.py pytracking/pytracking/evaluation
cp modified_pytracking/tracker_360_border.py pytracking/pytracking/evaluation
cp modified_pytracking/tracker_360_nfov.py pytracking/pytracking/evaluation
cp modified_pytracking/run_video_360.py pytracking/pytracking/

echo "******* Installing gdown... *******"
pip install gdown

mkdir pytracking/pytracking/networks

echo "******* Downloading ATOM model... *******"
gdown https://drive.google.com/u/0/uc\?id\=1VNyr-Ds0khjM0zaq6lU-xfY74-iWxBvU -O pytracking/pytracking/networks/atom_default.pth

echo "******* Downloading DiMP50 model... *******"
gdown https://drive.google.com/u/0/uc\?id\=1qgachgqks2UGjKx-GdO1qylBDdB1f9KN -O pytracking/pytracking/networks/dimp50.pth

echo "******* Downloading KYS model... *******"
gdown https://drive.google.com/u/0/uc\?id\=1nJTBxpuBhN0WGSvG7Zm3yBc9JAC6LnEn -O pytracking/pytracking/networks/kys.pth

echo "******* Downloading ECO model... *******"
mkdir pytracking/pytracking/networks/resnet18_vggmconv1
gdown https://drive.google.com/u/0/uc\?id\=1aWC4waLv_te-BULoy0k-n_zS-ONms21S -O pytracking/pytracking/networks/resnet18_vggmconv1/resnet18_vggmconv1.pth