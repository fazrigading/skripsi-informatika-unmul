import streamlit as st

def kalkulator_referensi(jurnal, buku, web):
    total = jurnal + buku + web
    min_total, max_total = 30, 50
    
    result = ""
    if total < min_total or total > max_total:
        return f"⚠️ Jumlah referensi sekarang {total}, harus antara {min_total}-{max_total}."
    
    target_jurnal = round(total * 0.6)
    target_buku = round(total * 0.3)
    target_web = total - target_jurnal - target_buku
    
    result += f"Target proporsi (dari total {total} referensi):\n"
    result += f"- Jurnal: {target_jurnal}\n"
    result += f"- Buku  : {target_buku}\n"
    result += f"- Web   : {target_web}\n\n"
    
    diff_jurnal = jurnal - target_jurnal
    diff_buku = buku - target_buku
    diff_web = web - target_web

    result += "Penyesuaian:\n"
    if diff_jurnal < 0:
        result += f"- Tambah {abs(diff_jurnal)} jurnal\n"
    elif diff_jurnal > 0:
        result += f"- Kurangi {diff_jurnal} jurnal\n"

    if diff_buku < 0:
        result += f"- Tambah {abs(diff_buku)} buku\n"
    elif diff_buku > 0:
        result += f"- Kurangi {diff_buku} buku\n"

    if diff_web < 0:
        result += f"- Tambah {abs(diff_web)} web\n"
    elif diff_web > 0:
        result += f"- Kurangi {diff_web} web\n"

    if diff_jurnal == 0 and diff_buku == 0 and diff_web == 0:
        result += "✅ Proporsi sudah sesuai."
    
    return result

st.title("📚 Kalkulator Referensi Skripsi")
jurnal = st.number_input("Jumlah jurnal artikel:", min_value=0, step=1)
buku = st.number_input("Jumlah buku:", min_value=0, step=1)
web = st.number_input("Jumlah situs web:", min_value=0, step=1)

if st.button("Hitung"):
    st.text(kalkulator_referensi(jurnal, buku, web))
