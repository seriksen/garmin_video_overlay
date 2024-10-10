from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory  
from routes.upload_data import save_video, extract_first_frame  # Updated import

app = Flask(__name__)

# Route for the video upload page
@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        if file:
            # Save the uploaded video
            filepath = save_video(file)
            
            # Extract the first frame from the video
            first_frame_path = extract_first_frame(filepath)
            
            # Redirect to the image manipulation page
            return redirect(url_for('edit_image', frame=first_frame_path))
    
    return render_template('upload.html')

# Route to display the image manipulation page
@app.route('/edit-image')
def edit_image():
    frame = request.args.get('frame')
    if not frame:
        return 'No frame available'
    return render_template('position_overlays.html', frame=frame)

# Serve static images (frames) from the frame folder
@app.route('/frames/<filename>')
def serve_frame(filename):
    return send_from_directory('frames', filename)

# Route to capture the size and position of the second image
@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json
    width = data.get('width')
    height = data.get('height')
    top = data.get('top')
    left = data.get('left')

    # Process or save the data here
    print(f"Width: {width}, Height: {height}, Top: {top}, Left: {left}")
    
    return jsonify({'status': 'success', 'message': 'Data saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
