## Guide to enable DaSiamRPN

First make sure that you had cloned the original repository.

```
git submodule update --init  
```

Then you should copy the necessary modified files and download pretrained network. You could use the script in "360Tracking/code/" directory.

```
$360Tracking/code/
bash script_modify_DaSiamRPN.sh
```



After that,  this guide is now exactly the same as the tutorial on the original repository [DaSiamRPN](https://github.com/foolwood/DaSiamRPN). 

#### Install dependencies

Run the installation script to install all the dependencies.
(install pytorch, numpy, opencv following the instructions in the `run_install.sh`. Please do **not** use conda to install)

```
$360Tracking/code/
cd DaSiamRPN
bash run_install.sh
```

#### Let's test it!

A simple test example.

```
$360Tracking/code/DaSiamRPN
cd code
python demo.py
```



#### Let's test 360Tracking improvements!

Get back to "360Tracking/code/" directory and run the following command.

```
$360Tracking/code/
# default DaSiamRPN tracker
python DaSiamRPN/code/run_video_360.py -v annotation/dataset-demo/demo-annotation/demo.mp4

# DaSiamRPN tracking with equirectangular border improvement
python DaSiamRPN/code/run_video_360.py -v annotation/dataset-demo/demo-annotation/demo.mp4 -border

# DaSiamRPN tracking with NFOV improvement
python DaSiamRPN/code/run_video_360.py -v annotation/dataset-demo/demo-annotation/demo.mp4 -nfov
```

