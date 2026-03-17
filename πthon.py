import math, itertools
M = lambda f, t: "<"*(t-f) if t>f else ">"*(f-t)
chk = lambda vp, tgt, fp, t1=5, t2=6: M(0, vp) + "[-" + M(vp, t1) + "+" + M(t1, t2) + "+" + M(t2, vp) + "]" + M(vp, t1) + "[-" + M(t1, vp) + "+" + M(vp, t1) + "]" + M(t1, t2) + "-"*tgt + M(t2, fp) + "+" + M(fp, t2) + "[" + M(t2, fp) + "[-]" + M(fp, t2) + "[-]]" + M(t2, 0)
P = lambda txt: "".join("<"*1000 + "".join("+"*v+"<" for v in c) + "." + ">[-]"*7 + ">"*1000 for char in txt for c in [next(c for c in itertools.product(range(4),repeat=7) if int(math.floor(sum(v*(math.pi**k) for k,v in enumerate(c))))%256==ord(char))])
ifa = lambda f1, f2, txt: M(0, f1) + "[" + M(f1, f2) + "[" + M(f2, 0) + P(txt) + M(0, f2) + "[-]]" + M(f2, f1) + "[-]]" + M(f1, 0)
C = lambda d0, d2, txt: chk(1, d0, 7) + chk(3, d2, 8) + ifa(7, 8, txt)
pi_eval = '{double v=0; for(int i=0;i<20000;i++){if(t[i])v+=t[i]*pow(3.141592653589793, i-10000);} putchar((int)floor(v)%256);}'
in_c = 'ch=getchar(); if(ch!=EOF){t[p]=1; t[p+1]=ch%4; t[p+2]=(ch/4)%4; t[p+3]=(ch/16)%4;}else{t[p]=0;}'
code = ",[" + C(3,2,"t[p]=(t[p]+1)%4;") + C(1,2,"t[p]=(t[p]+3)%4;") + C(2,3,"p--;") + C(0,3,"p++;") + C(2,2,pi_eval) + C(0,2,in_c) + C(3,1,"while(t[p]!=0){") + C(1,1,"}") + ",]"
c_src = ["#include <stdio.h>\n#include <math.h>\nint main(){int t[20000]={0}; int p=9000; int ch;"]
[c_src.append("p--;") if c==">" else (c_src.append("p++;") if c=="<" else (c_src.append("t[p]=(t[p]+1)%4;") if c=="+" else (c_src.append("t[p]=(t[p]+3)%4;") if c=="-" else (c_src.append("while(t[p]!=0){") if c=="[" else (c_src.append("}") if c=="]" else (c_src.append(pi_eval) if c=="." else (c_src.append(in_c) if c=="," else None))))))) for c in code]
c_src.append("return 0;}")
open("pi_out.c","w").write("\n".join(c_src))
print("SUCCESS: Stage 0 Transpiler Generated!")
