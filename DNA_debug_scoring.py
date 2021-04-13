sample = ['GTA','GGG','CAC']

def read_dna(dna_file): # def read_dna():
  dna_data = "" # dna_data = [] 
  with open(dna_file, 'r') as f: # with open(dna_file, 'w') as f:
    for line in f: # for line in file:
      dna_data += line
  return dna_data

def dna_codons(dna):
  codons = [] # codons = {}
  for i in range(0, len(dna), 3): # for i in range(0, 3, len(dna)):
    if i + 3 < len(dna): # if (i += 3) < len(dna):
      codons.append(dna[i:i+3]) # codons.append(dna[i])
  return codons

def match_dna(dna):
  matches = 0 # matches = "0"
  for codon in dna:
    if codon in sample: # if codon is in sample:
      matches += 1 # matches += "1"
  return matches # return matches (wrong indentation)

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3: # if num_matches >= 3
    print "%d matches found. Continue investigation." % num_matches # print "%f matches found. Continue investigation." % num_matches
  else:
    print "%d matches found. Free suspect." % num_matches

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
