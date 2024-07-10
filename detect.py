import cv2
import supervision as sv
from ultralytics import YOLO

model = YOLO('yolov8s.pt')
bbox_annotator = sv.BoxAnnotator()

# real-time detection
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        result = model(frame)[0]
        detections = sv.Detections.from_ultralytics(result)
        detections = detections[detections.confidence > 0.5]
        labels = [
            result.names[class_id]
            for class_id in detections.class_id
        ]
        frame = bbox_annotator.annotate(scene=frame, detections=detections, labels=labels)
        
        cv2.imshow('Real-time Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
