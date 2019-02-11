# spacy_langdetect
Fully customizable language detection pipeline for [spaCy](https://github.com/explosion/spaCy)

## Basic Usage
Out of the box, under the hood it uses [langdetect](https://github.com/Mimino666/langdetect) to detect language of Doc and Span objects.

```python
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
