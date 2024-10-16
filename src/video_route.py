from flask import render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from .upload_route import get_uploaded_files

def configure_video_route(app):

    @app.route('/video', methods=['GET', 'POST'], endpoint='video')
    def display_video():
        uploaded_files = get_uploaded_files(app.config['UPLOAD_FOLDER'], return_full_path=True)

        if app.config['VIDEO_PATH'] is None:
            # Select a video file from the uploaded files

            files = [file for file in uploaded_files if file.endswith(('.mp4', '.mov'))]
            
            if len(files) == 0:
                video_path = None
            else:
                # Select the first video file
                # TODO: Create popup box to select video file
                video_path = files[0]  

        else:
            video_path = app.config['VIDEO_PATH']

        return render_template('video.html', uploaded_files=uploaded_files, 
                               video_path=video_path)

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)