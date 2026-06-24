# Bloque de datos sin procesar (Texto no estructurado)
medical_data = """Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# --- 1. Fase de Reemplazo y Segmentación de Registros ---
updated_medical_data = medical_data.replace("#", "$")
num_records = 0
medical_data_split = updated_medical_data.split(";")

# Conteo de registros basado en el marcador de costo
for medical_dat in updated_medical_data:
    if medical_dat == "$":
        num_records += 1

# --- 2. Fase de Parseo y Limpieza de Espacios (*Data Stripping*) ---
medical_records = []
for medical_split in medical_data_split:
    medical_records.append(medical_split.split(","))

medical_records_clean = []
for medical_rec in medical_records:
    record_clean = []
    for rec in medical_rec:
        record_clean.append(rec.strip())
    medical_records_clean.append(record_clean)

# Normalización de nombres a mayúsculas sostenidas
for record in medical_records_clean:
    record[0] = record[0].upper()

# --- 3. Fase de Distribución de Atributos y Análisis Estadístico ---
names = []
ages = []
bmis = []
insurance_costs = []
total_bmi = 0

for medical_clean in medical_records_clean:
    names.append(medical_clean[0])
    ages.append(medical_clean[1])
    bmis.append(medical_clean[2])
    insurance_costs.append(medical_clean[3])

# Conversión de tipos y acumulación para cálculo estadístico
for bm in bmis:
    total_bmi += float(bm)

average_bmi = total_bmi / len(bmis)

# Impresión de control y resultados analíticos en consola
print("There are " + str(num_records) + " medical records in the data.")
print("Average BMI: " + str(average_bmi))
print(names)
