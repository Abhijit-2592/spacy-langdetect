import pytest
from spacy_langdetect import LanguageDetector
import spacy


def test_language_detector():
    nlp = spacy.load("en")
    nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
    text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, \
     j'ai 12 ans et je suis canadienne."
    doc = nlp(text)
    assert doc._.language["language"] == "fr"  # majority is french
    languages = ["en", "de", "es", "fr"]
    for i, sent in enumerate(doc.sents):
        assert sent._.language["language"] == languages[i]


def test_custom_language_detector():
    nlp = spacy.load("en")
    nlp.add_pipe(LanguageDetector(language_detection_function=lambda spacy_object: "from custom function"), name="language_detector", last=True)
    text = "This is a test"
    doc = nlp(text)
    assert doc._.language == "from custom function"
    for i, sent in enumerate(doc.sents):
        assert sent._.language == "from custom function"


if __name__ == '__main__':
    pytest.main([__file__])
