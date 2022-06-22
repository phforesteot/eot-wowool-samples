#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
#  requirements.txt
#
from eot.wowool.error import Error
from eot.wowool.topic_identifier import TopicIdentifier
from eot.wowool.document import Document

try:

    topic_it = TopicIdentifier(language="english", topic_model="english.topic_model")
    doc = Document("I saw black cars and a green bird and green house.")
    doc = topic_it( doc )
    print(doc.topics)

except Error as ex:
    print("Exception:",ex)
