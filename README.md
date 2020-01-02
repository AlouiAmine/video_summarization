# video summarization
## Environment
- python2
- torch 1.2.0
- torchvison 0.2.0

## Get started
1. Download the video dataset 
2. Generate features using the resnet model
``` 
nohup python2 -u generate_dataset_mod.py --model_name resnet --data path_to_videos --out file_output.h5 > file_log.log & tail -f file_log.log
```
As an output we get a file which contains the visual features for each video.

3. Make splits

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

## Visualize summary
You can use `summary2video.py` to transform the binary `machine_summary` to real summary video. You need to have a directory containing video frames. The code will automatically write summary frames to a video where the frame rate can be controlled. Use the following command to generate a `.mp4` video
```bash
python summary2video.py -p path_to/result.h5 -d path_to/video_frames -i 0 --fps 30 --save-dir log --save-name summary.mp4
```


## Citation
```
@article{zhou2017reinforcevsumm, 
   title={Deep Reinforcement Learning for Unsupervised Video Summarization with Diversity-Representativeness Reward},
   author={Zhou, Kaiyang and Qiao, Yu and Xiang, Tao}, 
   journal={arXiv:1801.00054}, 
   year={2017} 
}
```

