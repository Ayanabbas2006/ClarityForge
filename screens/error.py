import sys,os,random
matches = ''
for root, dirs, files in os.walk("/"):
    if "ERROR.txt" in files:
        full_path = os.path.join(root, "ERROR.txt")
        matches+=(full_path)
        break
else:
    matches="ERROR.txt"
print(matches)
try:
    with open(matches) as f:
        Error=eval(f.read())
except Exception:
    with open(matches,'w') as f:
        f.write("{}")
def check(a,b):
    name=str(type(a).__name__)
    for i in Error:
        if Error[i]==name:
            print(f"Errorcode{i}:",Error[i],f"in {b}")
            sys.exit()
    else:
        code=str(random.randint(0,999))
        while code in Error.keys():
            code=str(random.randint(0,999))
        Error[code]=name
        with open(matches,'w') as g:
            g.write(str(Error))
        check(a,b)
