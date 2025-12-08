import math
import time
import heapq

raw = open('input.dat').readlines()

lines = raw

class JunktionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

class Circuit:
    def __init__(self, boxes):
        self.boxes = boxes

    def connect(self, other):
        self.boxes.append(other)

    def length(self):
        return len(self.boxes)

    def __hash__(self):
        return hash(tuple(self.boxes))

    def __str__(self):
        return f'[{", ".join(str(box) for box in self.boxes)}]'

def topKLongestCircuits(circuits, k):
    circuits.sort(key=lambda x: x.length(), reverse=True)
    return circuits[:k]

junktion_boxes = []
for line in lines:
    x, y, z = map(int, line.split(','))
    junktion_boxes.append(JunktionBox(x, y, z))

distances_heap = []
for i in range(len(junktion_boxes)):
    for j in range(i + 1, len(junktion_boxes)):
        heapq.heappush(distances_heap, (junktion_boxes[i].distance(junktion_boxes[j]), i, j))

junk_circuits_map = {}
not_connected = set(range(len(junktion_boxes)))
circuits = []
while len(circuits) != 1 or not_connected:
    if not distances_heap:
        break

    closest, junkA, junkB = heapq.heappop(distances_heap)
    
    inA = junkA in junk_circuits_map
    inB = junkB in junk_circuits_map

    if inA and inB:
        cA = junk_circuits_map[junkA]
        cB = junk_circuits_map[junkB]
        if cA != cB:
            cA.boxes.extend(cB.boxes)
            for k, v in junk_circuits_map.items():
                if v == cB:
                    junk_circuits_map[k] = cA
            if cB in circuits:
                circuits.remove(cB)
    elif inA:
        junk_circuits_map[junkA].connect(junktion_boxes[junkB])
        junk_circuits_map[junkB] = junk_circuits_map[junkA]
        if junkB in not_connected: not_connected.remove(junkB)
    elif inB:
        junk_circuits_map[junkB].connect(junktion_boxes[junkA])
        junk_circuits_map[junkA] = junk_circuits_map[junkB]
        if junkA in not_connected: not_connected.remove(junkA)
    else:
        circuit = Circuit([junktion_boxes[junkA], junktion_boxes[junkB]])
        circuits.append(circuit)
        junk_circuits_map[junkA] = circuit
        junk_circuits_map[junkB] = circuit
        if junkA in not_connected: not_connected.remove(junkA)
        if junkB in not_connected: not_connected.remove(junkB)

print(junktion_boxes[junkA].x * junktion_boxes[junkB].x)
