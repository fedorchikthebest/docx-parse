from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
from pdf_parse import pdf_parse

app = Flask(__name__)

app.config['SECRET_KEY'] = "adawdadawd"
app.config['UPLOAD_FOLDER'] = "upload"


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # проверим, передается ли в запросе файл 
        if 'file' not in request.files:
            # После перенаправления на страницу загрузки
            # покажем сообщение пользователю 
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        # Если файл не выбран, то браузер может
        # отправить пустой файл без имени.
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file:
            # безопасно извлекаем оригинальное имя файла
            filename = file.filename
            # сохраняем файл
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # если все прошло успешно, то перенаправляем  
            # на функцию-представление `download_file` 
            # для скачивания файла
            return redirect(f"/static/{pdf_parse(filename)}")
    return render_template("index.html")