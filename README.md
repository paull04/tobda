# Project TOBDA 
### **0\. TOBDA Introduction**

We thought about how to make it easier for blind people to obtain spatial information. Since We live in a dormitory school, the target was limited to the school. We were able to take and label hallway photos, learn segmentation models based on U-net architecture, obtain relative Depth information with Depth Estimation models, convert them into world coordinates to find correspondence, calculate homography matrix, and obtain Bird eye views without RGB-d cameras and Lidar sensors.

If you touch a non-hallway part of the Bird Eye View's hallway map, the vibration will ring, and if you touch the hallway part, the vibration will not ring. In this way, we expect the visually impaired to be able to understand space and plan the path they will move proactively.

In Korean, 톺다(tobda) means searching, fumbling, or looking for it, and the project name was named "TOBDA" because it aims to understand the space while fumbling through the smartphone screen.

![1](https://user-images.githubusercontent.com/67684178/134816698-a72b2bd2-035b-443d-a403-fc96cb50682b.PNG)
### **1\. Semantic Segmentation**

We made a dataset from the hallway of our high school and trained U-Net for Semantic Segmentation.


- Dataset: https://www.kaggle.com/taegukang0305/semantic-hallway-dataset

- Video: https://www.youtube.com/watch?v=ZjD5f1sja1A&ab_channel=TaeguKang


![2](https://user-images.githubusercontent.com/67684178/134816947-9047c6b8-81f0-463d-bf57-b060c9cbe51c.PNG)



### **2\. Depth Estimation**

We use MiDasV2 which learned from datasets targeting indoor spaces for obtaining depth map. 

- Video:  https://www.youtube.com/watch?v=p8Vm0s8-S_Y&ab_channel=TaeguKang

![3](https://user-images.githubusercontent.com/67684178/134817035-7a65d08c-f100-4cd3-ac54-44c8da11a186.PNG)


### **3\. Real World Mapping From Depth Map**

We matched a image pixel (u,v,d) to a point cloud (x,y,z) of the real world based on camera's properties and geometric relationships.

-   More information: [https://medium.com/yodayoda/from-depth-map-to-point-cloud-7473721d3f](https://medium.com/yodayoda/from-depth-map-to-point-cloud-7473721d3f)

![4](https://user-images.githubusercontent.com/67684178/134817263-60921c09-4b21-4c01-8edf-210c9eed0d1f.PNG)


### **4\. Select points from image**

To obtain the transformation matrix, the world coordinates of four points on any pixel must be calculated.

![5](https://user-images.githubusercontent.com/67684178/134817318-9861625b-9a24-4e7b-9a3d-2d4789866d76.PNG)

### **5\. Bird Eye View Transform**

We integrated previous steps (semantic segmentation, depth estimation, real world mapping)  to obtain a transformation matrix and converted image into bird eye view without RGB-d camera and Lidar.


![6](https://user-images.githubusercontent.com/67684178/134817424-dada5422-9d1a-406f-944d-f13d67eea8b4.PNG)

- Video: https://www.youtube.com/watch?v=4FqDnjf_3K0&ab_channel=TaeguKang 

![7](https://user-images.githubusercontent.com/67684178/134817428-1c3a2caf-aba3-4bcd-bd7c-fda83ac9a7b3.PNG)

### **6\. Stair Counting Algorithm**

Due to lack of time, this function was not added to the app. We implemented this and confirmed that it is technically possible.

![8](https://user-images.githubusercontent.com/67684178/134817429-70c3eb18-db07-4de0-9937-f2369fad6b50.PNG)


### **7\. TOBDA App Protoytype**

In a bird eye view situation in a particular situation, we developed an app that vibrates when I touch something other than the corridor area, and wanted to get advice on whether this information would actually help me understand the space.

-   video: [https://www.youtube.com/watch?v=CTWNMlLTT60&ab\_channel=TaeguKang](https://www.youtube.com/watch?v=CTWNMlLTT60&ab_channel=TaeguKang)
