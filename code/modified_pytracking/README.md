## Guide to enable pytracking

First make sure that you had cloned the original repository.

```
git submodule update --init  
```

Then you should copy the necessary modified files and download pretrained networks. You could use the [script](./code/script_modify_pytracking.sh) in "360Tracking/code/" directory.

```
$360Tracking/code/
bash script_modify_pytracking.sh
```



After that,  this guide is now exactly the same as tutorial on the original repository [pytracking](https://github.com/visionml/pytracking). 

#### Clone the submodules

```
cd pytracking
git submodule update --init
```

#### Install dependencies

Run the installation script to install all the dependencies. You need to provide the conda install path (e.g. /home/user/anaconda3) and the name for the  created conda environment (here `pytracking`).

```
bash install.sh conda_install_path pytracking
```

This script will also download the default network and set-up the environment.

#### Let's test it!

Activate the conda environment and run the script pytracking/run_webcam.py to run ATOM using the webcam input.

```
conda activate pytracking
cd pytracking
python run_webcam.py dimp dimp50    
```



#### Let's test 360Tracking improvements!

Get back to "360Tracking/code/" directory and run the following command.

```
$360Tracking/code/
# default tracker
python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset-demo/demo-annotation/demo.mp4

# tracking with equirectangular border improvement
python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset-demo/demo-annotation/demo.mp4 -border

# tracking with NFOV improvement
python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset-demo/demo-annotation/demo.mp4 -nfov
```

