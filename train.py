from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data = "data.yaml",
    epochs = 50,
    imgsz =512,
    batch = 32,
    workers = 8,
    half = True,
    optimizer = "Adam",
)

