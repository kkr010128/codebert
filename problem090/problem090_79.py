s = input()
if s in ["RRR"]:
        print(3)
if s in ["RRS",  "SRR"]:
        print(2)
if s in ["RSR", "RSS", "SRS", "SSR"]:
        print(1)
if s == "SSS":
        print(0)