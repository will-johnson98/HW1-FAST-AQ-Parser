# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest

FASTA_FILE = "data/test.fa"
FASTQ_FILE = "data/test.fq"

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    parser = FastaParser(FASTA_FILE)
    
    records = list(parser)
    assert len(records) == 2
    assert records[0] == ("seq1", "ACGT")
    assert records[1] == ("seq2", "TGCA")
    

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    parser = FastaParser(FASTQ_FILE)
    
    with pytest.raises(ValueError):
        list(parser)

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    parser = FastqParser(FASTQ_FILE)
    
    records = list(parser)
    assert len(records) == 2
    assert records[0] == ("seq1", "ACGT", "IIII")
    assert records[1] == ("seq2", "TGCA", "HHHH")

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    parser = FastqParser(FASTA_FILE)
    
    with pytest.raises(ValueError):
        list(parser)