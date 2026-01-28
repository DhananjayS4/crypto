import numpy as np
from PIL import Image

TAG="stego"

def encode(src,message,dest):
    img=Image.open(src)
    data=np.array(img)

    message+=TAG
    binary="".join(format(ord(i),"08b") for i in message)

    if len(binary)>data.shape[0]*data.shape[1]*3:
        return print("Message too large for this image")

    index=0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(3):
                if index<len(binary):
                    data[i][j][k]=(data[i][j][k]&254)|int(binary[index])
                    index+=1

    Image.fromarray(data).save(dest)
    print("Image Encoded Successfully!")

def decode(src):
    img=Image.open(src)
    data=np.array(img)

    bits=""
    msg=""

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(3):
                bits+=str(data[i][j][k]&1)

                if len(bits)==8:
                    msg+=chr(int(bits,2))
                    bits=""

                    if msg.endswith(TAG):
                        print("Hidden message:",msg[:-len(TAG)])
                        return

    print("No hidden message found")

print("1 Encode\n2 Decode")
c=input()

encode(input("Source image: "),input("Message: "),"output.png") if c=="1" \
else decode(input("Encoded image: "))
