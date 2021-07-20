
from Crypto.Util import number
from sympy import prime
import random
#文字入力
print('文字を入力して下さい')
x=input()
word=[]
for w in x:
  word.append(ord(w)) 
#もともとの文字コード
print(word)

#鍵生成
def key_gen(bit):
  #素数生成
  ram = random.randint(1,1000)
  ram_prime=prime(ram)
  ram_prime2=2*ram_prime+1
  #原始元ｇを求める
  while True:
    g=number.getRandomRange(3,ram_prime)
    #ｇが原始元を持つか判別
    if pow(g,2,ram_prime)==1:
      continue
    if pow(g,ram_prime2,ram_prime)==1:
      continue
    break
  #秘密値
  x=number.getRandomRange(2,ram_prime-1)
  #公開値
  y=pow(g,x,ram_prime)
  return (ram_prime,g,y),x

#暗号化
def encrypt(m,pk):
  cipher =[]
  p,g,y=pk
  r=number.getRandomRange(2,p-1)
  c1=pow(g,r,p)
  for l in m:
    c2=(l*pow(y,r,p))%p
    cipher.append(c2)
  return (c1,cipher)

#復号化
def decrypt(c,pk,sk):
  decode=''
  p,g,y=pk
  c1,c2=c
  x=sk
  c3=pow(c1,p-1-sk,p)
  for cc in c2:
    m=(cc*c3)%p
    decode +=chr(m)
  return decode 

#復号化しないで出力
def f_decrypt(c):
  decode =''
  c1,c2=c
  for cc in c2:
   decode+=chr(cc)
   
  return decode


pk,sk=key_gen(8)
#秘密鍵
print('pk:',pk)
#公開鍵
print('sk:',sk)
#暗号化された文字コード
c=encrypt(word,pk)
print(c)
#復号化されていないまま出力した文
f=f_decrypt(c)
print(f)

#復号化された平文
d=decrypt(c,pk,sk)
print(d)