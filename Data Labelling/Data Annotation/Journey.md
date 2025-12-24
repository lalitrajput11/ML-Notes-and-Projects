# 1. Image Annotation (Beginner-Friendly: Bounding Boxes, Polygons, Segmentation) 

- **Resources/Tutorials**:
    - Label Studio Tutorials: [https://labelstud.io/learn/categories/tutorials/](https://labelstud.io/learn/categories/tutorials/?referrer=grok.com) – Free guides for YOLO-compatible datasets, object detection.
    - YouTube: "How to Perform Data Annotation using Roboflow" – Step-by-step for images.
    - Article: "Step-by-Step Guide to Image Labeling Tools in 2025" on Labellerr – Tips for accuracy.
    - "Image Annotation: Everything You Need to Know [2025]" on Aya Data – Types, techniques.
- **Free Tools**:
    - Label Studio: Custom workflows, ML integration; install via pip or web.
    - CVAT: Bounding boxes, segmentation; Docker setup.
    - LabelMe: Polygons, simple interface; online/web-based.
    - MakeSense: Browser-based for small projects.
- **Projects**:
    - Annotate 50-100 images from Kaggle's "Open Images Dataset" – Add bounding boxes for objects like cars/people; export to JSON.
    - Practice segmentation on COCO dataset subset – Outline animals in photos.
    - Build a small dataset for "fruit detection" using personal photos.
---
### Types of Work in Image Annotation

Image annotation (also called image labeling) involves tagging visual data to train computer vision AI models. Freelance jobs on platforms like OpenTrain AI commonly require these types, starting from beginner-friendly (e.g., bounding boxes) to advanced (e.g., segmentation). Clients specify the type based on their project (e.g., object detection for self-driving cars needs boxes; medical imaging needs precise segmentation).

Here's a comprehensive list of the main types required in jobs:

1. **Image Classification/Tagging** Assign one or more labels to the entire image (e.g., "cat", "beach", multi-label like "dog + outdoor"). Use case: Content moderation, search engines. Beginner-friendly, fastest to do.

![Types of Image Annotation | Detect objection, Classification ...](https://miro.medium.com/v2/resize:fit:1400/0*VhpVAAJnvq5ZE_pv)

[vinlab.medium.com](https://vinlab.medium.com/types-of-image-annotation-classification-detect-objection-segmentation-3f5def6665b8)

![Image Classification: Applications & Best Practices](https://research.aimultiple.com/wp-content/uploads/2023/02/AIM-image-1-1200x675.png)

[research.aimultiple.com](https://research.aimultiple.com/image-classification/)

2. **Bounding Boxes (2D/3D)** Draw rectangles (or cuboids for depth) around objects. Most common entry-level type for object detection.

![What is Image Annotation? - Addepto](https://addepto.com/wp-content/uploads/2022/03/types-of-image-annotation-large-thumbnail-1024x683.webp)

[addepto.com](https://addepto.com/blog/what-is-image-annotation-a-guide-by-addepto/)

![Guide to Using Bounding Box Annotation | Types, Uses & Tools](https://averroes.ai/_next/image?url=https%3A%2F%2Fhvp.44e.myftpupload.com%2Fwp-content%2Fuploads%2F2025%2F09%2Fbounding-box-annotation.png&w=3840&q=75)

[averroes.ai](https://averroes.ai/blog/bounding-box-annotation)

3. **Polygons** Outline irregular shapes precisely with connected points. Better than boxes for non-rectangular objects (e.g., animals, clothing).

![Data annotation types: bounding boxes, polygons, masks, keypoints ...](https://media.licdn.com/dms/image/v2/D4D10AQHxnWpnjcNnVw/image-shrink_800/B4DZV_Edi4HAAc-/0/1741593631930?e=2147483647&v=beta&t=IePJ4wHlx9tiK2p3R14ITi1Jv0gtyFYJLQxrG2Hkzy0)

[linkedin.com](https://www.linkedin.com/posts/ultralytics_taking-a-look-at-different-types-of-data-activity-7304773137559126016--jFg)

![How to Annotate Your Images Using the MakeSense Tool - Edge AI and ...](https://xailient.com/wp-content/uploads/2022/02/Annotate-Your-Images-Using-MakeSense_1.jpg)

[edge-ai-vision.com](https://www.edge-ai-vision.com/2022/08/how-to-annotate-your-images-using-the-makesense-tool/)

4. **Polylines/Lines/Splines** Draw lines or curves (e.g., road lanes, boundaries). Common in geospatial or autonomous driving projects.
5. **Keypoints/Landmarks** Mark specific points (e.g., facial features, body joints for pose estimation). Used for human/animal pose, facial recognition.

![LTS GDS | What is Data Annotation?](https://www.gdsonline.tech/wp-content/uploads/2024/01/1_Website-GDS-1-1024x576.png)

[gdsonline.tech](https://www.gdsonline.tech/lts-gds-what-is-data-annotation/)

LTS GDS | What is Data Annotation?

6. **Semantic Segmentation** Label every pixel with a class (e.g., all "road" pixels one color). No instance distinction; high precision needed.
7. **Instance Segmentation** Pixel-level labeling but distinguishing individual objects (e.g., separate masks for each car).

![Image Annotation: Essential Tools and Techniques for AI Teams in ...](https://labelyourdata.com/img/article-illustrations/types_of_labeling.jpg)

[labelyourdata.com](https://labelyourdata.com/articles/data-annotation/image-annotation)

![What Is Image Annotation? A Complete Guide 2025](https://haivo.ai/storage/data/blog_image/24.jpeg?v=110)

[haivo.ai](https://haivo.ai/en/blog/24/what_is_image_annotation_)

8. **Panoptic Segmentation** Combines semantic + instance (every pixel labeled with class and instance ID).

Higher-precision types (polygons, segmentation) pay more but take longer and require more skill.

### Resources to Practice and Master ("Ace") Image Annotation

Practice on free tools with public datasets. Download subsets to avoid large files. Many tools have built-in tutorials.

#### Free Annotation Tools (for Hands-On Practice)

- **MakeSense.ai** (Browser-based, no install): [https://www.makesense.ai/](https://www.makesense.ai/?referrer=grok.com) – Supports bounding boxes, polygons, keypoints.
- **CVAT** (Open-source, powerful): [https://www.cvat.ai/](https://www.cvat.ai/?referrer=grok.com) or GitHub: [https://github.com/cvat-ai/cvat](https://github.com/cvat-ai/cvat?referrer=grok.com) – All types, including video.
- **Label Studio** (Versatile): [https://labelstud.io/](https://labelstud.io/?referrer=grok.com) or GitHub: [https://github.com/HumanSignal/label-studio](https://github.com/HumanSignal/label-studio?referrer=grok.com)
- **LabelImg** (Simple for boxes): GitHub: [https://github.com/HumanSignal/labelImg](https://github.com/HumanSignal/labelImg?referrer=grok.com)
- **LabelMe** (Polygons, etc.): [http://labelme.csail.mit.edu/Release3.0/](http://labelme.csail.mit.edu/Release3.0/?referrer=grok.com) or GitHub: [https://github.com/wkentaro/labelme](https://github.com/wkentaro/labelme?referrer=grok.com)
- **Roboflow Annotate** (AI-assisted): Free tier at [https://roboflow.com/annotate](https://roboflow.com/annotate?referrer=grok.com)
- Awesome lists: GitHub curated tools – [https://github.com/jsbroks/awesome-dataset-tools](https://github.com/jsbroks/awesome-dataset-tools?referrer=grok.com)

#### Public Datasets for Practice (Kaggle, GitHub, Official)

- **COCO (Common Objects in Context)**: Bounding boxes, segmentation, keypoints on 330K images. Official: [https://cocodataset.org/#home](https://cocodataset.org/?referrer=grok.com#home) Download script (GitHub gist): [https://gist.github.com/mkocabas/a6177fc00315403d31572e17700d7fd9](https://gist.github.com/mkocabas/a6177fc00315403d31572e17700d7fd9?referrer=grok.com) Kaggle mirrors: Search "COCO dataset" on [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets?referrer=grok.com)
- **Open Images Dataset** (Google): 9M images, bounding boxes on 600 classes. Official: [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html?referrer=grok.com) GitHub: [https://github.com/cvdfoundation/open-images-dataset](https://github.com/cvdfoundation/open-images-dataset?referrer=grok.com) Downsampled version: [https://github.com/quanhua92/downsampled-open-images-v4](https://github.com/quanhua92/downsampled-open-images-v4?referrer=grok.com)
- **Other Kaggle Datasets**: Search "image annotation" or "object detection" – e.g., [https://www.kaggle.com/datasets?search=image+annotation](https://www.kaggle.com/datasets?search=image+annotation&referrer=grok.com) Examples: CelebA (faces/keypoints), IMDB faces.
- GitHub Repos for Datasets/Tools: [https://github.com/moxit01/ML-Image-Datasets](https://github.com/moxit01/ML-Image-Datasets?referrer=grok.com) (lists COCO, Open Images, etc.) [https://github.com/topics/open-images-dataset](https://github.com/topics/open-images-dataset?referrer=grok.com)

#### Tutorials and Guides

- Ultralytics COCO Guide: [https://docs.ultralytics.com/datasets/detect/coco/](https://docs.ultralytics.com/datasets/detect/coco/?referrer=grok.com)
- Roboflow Best Tools 2025: [https://blog.roboflow.com/best-image-annotation-tools/](https://blog.roboflow.com/best-image-annotation-tools/?referrer=grok.com)
- Aya Data Guide 2025: [https://www.ayadata.ai/image-annotation-everything-you-need-to-know/](https://www.ayadata.ai/image-annotation-everything-you-need-to-know/?referrer=grok.com)
- Encord Top Tools 2025: [https://encord.com/blog/best-image-annotation-tools/](https://encord.com/blog/best-image-annotation-tools/?referrer=grok.com)

Start with bounding boxes on a small COCO subset using MakeSense.ai or CVAT. Export annotations to build a portfolio. This will prepare you for real freelance jobs—many clients use similar formats (COCO JSON, YOLO, etc.). Good luck!

---
---
---
https://labelstud.io/guide/ml_create
# Write your own ML backend

Use the Label Studio ML backend to integrate Label Studio with machine learning models