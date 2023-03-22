import os 
# os.rename("nnFolder?file.txt","nnfolder/6.txt")
files = os.listdir("nnfolder")
i = 1
for file in files:
    if file.endswith(".png"):

        print(file)
        os.rename(f"nnfolder/{file}",f"nnfolder/{i}.png")
        i = i+1
