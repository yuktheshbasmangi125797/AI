print("hello! I am treasure hunt robot")
print("I am here to search the treasure in rooms")

map_rooms = {
"A" : ["B", "C"],
"B" : ["D"],
"C" : ["D"]'
"D" : ["G"],
"G" : [],
}
print("our map:")
print("            A   (start)")
print("           /  \\")
print("          B    C ")
print("          \\   / ")
print("             D   ")
print("             ||  ")
print("             G (treasure 💎) ")
print("doors from each",map_rooms)

def bfs(start, goal):
  to_do = [start]
  visiter = []
  order = []
  while to_do:
    room = to_do.pop(0)
    if room is visited :
      continue
      visited.append(room)
      order.appen(room)

if room = goal




