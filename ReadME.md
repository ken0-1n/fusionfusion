# fusionfusion 

## Introduction

fusionfusion is a software for detecting gene fusion 
using the putative chimeric transcript generated by several well-known transcriptome alignment tools (STAR, MapSplice2 and TopHat2).
Many of those predicted chimeric transcripts are "false positives".
However, by performing effective filtering, sensitive and accurate gene fusion detection is possible.
After the alignment steps, the software can generate final gene fusion candidates
and integrating our software into the pipeline will come very easily to you!

## Dependency

### Python
Python (>= 2.7), `pysam (>= 0.8.1)`and [`annot_utils`](https://github.com/friend1ws/annot_utils) packages.

### Software
blat

## Install

First, download the latest release from the release section or type the following command
```
wget https://github.com/Genomon-Project/fusionfusion/archive/v0.3.0rc1.tar.gz
tar zxvf v0.3.0rc1.tar.gz
```

Alternatively, you can download the latest developing version (which may be unstable)
```
git clone https://github.com/Genomon-Project/fusionfusion.git
```

Then, install the package by standard python package protocol (https://docs.python.org/2/install/)
```
cd fusionfusion-0.3.0rc1
python setup.py build
python setup.py install
```

For the last command, you may need to add --user if you are using a shared computing cluster.
```
python setup.py install --user
```

## Preparation

First, you need to perform transcriptome sequencing alignemnt by STAR, MapSplice2, TopHat2. 

For STAR, our software uses the chimeric sam file
```
{output_prefix}.Chimeric.out.sam
```

For MapSplice2, our software uses the read alignment file
```
alignments.sam (bam)
```
You do not need to care about the sorting status.

For TopHat2, our software uses the read alignment file
```
accepted_hits.bam
```

## Commands

```
fusionfusion [-h] [--version] [--star star.Chimeric.out.sam]
                  [--ms2 ms2.bam] [--th2 th2.bam] --out output_dir
                  --reference_genome reference.fa [--grc]
                  [--genome_id {hg19,hg38,mm10}]
                  [--pooled_control_file POOLED_CONTROL_FILE] [--debug]
                  [--debug] [--abnormal_insert_size ABNORMAL_INSERT_SIZE]
                  [--min_major_clipping_size MIN_MAJOR_CLIPPING_SIZE]
                  [--min_read_pair_num MIN_READ_PAIR_NUM]
                  [--min_valid_read_pair_ratio MIN_VALID_READ_PAIR_RATIO]
                  [--min_cover_size MIN_COVER_SIZE]
                  [--anchor_size_thres ANCHOR_SIZE_THRES]
                  [--min_chimeric_size MIN_CHIMERIC_SIZE]
                  [--min_allowed_contig_match_diff MIN_ALLOWED_CONTIG_MATCH_DIFF]
                  [--check_contig_size_other_breakpoint CHECK_CONTIG_SIZE_OTHER_BREAKPOINT]
                  [--filter_same_gene]
```
At least one of --star, --ms2, --th2 arguments should be specified.
The arguments of --out and --reference_genome are mandatory. 
Set the genome model by --genome_id (default is hg19).
Currently, we support hg19, hg38 and mm10.
Also, if you are using GRC-based files (no "chr" in chromosome names), set --grc.
For other arguments, please type `fusionfusion -h`.
Although we believe default settings are fine for 100bp-length paired read data., 
tuning *min_cover_size* may help improve the accuracy.
Also, using pooled control files generated by the merge_control command of [chimera_utils](https://github.com/friend1ws/chimera_utils)
will greatly reduce false positives.

## Results

For the result generated by single tool (star.fusion.result.txt, ms2.fusion.result.txt and th2.fusion.result.txt):

1. chromosome for the 1st breakpoint
1. coordinate for the 1st breakpoint
1. direction of the 1st breakpoint
1. chromosome for the 2nd breakpoint
1. coordinate for the 2nd breakpoint
1. direction of the 2nd breakpoint
1. inserted nucleotides within the breakpoints
1. #read_pairs supporting the fusion
1. gene overlapping the 1st breakpoint
1. exon-intron junction overlapping the 1st breakpoint
1. gene overlapping the 2nd breakpoint
1. exon-intron junction overlapping the 2nd breakpoint
1. contig match score for the 1st breakpoint
1. contig size for the 1st breakpoint
1. contig match score for the 2nd breakpoint
1. conting size for the 2nd breakpoint

For the merged result (fusionfusion.result.txt):

1. chromosome for the 1st breakpoint
1. coordinate for the 1st breakpoint
1. direction of the 1st breakpoint
1. chromosome for the 2nd breakpoint
1. coordinate for the 2nd breakpoint
1. direction of the 2nd breakpoint 
1. inserted nucleotides within the breakpoints 
1. gene overlapping the 1st breakpoint
1. exon-intron junction overlapping the 1st breakpoint
1. gene overlapping the 2nd breakpoint
1. exon-intron junction overlapping the 2nd breakpoint
1. #read_pairs supporting the variant (by MapSplice2 if --ms2 is specified)
1. #read_pairs supporting the variant (by STAR if --star is specified)
1. #read_pairs supporting the variant (by TopHat2 if --th2 is specified)

