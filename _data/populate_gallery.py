import sys

with open(sys.argv[2], "w") as output:
	for i in range(int(sys.argv[1])):
		output.write("- image_thumb: %03d.jpg\n" % (i+1))
		output.write("  image_large: %03d.jpg\n" % (i+1))
		output.write("  image_alt: gallery %03d\n" % (i+1))
		output.write("\n")
