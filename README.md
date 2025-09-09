# Stop-Sign-Detection-with-Yolov8
In the modern world, image processing is widely applied across various large-scale applications. To simplify these tasks, many pre-trained models such as YOLO and SSD are available. In this project, YOLOv8 is trained specifically for detecting stop signs.

# Necessary Libraries
The project uses the Ultralytics library, which provides pre-trained YOLO models and convenient tools for training and inference.

# Usage
Firstly, "train.py" should be run to train the model.  
Secondly, "valid.py" should be run to validate the trained model and make predictions on the testing data.  
These predictions allow evaluation of the model's performance through metrics such as precision, recall, and mAP.  
The metrics and training curves are saved in "runs/detect/train/results.png".

# Limitations
YOLO achieves high accuracy in real-world conditions but may be less reliable for tasks requiring highly sensitive measurements. Despite this, it is well-suited for real-time applications due to its speed.
