import re

reCigar = re.compile(r'(\d+)([DIMNS])')

def getCoverRegion(chr, pos, cigar):

    tempStart = int(pos)
    tempSize = 0 
    coverRegion = []
    for m in reCigar.finditer(cigar):
        if m.group(2) == "N":
            coverRegion.append(chr + ":" + str(tempStart) + "-" + str(tempStart + tempSize - 1))
            tempStart = tempStart + tempSize + int(m.group(1))
            tempSize = 0 
        elif m.group(2) in ["M", "D"]:
            tempSize = int(tempSize) + int(m.group(1))

    coverRegion.append(chr + ":" + str(tempStart) + "-" + str(tempStart + tempSize - 1))

    return ','.join(coverRegion)


if __name__ == "__main__":
    import sys
    print getCoverRegion(sys.argv[1], sys.argv[2], sys.argv[3])
