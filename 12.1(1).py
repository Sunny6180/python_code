with open("xiaolan.txt",mode="r",encoding="utf-8") as f:
    reader=f.read()

sentences=reader.split(",")

front=[s.replace("兰", "君") for s in sentences[:3]]
back=[s.replace("兰", "利") for s in sentences[3:]]

with open("xiaojun.txt", mode="w", encoding="utf-8") as f:
    f.write(",".join(front))

with open("xiaoli.txt", mode="w", encoding="utf-8") as f:
    f.write(",".join(back))

print("处理完成！")