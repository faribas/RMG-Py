species(
    label = '[CH2]CC(=O)OC(71)',
    structure = SMILES('[CH2]CC(=O)OC'),
    E0 = (-246.658,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,2750,2850,1437.5,1250,1305,750,350,3000,3100,440,815,1455,1000,425,2750,2800,2850,1350,1500,750,1050,1375,1000,180,1058.84],'cm^-1')),
        HinderedRotor(inertia=(0.128701,'amu*angstrom^2'), symmetry=1, barrier=(2.95909,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.126412,'amu*angstrom^2'), symmetry=1, barrier=(2.90646,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.126627,'amu*angstrom^2'), symmetry=1, barrier=(2.91141,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.127811,'amu*angstrom^2'), symmetry=1, barrier=(2.93864,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (87.0972,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.64873,0.0566674,-6.71751e-05,5.66226e-08,-2.13497e-11,-29586.2,20.4831], Tmin=(100,'K'), Tmax=(716.096,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[4.49605,0.0369913,-1.80596e-05,3.54265e-09,-2.51032e-13,-29897.3,8.37246], Tmin=(716.096,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-246.658,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.053*R; Unweighted RMS error = 0.076*R; 
Thermo group additivity estimation: group(Cs-(Cds-Od)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-OsHHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-OdCsOs) + other(R) + group(Os-Cs(Cds-Od)) + gauche(Os(CsR)) + other(R) + group(Od-Cd) + other(R) + radical(RCCJ)"""),
)

species(
    label = 'COC1([O])CC1(153)',
    structure = SMILES('COC1([O])CC1'),
    E0 = (-79.0233,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (87.0972,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.86701,0.0349544,1.64987e-05,-4.37474e-08,1.83444e-11,-9416.97,19.2576], Tmin=(100,'K'), Tmax=(999.744,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[11.7828,0.0236542,-9.1169e-06,1.72155e-09,-1.24465e-13,-12817.5,-35.669], Tmin=(999.744,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-79.0233,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.079*R; Unweighted RMS error = 0.074*R; 
QM MopacMolPM3 calculation attempt 1 + radical(CsOJ)"""),
)

species(
    label = 'H(8)',
    structure = SMILES('[H]'),
    E0 = (211.805,'kJ/mol'),
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (1.00794,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,-2.06395e-14,3.16626e-17,-1.60855e-20,2.52789e-24,25474.2,-0.444973], Tmin=(100,'K'), Tmax=(3203.53,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[2.5,-8.60783e-12,3.51727e-15,-6.30075e-19,4.17513e-23,25474.2,-0.444973], Tmin=(3203.53,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(211.805,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.000*R; Unweighted RMS error = 0.000*R; 
primaryThermoLibrary"""),
)

species(
    label = 'C=CC(=O)OC(154)',
    structure = SMILES('C=CC(=O)OC'),
    E0 = (-328.688,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,2950,3100,1380,975,1025,1650,425,3010,987.5,1337.5,450,1655,2750,2800,2850,1350,1500,750,1050,1375,1000,180,180],'cm^-1')),
        HinderedRotor(inertia=(0.00109094,'amu*angstrom^2'), symmetry=1, barrier=(1.73552,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.876194,'amu*angstrom^2'), symmetry=1, barrier=(20.1454,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.715711,'amu*angstrom^2'), symmetry=1, barrier=(20.1457,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (86.0892,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.0779,0.0434394,-2.73742e-05,8.13748e-09,-9.80111e-13,-39464.7,19.336], Tmin=(100,'K'), Tmax=(1822.44,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[11.4093,0.0229582,-1.05167e-05,1.97081e-09,-1.34174e-13,-42865.9,-31.2833], Tmin=(1822.44,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-328.688,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.034*R; Unweighted RMS error = 0.030*R; 
Thermo group additivity estimation: group(Cs-OsHHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-Cds(Cds-Od)H) + gauche(CsOsCd) + other(R) + group(Cds-Od(Cds-Cds)Os) + other(R) + group(Cds-CdsHH) + gauche(CsOsCd) + other(R) + group(Os-Cs(Cds-Od)) + gauche(Os(CsR)) + other(R) + group(Od-Cd) + other(R)"""),
)

species(
    label = 'Mofml(29)',
    structure = SMILES('CO[C]=O'),
    E0 = (-171.184,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1855,455,950,425,2750,2800,2850,1350,1500,750,1050,1375,1000],'cm^-1')),
        HinderedRotor(inertia=(0.00273921,'amu*angstrom^2'), symmetry=1, barrier=(8.41939,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.34538,'amu*angstrom^2'), symmetry=1, barrier=(30.933,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (59.044,'amu'),
    collisionModel = LennardJones(sigma=(4.687e-10,'m'), epsilon=(4.41831,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.17385,0.0160845,-2.93048e-06,-3.33788e-09,1.28643e-12,-20557.3,12.7606], Tmin=(100,'K'), Tmax=(1366.1,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[6.09104,0.0131502,-5.86552e-06,1.0991e-09,-7.54102e-14,-21877.5,-4.13827], Tmin=(1366.1,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-171.184,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.021*R; Unweighted RMS error = 0.021*R; 
DFT_QCI_thermo"""),
)

species(
    label = 'C2H4(49)',
    structure = SMILES('C=C'),
    E0 = (41.9072,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2950,3000,3050,3100,1330,1430,900,1050,1000,1050,1600,1700],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (28.0532,'amu'),
    collisionModel = LennardJones(sigma=(4.443e-10,'m'), epsilon=(0.920412,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.98881,-0.00674768,5.04418e-05,-5.70772e-08,2.04958e-11,5047.05,3.80478], Tmin=(100,'K'), Tmax=(945.998,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[4.59008,0.00872748,-2.66508e-06,4.81746e-10,-3.6072e-14,4127.08,-3.32376], Tmin=(945.998,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(41.9072,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.036*R; Unweighted RMS error = 0.034*R; 
DFT_QCI_thermo"""),
)

species(
    label = 'CH3(19)',
    structure = SMILES('[CH3]'),
    E0 = (136.55,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([532.912,1391.06,1391.19,2779.19,3448.45,3448.48],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (15.0345,'amu'),
    collisionModel = LennardJones(sigma=(3.758e-10,'m'), epsilon=(1.23553,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.94801,0.000827588,8.34936e-06,-9.82641e-09,3.80107e-12,16425.4,0.336652], Tmin=(100,'K'), Tmax=(660.435,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[3.2217,0.00522646,-1.64125e-06,2.58224e-10,-1.62579e-14,16521.3,3.53938], Tmin=(660.435,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(136.55,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.003*R; Unweighted RMS error = 0.004*R; 
DFT_QCI_thermo"""),
)

species(
    label = '[CH2]CC([O])=O(155)',
    structure = SMILES('[CH2]CC([O])=O'),
    E0 = (-49.1847,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,2750,2850,1437.5,1250,1305,750,350,3000,3100,440,815,1455,1000,824.61,4000],'cm^-1')),
        HinderedRotor(inertia=(0.039003,'amu*angstrom^2'), symmetry=1, barrier=(2.68266,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0258675,'amu*angstrom^2'), symmetry=1, barrier=(12.4789,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (72.0627,'amu'),
    collisionModel = LennardJones(sigma=(5.784e-10,'m'), epsilon=(2.83607,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.81327,0.029584,-1.84173e-05,4.97687e-09,-5.22992e-13,-5876.85,14.4642], Tmin=(100,'K'), Tmax=(2114.44,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[11.4823,0.0131845,-6.7834e-06,1.30878e-09,-8.92985e-14,-9542.87,-33.8499], Tmin=(2114.44,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-49.1847,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.025*R; Unweighted RMS error = 0.017*R; 
Thermo group additivity estimation: group(Cs-(Cds-Od)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cds-OdCsOs) + other(R) + group(Os-(Cds-Od)H) + gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R) + radical(RCCJ) + radical(OJC=O)"""),
)

species(
    label = '[CH2]CC(=O)O[CH2](156)',
    structure = SMILES('[CH2]CC(=O)O[CH2]'),
    E0 = (-44.9537,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,2750,2850,1437.5,1250,1305,750,350,3000,3033.33,3066.67,3100,415,465,780,850,1435,1475,900,1100,425,180,1111.08],'cm^-1')),
        HinderedRotor(inertia=(0.0679921,'amu*angstrom^2'), symmetry=1, barrier=(1.56327,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0678965,'amu*angstrom^2'), symmetry=1, barrier=(1.56107,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0680014,'amu*angstrom^2'), symmetry=1, barrier=(1.56349,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.02757,'amu*angstrom^2'), symmetry=1, barrier=(23.6259,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (86.0892,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.45681,0.06146,-7.60908e-05,5.64055e-08,-1.7844e-11,-5320.12,20.8591], Tmin=(100,'K'), Tmax=(755.992,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[7.21108,0.0310122,-1.56746e-05,3.12504e-09,-2.23734e-13,-6190.11,-5.292], Tmin=(755.992,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-44.9537,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.052*R; Unweighted RMS error = 0.071*R; 
Thermo group additivity estimation: group(Cs-(Cds-Od)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-OsHHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-OdCsOs) + other(R) + group(Os-Cs(Cds-Od)) + gauche(Os(CsR)) + other(R) + group(Od-Cd) + other(R) + radical(RCCJ) + radical(CsJOC(O)C)"""),
)

species(
    label = 'CH3O(12)',
    structure = SMILES('C[O]'),
    E0 = (10.0502,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2800,2850,1350,1500,750,1050,1375,1000],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (31.0339,'amu'),
    collisionModel = LennardJones(sigma=(4.443e-10,'m'), epsilon=(0.920412,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.9532,-0.00381917,3.45421e-05,-3.89332e-08,1.37889e-11,1214.82,4.78508], Tmin=(100,'K'), Tmax=(959.551,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[4.2996,0.00731075,-2.51251e-06,4.67572e-10,-3.45462e-14,569.48,0.111873], Tmin=(959.551,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(10.0502,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.026*R; Unweighted RMS error = 0.026*R; 
DFT_QCI_thermo"""),
)

species(
    label = '[CH2]C[C]=O(157)',
    structure = SMILES('[CH2]C[C]=O'),
    E0 = (157.443,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1855,455,950,2750,2850,1437.5,1250,1305,750,350,3000,3100,440,815,1455,1000],'cm^-1')),
        HinderedRotor(inertia=(0.131485,'amu*angstrom^2'), symmetry=1, barrier=(3.0231,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.131569,'amu*angstrom^2'), symmetry=1, barrier=(3.02504,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (56.0633,'amu'),
    collisionModel = LennardJones(sigma=(4.687e-10,'m'), epsilon=(4.41831,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.52366,0.0206885,-9.55732e-06,1.25071e-09,2.0022e-14,18943.4,13.0535], Tmin=(100,'K'), Tmax=(2320.2,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[16.4234,0.0047709,-3.35335e-06,6.42359e-10,-4.09524e-14,11255.9,-63.704], Tmin=(2320.2,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(157.443,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.046*R; Unweighted RMS error = 0.026*R; 
Thermo group additivity estimation: group(Cs-(Cds-Od)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cds-OdCsH) + other(R) + group(Od-Cd) + other(R) + radical(RCCJ) + radical(CsCJ=O)"""),
)

species(
    label = '[CH2][CH]C(=O)OC(158)',
    structure = SMILES('[CH2][CH]C(=O)OC'),
    E0 = (-52.1162,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,3025,407.5,1350,352.5,3000,3100,440,815,1455,1000,425,2750,2800,2850,1350,1500,750,1050,1375,1000,1471.55,1472.95],'cm^-1')),
        HinderedRotor(inertia=(0.127204,'amu*angstrom^2'), symmetry=1, barrier=(2.92468,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.125719,'amu*angstrom^2'), symmetry=1, barrier=(2.89052,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.126613,'amu*angstrom^2'), symmetry=1, barrier=(2.91108,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.125721,'amu*angstrom^2'), symmetry=1, barrier=(2.89058,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (86.0892,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.757,0.0565283,-8.2857e-05,8.11082e-08,-3.22362e-11,-6194.39,22.6438], Tmin=(100,'K'), Tmax=(786.534,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[2.69692,0.0373858,-1.89595e-05,3.7323e-09,-2.62978e-13,-5897.98,21.1591], Tmin=(786.534,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-52.1162,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.048*R; Unweighted RMS error = 0.072*R; 
Thermo group additivity estimation: group(Cs-(Cds-Od)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-OsHHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-OdCsOs) + other(R) + group(Os-Cs(Cds-Od)) + gauche(Os(CsR)) + other(R) + group(Od-Cd) + other(R) + radical(Cs_S) + radical(RCCJ)"""),
)

species(
    label = '[CH2][CH2](140)',
    structure = SMILES('[CH2][CH2]'),
    E0 = (318.146,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3000,3100,440,815,1455,1000,180,994.926,995.805,2246.19,2948.63],'cm^-1')),
        HinderedRotor(inertia=(0.00722914,'amu*angstrom^2'), symmetry=1, barrier=(5.08388,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (28.0532,'amu'),
    collisionModel = LennardJones(sigma=(4.443e-10,'m'), epsilon=(0.920412,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.40736,0.0100312,6.40939e-06,-1.41292e-08,5.92678e-12,38288.2,6.11703], Tmin=(100,'K'), Tmax=(954.258,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[5.52248,0.00856174,-2.90744e-06,5.02355e-10,-3.44573e-14,37547.8,-5.75272], Tmin=(954.258,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(318.146,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.020*R; Unweighted RMS error = 0.018*R; 
DFT_QCI_thermo"""),
)

species(
    label = 'CO[C]1CCO1(159)',
    structure = SMILES('CO[C]1CCO1'),
    E0 = (-99.0499,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (87.0972,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.20778,0.0244094,4.56465e-05,-7.35886e-08,2.88037e-11,-11835,20.6492], Tmin=(100,'K'), Tmax=(982.934,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[11.7776,0.0226702,-8.47509e-06,1.62662e-09,-1.20609e-13,-15513.6,-34.4971], Tmin=(982.934,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-99.0499,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.091*R; Unweighted RMS error = 0.086*R; 
QM MopacMolPM3 calculation attempt 1 + radical(Cs_P)"""),
)

species(
    label = 'CH3OH(3)',
    structure = SMILES('CO'),
    E0 = (-212.697,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2800,2850,1350,1500,750,1050,1375,1000,2279.92,4000],'cm^-1')),
        HinderedRotor(inertia=(0.0159507,'amu*angstrom^2'), symmetry=1, barrier=(8.44782,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (32.0419,'amu'),
    collisionModel = LennardJones(sigma=(4.443e-10,'m'), epsilon=(0.920412,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.91002,-0.00131507,2.80669e-05,-2.98995e-08,9.9174e-12,-25575.4,5.89068], Tmin=(100,'K'), Tmax=(995.366,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[3.01639,0.011213,-4.28042e-06,7.85996e-10,-5.5259e-14,-25840.2,7.97394], Tmin=(995.366,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-212.697,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.023*R; Unweighted RMS error = 0.025*R; 
DFT_QCI_thermo"""),
)

species(
    label = '[CH2]C=C=O(160)',
    structure = SMILES('[CH2]C=C=O'),
    E0 = (83.3963,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3000,3100,440,815,1455,1000,3010,987.5,1337.5,450,1655,2120,512.5,787.5],'cm^-1')),
        HinderedRotor(inertia=(0.0619708,'amu*angstrom^2'), symmetry=1, barrier=(24.8487,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (55.0553,'amu'),
    collisionModel = LennardJones(sigma=(4.687e-10,'m'), epsilon=(4.41831,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.08335,0.0153203,6.54333e-06,-1.77545e-08,7.39411e-12,10067.5,11.895], Tmin=(100,'K'), Tmax=(1002.98,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[6.97832,0.0111886,-4.32955e-06,8.06766e-10,-5.75278e-14,8712.7,-9.76653], Tmin=(1002.98,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(83.3963,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.033*R; Unweighted RMS error = 0.031*R; 
DFT_QCI_thermo"""),
)

species(
    label = 'C[CH]C(=O)OC(161)',
    structure = SMILES('C[CH]C(=O)OC'),
    E0 = (-257.363,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (87.0972,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.24396,0.0393596,-1.97768e-05,3.95351e-09,-2.85945e-13,-30950.7,15.3867], Tmin=(100,'K'), Tmax=(3030.52,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[40.8511,-0.00593525,4.92799e-07,-3.25886e-11,3.87381e-15,-55739,-211.033], Tmin=(3030.52,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-257.363,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.121*R; Unweighted RMS error = 0.067*R; 
Thermo group additivity estimation: group(Cs-(Cds-Od)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-OsHHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-OdCsOs) + other(R) + group(Os-Cs(Cds-Od)) + gauche(Os(CsR)) + other(R) + group(Od-Cd) + other(R) + radical(Cs_S)"""),
)

species(
    label = '[CH2]OC(=O)CC(162)',
    structure = SMILES('[CH2]OC(=O)CC'),
    E0 = (-250.2,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,2750,2850,1437.5,1250,1305,750,350,425,2750,2800,2850,1350,1500,750,1050,1375,1000,3000,3100,440,815,1455,1000,1210,4000],'cm^-1')),
        HinderedRotor(inertia=(1.03303,'amu*angstrom^2'), symmetry=1, barrier=(23.7514,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.804321,'amu*angstrom^2'), symmetry=1, barrier=(18.4929,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.03282,'amu*angstrom^2'), symmetry=1, barrier=(23.7466,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.39561,'amu*angstrom^2'), symmetry=1, barrier=(9.09586,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (87.0972,'amu'),
    collisionModel = LennardJones(sigma=(5.949e-10,'m'), epsilon=(3.31997,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.57816,0.058788,-5.84964e-05,3.42209e-08,-8.78857e-12,-30009.6,18.6418], Tmin=(100,'K'), Tmax=(904.085,'K'), comment="""Low temperature range polynomial"""), NASAPolynomial(coeffs=[7.29229,0.0335071,-1.65528e-05,3.29245e-09,-2.36324e-13,-31042.8,-8.34953], Tmin=(904.085,'K'), Tmax=(5000,'K'), comment="""High temperature range polynomial""")], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-250.2,'kJ/mol'), comment="""NASA function fitted to Wilhoit function with B = 1000 K. Weighted RMS error = 0.062*R; Unweighted RMS error = 0.079*R; 
Thermo group additivity estimation: group(Cs-(Cds-Od)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-OsHHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-OdCsOs) + other(R) + group(Os-Cs(Cds-Od)) + gauche(Os(CsR)) + other(R) + group(Od-Cd) + other(R) + radical(CsJOC(O)C)"""),
)

species(
    label = 'N2(2)',
    structure = SMILES('N#N'),
    molecularWeight = (28.0135,'amu'),
    collisionModel = LennardJones(sigma=(4.443e-10,'m'), epsilon=(0.920412,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44485e-12,-1020.9,3.95037], Tmin=(298,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K'))], Tmin=(298,'K'), Tmax=(5000,'K'), E0=(-8.62478,'kJ/mol'), comment="""primaryThermoLibrary"""),
)

transitionState(
    label = 'TS1',
    E0 = (-79.0233,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (-98.892,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (-101.829,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (87.3654,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (166.851,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (167.493,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (159.689,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (146.963,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (-99.0499,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (39.7332,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (-129.925,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS12',
    E0 = (-200.996,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['[CH2]CC(=O)OC(71)'],
    products = ['COC1([O])CC1(153)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(1.61704e+10,'s^-1'), n=0.1195, Ea=(167.635,'kJ/mol'), T0=(1,'K'), comment="""Intra_R_Add_Exocyclic estimate: [R4_S_CO,carbonylbond_intra_Nd,radadd_intra_cs2H]
Ea raised from 164.9 to 167.6 kJ/mol to match endothermicity of reaction."""),
)

reaction(
    label = 'reaction2',
    reactants = ['H(8)', 'C=CC(=O)OC(154)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(2.85e+13,'cm^3/(mol*s)'), n=0, Ea=(17.9912,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""R_Addition_MultipleBond estimate: [Cd/H/De_Cd/H2,H_rad]"""),
)

reaction(
    label = 'reaction3',
    reactants = ['Mofml(29)', 'C2H4(49)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(1.04e+06,'m^3/(mol*s)'), n=0, Ea=(27.447,'kJ/mol'), T0=(1,'K'), comment="""R_Addition_MultipleBond estimate: [Cd/H2_Cd/H2,CO_rad/NonDe]"""),
)

reaction(
    label = 'reaction4',
    reactants = ['CH3(19)', '[CH2]CC([O])=O(155)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""R_Recombination estimate: [O_rad/OneDe,C_methyl]"""),
)

reaction(
    label = 'reaction5',
    reactants = ['H(8)', '[CH2]CC(=O)O[CH2](156)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""R_Recombination estimate: [C_rad/H2/O,H_rad]"""),
)

reaction(
    label = 'reaction6',
    reactants = ['CH3O(12)', '[CH2]C[C]=O(157)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""R_Recombination estimate: [CO_rad/NonDe,O_rad/NonDe]"""),
)

reaction(
    label = 'reaction7',
    reactants = ['H(8)', '[CH2][CH]C(=O)OC(158)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""R_Recombination estimate: [Y_rad,H_rad]"""),
)

reaction(
    label = 'reaction8',
    reactants = ['[CH2][CH2](140)', 'Mofml(29)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""R_Recombination estimate: [CO_rad/NonDe,Y_rad]"""),
)

reaction(
    label = 'reaction9',
    reactants = ['[CH2]CC(=O)OC(71)'],
    products = ['CO[C]1CCO1(159)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(4.06706e+08,'s^-1'), n=0.896, Ea=(147.608,'kJ/mol'), T0=(1,'K'), comment="""Intra_R_Add_Endocyclic estimate: [R4_S_CO,carbonyl_intra_Nd,radadd_intra_cs2H]
Ea raised from 143.4 to 147.6 kJ/mol to match endothermicity of reaction."""),
)

reaction(
    label = 'reaction10',
    reactants = ['CH3OH(3)', '[CH2]C=C=O(160)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(0.000227174,'m^3/(mol*s)'), n=2.96333, Ea=(169.034,'kJ/mol'), T0=(1,'K'), comment="""1,3_Insertion_ROR estimate: [Cd_Cdd,H_OCmethyl]"""),
)

reaction(
    label = 'reaction11',
    reactants = ['[CH2]CC(=O)OC(71)'],
    products = ['C[CH]C(=O)OC(161)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(2.82e+08,'s^-1'), n=1.28, Ea=(116.734,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""intra_H_migration estimate: [Others-R2H_S,C_rad_out_2H,Cs_H_out_H/OneDe]"""),
)

reaction(
    label = 'reaction12',
    reactants = ['[CH2]OC(=O)CC(162)'],
    products = ['[CH2]CC(=O)OC(71)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(1.284e+12,'s^-1'), n=-1.05, Ea=(49.2038,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""intra_H_migration estimate: [R5H_SSSS,C_rad_out_2H,Cs_H_out_2H]"""),
)

network(
    label = '53',
    isomers = [
        '[CH2]CC(=O)OC(71)',
    ],
    reactants = [
    ],
    bathGas = {
        'N2(2)': 1,
    },
)

pressureDependence(
    label = '53',
    Tmin = (300,'K'),
    Tmax = (2000,'K'),
    Tcount = 8,
    Tlist = ([302.47,323.145,369.86,455.987,609.649,885.262,1353.64,1896.74],'K'),
    Pmin = (0.01,'bar'),
    Pmax = (100,'bar'),
    Pcount = 5,
    Plist = ([0.0125282,0.0667467,1,14.982,79.8202],'bar'),
    maximumGrainSize = (1,'kcal/mol'),
    minimumGrainCount = 250,
    method = 'modified strong collision',
    interpolationModel = ('Chebyshev', 6, 4),
    activeKRotor = True,
    activeJRotor = True,
    rmgmode = True,
)

