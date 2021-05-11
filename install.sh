#!/bin/sh

## Tested on Windows 10 with python 3.9.4 and following package versions

# pip install opencv-contrib-python==4.4.0.46
# pip install "matplotlib>=3.3.4"
# pip install "numpy>=1.20.1"
# pip install "torch>=1.8.1"
# pip install statsmodels
# pip install seaborn


# Tested on Ubuntu 18.04 with python 3.8.3 and following package versions

echo "************ Installing opencv-contrib-python *************"
# last opencv-contrib-python release 4.5.1.48 raises errors for some trackers...
pip install opencv-contrib-python==4.4.0.46
echo ""
echo ""

echo "****************** Installing matplotlib ******************"
pip install "matplotlib>=3.2.2"
echo ""
echo ""

echo "****************** Installing numpy ***********************"
pip install "numpy>=1.18.5"
echo ""
echo ""

echo "****************** Installing torch ***********************"
pip install "torch>=1.7.0"
echo ""
echo ""


echo "************** Installing statsmodels *********************"
pip install statsmodels
echo ""
echo ""

echo "****************** Installing seaborn *********************"
pip install seaborn
echo ""
echo ""

echo "**************** Installation completed! ******************"
