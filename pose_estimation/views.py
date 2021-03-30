import os
import base64
import mediapipe as mp
import numpy as np
import cv2
from PIL import Image
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {'title':'姿勢判定アプリ'}
    return render(request, 'pose_estimation/index.html', context)

def upload(request):  
    # 画像データの取得
    files = request.FILES.getlist("files[]")
    # 簡易エラーチェック（jpg拡張子）
    for memory_file in files:
        root_name, ext = os.path.splitext(memory_file.name)
        if ext != '.jpg':
            message = "【ERROR】: jpg以外の拡張子ファイルが指定されています。"
            return render(request, 'pose_estimation/index.html', {"message": message})
 
    if request.method =='POST' and files:
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
        # Prepare DrawingSpec for drawing the face landmarks later.
        mp_drawing = mp.solutions.drawing_utils 
        drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=5, color=0)

        judged_list = []
        labels=[]
        for image in files:
            image = Image.open(image)
            image = pil2cv(image)
            # Convert the BGR image to RGB and process it with MediaPipe Pose.
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # Print bodypart landmark.
            image_hight, image_width, _ = image.shape
            if not results.pose_landmarks:
                labels.append("検出が困難")
                judged_list.append(image)
                continue
            
            # Draw pose landmarks.
            annotated_image = image.copy()
            print("shape:", image.shape)
            mp_drawing.draw_landmarks(image=annotated_image,
                landmark_list=results.pose_landmarks,
                connections=mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)

            # 右目の座標
            r_eye = (
                results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].x * image_hight,
                results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].y * image_hight
                )
            # 右足首の座標
            r_ankle = (
                results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x * image_hight,
                results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y * image_hight
                )

            # 姿勢の判定
            judged_image, judge = judge_pose(annotated_image, r_eye, r_ankle)

            # 判定結果の格納
            if judge == 'handstand':
                judge = '倒立'
            else:
                judge = '立位'
            labels.append(judge)

            # 姿勢推定結果（骨格の描画）
            judged_image = cv2pil(judged_image)
            judged_list.append(np.array(judged_image))

        result=[]      
        for image, label in zip(judged_list, labels):
            image = Image.fromarray(image)
            image = pil2cv(image)
            ret, jpg = cv2.imencode('.jpg', image)
            src = base64.b64encode(jpg.tostring())
            src = str(src)[2:-1]
            result.append((src, label))
 
        context = {'result': result}
        return render(request, 'pose_estimation/result.html', context)
    else:
        return redirect('index')

def judge_pose(image, r_eye_coord, r_ankle_coord):
    # 姿勢の判定（目と足首の座標: (x, y)）
    if r_eye_coord[1] > r_ankle_coord[1]: # y座標のみで比較
        pose_judged = 'handstand'
    if r_eye_coord[1] < r_ankle_coord[1]:
        pose_judged = 'upright posture'
    cv2.putText(image, 'Pose: ' + pose_judged, (10, 80),
               cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3,
               cv2.LINE_AA)
    return image, pose_judged

def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGR)
    return new_image

def cv2pil(image):
    ''' OpenCV型 -> PIL型 '''
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGB)
    new_image = Image.fromarray(new_image)
    return new_image