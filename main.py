# This is the highest level view which will include/call subroutines

# Include statements

# Initialize the 2d area
gridSize = 19
grids = [[] for _ in range (gridSize)]
for i in range(0,gridSize):
    grids[i-1]=[0 for _ in range(gridSize)]
print (grids)

a, _, b = (1, 2, 3) # a = 1, b = 3
print(a, b)

for _ in range(5):
    print(_)

languages = ["Python", "JS", "PHP", "Java"]
for _ in languages:
    print(_)

million = 1_000_000
binary = 0b_0010
octa = 0o_64
hexa = 0x_23_ab

print(million)
print(binary)
print(octa)
print(hexa)
# Alternating clicks will place black/white pieces (black goes first)

# Pieces are removed dependent upon board state & liberties

# Throw to the second player

