from lerobot.common.robot_devices.cameras.configs import OpenCVCameraConfig
from lerobot.common.robot_devices.cameras.opencv import OpenCVCamera
import cv2
import numpy as np

def test_lerobot_camera():
    # Create camera configuration
    config = OpenCVCameraConfig(
        camera_index=0,  # Use 0 for built-in camera on macOS
        fps=30,
        width=1280,  # Updated to match your camera's native resolution
        height=720   # Updated to match your camera's native resolution
    )
    
    # Create and connect camera
    camera = OpenCVCamera(config)
    camera.connect()
    
    print("Camera connected successfully")
    
    try:
        # Read a frame
        frame = camera.read()
        print(f"Frame shape: {frame.shape}")
        print(f"Frame dtype: {frame.dtype}")
        
        # Display the frame
        cv2.imshow('LeRobot Camera Test', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        cv2.waitKey(0)
        
    finally:
        # Clean up
        camera.disconnect()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    test_lerobot_camera() 