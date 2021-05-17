# Visual Object Tracking in Panoramic video

This repository 360Tracking has been created as the part of master thesis at  [Brno University of Technology - Faculty of Information Technology](https://www.fit.vut.cz/). The master thesis has been supervised by [Doc. Ing. Martin Čadík, Ph.D.](http://cadik.posvete.cz/)

## Improvements of Single Object Tracking (SOT) in 360° video

Single object trackers can fail or produce false positive results when tracking in equirectangular projection of 360° videos. The reasons of failures could be similar as in ordinary videos with limited field of view (e.g. occlusion). Although there might be other problems caused by equirectangular distortion. The tracked object can also cross horizontal borders of equirectangular frame. You could see how the state-of-the-art tracker [KYS](https://github.com/visionml/pytracking) generates false positive results and fails below.

<p align="center">
    <img src="./code/fig/kys_default.gif" alt="kys_default"  />
</p>

### Equirectangular rotation approach

This approach may be the right solution for border crossing problem of single object tracking in equirectangular panorama. We have provided the solution where we simply simulate the spherical rotation about z-axis (Yaw). The tracker predicts results in shifted/rotated frame and predicted bounding box is transformed backward to original frame.

<p align="center">
    <img src="./code/fig/kys_border.gif" alt="kys_border"  />
</p>



### Normal field of view (rectilinear) approach 

The second approach could improve tracking process in very distorted areas in equirectangular projection and solves border crossing problem as well. This solution simulates virtual camera system that tries to keep the tracked object in the center area of rectilinear projection. The tracker predicts results in rectilinear/perspective projection (adaptive field of view from 90° to 144°) and these results are converted backward to equirectangular (360°) coordinates.

<p align="center">
    <img src="./code/fig/kys_nfov.gif" alt="kys_nfov"  />
</p>



## Evaluation

We have evaluated 12 trackers for manually created dataset composed of 21 equirectangular videos.

### Dataset

New dataset with annotated objects in 360° equirectangular video has been created. You can see demo of this dataset [here](./code/annotation/dataset-demo/demo-annotation) or on [YouTube](https://www.youtube.com/watch?v=kgXd6uoXa8M). This dataset includes 21 video sequences with total 9909 annotated (groundtruth) frames. The bounding boxes could be overflowing the horizontal borders of equirectangular frames.

You can download full dataset using this [script](./code/script_dataset_download.sh) or you can download it manually as [zip](https://drive.google.com/file/d/1PWqpAb0DuXA58RZcEzfxqBP7C3yVH7uE/view?usp=sharing) or [folder](https://drive.google.com/drive/folders/13tkE4vY3FGGD42kDIjyS9K423vrvpKoU?usp=sharing).

The videos used in this dataset have been taken from these resources (datasets 1 a 2 have been reannotated):

> 1. Keng-Chi Liu, Yi-Ting Shen, Liang-Gee Chen. "Simple online and realtime tracking with spherical panoramic camera" (ICCE 2018) **[[Paper]](https://ieeexplore.ieee.org/document/8326132)  [[Dataset]](https://github.com/KengChiLiu/MOT360)**
>
> 2. Mi Tzu-Wei and Yang Mau-Tsuen.  "Comparison of Tracking Techniques on 360-Degree Videos" (2019) **[[Paper]](https://www.mdpi.com/2076-3417/9/16/3336)  [[Dataset]](https://drive.google.com/drive/folders/1Ybp0G6yWXYCsP06nzEMRJR-exK0DSos8)**
>
> 3. Afshin Taghavi Nasrabadi, Aliehsan Samiei, Anahita Mahzari, Ryan P. McMahan, Ravi Prakash, Mylène C. Q. Farias, and Marcelo M. Carvalho. "A taxonomy and dataset for 360° videos" (2019) **[[Paper]](https://arxiv.org/pdf/1905.03823.pdf)  [[Dataset]](https://github.com/afshin-aero/360dataset)**
>
> 4. Custom videos captured by [Ricoh Theta SC](https://theta360.com/en/about/theta/sc.html).



### Single object trackers

The custom improvements of Single Object Tracking in equirectangular projection of 360° video have been evaluated for the following well-known and state-of-the-art trackers. The python implementations of the selected trackers have been made publicly available by their authors or have been added to OpenCV extra modules.

- #### MIL **[[Paper]](https://faculty.ucmerced.edu/mhyang/papers/cvpr09a.pdf)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**

> B. Babenko, M. Yang and S. Belongie. 
> "Visual tracking with online Multiple Instance Learning" (CVPR 2009)

- #### MEDIANFLOW **[[Paper]](https://ieeexplore.ieee.org/document/5596017)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**

> Zdenek Kalal, Krystian Mikolajczyk, Jiri Matas.
> "Forward-Backward Error: Automatic Detection of Tracking Failures" (ICPR 2010)

- #### TLD **[[Paper]](https://ieeexplore.ieee.org/document/6104061)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**

> Zdenek Kalal, Krystian Mikolajczyk, Jiri Matas.
> "Tracking-Learning-Detection" (TPAMI 2011)

- #### KCF **[[Paper]](https://www.robots.ox.ac.uk/~joao/publications/henriques_tpami2015.pdf)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**

> João F. Henriques, Rui Caseiro, Pedro Martins, Jorge Batista. 
>"High-Speed Tracking with Kernelized Correlation Filters." (TPAMI 2015)

- #### CSR-DCF / CSRT **[[Paper]](https://openaccess.thecvf.com/content_cvpr_2017/papers/Lukezic_Discriminative_Correlation_Filter_CVPR_2017_paper.pdf)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**

> Alan Lukezic, Tomas Vojir, Luka Cehovin, Jiri Matas, Matej Kristan. 
>"Discriminative Correlation Filter with Channel and Spatial Reliability." (CVPR 2017)

- #### KYS **[[Paper]](https://arxiv.org/pdf/2003.11014.pdf)  [[Official Code]](https://github.com/visionml/pytracking)**

> Goutam Bhat, Martin Danelljan, Luc Van Gool, Radu Timofte. 
>"Know Your Surroundings: Exploiting Scene Information for Object Tracking." (ECCV 2020)

- #### DiMP **[[Paper]](https://arxiv.org/pdf/1904.07220)  [[Official Code]](https://github.com/visionml/pytracking)**


> Goutam Bhat, Martin Danelljan, Luc Van Gool, Radu Timofte. 
>"Learning Discriminative Model Prediction for Tracking." (ICCV 2019)

- #### ATOM **[[Paper]](https://arxiv.org/pdf/1811.07628)  [[Official Code]](https://github.com/visionml/pytracking)** 


> Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, Michael Felsberg. 
>"ATOM: Accurate Tracking by Overlap Maximization." (CVPR 2019)

- #### ECO **[[Paper]](https://arxiv.org/pdf/1611.09224.pdf)  [[Unofficial code]](./pytracking/README.md#ECO)** 


> Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, Michael Felsberg. 
>"ECO: Efficient Convolution Operators for Tracking." (CVPR 2017)

- #### DaSiamRPN **[[Paper]](https://openaccess.thecvf.com/content_ECCV_2018/papers/Zheng_Zhu_Distractor-aware_Siamese_Networks_ECCV_2018_paper.pdf)  [[Official Code]](https://github.com/foolwood/DaSiamRPN)**

> Zheng Zhu, Qiang Wang, Bo Li, Wu Wei, Junjie Yan, Weiming Hu. 
> "Distractor-aware Siamese Networks for Visual Object Tracking." (ECCV 2018)

- #### Ocean **[[Paper]](https://arxiv.org/pdf/2006.10721.pdf)  [[Official code]](https://github.com/researchmm/TracKit)**

> Zhipeng Zhang and Houwen Peng and Jianlong Fu and Bing Li and Weiming Hu. 
>"Ocean: Object-aware Anchor-free Tracking" (ECCV 2020)

- #### SiamDW **[[Paper]](https://openaccess.thecvf.com/content_CVPR_2019/papers/Zhang_Deeper_and_Wider_Siamese_Networks_for_Real-Time_Visual_Tracking_CVPR_2019_paper.pdf)  [[Official Code]](https://github.com/researchmm/TracKit)**

> Zhipeng Zhang, Houwen Peng. 
>"Deeper and Wider Siamese Networks for Real-Time Visual Tracking." (CVPR 2019)



### Results

These 12 trackers have been evaluated for the custom dataset mentioned above. You may notice the success plots based on Intersection over Union (IoU) metric with AUC values in legend and precision plots based on center error distance. DEFAULT plots display tracker results without any improvement, BORDER plots display "equirectangular rotation approach" results and finally NFOV plots display trackers results from normal field of view (rectilinear) approach.

<img src="./code/fig/success_plots.png" alt="success_plots"  />

<img src="./code/fig/precision_plots.png" alt="success_plots"  />



## Default installation (only OpenCV trackers)

#### Clone the GIT repository

```bash
git clone https://github.com/VitaAmbroz/360Tracking.git
```

#### Install dependencies

Run the installation script to install all the dependencies. These dependencies should enable OpenCV tracking.

```
bash install.sh
```

**Note:** The install script has been tested on an Ubuntu 18.04. You could probably use current releases of numpy, torch and matplotlib. The implementation has been tested also on Windows 10 platform.

#### Let's test it!

```
cd code

# try OpenCV implementation of tracker CSRT
python run_opencv_tracking.py -t CSRT -v annotation/dataset-demo/demo-annotation/demo.mp4

# try CSRT with BORDER improvement
python run_opencv_tracking.py -t CSRT -v annotation/dataset-demo/demo-annotation/demo.mp4 -border

# try CSRT with NFOV improvement
python run_opencv_tracking.py -t CSRT -v annotation/dataset-demo/demo-annotation/demo.mp4 -nfov
```



## Advanced installation

You could also try the official python implementations of selected trackers. 

#### Clone the submodules

This command clones 3 repositories ([pytracking](https://github.com/visionml/pytracking), [DaSiamRPN](https://github.com/foolwood/DaSiamRPN), [TracKit](https://github.com/researchmm/TracKit)) including implementations of some state-of-the-art trackers.

```
git submodule update --init  
```

#### Follow the instructions

- To enable ECO, ATOM, DiMP and KYS trackers ([pytracking](https://github.com/visionml/pytracking))

  -> Follow the instructions [here](./code/modified_pytracking/README.md) (see also modified [code](./code/modified_pytracking/))

- To enable DaSiamRPN tracker ([DaSiamRPN](https://github.com/foolwood/DaSiamRPN))
  
  -> Follow the instructions [here](./code/modified_DaSiamRPN/README.md) (see also modified [code](./code/modified_DaSiamRPN/))

- To enable SiamDW and Ocean trackers ([TracKit](https://github.com/researchmm/TracKit))
  
  -> Follow the instructions [here](./code/modified_TracKit/README.md) (see also modified [code](./code/modified_TracKit/))

  

## Directory structure

```
$360Tracking
|-- tech_report
|-- code
   |-- annotation
      |-- dataset
      |-- dateset-demo
      |-- results
   |-- opencv_tracking
   |-- boundingbox
   |-- nfov
   |-- modified_DaSiamRPN
   |-- modified_pytracking
   |-- modified_TracKit
   |-- DaSiamRPN
   |-- pytracking
   |-- TracKit
```