import sys

def main(argv):
  #implement your project below
  #open input file whose file name is argv[1] and the size of the matrix is int(argv[2]) * int(argv[2]), do not alter variable argv
  msize = int(argv[2])
  f1 = open(argv[1], 'r')
  matrix = []
  for line in f1.readlines():
    matrix.append([int(element) for element in line.strip().split(" ")])
  f1.close()
  for i in range(msize):
	  print(" ".join(str(x) for x in matrix[i]))


if __name__ == "__main__":
  main(sys.argv)
