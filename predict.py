from ultralytics import YOLO
import numpy as np

def prediction(filepath):
    model=YOLO(r"best.pt")

    result=model(f"{filepath}")

    print(result)

    names_dict=result[0].names

    probs=result[0].probs.data.tolist()

    print(names_dict)
    print(probs)

    return f"Image best match: {names_dict[np.argmax(probs)]}"
