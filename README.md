# spacy_langdetect
Fully customizable language detection pipeline for [spaCy](https://github.com/explosion/spaCy)

## Installation
`pip3 install spacy-langdetect`

## NOTE:
Requires spaCy >= 2.0. This dependency is removed in `pip install spacy-langdetect`

## Basic usage
Out of the box, under the hood it uses [langdetect](https://github.com/Mimino666/langdetect) to detect languages on spaCy's Doc and Span objects.

```python
import spacy
from spacy_langdetect import LanguageDetector
nlp = spacy.load("en")
nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne."
doc = nlp(text)
# document level language detection. Think of it like average language of document!
print(doc._.language)
# sentence level language detection
for i, sent in enumerate(doc.sents):
    print(sent, sent._.language)
```

## Using your own language detector
Suppose you are not happy with the accuracy of the out of the box language detector or you have your own language detector which you want to use with spaCy pipeline. How do you do it? That's where the `language_detection_function` argument comes in. The function takes in a Spacy Doc or Span object and can return any python object which is stored in `doc._.language` and `span._.language`. For example, let's say you want to use [googletrans](https://pypi.org/project/googletrans/) as your language detection module:

```python
import spacy
from spacy.tokens import Doc, Span
from spacy_langdetect import LanguageDetector
# install using pip install googletrans
from googletrans import Translator
nlp = spacy.load("en")

def custom_detection_function(spacy_object):
    # custom detection function should take a Spacy Doc or a
    assert isinstance(spacy_object, Doc) or isinstance(
        spacy_object, Span), "spacy_object must be a spacy Doc or Span object but it is a {}".format(type(spacy_object))
    detection = Translator().detect(spacy_object.text)
    return {'language':detection.lang, 'score':detection.confidence}

nlp.add_pipe(LanguageDetector(language_detection_function=custom_detection_function), name="language_detector", last=True)
text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne."
doc = nlp(text)
# document level language detection. Think of it like average language of document!
print(doc._.language)
# sentence level language detection
for i, sent in enumerate(doc.sents):
    print(sent, sent._.language)
```
Similarly you can also use [pycld2](https://pypi.org/project/pycld2/) and other language detectors with spaCy
