import streamlit as st
from collections import Counter

def leggyakoribb_szo(mondat):
    szavak = mondats.split()
    szavak_szama = len(szavak)
    szavak_gyakorisaga = Counter(szavak)
    leggyakoribb_szavak = szavak_gyakorisaga.most_common(1)

    if leggyakoribb_szavak:
        return leggyakoribb_szavak[0][0]
    else:
        return "Nincs szó a szövegben"

def leggyakoribb_betu(mondat):
    karakterek = [karakter.lower() for karakter in mondats if karakter.isalpha()]
    karakterek_gyakorisaga = Counter(karakterek)
    leggyakoribb_karakterek = karakterek_gyakorisaga.most_common(1)

    if leggyakoribb_karakterek:
        return leggyakoribb_karakterek[0][0]
    else:
        return "Nincs betű a szövegben"

mondats = st.text_input('Írj bele egy szöveget')

if st.button('Nagybetű'):
    st.write(str.upper(mondats))

if st.button('Szavak'):
    szavak_szama = len(mondats.split())
    st.write(f"{szavak_szama}")

if st.button('Betűk'):
    betuk_szama = len([betu for betu in mondats if betu.isalpha()])
    st.write(f"{betuk_szama}")

if st.button('Leggyakoribb szó'):
    leggyakoribb = leggyakoribb_szo(mondats)
    st.write(f'{leggyakoribb}')

if st.button('Leggyakoribb betű'):
    leggyakoribb_betu = leggyakoribb_betu(mondats)
    st.write(f'{leggyakoribb_betu}')