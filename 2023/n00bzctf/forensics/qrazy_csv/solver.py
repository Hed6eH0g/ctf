
data = []
coordinates = []
for i in range(29):
  coordinates.append([])
  for _ in range(29):
    coordinates[i].append(0)
    
with open('secret.csv') as f:
  line = f.readline()
  coordinates.append([])
  while line := f.readline():
    line = line.replace('"', '').replace('\n', '').split(',') 
    row = int(line[0])
    col = int(line[1])
    coordinates[row][col] = 1

with open('secret_squared.txt', 'w') as f:
  for row in range(29):
    for col in range(29):
      if coordinates[row][col]:
        f.write('■■')
        print('■', end=' ')
      else:
        f.write('  ')
        print(' ', end=' ')
    f.write('\n')
    print('')




