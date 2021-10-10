#!/usr/bin/env python3
#
# GlobalChem - Content Variable Store
#
# -----------------------------------


class GlobalChem(object):

    __version__ = "0.1.0"
    __allow_update__ = True

    """

    GlobalChem will be the master class of all variables, as the content store grows we can use this as the parent class.

    """
    
    def _get_common_regex_patterns(self):
                
        regex_patterns = {
            'mol2': '^@<\w+?>\w+?\n[COMPOUND_ID]\n(.|\n)*?@<TRIPOS>SUBSTRUCTURE\n.*?\n'
        }
        
        return regex_patterns

    def _get_amino_acids(self):

        amino_acid_side_chains = {
            "alanine": "C",  
            "arginine": "CCCCNC(N)=N",
            "asparagine": "CCC(N)=O",
            "aspartic acid": "CC(O)=O",
            "cysteine": "CS",
            "glutamic acid": "CCC(O)=O",
            "glutamine": "CCC(N)=O",
            "glycine": "[H]",
            "histidine": "CC1=CNC=N1",
            "isoleucine": "C(CC)([H])C",
            "leucine": "CC(C)C", 
            "lysine": "CCCCN",
            "methionine": "CCSC",
            "phenylalanine": "CC1=CC=CC=C1", 
            "proline": "C2CCCN2",
            "serine": "CO",
            "threonine": "C(C)([H])O",
            "tryptophan": "CCC1=CNC2=C1C=CC=C2",
            "tyrosine": "CC1=CC=C(O)C=C1",
            "valine": "C(C)C"
        }

        return amino_acid_side_chains
    
    def _get_iupac_blue_book_common_subsituents(self):
        
        radical_functional_groups = {
            'acetamido': 'O=C(N)C',
            'acetoacetyl': 'O=C(C)CC(=O)O',
            'acetyl': 'C(C)=O',
            'acryloyl': 'C=CC(C)=O',
            'alanyl': 'N[CH](C)C(C)=O',
            'beta-alanyl': 'NCCC(C)=O',
            'allyl': '[CH2]C=C',
            'allylidene': '[CH]C=C',
            'amidino': 'NC=N',
            'amino': 'N',
            'amyl': '[CH2]CCCC',
            'anilino': 'NC1=CC=CC=C1',
            'anisidino': 'NC1=CC=C(OC)C=C1',
            'anthranoyl': 'NC1=CC=CC=C1[C](C)=O',
            'arsino': '[AsH3]',
            'azelaoyl': 'O=CCCCCCCCC=O',
            'azido': '[N]=[N+]=[N-]',
            'azo': 'C/N=N/C',
            'azoxy': 'C/N=[N+]([O-])/C',
            'benzal': '[CH]C1=CC=CC=C1',
            'benzamido': 'O=C(N)C1=CC=CC=C1',
            'benzhydrol': 'OC(C1=CC=CC=C1)C2=CC=CC=C2',
            'benzoxy': '[O]CC1=CC=CC=C1',
            'benzoyl': 'O=[C]C1=CC=CC=C1',
            'benzyl': '[CH2]C1=CC=CC=C1',
            'benzylidene': '[CH]C1=CC=CC=C1',
            'benzylidyne': '[C]C1=CC=CC=C1',
            'biphenylyl': 'C1(C2=CC=CC=C2)=CC=CC=[C]1',
            'biphenylene': 'C12=C3C=CC=CC3=C1C=CC=C2',
            'butoxy': '[O]CCCC',
            'sec-butoxy': '[O]C(C)CC',
            'tert-butoxy': '[O]C(C)(C)C',
            'butyl': '[CH2]CCC',
            'sec-butyl': 'CC[CH]C',
            'tert-butyl': 'C[C](C)C',
            'butyryl': 'O=[C]CCC',
            'caproyl': 'CCCCC[C]=O',
            'capryl': 'CCCCCCCC',
            'capryloyl': 'CCCCCCC[C]=O',
            'carbamido': 'C(=O)(N)N',
            'carbamoyl': 'N[C]=O',
            'carbamyl': 'N[C]=O',
            'carbazoyl': 'NN[C]=O',
            'carbethoxy': 'O=[C]OCC',
            'carbonyl': '[CH]=O',
            'carboxy': 'O=[C]O',
            'cetyl': '[CH2]CCCCCCCCCCCCCCC',
            'chloroformyl': 'O=[C]Cl',
            'cinnamoyl': 'O=[C]C=CC1=CC=CC=C1',
            'cinnamyl': '[CH2]C=CC1=CC=CC=C1',
            'cinnamylidene': '[CH]C=CC1=CC=CC=C1',
            'cresyl': 'OC1=CC=C(C)C=C1',
            'crotonoyl': 'C/C=C/[C]=O',
            'crotyl': '[CH2]/C=C/C',
            'cyanamido': '[NH]C#N',
            'cyanato': '[O]C#N',
            'cyano': '[C]#N',
            'decanedioyl': 'O=[C]CCCCCCCC[C]=O',
            'decanoyl': 'CCCCCCCCC[C]=O',
            'diazo': '[N+]=[N-]',
            'diazoamino': 'N=NN',
            'disilanyl': '[SiH2][SiH3]',
            'disiloxanyloxy': '[O][SiH2]O[SiH3]',
            'disulfinyl': 'O=[S]S=O',
            'dithio': '[S]S',
            'enanthoyl': 'CCCCCC[C]=O',
            'epoxy': '[O]',
            'ethenyl': '[CH]=C',
            'ethynyl': '[C]#C',
            'ethoxy': '[O]CC',
            'ethyl': '[CH2]C',
            'ethylene': 'C=C',
            'ethylidene': '[CH]C',
            'ethylthio': '[S]CC',
            'formamido': 'O=C[NH]',
            'formyl': '[CH]=O',
            'furmaroyl': 'O=CO',
            'furfuryl': '[CH2]C1=CC=CO1',
            'furfurylidene': '[CH]C1=CC=CO1',
            'glutamoyl': 'N[C@@H](CC[C]=O)[C]=O',
            'glutaryl': 'O=[C]CCC[C]=O',
            'glycylamino': '[NH]C(CN)=O',
            'glycoloyl': 'OC[C]=O',
            'glycyl': 'NC[C]=O',
            'glyoxyoyl': 'O=[C]C=O',
            'guanidino': '[NH]C(N)=N',
            'guanyl': 'N=[C]N',
            'heptadecanoyl': 'CCCCCCCCCCCCCCCC[C]=O',
            'heptanamido': '',
            'heptanoyl': '',
            'hexadecanoyl': '',
            'hexamethylene': '',
            'hexanedioyl': '',
            'hippuryl': '',
            'hydrazino': '',
            'hydrazo': '',
            'hydrocinnamoyl': '',
            'hydroperoxy': '',
            'hydroxyamino': '',
            'imino': '',
            'iodoso': '',
            'iodyl': '',
            'isoamyl': '',
            'isobutenyl': '',
            'isobutoxy': '',
            'isobutyl': '',
            'isobutylidene': '',
            'isobutyryl': '',
            'isocyanato': '',
            'isocyano': '',
            'isohexyl': '',
            'isoleucyl': '',
            'isonitroso': '',
            'isopentyl': '',
            'isopentylidene': '',
            'isopropenyl': '',
            'isopropoxy': '',
            'isopropyl': '',
            'isopropylidene': '',
            'isothiocynato': '',
            'isovaleryl': '',
            'lactoyl': '',
            'lauroyl': '',
            'lauryl': '',
            'leucyl': '',
            'levulinoyl': '',
            'malonyl': '',
            'mandeloyl': '',
            'mercapto': '',
            'mesityl': '',
            'methacryloyl': '',
            'methallyl': '',
            'methionyl': '',
            'methoxy': '',
            'methyl': '',
            'methylene': '',
            'methylthio': '',
            'myristoyl': '',
            'myristyl': '',
            'naphthyl': '',
            'naphthylene': '',
            'neopentyl': '',
            'nitramino': '',
            'nitro': '',
            'nitrosamino': '',
            'nitroso': '',
            'nonanoyl': '',
            'oleoyl': '',
            'oxalyl': '',
            'oxo': '',
            'palmitoyl': '',
            'pentamethylene': '',
            'pentyl': '',
            'tert-pentyl': '',
            'phenacyl': '',
            'phenacylidene': '',
            'phenethyl': '',
            'phenoxy': '',
            'phenyl': '',
            'phenylene': '',
            'phosphino': '',
            'phosphinyl': '',
            'phospho': '',
            'phosphono': '',
            'phthaloyl': '',
            'picryl': '',
            'pimeloyl': '',
            'piperidino': '',
            'pivaloyl': '',
            'prenyl': '',
            'propargyl': '',
            '1-propenyl': '',
            '2-propenyl': '',
            'propionyl': '',
            'propoxy': '',
            'propyl': '',
            'propylidene': '',
            'pyrryl': '',
            'salicyloyl': '',
            'selenyl': '',
            'seryl': '',
            'siloxy': '',
            'silyl': '',
            'silyene': '',
            'sorboyl': '',
            'stearoyl': '',
            'stearyl': '',
            'styryl: '',
            'suberoyl': '',
            'succinyl': '',
            'sulfamino': '',
            'sulfamoyl': '',
            'sulfanilyl': '',
            'sulfeno': '',
            'sulfhydryl': '',
            'sulfinyl': '',
            'sulfo': '',
            'sulfonyl': '',
            'terephthaloyl': '',
            'tetramethylene': '',
            'thienyl': '',
            'thiocarbonyl': '',
            'thiocarboxy': '',
            'thiocyanato': '',
            'thionyl': '',
            'threonyl': '',
            'toluidino': '',
            'toluoyl': '',
            'tolyl': '',
            'alpha-tolyl': '',
            'tolylene': '',
            'tosyl': '',
            'triazano': '',
            'trimethylene': '',
            'trityl': '',
            'valeryl': '',
            'valyl': '',
            'vinyl: '',
            'vinylidene': '',
            'xylidino': '',
            'xylyl': '',
            'xylylene': '',
        }
        
        ring_functional_groups = {
            'cyclopropane': '',
            'spiropentane': '',
            'cyclobutane': '',
            'cyclopentane': '',
            'furan': '',
            'thiophene': '',
            'pyrrole': '',
            '2H-pyrrole': '',
            '3H-pyrrole': '',
            'pyrazole': '',
            '2H-imidazole': '',
            '1,2,3-triazole': '',
            '1,2,4-triazole': '',
            '1,2-dithiole': '',
            '1,3-dithiole': '',
            '3H-1,2-oxathiole': '',
            'isoxazole': '',
            'oxazole': '',
            'thiazole': '',
            'isothiazole': '',
            '1,2,3-oxadiazole': '',
            '1,2,4-oxadiazole': '',
            '1,2,5-oxadiazole': '',
            '1,3,4-oxadiazole': '',
            '1,2,3,4-oxatriazole': '',
            '1,2,3,5-oxatriazole': '',
            '3H-1,2,3-dioxazole': '',
            '1,2,4-dioxazole': '',
            '1,3,2-dioxazole': '',
            '1,3,4-dioxazole': '',
            '5H-1,2,5-oxathiazole': '',
            '1,3-oxathiole': '',
            'benzene': '',
            'cyclohexane': '',
            '2H-pyran': '',
            '4H-pyran': '',
            '2H-pyran-2-one': '',
            '4H-pyran-4-one': '',
            '1,2-dioxin': '',
            '1,3-dioxin': '',
            'pyridine': '',
            'pyridazine': '',
            'pyrimidine': '',
            'pyrazine': '',
            'piperazine': '',
            '1,3,5-triazine': '',
            '1,2,4-triazine': '',
            '1,2,3-triazine': '',
            '4H-1,2-Oxazine': '',
            '2H-1,3-Oxazine': '',
            '6H-1,3-Oxazine': '',
            '6H-1,2-Oxazine': '',
            '1,4-Oxazine': '',
            '2H-1,2-Oxazine': '',
            '4H-1,4-Oxazine': '',
            '1,2,5-Oxathiazine: '',
            '1,4-Oxazine': '',
            '2H-1,2-Oxazine': '',
            '4H-1,4-Oxazine': '',
            '1,2,5-Oxathiazine': '',
            '1,2,6-Oxathiazine': '',
            '1,2,4-Oxadiazine': '',
            '1,3,5-Oxadiazine': '',
            'morpholine': '',
            'azepine': '',
            'oxepin': '',
            'thiepin': '',
            '4H-1,2-diazepine': '',
            'indene': '',
            '2H-indene': '',
            'benzofuran': '',
            'isobenzofuran': '',
            'benzo[b]thiophene': '',
            'benzo[c]thiophene': '',
            'indole': '',
            '3H-indole': '',
            '1H-indole': '',
            'cyclopenta[b]pyridine': '',
            'pyrano[3,4-b]-pyrrole': '',
            'indazole': '',
            'benzisoxazole': '',
            'benzoxazole': '',
            '2,1-benzisoxazole': '',
            'naphthalene': '',
            '1,2,3,4-tetrahydronaphthalene': '',
            'octahydronaphthalene': '',
            '2H-1-benzopyran': '',
            '2H-1-benzopyran-2-one': '',
            '4H-1-benzopyran-4-one': '',
            '1H-2-benzopyran-1-one': '',
            '3H-2-benzopyran-1-one': '',
            'quinoline': '',
            'isoquinoline': '',
            'cinnoline': '',
            'quinazoline': '',
            '1,8-napthyhridine': '',
            '1,7-napththyridine': '',
            '1,5-napththridine': '',
            '1,6-napthyridine': '',
            '2H-1,3-benzoxazine': '',
            '2H-1,4-benzoxazine': '',
            '1H-2,3-benzoxazine': '',
            '4H-3,1-benzoxazine': '',
            '2H-1,2-benzoxazine': '',
            '4H-1,3-benzoxazine': '',
            'anthracene': '',
            'phenanthrene': '',
            'phenalene': '',
            'fluorene': '',
            'carbazole': '',
            'xanthene': '',
            'acridine': '',
            'norpinane': '',
            '7H-purine': '',
            'steroid_ring_system': '',
            
        }
        
        return organic_substituents, ring_systems
        
    def _get_functional_groups_smiles(self):

        functional_groups_smiles = {
            "1,1,1-trifluoroethane": "CC(F)(F)F",
            "1,1'-biphenyl": "C1(C2=CC=CC=C2)=CC=CC=C1",
            "1H-indene": "C1(CC=C2)=C2C=CC=C1",
            "1H-pyrrole": "[NH]1CCCC1",
            "2-butyne": "CC#CC",
            "2-ethyl-1-butanol": "CCC(CC)CO",
            "2-methylpenta-2,3-diene": "CC=C=C(C)C",
            "(E)-1,2-dimethyldiazene": "C/N=N/C",
            "N,N-dimethylacetamide": "CC(N(C)C)=O",
            "N-methylpropan-2-imine": "C/C(C)=N/C",
            "(Z)-N,N,N'-trimethylacetimidamide": "C/C(N(C)C)=N/C",
            "acetic anydride": "CC(=O)OC(=O)C",
            "acyl bromide": "C(=O)Br",
            "acyl chloride": "C(=O)Cl",
            "acyl fluoride": "C(=O)F",
            "acyl iodide": "C(=O)I",
            "aldehyde": "CC=O",
            "amide": "C(=O)N",
            "amino": "*N",
            "anthracene": "C12=CC=CC=C1C=C3C(C=CC=C3)=C2",
            "azide": "C([N-][N+]#N)",
            "benzene": "C1=CC=CC=C1",
            "benzene thiol": "C1=CC=C(C=C1)S",
            "bicyclohexyl": "C1CCCCC1C1CCCCC1",
            "bromine": "Br",
            "but-1-ene": "CCC=C",
            "but-1-yne": "CCC#C",
            "carbon dioxide": "O=C=O",
            "carboxylic acid": "C(=O)O",
            "chlorine": "Cl",
            "chloromethyl methyl ether": "COCCl",
            "cyclobutadiene": "C1=CC=C1",
            "cyclobutane": "C1CCC1",
            "cycloheptane": "C1CCCCCC1",
            "cyclohexane": "C1CCCCC1",
            "cyclohexa-1,3-diene": "C1=CCCC=C1",
            "cyclohexa-1,4-diene": "C1=CCC=CC1",
            "cyclohexene": "C=1CCCCC=1",
            "cyclopentane": "C1CCCC1",
            "cyclopenta-1,3-diene": "C1=CCC=C1",
            "cyclopropane": "C1CC1",
            "cyclopropene": "C1=CC1",
            "deuteroethane": "[2H][CH2]C",
            "dimethyl ether": "COC",
            "diethyl ether": "CCOCC",
            "diisopropyl ether": "CC(C)OC(C)C",
            "diamond": "C&1&1&1&1",
            "diazomethane": "C=[N+]=[N-]",
            "diammonium thiosulfate": "[NH4+].[NH4+].[O-]S(=O)(=O)[S-]",
            "enamine": "N",
            "ethane": "CC",
            "ethanethiol": "CCS",
            "ethanol": "CCO",
            "ethene": "C=C",
            "ether": "COC",
            "ester": "C(=O)OC",
            "fluorine": "F",
            "formaldehyde": "C=O",
            "furan": "C1OC=CC=1",
            "graphite": "C&1&1&1",
            "hydrogen cyanide": "C#N",
            "hydroxide": "[OH-]",
            "hydroxyl amine": "NO",
            "indane": "C1=CC=CC(CCC2)=C12",
            "ketone": "CC(=O)C",
            "methane": "C",
            "methanethiol": "CS",
            "methyl acetate": "CC(OC)=O",
            "methyl pyrrole": "CN1CCCC1",
            "methyl tert-butyl ether": "CC(C)(C)OC",
            "naphthalene": "C12=CC=CC=C1C=CC=C2",
            "nitro": "[N+](=O)[O-]",
            "nitromethane": "C[N+]([O-])=O",
            "pentalene": "C12=CC=CC1=CC=C2",
            "perhydroisoquinoline": "N1CC2CCCC2CC1",
            "phenol": "OC1CCCCC1",
            "phenyl": "C=1(C=CC=CC1)",
            "polystyrene": "c1ccccc1C&1&1",
            "primary alcohol": "O",
            "primary amine": "N",
            "propan-2-one": "CC(C)=O",
            "propanol": "CCC=O",
            "prop-1-ene": "CC=C",
            "prop-1-yne": "CC#C",
            "pyridine": "N1CCCCC1",
            "pyridine-n-oxide": "O=N1CCCCC1",
            "secondary amine": "NC",
            "spiro[5.5]undecane": "C12(CCCCC1)CCCCC2",
            "sulfoxide": "S(=O)(=O)",
            "tetramethylammonium": "C[N+](C)(C)C",
            "thiol": "S",
            "thiosulfate": "OS(=O)(=S)O",
            "trimethylamine": "CN(C)C",
            "triphenylene": "C1(C=CC=C2)=C2C(C=CC=C3)=C3C4=C1C=CC=C4",
        }

        return functional_groups_smiles

    def _get_functional_groups_smarts(self):

        functional_groups_smarts = {
            "acetic anydride": "[CX3](=[OX1])[OX2][CX3](=[OX1])",
            "acetylenic carbon": "[$([CX2]#C)]",
            "acyl bromide": "[CX3](=[OX1])[Br]",
            "acyl chloride": "[CX3](=[OX1])[Cl]",
            "acyl fluoride": "[CX3](=[OX1])[F]",
            "acyl iodide": "[CX3](=[OX1])[I]",
            "aldehyde": "[CX3H1](=O)[#6]",
            "alkane": "[CX4]",
            "allenic carbon": "[$([CX2](=C)=C)]",
            "amide": "[NX3][CX3](=[OX1])[#6]",
            "amidium": "[NX3][CX3]=[NX3+]",
            "amino acid": "[$([NX3H2,NX4H3+]),$([NX3H](C)(C))][CX4H]([*])[CX3](=[OX1])[OX2H,OX1-,N]",
            "azide": "[$(-[NX2-]-[NX2+]#[NX1]),$(-[NX2]=[NX2+]=[NX1-])]",
            "azo nitrogen": "[NX2]=N",
            "azole": "[$([nr5]:[nr5,or5,sr5]),$([nr5]:[cr5]:[nr5,or5,sr5])]",
            "azoxy nitrogen": "[$([NX2]=[NX3+]([O-])[#6]),$([NX2]=[NX3+0](=[O])[#6])]",
            "diazene": "[NX2]=[NX2]",
            "diazo nitrogen": "[$([#6]=[N+]=[N-]),$([#6-]-[N+]#[N])]",
            "bromine": "[Br]",
            "carbamate": "[NX3,NX4+][CX3](=[OX1])[OX2,OX1-]",
            "carbamic ester": "[NX3][CX3](=[OX1])[OX2H0]",
            "carbamic acid": "[NX3,NX4+][CX3](=[OX1])[OX2H,OX1-]",
            "carbo azosulfone": "[SX4](C)(C)(=O)=N",
            "carbo thiocarboxylate": "[S-][CX3](=S)[#6]",
            "carbo thioester": "S([#6])[CX3](=O)[#6]",
            "carboxylate ion": "[CX3](=O)[O-]",
            "carbonic acid": "[CX3](=[OX1])(O)O",
            "carbonic ester": "C[OX2][CX3](=[OX1])[OX2]C",
            "carbonyl group": "[$([CX3]=[OX1]),$([CX3+]-[OX1-])]",
            "carbonyl with carbon": "[CX3](=[OX1])C",
            "carbonyl with nitrogen": "[OX1]=CN",
            "carbonyl with oxygen": "[CX3](=[OX1])O",
            "carboxylic acid": "[CX3](=O)[OX1H0-,OX2H1]",
            "chlorine": "[Cl]",
            "cyanamide": "[NX3][CX2]#[NX1]",
            "di sulfide": "[#16X2H0][#16X2H0]",
            "enamine": "[NX3][CX3]=[CX3]",
            "enol": "[OX2H][#6X3]=[#6]",
            "ester": "[#6][CX3](=O)[OX2H0][#6]",
            "ether": "[OD2]([#6])[#6]",
            "fluorine": "[F]",
            "hydrogen": "[H]",
            "hydrazine": "[NX3][NX3]",
            "hydrazone": "[NX3][NX2]=[*]",
            "hydroxyl": "[OX2H]",
            "hydroxyl in alcohol": "[#6][OX2H]",
            "hydroxyl in carboxylic acid": "[OX2H][CX3]=[OX1]",
            "isonitrile": "[CX1-]#[NX2+]",
            "imide": "[CX3](=[OX1])[NX3H][CX3](=[OX1])",
            "imine": "[CX3;$([C]([#6])[#6]),$([CH][#6])]=[NX2][#6]",
            "iminium": "[NX3+]=[CX3]",
            "ketone": "[CX3]=[OX1]",
            "peroxide": "[OX2,OX1-][OX2,OX1-]",
            "phenol": "[OX2H][cX3]:[c]",
            "phosphoric acid": "[$(P(=[OX1])([$([OX2H]),$([OX1-]),$([OX2]P)])([$([OX2H]),$([OX1-]),$([OX2]P)])[$([OX2H]),$([OX1-]),$([OX2]P)]),$([P+]([OX1-])([$([OX2H]),$([OX1-]),$([OX2]P)])([$([OX2H]),$([OX1-]),$([OX2]P)])[$([OX2H]),$([OX1-]),$([OX2]P)])]",
            "phosphoric ester": "[$(P(=[OX1])([OX2][#6])([$([OX2H]),$([OX1-]),$([OX2][#6])])[$([OX2H]),$([OX1-]),$([OX2][#6]),$([OX2]P)]),$([P+]([OX1-])([OX2][#6])([$([OX2H]),$([OX1-]),$([OX2][#6])])[$([OX2H]),$([OX1-]),$([OX2][#6]),$([OX2]P)])]",
            "primary alcohol": "[OX2H]",
            "primary amine": "[NX3;H2;!$(NC=[!#6]);!$(NC#[!#6])][#6]",
            "proton": "[H+]",
            "mono sulfide": "[#16X2H0][!#16]",
            "nitrate": "[$([NX3](=[OX1])(=[OX1])O),$([NX3+]([OX1-])(=[OX1])O)]",
            "nitrile": "[NX1]#[CX2]",
            "nitro": "[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8]",
            "nitroso": "[NX2]=[OX1]",
            "n-oxide": "[$([#7+][OX1-]),$([#7v5]=[OX1]);!$([#7](~[O])~[O]);!$([#7]=[#7])]",
            "secondary amine": "[NX3;H2,H1;!$(NC=O)]",
            "sulfate": "[$([#16X4](=[OX1])(=[OX1])([OX2H,OX1H0-])[OX2][#6]),$([#16X4+2]([OX1-])([OX1-])([OX2H,OX1H0-])[OX2][#6])]",
            "sulfamate": "[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2][#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2][#6])]",
            "sulfamic acid": "[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2H,OX1H0-]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2H,OX1H0-])]",
            "sulfenic acid": "[#16X2][OX2H,OX1H0-]",
            "sulfenate": "[#16X2][OX2H0]",
            "sulfide": "[#16X2H0]",
            "sulfonate": "[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H0]),$([#16X4+2]([OX1-])([OX1-])([#6])[OX2H0])]",
            "sulfinate": "[$([#16X3](=[OX1])[OX2H0]),$([#16X3+]([OX1-])[OX2H0])]",
            "sulfinic acid": "[$([#16X3](=[OX1])[OX2H,OX1H0-]),$([#16X3+]([OX1-])[OX2H,OX1H0-])]",
            "sulfonamide": "[$([#16X4]([NX3])(=[OX1])(=[OX1])[#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[#6])]",
            "sulfone": "[$([#16X4](=[OX1])(=[OX1])([#6])[#6]),$([#16X4+2]([OX1-])([OX1-])([#6])[#6])]",
            "sulfonic acid": "[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H,OX1H0-]),$([#16X4+2]([OX1-])([OX1-])([#6])[OX2H,OX1H0-])]",
            "sulfoxide": "[$([#16X3](=[OX1])([#6])[#6]),$([#16X3+]([OX1-])([#6])[#6])]",
            "sulfur": "[#16!H0]",
            "sulfuric acid ester": "[$([SX4](=O)(=O)(O)O),$([SX4+2]([O-])([O-])(O)O)]",
            "sulfuric acid diester": "[$([#16X4](=[OX1])(=[OX1])([OX2][#6])[OX2][#6]),$([#16X4](=[OX1])(=[OX1])([OX2][#6])[OX2][#6])]",
            "thioamide": "[NX3][CX3]=[SX1]",
            "thiol": "[#16X2H]",
            "vinylic carbon": "[$([CX3]=[CX3])]",
        }

        return functional_groups_smarts

    def _get_common_organic_solvents_smiles(self):

        common_organic_solvents_smiles = {
            'acetic acid': 'CC(=O)O',
            'acetone' : 'CC(=O)C',
            'acetonitrile': 'CC#N',
            'benzene': 'C1=CC=CC=C1',
            'tert-butyl alcohol': 'CC(C)(C)O',
            'tert-butyl methyl ether': 'CC(C)(C)OC',
            'butylated hydroxytoluene': 'CC1=CC(=C(C(=C1)C(C)(C)C)O)C(C)(C)C',
            'chloroform': 'C(Cl)(Cl)Cl',
            '18-crown-6': 'C1COCCOCCOCCOCCOCCO1',
            'cyclohexane': 'C1CCCCC1',
            '1,2-dichloroethane': 'C(CCl)Cl',
            'dichloromethane': 'C(Cl)Cl',
            'diethyl ether': 'CCOCC',
            'diglyme': 'COCCOCCOC',
            '1,2-dimethoxyethane': 'COCCOC',
            'dimethylacetamide': 'CC(=O)N(C)C',
            'dimethylformamide': 'CN(C)C=O',
            'dimethyl sulfoxide': 'CS(=O)C',
            'dioxane': 'C1COCCO1',
            'ethanol': 'CCO',
            'ethyl acetate': 'CCOC(=O)C',
            'ethyl methyl ketone': 'CCC(=O)C',
            'ethylene': 'C=C',
            'ethylene glycol': 'C(CO)O',
            'grease': 'C(C(F)(F)F)OCC(F)(F)F',
            'n-hexane': 'CCCCCC',
            'hexamethylbenzene': 'CC1=C(C(=C(C(=C1C)C)C)C)C',
            'hexamethylphosphoramide': 'CN(C)P(=O)(N(C)C)N(C)C',
            'hexamethyldisiloxane': 'O([Si](C)(C)C)[Si](C)(C)C',
            'methanol': 'CO',
            'nitromethane': 'C[N+](=O)[O-]',
            'n-pentane': 'CCCCC',
            'propylene': 'CC=C',
            '2-propanol': 'CC(C)O',
            'pyridine': 'C1=CC=NC=C1',
            'pyrrole': 'C1=CNC=C1',
            'pyrrolidine': 'C1CCNC1',
            'silicon grease': 'C[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)C',
            'tetrahydrofuran': 'C1CCOC1',
            'toluene': 'CC1=CC=CC=C1',
            'triethylamine': 'CCN(CC)CC',
        }

        return common_organic_solvents_smiles

    def _get_common_organic_solvents_smarts(self):

        common_organic_solvents_smarts = {
            'acetic acid': '[#6]-[#6](=[#8])-[#8]',
            'acetone': '[#6]-[#6](=[#8])-[#6]',
            'acetonitrile': '[#6]-[#6]#[#7]',
            'benzene': '[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'tert-butyl alcohol': '[#6]-[#6](-[#6])(-[#6])-[#8]',
            'tert-butyl methyl ether': '[#6]-[#6](-[#6])(-[#6])-[#8]-[#6]',
            'butylated hydroxytoluene': '[#6]-[#6]1:[#6]:[#6](:[#6](:[#6](:[#6]:1)-[#6](-[#6])(-[#6])-[#6])-[#8])-[#6](-[#6])(-[#6])-[#6]',
            'chloroform': '[#6](-[#17])(-[#17])-[#17]',
            '18-crown-6': '[#6]1-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-1',
            'cyclohexane': '[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            '1,2-dichloroethane': '[#6](-[#6]-[#17])-[#17]',
            'dichloromethane': '[#6](-[#17])-[#17]',
            'diethyl ether': '[#6]-[#6]-[#8]-[#6]-[#6]',
            'diglyme': '[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]',
            '1,2-dimethoxyethane': '[#6]-[#8]-[#6]-[#6]-[#8]-[#6]',
            'dimethylacetamide': '[#6]-[#6](=[#8])-[#7](-[#6])-[#6]',
            'dimethylformamide': '[#6]-[#7](-[#6])-[#6]=[#8]',
            'dimethyl sulfoxide': '[#6]-[#16](=[#8])-[#6]',
            'dioxane': '[#6]1-[#6]-[#8]-[#6]-[#6]-[#8]-1',
            'ethanol': '[#6]-[#6]-[#8]',
            'ethyl acetate': '[#6]-[#6]-[#8]-[#6](=[#8])-[#6]',
            'ethyl methyl ketone': '[#6]-[#6]-[#6](=[#8])-[#6]',
            'ethylene': '[#6]=[#6]',
            'ethylene glycol': '[#6](-[#6]-[#8])-[#8]',
            'grease': '[#6](-[#6](-[#9])(-[#9])-[#9])-[#8]-[#6]-[#6](-[#9])(-[#9])-[#9]',
            'n-hexane': '[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'hexamethylbenzene': '[#6]-[#6]1:[#6](:[#6](:[#6](:[#6](:[#6]:1-[#6])-[#6])-[#6])-[#6])-[#6]',
            'hexamethylphosphoramide': '[#6]-[#7](-[#6])-[#15](=[#8])(-[#7](-[#6])-[#6])-[#7](-[#6])-[#6]',
            'hexamethyldisiloxane': '[#8](-[Si](-[#6])(-[#6])-[#6])-[Si](-[#6])(-[#6])-[#6]',
            'methanol': '[#6]-[#8]', 
            'nitromethane': '[#6]-[#7+](=[#8])-[#8-]',
            'n-pentane': '[#6]-[#6]-[#6]-[#6]-[#6]',
            'propylene': '[#6]-[#6]=[#6]',
            '2-propanol': '[#6]-[#6](-[#6])-[#8]',
            'pyridine': '[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            'pyrrole': '[#6]1:[#6]:[#7H]:[#6]:[#6]:1',
            'pyrrolidine': '[#6]1-[#6]-[#6]-[#7]-[#6]-1',
            'silicon grease': '[#6]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#6]',
            'tetrahydrofuran': '[#6]1-[#6]-[#6]-[#8]-[#6]-1',
            'toluene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'triethylamine': '[#6]-[#6]-[#7](-[#6]-[#6])-[#6]-[#6]'
        }

        return common_organic_solvents_smarts

    #------------------------- Property Declaration for GlobalChem ---------------------------#

    amino_acid_side_chains = property(_get_amino_acids)
    functional_groups_smiles = property(_get_functional_groups_smiles)
    functional_groups_smarts = property(_get_functional_groups_smarts)
    common_organic_solvents_smiles = property(_get_common_organic_solvents_smiles)
    common_organic_solvents_smarts = property(_get_common_organic_solvents_smarts)
    common_regex_patterns = property(_get_common_regex_patterns)
