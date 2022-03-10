#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
# If you run from the docker container you will need to open a port while starting:
# `pwd` would be the location of this file.

# docker run -v `pwd`:/eotws/ -p 5000:5000 -it docker.eyeontext.com/eot/sdk:2.1.2 bash

# HOW TO RUN: export FLASK_APP=eot-server:app ;flask run --host 0.0.0.0
#
# curl -X POST -H 'Content-Type: application/json' -i http://localhost:5000/topics --data '{
#    "text": "this document is about green gasses and yellow houses."
# }'

from flask import Flask, abort, request, jsonify
from eot.wowool.native import Language, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.topic_identifier import TopicIdentifier

app = Flask(__name__)

english = Language("english")
entities = Domain("english-entity")
topicit = TopicIdentifier(language="english", topic_model="english.topic_model")



@app.route("/entities", methods=["POST"])
def analyze():

    if not request.json:
        abort(400)

    if "text" not in request.json:
        return jsonify({"Error": '"text" param missing in post request.'})
    doc = entities(english(request.json["text"]))
    concepts = [{**concept} for concept in Concept.iter(doc)]
    print("concepts:", concepts)
    return jsonify(concepts)


@app.route("/topics", methods=["POST"])
def get_topics():

    if not request.json:
        abort(400)

    if "text" not in request.json:
        return jsonify({"Error": '"text" param missing in post request.'})

    topics = topicit.get_topics(request.json["text"], 5)
    return jsonify(topics)
