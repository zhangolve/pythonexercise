# 20180531 根据输入，先创建临时文件，再由临时文件生成实际文件。模拟服务端，临时文件的产生。
import tempfile

arr = ["123","456", "789"]
with tempfile.TemporaryFile(mode='wb+') as out_file:
    for i in arr:
        out_file.write(i+'\n')
    out_file.seek(0)


    file = open("testfile.txt","w") 
    mapping_file_lines = out_file.readlines()
    for line in mapping_file_lines:
        print(line)
        file.write(line)
    file.close() 
