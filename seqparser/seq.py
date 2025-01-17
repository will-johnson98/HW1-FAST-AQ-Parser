# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def check_sequence(seq):
    if any(base not in ALLOWED_NUC for base in seq.upper()):
        raise ValueError("Invalid DNA sequence: contains non-nt characters.")


def dna_complement(seq):
    check_sequence(seq)
    complement = {'A':'T', 'a':'t',
                  'G':'C', 'g':'c',
                  'C':'G', 'c':'g',
                  'T':'A', 't':'a',
                  'N':'N', 'n':'n',
                  'U':'A', 'u':'a'}
    return "".join([complement[base] for base in seq])


def dna_reverse_complement(seq):
    seq = dna_complement(seq)
    return seq[::-1]


def rna_complement(seq):
    # check_sequence(seq)
    complement = {'A':'U', 'a':'u',
                  'G':'C', 'g':'c',
                  'C':'G', 'c':'g',
                  'U':'A', 'u':'a',
                  'N':'N', 'n':'n',
                  'T':'A', 't':'a'}
    return "".join([complement[base] for base in seq])


def rna_reverse_complement(seq):
    seq = rna_complement(seq)
    return seq[::-1]


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    check_sequence(seq)
    result = "".join([TRANSCRIPTION_MAPPING[base] for base in seq])

    if reverse:
        return result[::-1]
    else:
        return result


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    check_sequence(seq)
    return transcribe(seq, reverse = True)
