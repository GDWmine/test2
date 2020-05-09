menu='上证综合指数   沪深股市概况'
title='沪A,深A,全B,创业'
chart='683,111,657,1158,141,829,34,20,44,456,41,245'
infotitle=title.split(',')
infochart=chart.split(',')
hchartall=int(infochart[0])
+int(infochart[1])+int(infochart[2])
hchartwid=[int(int(infochart[0])/hchartall*50),
int(int(infochart[1])/hchartall*50),
50-int(int(infochart[0])/hchartall*50)
-int(int(infochart[1])/hchartall*50)]
schartall=int(infochart[3])
+int(infochart[4])+int(infochart[5])
schartwid=[int(int(infochart[3])/schartall*50),
int(int(infochart[4])/schartall*50),
50-int(int(infochart[3])/schartall*50)
-int(int(infochart[4])/schartall*50)]
qchartall=int(infochart[6])
+int(infochart[7])+int(infochart[8])
qchartwid=[int(int(infochart[6])/qchartall*50),
int(int(infochart[7])/qchartall*50),
50-int(int(infochart[6])/qchartall*50)
-int(int(infochart[7])/qchartall*50)]
cchartall=int(infochart[9])
+int(infochart[10])+int(infochart[11])
cchartwid=[int(int(infochart[9])/cchartall*50),
int(int(infochart[10])/cchartall*50),
50-int(int(infochart[9])/cchartall*50)
-int(int(infochart[10])/cchartall*50)]
print(hchartwid)
print(menu.center(50) )
print(60 * '-'  )
print(infotitle[0] +'  \033[1;37;41m '+infochart[0].center(int(hchartwid[0]))
+'\033[1;36;47m '+infochart[1].
center(int(hchartwid[1]))
+'\033[1;37;42m'+infochart[2].
center(int(hchartwid[2]))+'\033[0m')
print(  )
print(infotitle[1] +'  \033[1;37;41m '+infochart[3].center(int(schartwid[0]))
+'\033[1;36;47m '+infochart[4].
center(int(schartwid[1]))
+'\033[1;37;42m'+infochart[5].
center(int(schartwid[2]))+'\033[0m')
print(  )
print(infotitle[2] +'  \033[1;37;41m '+infochart[6].center(int(qchartwid[0]))
+'\033[1;36;47m '+infochart[7].
center(int(qchartwid[1]))
+'\033[1;37;42m'+infochart[8].
center(int(qchartwid[2]))+'\033[0m')
print(  )
print(infotitle[3] +' \033[1;37;41m  '+infochart[9].
center(int(cchartwid[0]))
+'\033[1;36;47m'+infochart[10].
center(int(cchartwid[1]))+'\033[1;37;42m'
+infochart[11].center(int(cchartwid[2]))+'\033[0m')