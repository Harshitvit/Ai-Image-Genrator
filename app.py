import os
import io
import logging
from flask import Flask, render_template, request, jsonify
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PIL import Image
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import time

# Load environment variables
load_dotenv()

# Ensure STABILITY_KEY is set
STABILITY_KEY = os.getenv('STABILITY_KEY')
if not STABILITY_KEY:
    raise ValueError("STABILITY_KEY environment variable not set")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = 'static/images'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize Stability AI client
stability_api = client.StabilityInference(
    key=STABILITY_KEY,
    verbose=True,
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({'error': 'No prompt provided'}), 400

        prompt = data['prompt'].strip()
        if not prompt:
            return jsonify({'error': 'Empty prompt'}), 400

        # Generate the image
        answers = stability_api.generate(
            prompt=prompt,
            seed=int(time.time()), # Random seed
            steps=30,
            cfg_scale=7.0,
            width=512,
            height=512,
            samples=1,
            sampler=generation.SAMPLER_K_DPMPP_2M
        )

        # Process the generated image
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    
                    # Save the image
                    filename = f"generated_{int(time.time())}_{secure_filename(prompt[:30])}.png"
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    img.save(filepath)
                    
                    return jsonify({
                        'success': True,
                        'image_url': f"/static/images/{filename}"
                    })

        return jsonify({'error': 'Failed to generate image'}), 500

    except Exception as e:
        logger.error(f"Error generating image: {str(e)}")
        return jsonify({'error': 'Failed to generate image'}), 500

if __name__ == '__main__':
    app.run(debug=True)
