# MomentsExtractor

## Probem Statement
The video recorded for this test consists of several kids entering a house. Extract the time-intervals during which interesting activity takes place. [Interest factor: human presence]
__Required:__ _Generate and store a list of timestamps `t_start - t_end` in a file `output.txt` for the given video by __Python__ scripts_.

## Solution
* We first extract the possibly interesting moments by the script `extractor.py` and store the time-stamps in the file `meta.txt`
* The detection of human presence is done through __haarcascade__. Here, the __upper_body__ haarcascade is used.
* These timestamps are then analyzed for grouping based on the parameters `WIDTH` and `THRESHOLD` using the script `group.py`
* The groups formed are expanded to include the neighbors close to the interesting durations
* The time-durations are then checked for overlap, if overlap is present, then the multiple time-intervals are reduced to one.
* The final time-intervals are written in the file `output.txt`

### Requirements
OpenCV, NumPy, Matplotlib (visualization)

### Usage
```
git clone https://github.com/Aniq55/MomentsExtractor.git
cd MomentsExtractor
```

Download the test video [here](https://drive.google.com/file/d/0B2vPCVjlmUOsa2otcnJMbmtKRFE/view?usp=sharing)

Now, run the script and enter the filename with path and press enter
```
python3 extractor.py
```
After this script completes execution, run another script and provide the filename with path of the test video

```
python3 group.py
```
On completion, an `output.txt` is  generated.

### Visualization
![alt text](https://github.com/Aniq55/MomentsExtractor/blob/master/tests/test_W200_T80.png)

This project was assigned by: saurav@getalice.co 