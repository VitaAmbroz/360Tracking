# Visual Object Tracking in Panoramic video

This repository 360Tracking has been created as the part of master thesis at  [Brno University of Technology - Faculty of Information Technology](https://www.fit.vut.cz/). The master thesis has been supervised by [Doc. Ing. Martin Čadík, Ph.D.](http://cadik.posvete.cz/)

TODO - brief description

## Improvements of Single Object Tracking (SOT) in 360° video

TODO - add final code and brief description of improvements



## Evaluation

TODO - brief description

### Dataset

TODO - brief description

### Single object trackers

The custom improvements of Single Object Tracking in equirectangular projection of 360° video has been evaluated for the following well-known and state-of-the-art trackers. The python implementations of selected trackers have been made publicly available by their authors or have been added to OpenCV library.

- #### MIL

> **[[Paper]](https://faculty.ucmerced.edu/mhyang/papers/cvpr09a.pdf)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**
> B. Babenko, M. Yang and S. Belongie, 
> "Visual tracking with online Multiple Instance Learning" (CVPR 2009)

- #### KCF

> **[[Paper]](https://www.robots.ox.ac.uk/~joao/publications/henriques_tpami2015.pdf)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**
> João F. Henriques, Rui Caseiro, Pedro Martins, Jorge Batista. 
> "High-Speed Tracking with Kernelized Correlation Filters." (TPAMI 2015)

- #### CSR-DCF / CSRT

> **[[Paper]](https://openaccess.thecvf.com/content_cvpr_2017/papers/Lukezic_Discriminative_Correlation_Filter_CVPR_2017_paper.pdf)  [[OpenCV extra modules]](https://github.com/opencv/opencv_contrib)**
> Alan Lukežič, Tomáš Vojíř, Luka Čehovin, Jiří Matas, Matej Kristan. 
> "Discriminative Correlation Filter with Channel and Spatial Reliability." (CVPR 2017)

- #### KYS

> **[[Paper]](https://arxiv.org/pdf/2003.11014.pdf)  [[Official Code]](https://github.com/visionml/pytracking)**
> Goutam Bhat, Martin Danelljan, Luc Van Gool, Radu Timofte. 
> "Know Your Surroundings: Exploiting Scene Information for Object Tracking." (ECCV 2020)

- #### DiMP


> **[[Paper]](https://arxiv.org/pdf/1904.07220)  [[Official Code]](https://github.com/visionml/pytracking)**
> Goutam Bhat, Martin Danelljan, Luc Van Gool, Radu Timofte. 
> "Learning Discriminative Model Prediction for Tracking." (ICCV 2019)

- #### ATOM


> **[[Paper]](https://arxiv.org/pdf/1811.07628)   [[Official Code]](https://github.com/visionml/pytracking)** 
> Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, Michael Felsberg. 
> "ATOM: Accurate Tracking by Overlap Maximization." (CVPR 2019)

- #### ECO


> **[[Paper]](https://arxiv.org/pdf/1611.09224.pdf)  [[Unofficial code]](./pytracking/README.md#ECO)** 
> Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, Michael Felsberg. 
> "ECO: Efficient Convolution Operators for Tracking." (CVPR 2017)

- #### Ocean

> **[[Paper]](https://arxiv.org/pdf/2006.10721.pdf)  [[Official code]](https://github.com/researchmm/TracKit)**
> Zhipeng Zhang and Houwen Peng and Jianlong Fu and Bing Li and Weiming Hu. 
> "Ocean: Object-aware Anchor-free Tracking" (ECCV 2020)

- #### SiamDW

> **[[Paper]](https://openaccess.thecvf.com/content_CVPR_2019/papers/Zhang_Deeper_and_Wider_Siamese_Networks_for_Real-Time_Visual_Tracking_CVPR_2019_paper.pdf)  [[Official Code]](https://github.com/researchmm/TracKit)**
> Zhipeng Zhang, Houwen Peng. 
> "Deeper and Wider Siamese Networks for Real-Time Visual Tracking." (CVPR 2019)

- #### DaSiamRPN

> **[[Paper]](https://openaccess.thecvf.com/content_ECCV_2018/papers/Zheng_Zhu_Distractor-aware_Siamese_Networks_ECCV_2018_paper.pdf)  [[Official Code]](https://github.com/foolwood/DaSiamRPN)**
> Zheng Zhu, Qiang Wang, Bo Li, Wu Wei, Junjie Yan, Weiming Hu. 
> "Distractor-aware Siamese Networks for Visual Object Tracking." (ECCV 2018)

### Results

TODO - brief description



## Installation

#### Clone the GIT repository.  

```bash
git clone https://github.com/VitaAmbroz/360Tracking.git
```

#### Install dependencies

TODO

#### Let's test it!

TODO