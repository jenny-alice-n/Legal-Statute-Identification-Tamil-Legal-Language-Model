import spacy
nlp = spacy.load(r"en_legal_ner_trf")
doc = nlp(text = """
Writ Petition No. 1234 of 2022 was filed by Ramesh Sharma against the Central Bureau of Investigation.
"""
)
for ent in doc.ents:
    print(ent.text, ent.label_)