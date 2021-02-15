sample = ['GTA','GGG','CAC']

def read_dna():
  dna_data = []
  with open(dna_file, 'w') as f:
    for line in readlines(f):
      dna_data += line
  return dna_data

def dna_codons(codons):
  codons = {}
  for i in range(0, 3, len(dna)):
    if i += 3 < len(dna):
      codons.append(dna[i])
  return codons

def match_dna(dna):
  matches = "0"
  for codon in dna:
    if codon is in sample:
      matches += "1"
    return matches

def is_criminal(dna_sample):
  dna_data = dna_sample.read_dna()
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3
    print "There were %s matches found. Investigation sould continue." % num_matches
  else:
    print "There were %s matches found. Suspect can be freed." % num_matches

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
