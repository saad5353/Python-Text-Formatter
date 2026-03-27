import textwrap


def Left(text, width):
    return textwrap.fill(text, width)


def RightLeft(text: str):
    lines = text.split('\n')
    max_length = len(max(lines, key=len))
    controller = 0
    for line in lines:
        position = 0
        while len(line) < max_length and (controller != len(lines)-1):
            position = line.find(" ", position)
            if position == -1:
                position = line.find(" ", 0)
                if position == -1:
                    break
            line = line[:position] + " " + line[position:]
            position += 2
        lines[controller] = line
        controller += 1
    return lines


# Reading File Data
print("Reading File Data")
file = open("KantWhatIsEnlightenment.txt", "r")
data = file.read()
file.close()
print("File Data Read")
paragraphs = data.split("\n\n")

# 70-Left
print("Generating 70-Left")
file = open("Kant70-L.txt", "w")
file.write("** Rakesh Jakkireddy\n")
file.write("*** Left side alignment, width = 70\n\n")
for paragraph in paragraphs:
    file.write(Left(paragraph, 70))
    file.write("\n===\n")
file.close()
print("70-Left Generated")

# 40-Left
print("Generating 40-Left")
file = open("Kant40-L.txt", "w")
file.write("** Rakesh Jakkireddy\n")
file.write("*** Left side alignment, width = 40\n\n")
for paragraph in paragraphs:
    file.write(Left(paragraph, 40))
    file.write("\n===\n")
file.close()
print("40-Left Generated")

# 70-LeftRight
print("Generating 70-LeftRight")
file = open("Kant70-LR.txt", "w")
file.write("** Rakesh Jakkireddy\n")
file.write("*** Both sides alignment, width = 70\n\n")
for paragraph in paragraphs:
    lines = RightLeft(Left(paragraph, 70))
    for line in lines:
        file.write(line)
        file.write("\n")
    file.write("===\n")
file.close()
print("70-LeftRight Generated")

# 40-LeftRight
print("Generating 40-LeftRight")
file = open("Kant40-LR.txt", "w")
file.write("** Rakesh Jakkireddy\n")
file.write("*** Both sides alignment, width = 40\n\n")
for paragraph in paragraphs:
    lines = RightLeft(Left(paragraph, 40))
    for line in lines:
        file.write(line)
        file.write("\n")
    file.write("===\n")
file.close()
print("All Allignments Generated")
print("Done")
