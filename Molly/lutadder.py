import os
from PIL import Image

DLNs = ["Fogotten One","Bilbo","Orang Salad","Sandvich","19 dollar fortnite card","axolotl","Lucky Slime","Hello my name is Inigo Montoya","You killed my father","prepare to die","Thats just a thoery","wonka","c u b e","awooooo","squimshy","we do a little forgetting to name this lut in LutNames txt"]

#change these vars only when necissary
DLNo = open(".ai", "r")#8 or the amount of already listed luts
g = DLNo.readline()
DLNo.close()
FL = 449 #449 line in final.glsl to replace
GL = 209 #209 line in grading.glsl to replace
LL = 260 #260 line start in en_us.lang to replace
OL = 381 #381 line in options.glsl to replace
#------------------------------------

skc = 0
skipi = False
ncounter = 0
nnl = []
Langl = []
olive = []
LG = "..\..\lang\en_US.lang"
OP = "..\Settings.glsl"

def LSR(FILE, nh, FLN):
  nftst = []
  counter = 0
  newline = f"    const vec2 inverseSize = vec2(1.0 / 512, 1.0 / {nh});\n"
  
  f = open(FILE, 'r', encoding="UTF-8")
  lines = f.readlines()
  for line in lines:
    if counter == FLN - 1:
      nftst.append(newline)
    else:
      nftst.append(line)
    counter += 1
  f.close()
  
  counter = 0
  open(FILE, "w", encoding="UTF-8").close()
  a = open(FILE, "a", encoding="UTF-8")
  for i in nftst:
    a.write(nftst[counter])
    counter += 1
  a.close()

LUT = Image.open("Luts.png")
w, h = LUT.size
LUT.close()

LSR("..\..\program\composite\Final.glsl", h, FL)
LSR("..\..\program\odt\Grading.glsl", h, GL)

names = open("LutNames.txt", "r", encoding="UTF-8")
namess = names.read()
names.close()
namesl = namess.split(",")

for i in namesl:
  named = len(namesl) + len(DLNs)
  if ncounter > len(namesl):
    dnc = ncounter - len(namesl)
    nn = DLNs[dnc]
  elif ncounter > named:
    ulc = ncounter - named
    nn = f"Unnamed Lut {ulc}"
  else:
    nn = namesl[ncounter]
  VSL = f"value.Selected_LUT.{ncounter}={nn}\n"
  ncounter += 1
  nnl.append(VSL)

lca = int(h / 512)
lcb = len(nnl)
lcm = max(lca, lcb)

x = open(".ai", "w")
x.write(str(lcm))
x.close()

ncounter = 0
Lang = open(LG, "r", encoding="UTF-8")
langs = Lang.readlines()
for line in langs:
    luno = ncounter - LL
    if ncounter == LL - 1:
      skipi = True
      for i in nnl:
        Langl.append(i)
    else:
      if skipi == True:
        if skc == int(g):
          skipi = False
        else:
          skc += 1
      else:
        Langl.append(line)
    ncounter += 1
if str(Langl[-1]) != "option.AP1=AP1 Color Space":
  Langl.append("\n\noption.AP1=AP1 Color Space")
else:
  donothing = True
Lang.close()

ncounter = 0
open(LG, "w", encoding="UTF-8").close()
c = open(LG, "a", encoding="UTF-8")
for i in Langl:
  c.write(Langl[ncounter])
  ncounter += 1
c.close()

onums = "0"
h = 1

while h < lcm:
  onums = (str(onums) + " " + str(h))
  h += 1
nol = f"#define Selected_LUT                 0         //[{onums}]\n"

opt = open(OP, "r", encoding="UTF-8")
k = opt.readlines()
rcounter = 0

for d in k:
  if rcounter == OL - 1:
    olive.append(nol)
  else:
    olive.append(d)
  rcounter += 1
opt.close()

rcounter = 0
open(OP, "w", encoding="UTF-8").close()
aa = open(OP, "a", encoding="UTF-8")
for i in olive:
  aa.write(olive[rcounter])
  rcounter += 1
aa.close()
