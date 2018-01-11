import os
note_path='./My Clippings.txt'
f=open(note_path,'r+')
digest_path='./digest/'
os.mkdir(digest_path)
while True:
    onenote=[]
    for i in range(0,5):
        line=f.readline()
        if not line:
            exit()
        onenote.append(line)
    book_note=open('%s%s.txt'%(digest_path,onenote[0]),'a+')
    book_note.write(onenote[3]+'\n')
    book_note.close()

