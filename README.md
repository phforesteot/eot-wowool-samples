# eot-wowool-samples
Samples for the Wowool-sdk 2.x version.
Make sure you have your lic.dat file installed or the environment variabel points to it

## Setup

export PIP_EXTRA_INDEX_URL=https://partners:[YourPassword]@repo.eyeontext.com/repository/eyeontext-pypi/simple

Not the password need to be encoded to pass in the url
to encode url password:

  python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" [YourPassword]

pip3 install eot-wowool-common
pip3 install eot-wowool-sdk
pip3 install eot-wowool-english_entity
pip3 install eot-wowool-topic_identifier


## dutch_entity.py
Analyse a input string and return the analytic results and it's entities.

## concept_iter.py
Shows you how to traverse the concepts in a result object.

## callback.py
Explains you how to capture some data passing it to python at matching time, so that you can decide if this is a valid hit or discard the matching results.
Before it can be processed later.

