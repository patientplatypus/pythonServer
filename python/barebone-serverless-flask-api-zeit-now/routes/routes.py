


from flask import send_from_directory, request
from index import app
from werkzeug.utils import secure_filename
import os
import sqlite3

ALLOWED_EXTENSIONS = set(['sqlite', 'jpg', 'txt'])

# default to catch any route not already predefined
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'This path is not defined in routes: %s' % path


@app.route('/getTEST', methods=['GET'])
def test():
  return "hello_there_sailor"

def allowed_file(filename):
    print("inside allowed_file")
    print("filename.rsplit('.', 1)[1].lower()")
    print(filename.rsplit('.', 1)[1].lower())
    print("ALLOWED_EXTENSIONS")
    print(ALLOWED_EXTENSIONS)
    fileval = filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    print("value of fileval")
    print(fileval)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# file upload does not work on lambda! no memory to save to!
@app.route('/upload', methods=['POST'])
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
            print("allowed_file ok and file exists")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "file uploaded successfully!"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/firefox_places', methods=['POST'])
def firefox_places():
  print("inside firefox_places")
  if 'file' not in request.files:
    print("file not in request.files")
    return "file not in request.files"
  file = request.files['file']
  if file.filename == '':
    print("inside another if statement")
    return "No file selected"
  if file and allowed_file(file.filename):
    print("allowed_file ok and file exists")
    filename = secure_filename(file.filename)
    conn = sqlite3.connect(filename)
    print ("Operation done successfully")
    conn.close()
    print("after connect to sqlite3 db")
    return "after sqlite query"


@app.route("/upload_chunk_example", methods=["POST"])
def upload_chunk_example():
  print('inside /upload_chunk_example')
  with open("/tmp/output_file", "bw") as f:
    print("inside with open in upload_chunk")
    chunk_size = 256
    while True:
      print("inside while true statement")
      chunk = request.stream.read(chunk_size)
      print("value of chunk")
      print(chunk)
      if len(chunk) == 0:
        return
      f.write(chunk)

# from here: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py

# @app.route('/streaming_test', methods=['POST'])
# def streaming_test():
#     r = requests.get(url, stream=True)
#     with open(local_filename, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024): 
#             if chunk: # filter out keep-alive new chunks
#                 f.write(chunk)
#                 #f.flush() commented by recommendation from J.F.Sebastian
#     return local_filename