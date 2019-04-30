import pytest
from spacy_langdetect import LanguageDetector
import spacy


def test_language_detector():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
    text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, \
     j'ai 12 ans et je suis canadienne."
    doc = nlp(text)
    doc._.language["language"]
    for i, sent in enumerate(doc.sents):
        sent._.language["language"]


def test_tokens():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
    text = "English Hello"
    doc = nlp(text)
    languages = []
    for i, token in enumerate(doc):
        languages.append(token._.language["language"])
    assert len(languages) == 2


def test_custom_language_detector():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(LanguageDetector(language_detection_function=lambda spacy_object: "from custom function"), name="language_detector", last=True)
    text = "This is a test"
    doc = nlp(text)
    assert doc._.language == "from custom function"
    for i, sent in enumerate(doc.sents):
        assert sent._.language == "from custom function"


if __name__ == '__main__':
    pytest.main([__file__])
