
import sys
#from Bio.SeqUtils import GC
# GC no longer exists 
# editing script to use latest biopython (1.83)
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO

fastafile=sys.argv[1]
ID=sys.argv[2]

#read fasta file
allseq=[i for i in SeqIO.parse(fastafile,'fasta')]

#extract sequence with the RagTag label
reordered=[i for i in allseq if 'RagTag' in i.id and ID in i.id][0]

reordered.id='P7741'
reordered.name=''
reordered.description=''
#gc=reordered.seq.count('G')+ reordered.seq.count('C')
#gc_percent=GC(reordered.seq) 
gci = gc_fraction(reordered.seq, "ignore") * 100
print('GC Percent, opt=ignore: %04f'%gci)
gcr = gc_fraction(reordered.seq, "remove") * 100
print('GC Percent, opt=ignore: %04f'%gcr)
gcw = gc_fraction(reordered.seq, "weighted") * 100
print('GC Percent, opt=weighted: %04f'%gcw)

sequence_length=len(reordered.seq)

print('Sequence Length: %d bp'%sequence_length)

SeqIO.write(reordered,'P7741.reordered.fasta','fasta')
 

print('draft genome sequence extracted')


