#### TODO description...


##### run_annotation

```
# run annotation tool without existing groundtruth data
python run_annotation_tool.py -v annotation/dataset/01/01.mp4

# run annotation tool with existing groundtruth data - parse groundtruth and possible update
python run_annotation_tool.py -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt

# run annotation tool and save frames as *.jpg images when annotating
python run_annotation_tool.py -v annotation/dataset/01/01.mp4 --save
```


##### run_draw_annotation

```
# demo of drawing annotations
python run_draw_annotation.py --demo

# drawing annotations in video frames in given dataset directory
python run_draw_annotation.py -dir annotation/dataset/03

# drawing annotations in images sequence in given dataset directory
python run_draw_annotation.py -dir annotation/dataset/03 -img
```


##### run_evaluation

```
# running demo evaluation - just show groundtruth and result data
python run_evaluation.py -demo

# run drawing of evaluation for given video, groundtruth and result data
python run_evaluation.py -video annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -result annotation/results/CSRT/03/03-result-border.txt

# run computing Intersection over Union metric for given video, groundtruth and result file
python run_evaluation.py -video annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -result annotation/results/CSRT/03/03-result-border.txt -iou

# run drawing of evaluation for given images sequence directory, groundtruth and result data
python run_evaluation.py -img annotation/dataset/03/img/ -gt annotation/dataset/03/groundtruth.txt -result annotation/results/CSRT/03/03-result-border.txt
```


##### run_tracking
```
python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4

python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt

python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -border

python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -nfov

python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/CSRT/01-result-default.txt

python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/CSRT/01-result-border.txt -border

python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/CSRT/01-result-rect.txt -nfov


python pytracking/pytracking/run_video_default.py atom default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt

python pytracking/pytracking/run_video_default.py dimp dimp50 annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt

python pytracking/pytracking/run_video_default.py dimp dimp18 annotation/dataset/02/02.mp4

python pytracking/pytracking/run_video_default.py atom default annotation/dataset/03/03.mp4

python pytracking/pytracking/run_video_default.py kys default annotation/dataset/01/01.mp4

python pytracking/pytracking/run_video_default.py eco default annotation/dataset/01/01.mp4
```

