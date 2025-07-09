from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project/maatulja')
def project_maatulja():
    return render_template('project_maatulja.html')

@app.route('/project/hardware')
def project_hardware():
    return render_template('project_hardware.html')

@app.route('/project/affiliate')
def project_affiliate():
    return render_template('project_affiliate.html')

# Optional: Serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug=True) 