# video summarization
## Environment
- python2
- pytorch 3.1.0

## Get started
1. Download the video dataset 
2. Generate features using the resnet model
``` 
nohup python2 -u generate_dataset_mod.py --model_name resnet --data path_to_videos --out file_output.h5 > resnet_log.log & tail -f file_log.log
```


