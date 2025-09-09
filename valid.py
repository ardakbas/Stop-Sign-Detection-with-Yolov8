from ultralytics import YOLO

model = YOLO("C:\\Users\\Arda\\OneDrive\\Masaüstü\\YOLO Model\\runs\\detect\\train\\weights\\best.pt")

metrics = model.val(data = "data.yaml")

print(metrics)

model.predict(source="test/images", conf=0.25, save=True)
