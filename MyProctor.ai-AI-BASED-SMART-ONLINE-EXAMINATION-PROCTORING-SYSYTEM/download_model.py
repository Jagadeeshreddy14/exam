import os
import bz2
import wget
import shutil

def download_dlib_model():
    model_name = "shape_predictor_68_face_landmarks.dat"
    bz2_name = model_name + ".bz2"
    url = f"http://dlib.net/files/{bz2_name}"
    
    target_dir = os.path.join("gaze_tracking", "trained_models")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    target_path = os.path.join(target_dir, model_name)
    bz2_path = os.path.join(target_dir, bz2_name)
    
    if os.path.exists(target_path):
        print(f"Model already exists at {target_path}")
        return

    print(f"Downloading {url}...")
    try:
        wget.download(url, bz2_path)
        print(f"\nExtracting {bz2_name}...")
        
        with bz2.BZ2File(bz2_path) as fr, open(target_path, "wb") as fw:
            shutil.copyfileobj(fr, fw)
            
        os.remove(bz2_path)
        print("Model downloaded and extracted successfully.")
    except Exception as e:
        print(f"Error downloading model: {e}")
        print("Please download it manually from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
        print(f"Then extract it to {target_path}")

if __name__ == "__main__":
    download_dlib_model()
