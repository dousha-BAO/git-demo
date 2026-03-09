from time import sleep
for i in range(0,101):
    print(f"{'■'*i}{'□'*(100-i)}){i}%",end="\r")
    sleep(0.1) 
print("\n加载完成")