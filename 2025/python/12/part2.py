
raw = open('input.dat').readlines()

class Present:
    def __init__(self, pid, shape):
        self.id = pid
        self.shape = shape
        self.height = len(shape)
        self.width = len(shape[0])
        self.points = self.parse_points(shape)
        self.area = len(self.points)

    def parse_points(self, shape):
        pts = set()
        for r, row in enumerate(shape):
            for c, char in enumerate(row):
                if char == '#':
                    pts.add((r, c))
        return pts

    def __repr__(self):
        return f"Present(id={self.id}, size={self.width}x{self.height}, area={self.area})"

class Region:
    def __init__(self, width, height, requirements):
        self.width = width
        self.height = height
        self.requirements = requirements
        self.area = width * height

    def __repr__(self):
        return f"Region(size={self.width}x{self.height}, area={self.area}, reqs={self.requirements})"

def parse_lines(lines):
    presents, regions = {}, []
    pid, shape = None, []

    def add_present():
        if pid is not None: presents[pid] = Present(pid, shape)

    for line in (l.strip() for l in lines if l.strip()):
        if line.endswith(':') and line[:-1].isdigit():
            add_present()
            pid, shape = int(line[:-1]), []
        elif 'x' in line and ':' in line:
            add_present()
            pid = None
            dims, reqs = line.split(':')
            w, h = int(dims.split('x')[0]), int(dims.split('x')[1])
            counts = {i: int(c) for i, c in enumerate(reqs.split()) if c}
            regions.append(Region(w, h, counts))
        elif pid is not None:
            shape.append(line)

    add_present()
    return presents, regions

presents, regions = parse_lines(raw)
print("Presents:")
for pid, p in presents.items():
    print(f"  {p}")

print("Regions:")
for i, r in enumerate(regions):
    print(f"  {r}")

possible_by_area = 0
impossible_by_area = 0

for i, r in enumerate(regions):
    total_present_area = sum(presents[pid].area * count for pid, count in r.requirements.items())
    density = total_present_area / r.area
    
    if total_present_area <= r.area:
        possible_by_area += 1
    else:
        impossible_by_area += 1

print(f"\nImpossible (Need > Area): {impossible_by_area}")
print(f"Possible (Need <= Area): {possible_by_area}")
