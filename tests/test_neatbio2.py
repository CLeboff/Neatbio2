from neatbio2 import __version__
import neatbio2 as nt
from neatbio2.sequtils import gc_content,at_content

def test_version():
	assert __version__ == '0.1.0'

def test_issequence():
	seq1 = nt.Sequence('ATGCTATGCTT')
	assert isinstance(seq1,type(seq1))

def test_complement():
	seq1 = nt.Sequence('ATGCTATGCTT')
	res_complement = seq1.complement()
	assert res_complement == 'TACGATACGAA'

def test_reverse_complement():
	seq1 = nt.Sequence('ATGCTATGCTT')
	res_complement = seq1.reverse_complement()
	assert res_complement == 'AAGCATAGCAT'

def test_translate():
	seq1 = nt.Sequence('ATGCTATGCTT')
	result = seq1.translate()
	assert result == 'MLC'

def test_transcription():
	seq1 = nt.Sequence('ATGCTATGCTT')
	result = seq1.transcribe()
	assert result == 'AUGCUAUGCUU'

def test_nucleotide_freq():
	seq1 = nt.Sequence('ATGCTATGCTT')
	result = seq1.get_symbol_frequency()
	assert result =={'A': 2,'T': 5,'C': 2,'G': 2,'a': 0,'t': 0,'c': 0,'g': 0}

def test_gc_content():
	seq1 = nt.Sequence('ATGCTATGCTT')
	result = gc_content(seq1)
	assert result == 36.36363636363637
