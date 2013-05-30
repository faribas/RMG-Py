#!/bin/bash
# Run under a profiler
# Serve on Port 8081

python -m cProfile -o importChemkin.profile $RMGpy/importChemkin.py  --species mbmechrev.txt --reactions mbmechrev.txt --thermo mmmbthermo.txt --known SMILES.txt --port 8082
gprof2dot -f pstats  importChemkin.profile | dot -Tpdf -o importChemkin.profile.pdf