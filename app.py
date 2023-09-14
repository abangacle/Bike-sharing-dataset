import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Impor data
data_day = pd.read_csv("day.csv")
data_hour = pd.read_csv("hour.csv")

# Judul aplikasi
st.title('Analisis Data Penyewaan Sepeda')

# Deskripsi dan Penjelasan
st.write(
    "Selamat datang di aplikasi analisis data penyewaan sepeda. Aplikasi ini memungkinkan Anda untuk "
    "melihat data harian dan per jam serta menjawab beberapa pertanyaan bisnis yang relevan."
)

# Tabs
tabs = ["Pertanyaan Bisnis","Data Harian", "Data per Jam", "Kesimpulan", "Analisis Clustering", "Kesimpulan Analisis Clustering"]
selected_tab = st.sidebar.selectbox("Pilih Tab", tabs)

# Tab "Data Harian"
if selected_tab == "Data Harian":
    st.subheader('Data Harian')
    st.write(
        "Data harian mencakup informasi tentang penyewaan sepeda dalam interval harian. "
        "Berikut adalah lima baris pertama dari data ini:"
    )
    st.write(data_day.head())

    # Visualisasi distribusi jumlah peminjaman (cnt)
    st.subheader('Distribusi Jumlah Peminjaman Harian')
    st.write(
        "Grafik histogram di bawah ini menunjukkan distribusi jumlah peminjaman harian. "
        "Anda dapat melihat sebaran jumlah peminjaman sepeda."
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data_day['cnt'], bins=30, kde=True, ax=ax)
    ax.set_title('Distribusi Jumlah Peminjaman Harian (day.csv)')
    ax.set_xlabel('Jumlah Peminjaman')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)

    # Box plot perbandingan jumlah peminjaman antara hari libur dan bukan hari libur
    st.subheader('Perbandingan Jumlah Peminjaman antara Hari Libur dan Bukan Hari Libur')
    st.write(
        "Box plot di bawah ini membandingkan jumlah peminjaman antara hari libur (holiday=1) dan bukan hari libur (holiday=0)."
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='holiday', y='cnt', data=data_day, ax=ax)
    ax.set_title('Perbandingan Jumlah Peminjaman antara Hari Libur dan Bukan Hari Libur')
    ax.set_xlabel('Hari Libur')
    ax.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

    # Bar plot untuk melihat pengaruh kondisi cuaca terhadap jumlah peminjaman
    st.subheader('Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman')
    st.write(
        "Bar plot di bawah ini menunjukkan pengaruh kondisi cuaca (weathersit) terhadap jumlah peminjaman."
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='weathersit', y='cnt', data=data_day, ax=ax)
    ax.set_title('Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

# Tab "Data per Jam"
elif selected_tab == "Data per Jam":
    st.subheader('Data per Jam')
    st.write(
        "Data per jam berisi informasi tentang penyewaan sepeda dalam interval per jam. "
        "Berikut adalah lima baris pertama dari data ini:"
    )
    st.write(data_hour.head())

    # Visualisasi pola jam penggunaan sepeda
    st.subheader('Pola Jam Penggunaan Sepeda dalam Sehari')
    st.write(
        "Grafik line plot di bawah ini menunjukkan pola jam penggunaan sepeda dalam sehari, dengan perbedaan antara hari kerja dan hari libur."
    )
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='hr', y='cnt', data=data_hour, hue='workingday', ax=ax)
    ax.set_title('Pola Jam Penggunaan Sepeda dalam Sehari')
    ax.set_xlabel('Jam dalam Sehari')
    ax.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

    # Grafik batang untuk membandingkan penggunaan sepeda pada hari kerja dan hari libur
    st.subheader('Perbandingan Penggunaan Sepeda antara Hari Kerja dan Hari Libur')
    st.write(
        "Bar plot di bawah ini membandingkan penggunaan sepeda antara hari kerja (workingday=1) dan hari libur (workingday=0)."
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='holiday', y='cnt', data=data_hour, hue='workingday', ax=ax)
    ax.set_title('Perbandingan Penggunaan Sepeda antara Hari Kerja dan Hari Libur')
    ax.set_xlabel('Hari Libur')
    ax.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

    # Scatter plot untuk melihat korelasi antara kecepatan angin dan suhu dengan jumlah peminjaman
    st.subheader('Korelasi antara Kecepatan Angin dan Suhu dengan Jumlah Peminjaman')
    st.write(
        "Scatter plot di bawah ini menunjukkan korelasi antara kecepatan angin dan suhu dengan jumlah peminjaman. "
        "Warna scatter plot menunjukkan tingkat jumlah peminjaman."
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = sns.scatterplot(x='windspeed', y='temp', hue='cnt', data=data_hour, palette='viridis', ax=ax)
    scatter.set_title('Korelasi antara Kecepatan Angin dan Suhu dengan Jumlah Peminjaman')
    scatter.set_xlabel('Kecepatan Angin')
    scatter.set_ylabel('Suhu')
    st.pyplot(fig)
    
# Tab "Analisis Clustering"
elif selected_tab == "Analisis Clustering":
    st.subheader('Analisis Clustering')
    st.write(
        "Pada tab ini, kami akan melakukan analisis clustering pada data penyewaan sepeda berdasarkan beberapa faktor. "
        "Kami akan mengidentifikasi kelompok-kelompok atau pola-pola tertentu dalam data."
    )

    # Pengelompokan Berdasarkan Musim pada Data Day
    total_sewa_per_musim = data_day.groupby('season')['cnt'].sum()
    st.subheader('Pengelompokan Berdasarkan Musim pada Data Harian')
    st.write(
        "Analisis clustering pada data harian (day) berdasarkan musim. Berikut adalah plot total sewa sepeda per musim:"
    )
    fig, ax = plt.subplots(figsize=(10, 5))
    total_sewa_per_musim.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Total Sewa Sepeda')
    ax.set_title('Total Sewa Sepeda per Musim')
    ax.set_xticklabels(['Musim 1', 'Musim 2', 'Musim 3', 'Musim 4'], rotation=0)
    st.pyplot(fig)

    # Pengelompokan Berdasarkan Bulan pada Data Day
    total_sewa_per_bulan = data_day.groupby('mnth')['cnt'].sum()
    st.subheader('Pengelompokan Berdasarkan Bulan pada Data Harian')
    st.write(
        "Analisis clustering pada data harian (day) berdasarkan bulan. Berikut adalah plot total sewa sepeda per bulan:"
    )
    fig, ax = plt.subplots(figsize=(12, 6))
    total_sewa_per_bulan.plot(kind='line', marker='o', color='green', ax=ax)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total Sewa Sepeda')
    ax.set_title('Total Sewa Sepeda per Bulan')
    ax.grid(True)
    st.pyplot(fig)

    # Pengelompokan Berdasarkan Jam Puncak pada Data Hour
    jam_puncak = data_hour[(data_hour['hr'] >= 7) & (data_hour['hr'] <= 9)]
    total_sewa_jam_puncak = jam_puncak['cnt'].sum()
    st.subheader('Pengelompokan Berdasarkan Jam Puncak pada Data per Jam')
    st.write(
        "Analisis clustering pada data per jam (hour) berdasarkan jam puncak. Total sewa sepeda pada jam puncak adalah:"
    )
    st.write(total_sewa_jam_puncak)

    # Pengelompokan Berdasarkan Jam Kerja pada Data Hour
    jam_kerja = data_hour[(data_hour['hr'] >= 9) & (data_hour['hr'] <= 17) & (data_hour['workingday'] == 1)]
    total_sewa_jam_kerja = jam_kerja['cnt'].sum()
    st.subheader('Pengelompokan Berdasarkan Jam Kerja pada Data per Jam')
    st.write(
        "Analisis clustering pada data per jam (hour) berdasarkan jam kerja. Total sewa sepeda pada jam kerja adalah:"
    )
    st.write(total_sewa_jam_kerja)

    # Pengelompokan Berdasarkan Kondisi Cuaca pada Data Hour
    total_sewa_per_cuaca = data_hour.groupby('weathersit')['cnt'].sum()
    st.subheader('Pengelompokan Berdasarkan Kondisi Cuaca pada Data per Jam')
    st.write(
        "Analisis clustering pada data per jam (hour) berdasarkan kondisi cuaca. Berikut adalah plot total sewa sepeda per kondisi cuaca:"
    )
    fig, ax = plt.subplots(figsize=(10, 5))
    total_sewa_per_cuaca.plot(kind='bar', color='orange', ax=ax)
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Total Sewa Sepeda')
    ax.set_title('Total Sewa Sepeda per Kondisi Cuaca')
    ax.set_xticklabels(['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Berat'], rotation=0)
    st.pyplot(fig)

    # Pengelompokan Berdasarkan Durasi Peminjaman pada Data Hour
    data_hour['durasi'] = pd.cut(data_hour['hr'], bins=[0, 6, 12, 18, 24], labels=['Pagi', 'Siang', 'Sore', 'Malam'])
    total_sewa_per_durasi = data_hour.groupby('durasi')['cnt'].sum()
    st.subheader('Pengelompokan Berdasarkan Durasi Peminjaman pada Data per Jam')
    st.write(
        "Analisis clustering pada data per jam (hour) berdasarkan durasi peminjaman. Berikut adalah plot total sewa sepeda per durasi peminjaman:"
    )
    fig, ax = plt.subplots(figsize=(10, 5))
    total_sewa_per_durasi.plot(kind='bar', color='purple', ax=ax)
    ax.set_xlabel('Durasi Peminjaman')
    ax.set_ylabel('Total Sewa Sepeda')
    ax.set_title('Total Sewa Sepeda per Durasi Peminjaman')
    ax.set_xticklabels(['Pagi', 'Siang', 'Sore', 'Malam'], rotation=0)
    st.pyplot(fig)

    # Pengelompokan Berdasarkan Jenis Pengguna pada Data Hour
    total_sewa_per_pengguna = data_hour.groupby('registered')['cnt'].sum()
    st.subheader('Pengelompokan Berdasarkan Jenis Pengguna pada Data per Jam')
    st.write(
        "Analisis clustering pada data per jam (hour) berdasarkan jenis pengguna. Berikut adalah plot total sewa sepeda per jenis pengguna:"
    )
    fig, ax = plt.subplots(figsize=(8, 4))
    total_sewa_per_pengguna.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightcoral'], ax=ax)
    ax.set_ylabel('')
    ax.set_title('Total Sewa Sepeda per Jenis Pengguna')
    st.pyplot(fig)


# Tab "Kesimpulan"
elif selected_tab == "Kesimpulan":
    st.subheader('Kesimpulan')
    st.write(
        "Hasil analisis data sebagai berikut:\n\n"
        "**Tren Harian Jumlah Penyewa Sepeda:**\n\n"
        "Rata-rata suhu harian (day) adalah sekitar 0.4954, sedangkan median suhu harian adalah sekitar 0.4983. "
        "Ini menunjukkan bahwa suhu harian cenderung stabil dan tidak memiliki variasi yang signifikan selama setahun.\n\n"
        "Rata-rata suhu per jam (hour) adalah sekitar 0.4970, sedangkan median suhu per jam adalah sekitar 0.5000. "
        "Hal ini juga menunjukkan suhu per jam cenderung stabil dan tidak bervariasi secara signifikan.\n\n"
        "**Pengaruh Cuaca terhadap Jumlah Penyewa Sepeda:**\n\n"
        "Korelasi antara suhu harian (day) dan jumlah penyewa sepeda adalah sekitar 0.6275. "
        "Ini menunjukkan bahwa terdapat hubungan positif yang cukup kuat antara suhu harian dan jumlah penyewa sepeda harian. "
        "Ketika suhu naik, jumlah penyewa sepeda harian juga cenderung meningkat.\n\n"
        "Korelasi antara suhu per jam (hour) dan jumlah penyewa sepeda adalah sekitar 0.4048. "
        "Meskipun masih positif, hubungan antara suhu per jam dan jumlah penyewa sepeda tidak sekuat hubungan pada tingkat harian. "
        "Ini bisa mengindikasikan bahwa faktor-faktor lain, seperti cuaca per jam yang lebih dinamis, juga memengaruhi jumlah penyewa sepeda per jam.\n\n"
        "**Jumlah hari libur (holiday):**\n\n"
        "Dalam data harian (day), terdapat 21 hari libur dari total 731 hari, sementara dalam data per jam (hour), terdapat 500 hari libur dari total 17.379 jam. "
        "Ini menunjukkan bahwa hari libur lebih jarang terjadi dalam data harian dibandingkan dengan data per jam.\n\n"
        "Kesimpulannya, suhu memiliki pengaruh yang signifikan terhadap jumlah penyewa sepeda harian, di mana peningkatan suhu biasanya berhubungan dengan peningkatan jumlah penyewa sepeda. "
        "Namun, pengaruh cuaca pada tingkat per jam mungkin lebih kompleks karena faktor-faktor lain yang bisa memengaruhi jumlah penyewa sepeda dalam jangka waktu yang lebih pendek. "
        "Hari libur juga memiliki dampak yang cukup signifikan terutama dalam data per jam, yang dapat memengaruhi tingkat penyewaan sepeda."
    )
# Tab "Kesimpulan Analisis Clustering"
elif selected_tab == "Kesimpulan Analisis Clustering":
    st.subheader('Kesimpulan Analisis Clustering')
    st.write(
        "Dari analisis pengelompokan berdasarkan kriteria yang telah dilakukan pada data jam (data hour), berikut adalah hasil kesimpulan:\n\n"
        "**Pengelompokan Berdasarkan Musim pada Data Hour:**\n\n"
        "Terdapat empat musim yang dapat memengaruhi jumlah sewa sepeda. Musim dengan jumlah sewa sepeda tertinggi adalah musim ke-3 (spring) dengan total sewa sepeda sekitar 1.061.129, diikuti oleh musim ke-2 (summer) dengan total sewa sepeda sekitar 918.589. Musim dapat memengaruhi pola penggunaan sepeda.\n\n"
        "**Pengelompokan Berdasarkan Bulan pada Data Hour:**\n\n"
        "Analisis bulanan menunjukkan variasi dalam jumlah sewa sepeda. Bulan dengan jumlah sewa sepeda tertinggi adalah bulan ke-8 (Agustus) dengan total sekitar 351.194, sementara bulan ke-12 (Desember) memiliki jumlah sewa sepeda terendah sekitar 211.036. Ini menunjukkan adanya pola musiman dalam penggunaan sepeda.\n\n"
        "**Pengelompokan Berdasarkan Jam Puncak pada Data Hour:**\n\n"
        "Jam puncak penggunaan sepeda berlangsung antara pukul 7 hingga 9 pagi dengan total sewa sepeda sekitar 574.610. Ini mungkin berkaitan dengan jam masuk kerja atau aktivitas pagi.\n\n"
        "**Pengelompokan Berdasarkan Jam Kerja pada Data Hour:**\n\n"
        "Jam kerja, yang berlangsung antara pukul 9 pagi hingga 5 sore, menunjukkan total sewa sepeda sekitar 1.064.113. Hal ini menunjukkan bahwa sepeda sering digunakan selama jam kerja.\n\n"
        "**Pengelompokan Berdasarkan Kondisi Cuaca pada Data Hour:**\n\n"
        "Kondisi cuaca juga memengaruhi jumlah sewa sepeda. Cuaca dengan kode 1 (Cerah) memiliki jumlah sewa sepeda tertinggi sekitar 2.338.173, sementara cuaca dengan kode 4 (Berangin, Salju, dan Hujan) memiliki jumlah sewa sepeda yang sangat rendah sekitar 223. Pola ini menunjukkan bahwa cuaca yang baik mendukung penggunaan sepeda yang lebih tinggi.\n\n"
        "**Pengelompokan Berdasarkan Durasi Peminjaman pada Data Hour:**\n\n"
        "Durasi peminjaman juga memengaruhi jumlah sewa sepeda. Durasi peminjaman sore (Sore) memiliki jumlah sewa sepeda tertinggi sekitar 1.418.100, sementara durasi peminjaman pagi (Pagi) memiliki jumlah sewa sepeda yang lebih rendah sekitar 122.511. Ini menunjukkan bahwa sebagian besar orang lebih suka meminjam sepeda untuk waktu yang lebih lama.\n\n"
        "**Pengelompokan Berdasarkan Jenis Pengguna pada Data Hour:**\n\n"
        "Jenis pengguna juga memengaruhi jumlah sewa sepeda. Pengguna berlangganan (registered) memiliki kontribusi peminjaman sepeda yang jauh lebih besar daripada pengguna sekali jalan (casual). Pengguna berlangganan menyumbang sekitar 80% dari total sewa sepeda.\n\n"
        "Dengan demikian, kita dapat menyimpulkan bahwa ada beberapa faktor kunci yang memengaruhi pola penggunaan sepeda, seperti musim, bulan, jam, kondisi cuaca, durasi peminjaman, dan jenis pengguna. Analisis ini dapat membantu dalam perencanaan dan pengelolaan peminjaman sepeda yang lebih efisien."
    )


# Tab "Pertanyaan Bisnis"
elif selected_tab == "Pertanyaan Bisnis":
    st.subheader('Pertanyaan Bisnis')
    st.write(
        "Aplikasi ini dapat membantu Anda menjawab dua pertanyaan bisnis yang relevan:\n"
        "1. Bagaimana tren harian jumlah penyewa sepeda selama setahun?\n"
        "2. Apakah faktor cuaca berpengaruh terhadap jumlah penyewa sepeda harian?\n"
      
    )
    st.write(
        
        "Pertanyaan Bisnis Analisis Clusstering:\n"
        "1. Bagaimana pola penggunaan sepeda berdasarkan musim?\n"
        "2. Bagaimana pola penggunaan sepeda berdasarkan bulan?\n"
        "3. Bagaimana pola penggunaan sepeda selama jam puncak dan jam kerja?\n"
        "4. Bagaimana pengaruh kondisi cuaca terhadap jumlah peminjaman?\n"
        "5. Bagaimana durasi peminjaman memengaruhi jumlah penyewa sepeda?\n"
        "6. Bagaimana perbandingan antara pengguna berlangganan dan pengguna sekali jalan?"
    )

# Informasi Tambahan di Sidebar
st.sidebar.header('Informasi Tambahan')
st.sidebar.info(
    'Aplikasi ini dibuat untuk menyelesaikan Proyek Analisis Data Ihya Nashirudin Abrar yang diselenggarakan oleh Dicoding.'
)

# Menjalankan aplikasi Streamlit
if __name__ == '__main__':
    st.write("Silakan pilih tab yang sesuai di sidebar untuk melihat data dan visualisasi.")
