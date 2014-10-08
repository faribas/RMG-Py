species(
    label = 'C11H3J(22137)',
    E0 = (1179.54,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,808.597,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,805.484,180,180,180,180,180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(5.95229e-10,'m'), epsilon=(3.86134,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([171.418,211.669,229.158,259.617,281.207,294.261,314.972],'J/(mol*K)'), H298=(1.17954e+06,'J/mol'), S298=(285.446,'J/(mol*K)'), Cp0=(171.418,'J/(mol*K)'), CpInf=(314.972,'J/(mol*K)')),
)

species(
    label = 'C4(10323)',
    E0 = (681.917,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([741.399,742.519,741.673,742.239,742.088,742.002],'cm^-1')),
    ],
    spinMultiplicity = 8,
    opticalIsomers = 1,
    molecularWeight = (48,'amu'),
    collisionModel = LennardJones(sigma=(4.16179e-10,'m'), epsilon=(2.18325,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([45.9822,57.3626,65.5214,72.6342,80.8349,86.2741,92.5919],'J/(mol*K)'), H298=(681917,'J/mol'), S298=(207.769,'J/(mol*K)'), Cp0=(45.9822,'J/(mol*K)'), CpInf=(92.5919,'J/(mol*K)')),
)

species(
    label = 'C7H3J(20683)',
    E0 = (769.678,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([750,770,3400,2100,2137.5,2175,2212.5,2250,500,512.5,525,537.5,550,3000,3100,440,815,1455,212.536,212.45,211.998],'cm^-1')),
        HinderedRotor(inertia=(1.42652e-44,'kg*m^2'), symmetry=1, barrier=(38604.7,'J/mol'), semiclassical=False),
        HinderedRotor(inertia=(3.96806e-46,'kg*m^2'), symmetry=1, barrier=(38658.3,'J/mol'), semiclassical=False),
        HinderedRotor(inertia=(3.96806e-46,'kg*m^2'), symmetry=1, barrier=(38658.3,'J/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (87,'amu'),
    collisionModel = LennardJones(sigma=(5.43166e-10,'m'), epsilon=(3.74974,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([116.817,135.478,149.536,160.498,177.36,189.368,208.154],'J/(mol*K)'), H298=(769678,'J/mol'), S298=(347.567,'J/(mol*K)'), Cp0=(116.817,'J/(mol*K)'), CpInf=(208.154,'J/(mol*K)')),
)

species(
    label = 'C4(10322)',
    E0 = (428.39,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([509.435,508.774,509.083,509.403,509.798,509.603],'cm^-1')),
    ],
    spinMultiplicity = 4,
    opticalIsomers = 1,
    molecularWeight = (48,'amu'),
    collisionModel = LennardJones(sigma=(4.16179e-10,'m'), epsilon=(2.18325,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([59.2454,67.9482,73.6384,77.655,83.68,87.5293,93.2195],'J/(mol*K)'), H298=(428390,'J/mol'), S298=(86.8448,'J/(mol*K)'), Cp0=(59.2454,'J/(mol*K)'), CpInf=(93.2195,'J/(mol*K)')),
)

species(
    label = 'C4JJ(10324)',
    E0 = (768.766,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([542.781,542.9,542.382,543.609,542.008,543.079],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (48,'amu'),
    collisionModel = LennardJones(sigma=(4.45856e-10,'m'), epsilon=(2.57799,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([55.9819,67.9482,69.5381,82.1738,86.6088,88.5334,92.2154],'J/(mol*K)'), H298=(768766,'J/mol'), S298=(116.538,'J/(mol*K)'), Cp0=(55.9819,'J/(mol*K)'), CpInf=(92.2154,'J/(mol*K)')),
)

species(
    label = 'C7H2JJ(24851)',
    E0 = (885.817,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,716.288,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251,710.251],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (86,'amu'),
    collisionModel = LennardJones(sigma=(5.24069e-10,'m'), epsilon=(3.21144,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([98.4914,125.269,135.436,161.168,177.527,187.025,201.92],'J/(mol*K)'), H298=(885817,'J/mol'), S298=(204.289,'J/(mol*K)'), Cp0=(98.4914,'J/(mol*K)'), CpInf=(201.92,'J/(mol*K)')),
)

species(
    label = 'C4HJ(3161)',
    E0 = (776.713,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([750,770,3400,2100,2250,500,550,180,180],'cm^-1')),
        HinderedRotor(inertia=(3.40851e-44,'kg*m^2'), symmetry=1, barrier=(59034.6,'J/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (49,'amu'),
    collisionModel = LennardJones(sigma=(5.18e-10,'m'), epsilon=(2.9683,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([71.6719,77.5714,81.6298,84.6842,89.8305,93.7634,104.056],'J/(mol*K)'), H298=(776713,'J/mol'), S298=(264.66,'J/(mol*K)'), Cp0=(71.6719,'J/(mol*K)'), CpInf=(104.056,'J/(mol*K)')),
)

species(
    label = 'C9H2JJ(24852)',
    E0 = (1302.54,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,180,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,679.235,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (110,'amu'),
    collisionModel = LennardJones(sigma=(5.53261e-10,'m'), epsilon=(3.35301,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([139.662,171.167,182.841,209.158,224.848,233.886,251.751],'J/(mol*K)'), H298=(1.30254e+06,'J/mol'), S298=(245.09,'J/(mol*K)'), Cp0=(139.662,'J/(mol*K)'), CpInf=(251.751,'J/(mol*K)')),
)

species(
    label = 'C2H(33)',
    E0 = (573.73,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([750,770,3400,480.899],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (25,'amu'),
    collisionModel = LennardJones(sigma=(4.1e-10,'m'), epsilon=(1.73774,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([43.2626,44.5178,45.5638,46.6516,48.9528,51.1285,55.2706],'J/(mol*K)'), H298=(573730,'J/mol'), S298=(216.018,'J/(mol*K)'), Cp0=(43.2626,'J/(mol*K)'), CpInf=(55.2706,'J/(mol*K)')),
)

species(
    label = 'C11H2JJ(24853)',
    E0 = (1516.73,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,803.256,180,180,180,180,180,180,180,180,180,180,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512,805.512],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (134,'amu'),
    collisionModel = LennardJones(sigma=(5.87775e-10,'m'), epsilon=(3.83017,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([169.285,205.142,219.66,247.986,266.688,277.65,298.361],'J/(mol*K)'), H298=(1.51673e+06,'J/mol'), S298=(294.274,'J/(mol*K)'), Cp0=(169.285,'J/(mol*K)'), CpInf=(298.361,'J/(mol*K)')),
)

species(
    label = 'H(5)',
    E0 = (217.961,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (1,'amu'),
    collisionModel = LennardJones(sigma=(2.05e-10,'m'), epsilon=(1.20561,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([20.7526,20.7526,20.7526,20.7526,20.7526,20.7526,20.7526],'J/(mol*K)'), H298=(217961,'J/mol'), S298=(114.452,'J/(mol*K)'), Cp0=(20.7526,'J/(mol*K)'), CpInf=(20.7526,'J/(mol*K)')),
)

species(
    label = 'C11H2JJ(24854)',
    E0 = (1333.91,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,180,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,723.446,180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (134,'amu'),
    collisionModel = LennardJones(sigma=(5.87775e-10,'m'), epsilon=(3.83017,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([169.536,207.275,222.296,250.622,268.738,279.198,299.909],'J/(mol*K)'), H298=(1.33391e+06,'J/mol'), S298=(290.844,'J/(mol*K)'), Cp0=(169.536,'J/(mol*K)'), CpInf=(299.909,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24855)',
    E0 = (1426.2,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,180,180,180,180,180,180,180,180,180,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886,924.886],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(5.95229e-10,'m'), epsilon=(3.86134,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([154.222,190.372,214.304,239.408,267.86,285.851,316.645],'J/(mol*K)'), H298=(1.4262e+06,'J/mol'), S298=(403.515,'J/(mol*K)'), Cp0=(154.222,'J/(mol*K)'), CpInf=(316.645,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24856)',
    E0 = (1095.86,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,180,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,731.834,180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(5.95229e-10,'m'), epsilon=(3.86134,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([170.958,212.338,230.413,261.165,282.713,295.558,319.825],'J/(mol*K)'), H298=(1.09586e+06,'J/mol'), S298=(283.271,'J/(mol*K)'), Cp0=(170.958,'J/(mol*K)'), CpInf=(319.825,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24857)',
    E0 = (1278.69,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,180,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,807.21,180,180,180,180,180,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(5.95229e-10,'m'), epsilon=(3.86134,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([170.707,210.204,227.777,258.529,280.663,294.01,318.277],'J/(mol*K)'), H298=(1.27869e+06,'J/mol'), S298=(286.701,'J/(mol*K)'), Cp0=(170.707,'J/(mol*K)'), CpInf=(318.277,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24858)',
    E0 = (999.438,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,736.654,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521,737.521],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(6.10966e-10,'m'), epsilon=(3.58176,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([129.913,168.741,200.748,232.923,280.412,307.273,350.452],'J/(mol*K)'), H298=(999438,'J/mol'), S298=(175.469,'J/(mol*K)'), Cp0=(129.913,'J/(mol*K)'), CpInf=(350.452,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24859)',
    E0 = (1175.98,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,721.896,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204,722.204],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(5.97222e-10,'m'), epsilon=(3.27275,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([141.503,185.184,211.627,245.099,278.236,297.692,328.026],'J/(mol*K)'), H298=(1.17598e+06,'J/mol'), S298=(236.848,'J/(mol*K)'), Cp0=(141.503,'J/(mol*K)'), CpInf=(328.026,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24860)',
    E0 = (1083.11,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,722.457,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975,720.975],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(6.10966e-10,'m'), epsilon=(3.58176,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([140.415,183.929,210.455,244.136,277.567,297.231,331.917],'J/(mol*K)'), H298=(1.08311e+06,'J/mol'), S298=(236.43,'J/(mol*K)'), Cp0=(140.415,'J/(mol*K)'), CpInf=(331.917,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24861)',
    E0 = (1236.85,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,180,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,745.41,180,180,180],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(6.21296e-10,'m'), epsilon=(3.70823,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([157.741,192.385,216.593,243.019,275.14,293.817,329.59],'J/(mol*K)'), H298=(1.23685e+06,'J/mol'), S298=(225.328,'J/(mol*K)'), Cp0=(157.741,'J/(mol*K)'), CpInf=(329.59,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24862)',
    E0 = (1040.77,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,577.707,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917,575.917],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(5.97222e-10,'m'), epsilon=(3.27275,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([166.314,215.769,235.476,272.964,295.641,308.235,327.649],'J/(mol*K)'), H298=(1.04077e+06,'J/mol'), S298=(124.298,'J/(mol*K)'), Cp0=(166.314,'J/(mol*K)'), CpInf=(327.649,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24863)',
    E0 = (1030.02,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2950,3150,900,1000,1100,634.731,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155,637.155],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(6.06029e-10,'m'), epsilon=(3.36535,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([162.716,198.531,223.091,250.663,283.717,303.173,337.858],'J/(mol*K)'), H298=(1.03002e+06,'J/mol'), S298=(159.189,'J/(mol*K)'), Cp0=(162.716,'J/(mol*K)'), CpInf=(337.858,'J/(mol*K)')),
)

species(
    label = 'C11H3J(24864)',
    E0 = (1432.98,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2950,3100,1380,975,1025,750,770,3400,540,610,2055,2100,2130,2160,2190,2220,2250,500,510,520,530,540,550,210.807,210.807,210.807,210.807,210.807,210.807,210.807,210.807,210.807],'cm^-1')),
        HinderedRotor(inertia=(4.00607e-46,'kg*m^2'), symmetry=1, barrier=(39028.6,'J/mol'), semiclassical=False),
        HinderedRotor(inertia=(4.00607e-46,'kg*m^2'), symmetry=1, barrier=(39028.6,'J/mol'), semiclassical=False),
        HinderedRotor(inertia=(4.00607e-46,'kg*m^2'), symmetry=1, barrier=(39028.6,'J/mol'), semiclassical=False),
        HinderedRotor(inertia=(4.00607e-46,'kg*m^2'), symmetry=1, barrier=(39028.6,'J/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (135,'amu'),
    collisionModel = LennardJones(sigma=(6.04981e-10,'m'), epsilon=(4.39062,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([173.971,205.393,221.459,245.977,267.776,281.918,307.608],'J/(mol*K)'), H298=(1.43298e+06,'J/mol'), S298=(451.699,'J/(mol*K)'), Cp0=(173.971,'J/(mol*K)'), CpInf=(307.608,'J/(mol*K)')),
)

species(
    label = 'bath_gas',
    molecularWeight = (39.95,'amu'),
    collisionModel = LennardJones(sigma=(3.418e-10,'m'), epsilon=(1.03126,'kJ/mol')),
    energyTransferModel = SingleExponentialDown(alpha0=(1794.32,'J/mol'), T0=(300,'K'), n=0.85),
)

transitionState(
    label = 'TS1',
    E0 = (1473.31,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (1219.78,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (1538.44,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (1662.53,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (1876.27,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (1734.69,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (1555.97,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (1570.53,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (1323.86,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (1423.01,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (1293.26,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS12',
    E0 = (1293.26,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS13',
    E0 = (1293.26,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS14',
    E0 = (1293.26,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS15',
    E0 = (1293.26,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS16',
    E0 = (1308.47,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS17',
    E0 = (1561.91,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['C4(10323)', 'C7H3J(20683)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(307726,'m^3/(mol*s)'), n=0.536758, Ea=(21.7113,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction2',
    reactants = ['C4(10322)', 'C7H3J(20683)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(153863,'m^3/(mol*s)'), n=0.536758, Ea=(21.7113,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction3',
    reactants = ['C4JJ(10324)', 'C7H3J(20683)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction4',
    reactants = ['C7H2JJ(24851)', 'C4HJ(3161)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction5',
    reactants = ['C9H2JJ(24852)', 'C2H(33)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction6',
    reactants = ['C11H2JJ(24853)', 'H(5)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(1.81e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction7',
    reactants = ['C11H2JJ(24854)', 'H(5)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(5.36e+08,'m^3/(mol*s)'), n=0, Ea=(4.10032,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction8',
    reactants = ['C11H3J(24855)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(1.01392e+08,'s^-1'), n=1.22367, Ea=(144.326,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction9',
    reactants = ['C11H3J(22137)'],
    products = ['C11H3J(24856)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(2.02783e+08,'s^-1'), n=1.22367, Ea=(144.326,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction10',
    reactants = ['C11H3J(24857)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(1.01392e+08,'s^-1'), n=1.22367, Ea=(144.326,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction11',
    reactants = ['C11H3J(22137)'],
    products = ['C11H3J(24858)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(1.61704e+10,'s^-1'), n=0.1195, Ea=(113.72,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction12',
    reactants = ['C11H3J(22137)'],
    products = ['C11H3J(24859)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(1.61704e+10,'s^-1'), n=0.1195, Ea=(113.72,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction13',
    reactants = ['C11H3J(22137)'],
    products = ['C11H3J(24860)'],
    transitionState = 'TS13',
    kinetics = Arrhenius(A=(3.23408e+10,'s^-1'), n=0.1195, Ea=(113.72,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction14',
    reactants = ['C11H3J(22137)'],
    products = ['C11H3J(24861)'],
    transitionState = 'TS14',
    kinetics = Arrhenius(A=(1.61704e+10,'s^-1'), n=0.1195, Ea=(113.72,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction15',
    reactants = ['C11H3J(22137)'],
    products = ['C11H3J(24862)'],
    transitionState = 'TS15',
    kinetics = Arrhenius(A=(1.61704e+10,'s^-1'), n=0.1195, Ea=(113.72,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction16',
    reactants = ['C11H3J(22137)'],
    products = ['C11H3J(24863)'],
    transitionState = 'TS16',
    kinetics = Arrhenius(A=(4.06706e+08,'s^-1'), n=0.896, Ea=(128.939,'kJ/mol'), T0=(1,'K')),
)

reaction(
    label = 'reaction17',
    reactants = ['C11H3J(24864)'],
    products = ['C11H3J(22137)'],
    transitionState = 'TS17',
    kinetics = Arrhenius(A=(4.06706e+08,'s^-1'), n=0.896, Ea=(128.939,'kJ/mol'), T0=(1,'K')),
)

network(
    label = 'network',
    isomers = [
        'C11H3J(22137)',
    ],
    reactants = [
        ('C4(10323)', 'C7H3J(20683)'),
        ('C4(10322)', 'C7H3J(20683)'),
        ('C4JJ(10324)', 'C7H3J(20683)'),
        ('C7H2JJ(24851)', 'C4HJ(3161)'),
        ('C9H2JJ(24852)', 'C2H(33)'),
        ('C11H2JJ(24853)', 'H(5)'),
        ('C11H2JJ(24854)', 'H(5)'),
    ],
    bathGas = {
        'bath_gas': 1,
    },
)

pressureDependence(
    label = 'network',
    Tmin = (300,'K'),
    Tmax = (2200,'K'),
    Tcount = 8,
    Tlist = ([302.51,323.546,371.247,459.823,619.914,913.864,1434.46,2073.82],'K'),
    Pmin = (1000,'Pa'),
    Pmax = (1e+07,'Pa'),
    Pcount = 5,
    Plist = ([1252.82,6674.67,100000,1.4982e+06,7.98202e+06],'Pa'),
    maximumGrainSize = (4184,'J/mol'),
    minimumGrainCount = 251,
    method = 'modified strong collision',
    interpolationModel = ('chebyshev', 4, 4),
    activeKRotor = True,
    activeJRotor = True,
    rmgmode = True,
)

