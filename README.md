# handstand-v2
- [This application](https://ai-coach-eiji-handstand-v2.herokuapp.com) tells us the pose appears in the image. 


# Demo
- The poses are based on the results of [mediapipe](https://github.com/google/mediapipe).

![upright_posture](https://user-images.githubusercontent.com/81530619/113407475-51436880-93e8-11eb-98c0-0c00b1c4fd09.png)  ![handstand](https://user-images.githubusercontent.com/81530619/113407516-64563880-93e8-11eb-96c3-890c1a06da7e.png)

# Usage
1. Choose an image.jpg(or .png) from your device and upload.
2. Enter the buttom '送信'.
3. Wait for a moment.
4. The app return the result.
   
   Result: 
   
   image.jpg with human-pose skeleton and the pose(handstand or upright posture).

![pose_demo](https://user-images.githubusercontent.com/81530619/113387837-0e719880-93c8-11eb-85be-a56454b2db0f.png)



# ToDo (including future works)
- [x] pose estimation in the image
- [ ] calculate the body joint angles
- [ ] pose estimation in the video
- [ ] replace mediapipe with deeplabcut
- [ ] create a new model of pose classification

# Reference
- Pose estimation: [MediaPipe](https://github.com/google/mediapipe)
- App design: [sinyblog](https://sinyblog.com/django/api_001/)


# Author
北島栄司 [Twitter](https://twitter.com/1220castillo)


# License
This application is under [Apache License 2.0](https://github.com/ai-coach-eiji/handstand-v2/blob/main/LICENSE).
