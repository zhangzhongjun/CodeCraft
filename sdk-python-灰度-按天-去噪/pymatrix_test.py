import pymatrix

arr = [[1,2,3],[2,3,4],[123,12,124],[12,34,22],[123132,1234,43]]

mm = pymatrix.matrix(arr)

for row in mm.rows():
    print(row)

print(mm)
print("==================")
print(mm.subMatrix(2,3,1,3))

arr = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
print(len(arr))

m1 = [[1.1,2.5],[3,4]]
m1 = pymatrix.matrix(m1)
mm = m1.inverse()
print(mm)
print(mm*m1)
m2 = [[5,6],[7,8]]
m2 = pymatrix.matrix(m2)
m3 = m1 * m2
print(m3)