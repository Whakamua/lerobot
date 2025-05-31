import cv2

def test_camera():
    # Try to open the camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    print("Camera opened successfully")
    
    # Try to read a frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
    else:
        print("Successfully read frame")
        print(f"Frame shape: {frame.shape}")
    
    # Release the camera
    cap.release()

if __name__ == "__main__":
    test_camera() 