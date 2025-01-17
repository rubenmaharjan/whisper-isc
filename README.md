# Confidence scores for Whisper for ISC 

## Description
This script modifies methods of Whisper's model to gain access to the predicted timestamp tokens of each word (token) without needing additional inference. It also stabilizes the timestamps down to the word (token) level to ensure chronology. Additionally, it can suppress gaps in speech for more accurate timestamps.

![image](https://user-images.githubusercontent.com/28970749/192950141-40ac8cbd-ccac-45da-b563-f8144d22c54e.png)

Confidence score is a log_softmax used for sum_logprobs also.
```python
F.log_softmax(logits.float(), dim=-1)
```
![Screenshot_2022-12-15_12-25-55](https://user-images.githubusercontent.com/2093802/207827789-7e121a63-2dd6-4dc0-9618-b494bce47a1a.png)


## TODO
- [ ] Add function to stabilize with multiple inferences

## Dependency
* [Whisper](https://github.com/openai/whisper)

## Setup
#### Option 1: Install Whisper ISC (one line)
```
pip install it+https://github.com/rubenmaharjan/whisper-isc.git@main
```
#### Option 2 (without confidence): Install Whisper (repo) and stable-ts (PyPI) separately
1. Install [Whisper](https://github.com/openai/whisper#setup)
2. Check if Whisper is installed correctly by running a quick test
```python
import whisper
model = whisper.load_model('base')
assert model.transcribe('audio.mp3').get('segments')
```
3. Install whisper-isc
```commandline
pip install git+https://github.com/rubenmaharjan/whisper-isc.git@main
```

### Executing script from command line
```bash
# outpur_format generates a file saved in the current directory
# CSV is seperated with |
# word | timestamp | confidence 
whisper-isc audio.mp3 --output_format csv --model=tiny --language=en

# multiple file format generation
whisper-isc audio.mp3 --output_format csv --output_format txt --model=tiny --language=en

# multiple file format generation and specific directory to save files
whisper-isc audio.mp3 --output_dir /path/to/target/dir --output_format csv --output_format txt --model=tiny --language=en
```

### Executing script
```python
from isc_whisper import load_model

model = load_model('base')
# modified model should run just like the regular model but with additional hyperparameters and extra data in results
results = model.transcribe('audio.mp3')
stab_segments = results['segments']
first_segment_word_timestamps = stab_segments[0]['whole_word_timestamps']
# whole_word_timestamps key has the word, timestamp and confidence

# or to get token timestamps that adhere more to the top prediction
from isc_whisper import stabilize_timestamps
stab_segments = stabilize_timestamps(results, top_focus=True)
```

### Generate .srt with stable timestamps
```python
# word-level
from isc_whisper import results_to_word_srt
# after you get results from modified model
# this treats a word timestamp as end time of the word
# and combines words if their timestamps overlap
results_to_word_srt(results, 'audio.srt')  # combine_compound=True will merge words with no prepended space
```
```python
# sentence/phrase-level
from isc_whisper import results_to_sentence_srt
# after you get results from modified model
results_to_sentence_srt(results, 'audio.srt')
# below is from large model default settings
```

https://user-images.githubusercontent.com/28970749/202782436-0d56140b-5d52-4f33-b32b-317a19ad32ca.mp4


```python
# sentence/phrase-level & word-level
from isc_whisper import results_to_sentence_word_ass
# after you get results from modified model
results_to_sentence_word_ass(results, 'audio.ass')
# below is from large model default settings
```

https://user-images.githubusercontent.com/28970749/202782412-dfa027f8-7073-4023-8ce5-285a2c26c03f.mp4

#### Confidence Metrics
* To get confidence few lines have been added to ***whisper_word_level.py*** file.
* The file has been commented with #my before all the changes made.


#### Additional Info
* Since the sentence/segment-level timestamps are predicted directly, they are always more accurate and precise than word/token-level timestamps.
* Although timestamps are chronological, they can still be off sync depending on the model and audio.
* The `unstable_word_timestamps` are left in the results, so you can possibly find better way to utilize them.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
Includes slight modification of the original work: [Whisper](https://github.com/openai/whisper)
