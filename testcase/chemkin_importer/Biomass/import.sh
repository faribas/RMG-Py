#!/bin/bash
# Run under a profiler
# Serve on Port 8081

python -m cProfile -o importChemkin.profile $RMGpy/importChemkin.py  --species SpRxn.dat --reactions SpRxn.dat --thermo Thermo.dat --known SMILES.txt  --port 8082
gprof2dot -f pstats  importChemkin.profile | dot -Tpdf -o importChemkin.profile.pdf