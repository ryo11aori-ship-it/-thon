import math, itertools
P_bytes = lambda bl: "".join("<"*1000 + "".join("+"*v+"<" for v in c) + "." + ">[-]"*7 + ">"*1000 for b in bl for c in [next(c for c in itertools.product(range(4),repeat=7) if int(math.floor(sum(v*(math.pi**k) for k,v in enumerate(c))))%256==b)])
M = lambda f, t: "<"*(t-f) if t>f else ">"*(f-t)
chk = lambda vp, tgt, fp: M(0, vp) + "[-" + M(vp, 5) + "+" + M(5, 6) + "+" + M(6, vp) + "]" + M(vp, 5) + "[-" + M(5, vp) + "+" + M(vp, 5) + "]" + M(5, 6) + "-"*tgt + M(6, fp) + "+" + M(fp, 6) + "[" + M(6, fp) + "[-]" + M(fp, 6) + "[-]]" + M(6, 0)
ifa = lambda f1, f2, bl: M(0, f1) + "[" + M(f1, f2) + "[" + M(f2, 0) + P_bytes(bl) + M(0, f2) + "[-]]" + M(f2, f1) + "[-]]" + M(f1, 0)
C = lambda d0, d2, bl: chk(1, d0, 7) + chk(3, d2, 8) + ifa(7, 8, bl)
eh = [127,69,76,70, 2,1,1,0, 0,0,0,0, 0,0,0,0, 2,0,62,0, 1,0,0,0, 120,0,64,0, 0,0,0,0, 64,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 64,0,56,0, 1,0,64,0, 0,0,0,0, 1,0,0,0, 7,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,64,0, 0,0,0,0, 0,0,64,0, 0,0,0,0, 0,16,0,0, 0,0,0,0, 0,0,1,0, 0,0,0,0, 0,16,0,0, 0,0,0,0, 73,199,194,0,16,64,0, 77,49,246]
code = P_bytes(eh) + ",[" + C(3,2,[65,254,2]) + C(1,2,[65,254,10]) + C(2,3,[73,255,194]) + C(0,3,[73,255,202]) + ",]" + P_bytes([184,60,0,0,0,191,42,0,0,0,15,5])
open("compiler.π","w").write(code)
print("SUCCESS: Native ELF Emitter compiler.π generated!")
