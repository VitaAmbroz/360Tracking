## Guide to enable TracKit

First make sure that you had cloned the original repository.

```
git submodule update --init  
```

Then you should copy the necessary modified files and download pretrained networks. You could use the [script](./code/script_modify_TracKit.sh) in "360Tracking/code/" directory.

```
$360Tracking/code/
bash script_modify_TracKit.sh
```



After that,  this guide is now exactly the same as tutorial on the original repository [TracKit](https://github.com/researchmm/TracKit/blob/master/lib/tutorial/Ocean/ocean.md). 

#### Install dependencies

Run the installation script to install all the dependencies. You need to provide the conda install path (e.g. /home/user/anaconda3) and the name for the  created conda environment (here `TracKit`).

```
$360Tracking/code/

cd TracKit/lib/tutorial
bash install.sh $conda_path TracKit

# get back to $360Tracking/code/TracKit
cd ..
cd ..
conda activate TracKit
python setup.py develop
```

**Note:** We have used only pytorch version, yould try TensorRT version as well ([TracKit](https://github.com/researchmm/TracKit/blob/master/lib/tutorial/Ocean/ocean.md)).



#### Let's test 360Tracking improvements!

Get back to "360Tracking/code/" directory and run the following command.

```
$360Tracking/code/

# default Ocean
python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset-demo/demo-annotation/demo.mp4

# Ocean with equirectangular border improvement
python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset-demo/demo-annotation/demo.mp4 -border

# Pcean with NFOV improvement
python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset-demo/demo-annotation/demo.mp4 -nfov

# default SiamDW
python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset-demo/demo-annotation/demo.mp4

# SiamDW with equirectangular border improvement
python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset-demo/demo-annotation/demo.mp4 -border

# SiamDW with NFOV improvement
python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset-demo/demo-annotation/demo.mp4 -nfov
```

