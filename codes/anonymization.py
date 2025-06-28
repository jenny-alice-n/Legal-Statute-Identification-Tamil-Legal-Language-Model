import sys, time, logging, os, shutil
import re
import pickle as pkl
import pandas as pd
import numpy as np
import multiprocess as mp
from tqdm.notebook import tqdm_notebook
import requests, json
import bs4
from bs4 import BeautifulSoup
import spacy
import codecs
from tqdm import tqdm

spacy.prefer_gpu()
#spacy.require_gpu()

with open("indian_names.txt") as fr:
    indian_names = set(fr.read().strip().split('\n'))
    print("Loaded indian names:", len(indian_names))

    
try:
    nlp = spacy.load(r"C:\\Users\\jenny\\VS CODE\\legal-statute-identification\\en_legal_ner_trf")
    print("SpaCy model loaded successfully")
except Exception as e:
    print("Error loading model:", e)

files = [r"C:\Users\jenny\VS CODE\legal-statute-identification\ILSI\train.jsonl", r"C:\Users\jenny\VS CODE\legal-statute-identification\ILSI\dev.jsonl", r"C:\Users\jenny\VS CODE\legal-statute-identification\ILSI\test.jsonl"]


indian_names = [r'\b{}\b'.format(re.escape(i)) for i in indian_names] # match names only at word boundaries
match_string = '|'.join(indian_names)
vowels = set(['a', 'e', 'i', 'o', 'u'])

for f in files:
    print("Processing", f, "---")
    if not os.path.exists(f):
        print("File does not exist:", f)
    with open(f) as fr:
        D = {'data': [json.loads(line) for line in fr if line.strip()]}
    for i,doc in enumerate(tqdm(D['data'])):
        if i == 10:
            break
        text = []
        for sent in doc['text']:
            xsent = sent.lower()
            v = re.findall("a|e|i|o|u", xsent)
            if len(v) / len(xsent) < 0.2:
                continue
            psent = nlp(sent)
            fsent = psent.text
            for ent in psent.ents:
                if ent.label_ in ["PETITIONER", "RESPONDENT", "JUDGE", "LAWYER", "WITNESS", "OTHER_PERSON"]:
                    fsent = fsent.replace(ent.text, '[ENTITY]')
                elif ent.label_ == 'PROVISION':
                    fsent = fsent.replace(ent.text, '[SECTION]')
                elif ent.label_ == 'STATUTE':
                    fsent = fsent.replace(ent.text, '[ACT]')
                elif ent.label_ == 'PRECEDENT':
                    fsent = fsent.replace(ent.text, '[PRECEDENT]')
            fsent, nsub = re.subn(match_string, '[ENTITY]', fsent)
            text.append(fsent)
        doc['text'] = text
    print("Writing output to:", f.split('.')[0] + "2.json")
    with open(f.split('.')[0] + "2.json", 'w') as fw:
        json.dump(D, fw, indent=4)
    print("Finished processing, about to write file")

            
            
