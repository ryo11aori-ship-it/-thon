import math, itertools

P = lambda txt: "".join("<"*1017 + "".join("+"*v+">" for v in reversed(c)) + "<.[-]" + "<[-]"*6 + ">"*1017 for char in txt for c in [next(c for c in itertools.product(range(4),repeat=7) if int(math.floor(sum(v*(math.pi**k) for k,v in enumerate(c))))%256==ord(char))])

C = lambda tgt,txt: ">[-]>[-]<<[>+>+<<-]>>[<<+>>-]<"+"+"*((4-tgt)%4)+">+<[>-<[-]]>[[-]>>>>>>>>>>"+P(txt)+"<<<<<<<<<<]<<"

code = ",[<" + C(3,"t[p]++;") + C(1,"t[p]--;") + C(2,"p--;") + C(0,"p++;") + ">,]"

c_src = ["#include <stdio.h>\n#include <math.h>\nint main(){int t[20000]={0}; int p=9000; int ch;"]

[c_src.append("p--;") if c==">" else (c_src.append("p++;") if c=="<" else (c_src.append("t[p]=(t[p]+1)%4;") if c=="+" else (c_src.append("t[p]=(t[p]+3)%4;") if c=="-" else (c_src.append("while(t[p]!=0){") if c=="[" else (c_src.append("}") if c=="]" else (c_src.append("{double v=0; for(int i=0;i<20000;i++){if(t[i])v+=t[i]*pow(3.141592653589793, i-10000);} putchar((int)floor(v)%256);}") if c=="." else (c_src.append("ch=getchar(); if(ch!=EOF){t[p]=1; t[p+1]=ch%4; t[p+2]=(ch/4)%4; t[p+3]=(ch/16)%4;}else{t[p]=0;}") if c=="," else None))))))) for c in code]

c_src.append("return 0;}")

f = open("pi_out.c", "w")
f.write("\n".join(c_src))
f.close()

print("SUCCESS: The Decoupled πthon Compiler Generated!")
