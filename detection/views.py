from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from ultralytics import YOLO
import subprocess
import os
import torch
import ultralytics 
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from django.http import StreamingHttpResponse
from django.shortcuts import redirect




def home(request):
    return render(request, 'home.html')



def upload_photo(request):
    [os.remove(os.path.join(settings.MEDIA_ROOT, f)) for f in os.listdir(settings.MEDIA_ROOT)]
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        uploaded_url = fs.url(filename)

        # Get the absolute path of the uploaded file
        uploaded_path = os.path.join(settings.MEDIA_ROOT, filename)

        # Call the detect_objects function and pass the path
        result_image_path = detect_objects(request, uploaded_path)  # Pass the request and image path

        return render(request, 'upload_success.html', {'uploaded_url': uploaded_url, 'result_image_path': result_image_path})
    return render(request, 'upload_photo.html')

def camera_stream(request):
    [os.remove(os.path.join(settings.MEDIA_ROOT, f)) for f in os.listdir(settings.MEDIA_ROOT)]
    return render(request, 'camera_stream.html')

def upload_captured_image(request):
    [os.remove(os.path.join(settings.MEDIA_ROOT, f)) for f in os.listdir(settings.MEDIA_ROOT)]
    if request.method == 'POST' and request.FILES['captured_image']:
        captured_image = request.FILES['captured_image']
        fs = FileSystemStorage()
        filename = fs.save(captured_image.name, captured_image)
        uploaded_url = fs.url(filename)

        uploaded_path = os.path.join(settings.MEDIA_ROOT, filename)
        result_image_path = detect_objects(request, uploaded_path)

        # Store the detected image URL in the session
        request.session['detected_image_url'] = os.path.join(settings.MEDIA_URL, result_image_path)

        return JsonResponse({'uploaded_url': uploaded_url})
    return JsonResponse({'error': 'Image upload failed.'}, status=400)

def detected_image(request):
    detected_image_url = request.session.get('detected_image_url', '')
    return render(request, 'detected_image.html', {'detected_image_url': detected_image_url})


def detect_objects(request, image_path):
    model = YOLO('/home/romail/ML1/trainning/4.Shirt_color_detection/final_web/best2.pt')  # Update the path to the YOLO weights

    results = model(image_path)

    for r in results:
        im_array = r.plot()

        # Convert rendered image to RGB format
        rgb_im_array = cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB)

        #Display the rendered image using Matplotlib
        #plt.imshow(rgb_im_array)
        #plt.axis('off')
        #plt.show()

        im = Image.fromarray(rgb_im_array)
        #im.save('results.jpg')

        result_image_path = image_path.replace(".jpg", ".jpg")
        result_im = Image.fromarray(rgb_im_array)
        result_im.save(result_image_path)

        return result_image_path


def real_time_detection(request):
    return render(request, 'real_time_detection.html')

def detect(frame):
    model = YOLO('/home/romail/ML1/trainning/4.Shirt_color_detection/final_web/best2.pt')  # Update the path to the YOLO weights
    results = model(frame)

    for r in results:
        im_array = r.plot()

        # Convert the processed frame to RGB format
        rgb_im_array = cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB)

        return rgb_im_array

def camera_feed(request):
    cap = cv2.VideoCapture(0)  # 0 for default camera

    def generate():
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            # Convert the frame to RGB format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            processed_frame = detect(rgb_frame)

            # Convert the processed frame to base64
            _, img_encoded = cv2.imencode('.jpg', processed_frame)
            base64_encoded = img_encoded.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + base64_encoded + b'\r\n\r\n')

        cap.release()

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

