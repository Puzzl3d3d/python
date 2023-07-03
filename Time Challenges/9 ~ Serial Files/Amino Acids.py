compound = input("Acid compound") or "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCGGACTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
searchSequence = input("Sequence to search: ")

total = 0
for i in range(0,len(compound)-1, 3):
    sequence = compound[i:i+3]
    if sequence.upper() == searchSequence.upper():
        total += 1
        
print(total, "instances of",searchSequence,"found")