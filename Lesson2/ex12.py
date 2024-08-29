#You are given four real numbers- a1, b1, a2, b2 - The endpoints of two line segments on a line. Find the length of their intersection. Note that the order of the endpoints of a segment is irrelevant, i.e. the segments [1;2] and [2;1] are considered the same.

a1 = 1
b1 = 4
a2 = 9
b2 = 7
start_intersection = max(a1, a2)
end_intersection = min(b1, b2)
length_intersection = max(0, end_intersection - start_intersection)
print(f"Length of intersection: {length_intersection}")
