def copyFile(fromFile, toFile):
    print(f"copying from {fromFile} to {toFile}")
    from_file = open(fromFile)
    indata = from_file.read()
    out_file.write(indata)
    out_file = open(toFile, 'w')
    out_file.write(indata)