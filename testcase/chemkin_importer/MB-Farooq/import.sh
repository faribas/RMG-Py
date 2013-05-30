#!/bin/bash
# Run under a profiler

python -m cProfile -o importChemkin.profile $RMGpy/importChemkin.py  --species mmc1.txt --reactions mmc1.txt --thermo mmc2.txt --known SMILES.txt
gprof2dot -f pstats  importChemkin.profile | dot -Tpdf -o importChemkin.profile.pdf