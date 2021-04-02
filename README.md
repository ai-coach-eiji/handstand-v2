# handstand-v2
- [This application](https://ai-coach-eiji-handstand-v2.herokuapp.com) tells us the pose appears in the image. 


# Demo
- The poses are based on the results of [mediapipe](https://github.com/google/mediapipe).

![upright_posture](https://user-images.githubusercontent.com/81530619/113407475-51436880-93e8-11eb-98c0-0c00b1c4fd09.png)  ![handstand](https://user-images.githubusercontent.com/81530619/113407516-64563880-93e8-11eb-96c3-890c1a06da7e.png)

# Usage
1. Choose an image from your device and upload.
2. Tap the buttom '判定'.
3. Wait for a moment.
4. The app return the result.
   
   Result: 
   Human-pose skeleton and the pose.

![pose_demo](https://user-images.githubusercontent.com/81530619/113387837-0e719880-93c8-11eb-85be-a56454b2db0f.png)



# ToDo (including future works)
- [x] ~~Pose estimation in the image~~
- [ ] Calculate the body joint angles
- [ ] Pose estimation in the video
- [ ] Replace mediapipe with deeplabcut
- [ ] Create a new model of pose classification

# Reference
- Pose estimation: [MediaPipe](https://github.com/google/mediapipe)
- App design: [sinyblog](https://sinyblog.com/django/api_001/)
- App config: [bagelee](https://bagelee.com/programming/pwa/ios-korekara-pwa/)
- Opencv coding: [derodero24](https://qiita.com/derodero24/items/f22c22b22451609908ee)


# Author
北島栄司 （[https://twitter.com/1220castillo](https://twitter.com/1220castillo)）


# License
This application is under [Apache License 2.0](https://github.com/ai-coach-eiji/handstand-v2/blob/main/LICENSE).
