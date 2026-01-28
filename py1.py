#import libraries
import sys
import numpy as np
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)

#encoding function
password = &quot;&quot;
def Encode(src, message, dest,password):

img = Image.open(src, &#39;r&#39;)
width, height = img.size
array = np.array(list(img.getdata()))
#print(&quot;array &quot;,array.shape)

if img.mode == &#39;RGB&#39;:

n = 3
elif img.mode == &#39;RGBA&#39;:
n = 4

total_pixels = array.size//n
#print(&quot;total_pixels &quot;,total_pixels)

message += password
b_message = &#39;&#39;.join([format(ord(i), &quot;08b&quot;) for i in message])
req_pixels = len(b_message)
#print(&quot;req_pixels &quot;,req_pixels)

if req_pixels &gt; (total_pixels * 3):
print(&quot;ERROR: Need larger file size&quot;)

else:
index=0
for p in range(total_pixels):
for q in range(0, 3):
if index &lt; req_pixels:
array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
index += 1

array=array.reshape(height, width, n)
enc_img = Image.fromarray(array.astype(&#39;uint8&#39;), img.mode)
enc_img.save(dest)
print(&quot;Image Encoded Successfully&quot;)

#decoding function
def Decode(src, password):

img = Image.open(src, &#39;r&#39;)
array = np.array(list(img.getdata()))

if img.mode == &#39;RGB&#39;:
n = 3
elif img.mode == &#39;RGBA&#39;:
n = 4

total_pixels = array.size//n

hidden_bits = &quot;&quot;
for p in range(total_pixels):
for q in range(0, 3):
hidden_bits += (bin(array[p][q])[2:][-1])

#print(&quot;hidden_bits&quot;,hidden_bits)

hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

#print(&quot;hidden_bits&quot;,hidden_bits)

message = &quot;&quot;
hiddenmessage = &quot;&quot;
for i in range(len(hidden_bits)):
x = len(password)
if message[-x:] == password:
break
else:
message += chr(int(hidden_bits[i], 2))
message = f&#39;{message}&#39;
hiddenmessage = message
#verifying the password
if password in message:
print(&quot;Hidden Message:&quot;, hiddenmessage[:-x])
else:
print(&quot;You entered the wrong password: Please Try Again&quot;)

#main function

def Stego():
print(&quot;—Image Steganography--&quot;)
print(&quot;1: Encode&quot;)
print(&quot;2: Decode&quot;)

func = input()

if func == &#39;1&#39;:
print(&quot;Enter Source Image Path&quot;)
src = input()
print(&quot;Enter Message to Hide&quot;)
message = input()
print(&quot;Enter Destination Image Path&quot;)
dest = input()
print(&quot;Enter password&quot;)
password = input()
print(&quot;Encoding...&quot;)
Encode(src, message, dest,password)

elif func == &#39;2&#39;:
print(&quot;Enter Source Image Path&quot;)
src = input()
print(&quot;Enter Password&quot;)
password = input()
print(&quot;Decoding...&quot;)
Decode(src,password)

else:
print(&quot;ERROR: Invalid option chosen&quot;)

Stego()
