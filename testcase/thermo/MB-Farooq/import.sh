#!/bin/bash
# Run under a profiler

python -m cProfile -o convertThermo.profile $RMGpy/convertThermo.py  --species mmc1.txt --reactions mmc1.txt --thermo mmc2.txt --known SMILES.txt
gprof2dot -f pstats  convertThermo.profile | dot -Tpdf -o convertThermo.profile.pdf