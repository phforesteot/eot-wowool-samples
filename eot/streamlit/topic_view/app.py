import streamlit as st
from eot.wowool.native import Analyzer, Domain
from eot.wowool.topic_identifier import TopicIdentifier
from eot.wowool.annotation import Concept
import pandas as pd


entity_filter = set(["Person", "Company", "Address", "City", "Facility"])

st.write("EyeOnText English Topics and Entities")
name = st.text_area("Enter Your text", """John Smith works at EyeOnText in Antwerp.""")
if st.button("Analyze"):
    input_text = name
    analyzer = Analyzer(language="english")
    entities = Domain("english-entity")
    topicit = TopicIdentifier(language="english")

    doc = entities(analyzer(input_text))
    topics = topicit.get_topics(doc, 20)

    # st.write("topics")
    # st.write(pd.DataFrame(topics, columns=["topic", "relevancy"]))

    combined_topics = {}
    for topic in topics:
        combined_topics[topic[0]] = ["topic", topic[0], topic[1]]

    for concept in Concept.iter(doc, lambda concept: concept.uri in entity_filter):
        combined_topics[concept.literal] = [concept.uri, concept.literal, 1.0 ]

    st.write(f"topics and {','.join(entity_filter)}")
    st.write(pd.DataFrame([v for k, v in combined_topics.items()], columns=["type", "topic", 'relavancy']))
