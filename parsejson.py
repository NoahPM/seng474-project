import json
import sys
out =open("dp_fixed.json","w",encoding="utf-8")
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode+1),0xfffd)
with open('db.json','r',encoding='utf-8') as f:
	meme_data = json.load(f)
out.write("{\n")

for i in range(1,3227):
    out.write("\"%d\":{\n"%i)
    for key in meme_data["_default"]["%d"%i].keys():
        if key != "thumbnail":
            out.write("\"%s\":"%key)
            out.write("  \"%s\""%str(meme_data["_default"]["%d"%i][key]).translate(non_bmp_map))
        elif key == "thumbnail":
            for k in meme_data["_default"]["%d"%i]["thumbnail"].keys():
                out.write("\"%s\":"%k)
                out.write("  \"%s\",\n"%str(meme_data["_default"]["%d"%i]["thumbnail"][k]).translate(non_bmp_map))
        if key != "media" and key != "thumbnail":
            out.write(",\n")
    out.write("},\n\n")
    out.flush()
out.write("}")
out.close()
