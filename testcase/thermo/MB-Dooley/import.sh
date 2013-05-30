#!/bin/bash
# Run under a profiler

python -m cProfile -o convertThermo.profile $RMGpy/convertThermo.py  --species mb_cnf_08.dat --reactions mb_cnf_08.dat --thermo mb_cnf_08_thermo.dat --known SMILES.txt
gprof2dot -f pstats  convertThermo.profile | dot -Tpdf -o convertThermo.profile.pdf