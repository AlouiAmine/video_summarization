# video summarization
## Environment
- python2
- pytorch 3.1.0

## Get started
1. Download the video dataset 
2. Generate features using the resnet model
``` 
nohup python2 -u generate_dataset_mod.py --model_name resnet --data path_to_videos --out file_output.h5 > file_log.log & tail -f file_log.log
```
As an output we get a file which contains the visual features for each video.

2. Make splits

``` 
python create_split.py -d file_outut.h5 --save-dir datasets --save-name name_data_splits  --num-splits 5

```
As a result, the dataset is randomly split for 5 times, which are saved as json file.

Train and test codes are written in `main.py`. To see the detailed arguments, please do `python main.py -h`.
## How to train
```bash
python main.py -d file_output.h5 -s name_data_splits.json -m summe --gpu 0 --save-dir log/name_data-split0 --split-id 0 --verbose
```

## How to test
```bash
python main.py -d file_output.h5 -s name_data_splits.json -m summe --gpu 0 --save-dir log/name_data-split0 --split-id 0 --evaluate --resume path_to_your_model.pth.tar --verbose --save-results
```

If argument `--save-results` is enabled, output results will be saved to `results.h5` under the same folder specified by `--save-dir`. To visualize the score-vs-gtscore, simple do
```bash
python visualize_results.py -p path_to/result.h5
```

