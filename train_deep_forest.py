from sys import argv
import onnx

if len(argv) < 3:
    raise Exception("Expecting ONNX model file and CSV dataset")

modelFile = argv[1]
dataFile  = argv[2]

onnx_model = onnx.load(modelFile)

print(modelFile); print(dataFile)