from flask import Flask, abort, request, jsonify
from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.topic_identifier import TopicIdentifier

app = Flask(__name__)

english = Analyzer(language="english")
entities = Domain("english-entity")
topicit = TopicIdentifier(language="english", topic_model="english.topic_model")


# print(english("test"))

@app.route("/entities", methods=["POST"])
def analyze():

    if not request.json:
        abort(400)

    if "text" not in request.json:
        return jsonify({"Error": '"text" param missing in post request.'})
    doc = entities(english(request.json['text']))
    concepts = [ { **concept } for concept in Concept.iter(doc) ]
    print("concepts:" , concepts )
    return jsonify(concepts)



@app.route("/topics", methods=["POST"])
def get_topics():

    if not request.json:
        abort(400)

    if "text" not in request.json:
        return jsonify({"Error": '"text" param missing in post request.'})

    topics = topicit.get_topics(request.json['text'], 5)
    return jsonify(topics)
