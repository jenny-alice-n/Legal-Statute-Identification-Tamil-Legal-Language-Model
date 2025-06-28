---
tags:
- spacy
- token-classification
widget:
- text: >-
    Section 319 Cr.P.C. contemplates a situation where the evidence adduced by
    the prosecution for Respondent No.3-G. Sambiah on 20th June 1984
- text: |
    In The High Court Of Kerala At Ernakulam

    Crl Mc No. 1622 of 2006()


    1. T.R.Ajayan, S/O. O.Raman,
                          ...  Petitioner

                            Vs



    1. M.Ravindran,
                           ...       Respondent

    2. Mrs. Nirmala Dinesh, W/O. Dinesh,

                    For Petitioner  :Sri.A.Kumar

                    For Respondent  :Smt.M.K.Pushpalatha

    The Hon'ble Mr. Justice P.R.Raman
    The Hon'ble Mr. Justice V.K.Mohanan

     Dated :07/01/2008

     O R D E R
language:
- en
license: apache-2.0
model-index:
- name: en_legal_ner_trf
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: F1-Score
      value: 91.076
      name: Test F1-Score
datasets:
- opennyaiorg/InLegalNER
---
# Paper details
[Named Entity Recognition in Indian court judgments](https://aclanthology.org/2022.nllp-1.15/)
[Arxiv](https://arxiv.org/abs/2211.03442)

---
Indian Legal Named Entity Recognition(NER): Identifying relevant named entities in an Indian legal judgement using legal NER trained on [spacy](https://github.com/explosion/spaCy).

### Scores

| Type | Score |
| --- | --- |
| **F1-Score** | **91.076** |
| `Precision` | 91.979 |
| `Recall` | 90.19 |


| Feature | Description |
| --- | --- |
| **Name** | `en_legal_ner_trf` |
| **Version** | `3.2.0` |
| **spaCy** | `>=3.2.2,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [InLegalNER Train Data](https://storage.googleapis.com/indianlegalbert/OPEN_SOURCED_FILES/NER/NER_TRAIN.zip) [GitHub](https://github.com/Legal-NLP-EkStep/legal_NER)|
| **License** | `MIT` |
| **Author** | [Aman Tiwari](https://www.linkedin.com/in/amant555/) |

## Load Pretrained Model

Install the model using pip

```sh
pip install https://huggingface.co/opennyaiorg/en_legal_ner_trf/resolve/main/en_legal_ner_trf-any-py3-none-any.whl
```

Using pretrained NER model

```python
# Using spacy.load().
import spacy
nlp = spacy.load("en_legal_ner_trf")
text = "Section 319 Cr.P.C. contemplates a situation where the evidence adduced by the prosecution for Respondent No.3-G. Sambiah on 20th June 1984"
doc = nlp(text)

# Print indentified entites
for ent in doc.ents:
     print(ent,ent.label_)

##OUTPUT     
#Section 319 PROVISION
#Cr.P.C. STATUTE
#G. Sambiah RESPONDENT
#20th June 1984 DATE
```


### Label Scheme

<details>

<summary>View label scheme (14 labels for 1 components)</summary>

| ENTITY | BELONGS TO |
| --- | --- |
| `LAWYER` | PREAMBLE |
| `COURT` | PREAMBLE, JUDGEMENT |
| `JUDGE` | PREAMBLE, JUDGEMENT |
| `PETITIONER` | PREAMBLE, JUDGEMENT |
| `RESPONDENT` | PREAMBLE, JUDGEMENT |
| `CASE_NUMBER` | JUDGEMENT | 
| `GPE` | JUDGEMENT |
| `DATE` | JUDGEMENT |
| `ORG` | JUDGEMENT |
| `STATUTE` | JUDGEMENT |
| `WITNESS` | JUDGEMENT |
| `PRECEDENT` | JUDGEMENT |
| `PROVISION` | JUDGEMENT |
| `OTHER_PERSON` | JUDGEMENT |

</details>

## Author - Publication

```
@inproceedings{kalamkar-etal-2022-named,
    title = "Named Entity Recognition in {I}ndian court judgments",
    author = "Kalamkar, Prathamesh  and
      Agarwal, Astha  and
      Tiwari, Aman  and
      Gupta, Smita  and
      Karn, Saurabh  and
      Raghavan, Vivek",
    booktitle = "Proceedings of the Natural Legal Language Processing Workshop 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.nllp-1.15",
    doi = "10.18653/v1/2022.nllp-1.15",
    pages = "184--193",
    abstract = "Identification of named entities from legal texts is an essential building block for developing other legal Artificial Intelligence applications. Named Entities in legal texts are slightly different and more fine-grained than commonly used named entities like Person, Organization, Location etc. In this paper, we introduce a new corpus of 46545 annotated legal named entities mapped to 14 legal entity types. The Baseline model for extracting legal named entities from judgment text is also developed.",
}
```