

reagent_dic = {}

class Reagent:
    def __init__(self, ident, name, base = False, ignitetemp = -1):
        self.ident = ident
        self.name = name
        self.base = base
        self.ignitetemp = ignitetemp
        global reagent_dic
        reagent_dic[self.ident] = self

#Base Chems
Reagent("aluminium", "Aluminium", True)
Reagent("barium", "Barium", True)
Reagent("bromine", "bromine", True)
Reagent("carbon", "Carbon", True)
Reagent("calcium", "Calcium", True)
Reagent("chlorine", "Chlorine", True)
Reagent("chromium", "Chromium", True)
Reagent("copper", "Copper", True)
Reagent("ethanol", "Ethanol", True)
Reagent("fluorine", "Fluorine", True)
Reagent("helium", "Helium")
Reagent("hydrogen", "Hydrogen", True)
Reagent("iodine", "Iodine", True)
Reagent("iron", "Iron", True)
Reagent("lithium", "Lithium", True)
Reagent("magnesium", "Magnesium", True)
Reagent("mercury", "Mercury", True)
Reagent("nickel", "Nickel", True)
Reagent("nitrogen", "Nitrogen", True)
Reagent("oxygen", "Oxygen", True)
Reagent("phosphorus", "Phosphorus", True)
Reagent("plasma", "Plasma", True, 374)
Reagent("platinum", "Platinum", True)
Reagent("potassium", "Potassium", True)
Reagent("radium", "Radium", True)
Reagent("silicon", "Silicon", True)
Reagent("sodium", "Sodium", True)
Reagent("silver", "Silver", True)
Reagent("sugar", "Sugar", True)
Reagent("sulfur", "Sulfur", True)
Reagent("water", "Water", True, 374)

Reagent("fuel", "Welding Fuel", False, 474)
Reagent("blood", "Blood")
Reagent("space_fungus", "Space Fungus")

# Basic Compounds
Reagent("acetone", "Acetone")
Reagent("ammonia", "Ammonia")
Reagent("diethylamine", "Diethylamine")
Reagent("oil", "Oil", False, 474)
Reagent("phenol", "Phenol")
Reagent("stabiliser", "Stabilising Agent")

# Medical Chemicals
Reagent("smelling_salt", "Smelling Salts")
Reagent("antihol", "Antihol")
Reagent("atropine", "Atropine")
Reagent("calomel", "Calomel")
Reagent("charcoal", "Charcoal")
Reagent("cryoxadone", "Cryoxadone")
Reagent("diphenhydramine", "Antihistamine")
Reagent("ephedrine", "Ephedrine")
Reagent("epinephrine", "Epinephrine")
Reagent("ether", "Ether")
Reagent("hairgrownium", "Hairgrownium")
Reagent("haloperidol", "Haloperidol")
Reagent("heparin", "Heparin")
Reagent("mannitol", "Mannitol")
Reagent("mutadone", "Mutadone")
Reagent("oculine", "Oculine")
Reagent("penteticacid", "Pentetic Acid")
Reagent("perfluorodecalin", "Perfluorodecalin")
Reagent("anti_rad", "Potassium Iodide")
Reagent("proconvertin", "Proconvertin")
Reagent("salbutamol", "Salbutamol")
Reagent("salicylic_acid", "Salicylic Acid")
Reagent("saline", "Saline-Glucose Solution")
Reagent("silver_sufadiazine", "Silver Sulfadiazine")
Reagent("anti_fart", "Simethicone")
Reagent("spaceacillin", "Spaceacillin")
Reagent("styptic_powder", "Styptic Powder")
Reagent("super_hairgrownium", "Super Hairgrownium")
Reagent("synthflesh", "Synthflesh")
Reagent("teporone", "Teporone")

# poisons
Reagent("acetaldehyde", "Acetaldehyde")
Reagent("weedkiller", "Atrazine")
Reagent("capulettium", "Capulettium")
Reagent("capulettium_plus", "Capulettium Plus")
Reagent("cyanide", "Cyanide")
Reagent("formaldehyde", "Formaldehyde")
Reagent("itching", "Itching Powder")
Reagent("lipolicide", "Lipolicide")
Reagent("neurotoxin", "Neurotoxin")
Reagent("sarin", "Sarin")
Reagent("dna_mutagen", "Stable Mutagen")
Reagent("sulfonal", "Sulfonal")
Reagent("strychnine", "Strychnine")
Reagent("mutagen", "Unstable Mutagen")

# acids












class Container:
    def __init__(self, contents, temperature, limit):
        self.contents = contents
        self.temperature = temperature
        self.limit = limit

class Recipe:
    def __init__(self, educts, products, temperature, priority):
        self.educts = educts
        self.products = products
        self.temperature = temperature
        self.priority = priority





