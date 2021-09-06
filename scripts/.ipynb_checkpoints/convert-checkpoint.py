"""Convert textcat annotation from JSONL to spaCy v3 .spacy format."""
import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin


def convert(lang: str, input_path: Path, output_path: Path):
    #nlp = spacy.blank(lang)
    nlp = spacy.load("en_core_web_md")
    db = DocBin()
    for line in srsly.read_jsonl(input_path):
        doc = nlp.make_doc(line["text"])
        label = line["cats"]
        
        doc.cats["tech"] = 0
        doc.cats["sport"] = 0
        doc.cats["entertainment"] = 0
        
        if label == "tech":
            doc.cats["tech"] = 1
        elif label == "sport":
            doc.cats["sport"] = 1
        elif label == "entertainment":
            doc.cats["entertainment"] = 1

        db.add(doc)
    db.to_disk(output_path)


if __name__ == "__main__":
    typer.run(convert)
