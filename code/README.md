#### TODO description...


##### run_annotation

```
python run_annotation_tool.py -v annotation/dataset/01/01.mp4
```

```
python run_annotation_tool.py -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt
```

```
python run_annotation_tool.py -v annotation/dataset/01/01.mp4 --save
```


##### run_draw_annotation

```
python run_draw_annotation.py --demo
```

```
python run_draw_annotation.py -dir annotation/dataset/03
```

```
python run_draw_annotation.py -dir annotation/dataset/03 -img
```


##### run_evaluation

```
python run_evaluation.py -demo
```

```
python run_evaluation.py -video annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -result annotation/results/CSRT/03-result-borders.txt
```

```
python run_evaluation.py -img annotation/dataset/03/img/ -gt annotation/dataset/03/groundtruth.txt -result annotation/results/CSRT/03-result-borders.txt
```


##### run_tracking

