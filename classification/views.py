from django.shortcuts import render

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # disable info, warwning, error di console
from django.core.files.storage import FileSystemStorage 
from pathlib import Path
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import json
from PIL import Image
from classification.models import MotifBatik # nama class tabel motif batik
from django.shortcuts import redirect

BASE_DIR = Path(__file__).resolve().parent.parent

# Memanggil file model cnn
model_path = os.path.join(BASE_DIR, 'models/model_cnn.h5')
model = load_model(model_path)

# View beranda/home 
def beranda(request):
    return render(request, 'pages/beranda.html')

# View klasifikasi
def klasifikasi(request):
    return render(request, 'pages/klasifikasi.html')

# Proses preprocessing image
def preprocessing(image):
    input_size = 256,256
    img_resize = image.convert('RGB').resize((input_size), resample= 0)
    img_array = (np.array(img_resize))/255
    img_reshape = np.stack([img_array], axis=0)
    return img_reshape 

# Proses prediksi image
def prediction(model, image):
    # kelas = ['kawung','megamendung','parang','sidomukti','truntum']
    probabilitas = model.predict(image) # menampilkan nilai probabilitas
    prediksi = np.argmax(probabilitas) # mencari nilai probabilitas tertinggi 
    return probabilitas, prediksi

# View hasil klasifikasi
def hasil_klasifikasi(request):
    if 'filePath' in request.FILES:
        file_upload = request.FILES['filePath']
        file_save = FileSystemStorage().save(file_upload.name, file_upload)
        file_url = FileSystemStorage().url(file_save) # /media/test_megamendung_09_i8tGtCL.jpg
        path = '.'+file_url # ./media/test_megamendung_09_i8tGtCL.jpg
        image = Image.open(path)
        # preprocessing
        image_preprocessing = preprocessing(image)
        image = image_preprocessing
        # prediksi
        probabilitas, prediksi = prediction(model, image)
        akurasi = probabilitas[0][prediksi]
        akurasi = '{:2.0f}'.format(akurasi*100 )
        hasil_prediksi = prediksi+1 # karena id databes dimulai dari 1, maka hasil_prdiski ditambah satu

        # memanggil batik berdasarkan id hasil prediski
        motif_batik = MotifBatik.objects.get(id=hasil_prediksi)
        context = {
            'file_url' : file_url,
            'motif_batik' : motif_batik,
            'akurasi' : akurasi,
        }
        return render(request, 'pages/hasil-klasifikasi.html', context)
    else:
        return redirect('/klasifikasi')

# View daftar motif batik
def motif_batik(request):
    motif_batik = MotifBatik.objects.all()
    context = {
        'motif_batik' : motif_batik
    }
    return render(request, 'pages/motif-batik.html', context)

# View artikel deskripsi motif batik
def artikel(request, id_batik):
    motif_batik = MotifBatik.objects.get(id=id_batik)
    motif_batik_lainnya = MotifBatik.objects.all()[0:4]
    context = {
        'motif_batik' : motif_batik,
        'motif_batik_lainnya' : motif_batik_lainnya,
    }
    return render(request, 'pages/artikel-batik.html', context)

# View tentang/about
def tentang(request):
    return render(request, 'pages/tentang.html')
