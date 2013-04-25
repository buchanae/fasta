from collections import namedtuple


Fasta = namedtuple('Fasta', 'header sequence')


def parse(stream):

    header = ''
    sequence = ''

    for line in stream:
        line = line.strip()

        if line.startswith('>'):
            if header:
                yield Fasta(header, sequence)

            header = line[1:].strip()
            sequence = ''
        else:
            sequence += line

    if header:
        yield Fasta(header, sequence)
