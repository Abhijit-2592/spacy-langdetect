from langdetect.lang_detect_exception import LangDetectException
from langdetect import detect_langs
from spacy.tokens import Doc


def _detect_language(spacy_object):
    try:
        detected_language = detect_langs(spacy_object.text)[0]
        return {"language": str(detected_language.lang), "score": float(detected_language.prob)}
    except LangDetectException:
        return {"language": "UNKNOWN", "score": 0.0}


class LanguageDetector(object):
    """Fully customizable language detection pipeline for spaCy.

    Arguments:
        language_detection_function: An optional custom language_detection_function. (Default None).
                                     If None uses, langdetect package to detect language

    # writing a custom language_detection_function:
        The function must take in a spacy Doc or Span object only as input and can return the detected language.
        This is stored in Doc._.language, Span._.language and Token._.language attributes.
    """

    def __init__(self, language_detection_function=None):
        if not language_detection_function:
            self._language_detection_function = _detect_language
        else:
            self._language_detection_function = language_detection_function

    def __call__(self, doc):
        assert isinstance(doc, Doc), "doc must be an instance of spacy Doc. But got a {}".format(type(doc))
        doc.set_extension("language", getter=self._language_detection_function, force=True)
        for sent in doc.sents:
            sent.set_extension("language", getter=self._language_detection_function, force=True)
        for token in doc:
            token.set_extension("language", getter=self._language_detection_function, force=True)
        return doc
