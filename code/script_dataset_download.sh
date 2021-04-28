#!/bin/sh

echo "******* Installing gdown... *******"
pip install gdown

echo "******* Downloading dataset... *******"
gdown https://drive.google.com/u/0/uc\?id\=1PWqpAb0DuXA58RZcEzfxqBP7C3yVH7uE -O annotation/dataset.zip

echo "******* Unziping dataset folder... *******"
unzip annotation/dataset.zip -d annotation/