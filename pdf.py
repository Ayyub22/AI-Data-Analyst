from fpdf import FPDF

class MedicalReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'RUMAH SAKIT UMUM DAERAH SEHAT SEJAHTERA', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, 'Jl. Kesehatan No. 123, Surabaya | Telp: (031) 555-xxxx', 0, 1, 'C')
        self.line(10, 25, 200, 25)
        self.ln(10)

    def create_table(self, title, patient_info, data, headers):
        # Judul Halaman
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        
        # Info Pasien
        self.set_font('Arial', '', 11)
        for key, value in patient_info.items():
            self.cell(0, 6, f"{key:<15} : {value}", 0, 1)
        self.ln(5)

        # Header Tabel
        self.set_fill_color(220, 220, 220)
        self.set_font('Arial', 'B', 10)
        # Hitung lebar kolom otomatis (sederhana)
        w = [40, 60, 90] 
        if len(headers) == 4: w = [30, 50, 40, 70] # Penyesuaian untuk Data Jantung
        
        for i, h in enumerate(headers):
            self.cell(w[i], 10, h, 1, 0, 'C', 1)
        self.ln()

        # Isi Data
        self.set_font('Arial', '', 10)
        for row in data:
            self.set_font('Arial', '', 10)
            if "POSITIF" in str(row[-1]) or "1" == str(row[-1]): # Highlight jika positif
                 self.set_font('Arial', 'B', 10)
            
            for i, item in enumerate(row):
                self.cell(w[i], 8, str(item), 1, 0)
            self.ln()
            
        # Tanda Tangan
        self.ln(15)
        self.set_font('Arial', '', 11)
        self.cell(0, 5, 'Surabaya, 27 November 2025', 0, 1, 'R')
        self.cell(0, 5, 'Dokter Pemeriksa,', 0, 1, 'R')
        self.ln(20)
        self.set_font('Arial', 'B', 11)
        self.cell(0, 5, '( Tanda Tangan & Stempel )', 0, 1, 'R')

# --- 1. DATA DIABETES ---
pdf1 = MedicalReport()
pdf1.add_page()
headers_dm = ['Parameter', 'Hasil', 'Keterangan']
data_dm = [
    ("Pregnancies", "1", "Riwayat Hamil"),
    ("Glucose", "125", "mg/dL (Puasa Terganggu)"),
    ("BloodPressure", "130/85", "mmHg (Pre-Hipertensi)"),
    ("SkinThickness", "28", "mm (Lemak Subkutan)"),
    ("Insulin", "140", "mu U/ml (Resistensi)"),
    ("BMI", "31.2", "kg/m2 (Obesitas I)"),
    ("DiabetesPedigree", "0.850", "Risiko Genetik Tinggi"),
    ("Outcome", "1", "POSITIF DIABETES")
]
pdf1.create_table("LEMBAR MONITORING DIABETES", 
                  {"Nama": "Nn. Ratna Sari", "Usia": "29 Tahun", "No RM": "05-22-90-11"}, 
                  data_dm, headers_dm)
pdf1.output("1_Diabetes_Record_Baru.pdf")

# --- 2. DATA JANTUNG ---
pdf2 = MedicalReport()
pdf2.add_page()
headers_jantung = ['Kode', 'Parameter', 'Hasil', 'Keterangan Medis']
data_jantung = [
    ("age", "Usia", "62", "Tahun"),
    ("sex", "Gender", "0", "Perempuan"),
    ("cp", "Chest Pain", "2", "Non-anginal Pain"),
    ("trestbps", "Tensi", "140", "mmHg (Hipertensi)"),
    ("chol", "Kolesterol", "294", "mg/dL (Tinggi)"),
    ("fbs", "Gula Puasa", "1", "True (>120 mg/dl)"),
    ("restecg", "EKG", "1", "ST-T Abnormality"),
    ("thalach", "Max HR", "106", "bpm"),
    ("exang", "Angina Latih", "0", "Tidak"),
    ("oldpeak", "ST Depress", "1.9", "mm"),
    ("slope", "ST Slope", "1", "Flat"),
    ("ca", "Pembuluh", "3", "Major Vessels Colored"),
    ("thal", "Thalassemia", "2", "Fixed Defect"),
    ("target", "DIAGNOSA", "1", "POSITIF SAKIT JANTUNG")
]
pdf2.create_table("REKAM DATA KLINIS JANTUNG", 
                  {"Nama": "Ny. Ellyarni", "Usia": "62 Tahun", "No RM": "02-11-44-66"}, 
                  data_jantung, headers_jantung)
pdf2.output("2_Jantung_Record_Baru.pdf")

# --- 3. DATA STROKE ---
pdf3 = MedicalReport()
pdf3.add_page()
headers_stroke = ['Parameter', 'Nilai', 'Interpretasi']
data_stroke = [
    ("Gender", "Male", "Laki-laki"),
    ("Age", "79", "Tahun"),
    ("Hypertension", "1", "Positif Hipertensi"),
    ("Heart Disease", "0", "Negatif"),
    ("Ever Married", "Yes", "Menikah"),
    ("Work Type", "Self-employed", "Wiraswasta"),
    ("Residence", "Rural", "Pedesaan"),
    ("Avg Glucose", "105.92", "mg/dL (Normal)"),
    ("BMI", "32.5", "Obesitas"),
    ("Smoking", "Never smoked", "Tidak Merokok"),
    ("STROKE", "1", "POSITIF STROKE")
]
pdf3.create_table("DATA FAKTOR RISIKO STROKE", 
                  {"Nama": "Tn. Darmawan", "Usia": "79 Tahun", "No RM": "10-55-82-S"}, 
                  data_stroke, headers_stroke)
pdf3.output("3_Stroke_Record_Baru.pdf")

print("Berhasil membuat 3 file PDF baru!")