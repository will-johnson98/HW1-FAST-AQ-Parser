# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # Test basic transcription
    assert transcribe("ACGT") == "UGCA"
    assert transcribe("AAAA") == "UUUU"
    
    # Test case sensitivity
    with pytest.raises(ValueError):
        transcribe("acgt")
    
    # Test invalid nucleotides
    with pytest.raises(ValueError):
        transcribe("ACGTN")
    
    with pytest.raises(ValueError):
        transcribe("ACGU")  # RNA nucleotide in DNA sequence
    
    # Test empty sequence
    assert transcribe("") == ""
    
    # Test longer sequence
    assert transcribe("ATGCATGC") == "UACGUACG"
    
    # Test homopolymer
    assert transcribe("TTTT") == "AAAA"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Test basic reverse transcription
    assert reverse_transcribe("ACGT") == "ACGU"
    assert reverse_transcribe("AAAA") == "UUUU"
    
    # Test case sensitivity
    with pytest.raises(ValueError):
        reverse_transcribe("acgt")
    
    # Test invalid nucleotides
    with pytest.raises(ValueError):
        reverse_transcribe("ACGTN")
    
    with pytest.raises(ValueError):
        reverse_transcribe("ACGU")  # RNA nucleotide in DNA sequence
    
    # Test empty sequence
    assert reverse_transcribe("") == ""
    
    # Test longer sequence
    assert reverse_transcribe("ATGCATGC") == "GCAUGCAU"
    
    # Test homopolymer
    assert reverse_transcribe("TTTT") == "AAAA"
    
    # Verify it's actually reversed
    result = reverse_transcribe("ATGC")
    assert result == "GCAU"  # Both transcribed and reversed