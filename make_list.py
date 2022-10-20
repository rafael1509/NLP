import glob, sys
import yaml
import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def ajeitar(nome):
    nome = nome.title()
    if nome.find(",") > 0:
        nome = nome.split()
        nome.append(nome[0])
        nome.pop(0)
        nome = " ".join(nome)
        nome = nome.replace(",","")
    return nome

with open("novo.txt", "a") as g:
    g.write("[")
    for i in os.listdir("text/"):
        for fn in glob.glob(f"text/{i}"):
            with open(fn,"r") as f:
                content = f.read()
                # ignore the first line
                content = content[3:]
                p = content.find('---')
                header = content[0:p]
                d = yaml.load(header,Loader)
                x = d['title']
                x = ajeitar(x)
                g.write(f"\"{x}\",")
    g.write("]")
