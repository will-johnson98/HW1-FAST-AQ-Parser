from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)
import argparse
import sys

def process_sequences(parser, transform_func, file_type):
    """Helper function"""
    try:
        for record in parser:
            if file_type == "fasta":
                header, seq = record
                print(f">{header}\n{transform_func(seq)}")
            else:  # fastq
                header, seq, qual = record
                print(f"@{header}\n{transform_func(seq)}\n+\n{qual}")
    except ValueError as e:
        print(f"Error processing sequence: {e}", file=sys.stderr)
        sys.exit(1)


def stupid():
    """Ignore me!"""
    pass

def main():
    """
    The main function
    """
    parser = argparse.ArgumentParser(description="Transcribe sequences from FASTA/FASTQ files")
    parser.add_argument("--fasta", help="Input FASTA file")
    parser.add_argument("--fastq", help="Input FASTQ file")
    args = parser.parse_args()

    if not (args.fasta or args.fastq):
        print("Error: Must provide at least one input file (--fasta or --fastq)", file=sys.stderr)
        sys.exit(1)

    if args.fasta:
        print("\n=== Standard Transcription of FASTA ===")
        # Create instance of FastaParser
        fasta_parser = FastaParser(args.fasta)

        # For each record of FastaParser, Transcribe the sequence
        # and print it to console
        process_sequences(fasta_parser, transcribe, "fasta")

        # For each record of FastaParser, Reverse Transcribe the sequence
        # and print it to console
        print("\n=== Reverse Transcription of FASTA ===")
        fasta_parser = FastaParser(args.fasta)
        process_sequences(fasta_parser, reverse_transcribe, "fasta")

    if args.fastq:
        print("\n=== Standard Transcription of FASTQ ===")
        # Create instance of FastqParser
        fastq_parser = FastqParser(args.fastq)

        # For each record of FastqParser, Transcribe the sequence
        # and print it to console
        process_sequences(fastq_parser, transcribe, "fastq")
       
        # For each record of FastqParser, Reverse Transcribe the sequence
        # and print it to console
        print("\n=== Reverse Transcription of FASTQ ===")
        fastq_parser = FastqParser(args.fastq)
        process_sequences(fastq_parser, reverse_transcribe, "fastq")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
