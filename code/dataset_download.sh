#!/bin/sh

echo "******* Installing gdown... *******"
pip install gdown

echo "******* Downloading dataset... *******"
gdown https://drive.google.com/u/0/uc\?id\=1ktaXGqRrSJpZ8DvSgF1-ZTAj_KBP9wHG -O annotation/dataset.zip

echo "******* Unziping dataset folder... *******"
unzip annotation/dataset.zip -d annotation/