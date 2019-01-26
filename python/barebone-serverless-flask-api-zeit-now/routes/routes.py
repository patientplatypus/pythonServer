


from flask import send_from_directory, request
from index import app
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(['sqlite', 'jpg', 'txt'])

@app.route('/getTEST', methods=['GET'])
def test():
  return "hello_there_sailor"

def allowed_file(filename):
    print("inside allowed_file")
    print("filename.rsplit('.', 1)[1].lower()")
    print(filename.rsplit('.', 1)[1].lower())
    print(" ALLOWED_EXTENSIONS")
    print(ALLOWED_EXTENSIONS)
    fileval = filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    print("value of fileval")
    print(fileval)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        print("inside post method")
        # check if the post request has the file part
        if 'file' not in request.files:
            print("file not in request.files")
            return "file not in request.files"
        print("after if statement")
        file = request.files['file']
        print("after file request")
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print("inside another if statement")
            return "No file selected"
        if file and allowed_file(file.filename):
            print("inside last if statement")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "file uploaded successfully!"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)