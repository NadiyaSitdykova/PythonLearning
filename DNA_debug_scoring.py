sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
  dna_data = ""
  with open(dna_file) as f:
    for line in f:
      dna_data += line
  return dna_data

def dna_codons(dna):
  codons = {}
  for i in range(0, len(dna)):
    i+= 3
    if (i) == len(dna):
      codons.append(dna[i])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon == sample:
      matches += 1
  return matches

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "%f matches found. Continue investigation." % num_matches
  else:
    print "%d matches found. Free suspect." % num_matches

#something is wrong with line 35-37 but I am not sure how to fix them
is_criminal open(suspect1.txt)
is_criminal(suspect2.txt)
is_criminal(suspect3.txt)
