#!/bin/bash
# Run under a profiler
# Serve on Port 8081

python -m cProfile -o convertThermo.profile $RMGpy/convertThermo.py  --species mb_cnf_08.dat --reactions mb_cnf_08.dat --thermo mb_cnf_08_thermo.dat --known SMILES.txt --port 8081
gprof2dot -f pstats  convertThermo.profile | dot -Tpdf -o convertThermo.profile.pdf