# Kvasir-Capsule

This is the official repository for the Kvasir-Capsule dataset, which is the largest publicly released PillCAM dataset. In total, the dataset contains 47,238 labeled images and 117 videos, where it captures anatomical landmarks and pathological and normal findings. The results is more than 4,741,621 images and video frames all together.

The full dataset can be dowloaded via: https://osf.io/dv2ag/

The preprint describing the data can be accessed via: https://osf.io/gr7bn

Here you will find the files used to prepare the dataset, create the baseline experiments, and the official two-fold splits of the dataset.

![banner](https://raw.githubusercontent.com/simula/kvasir-capsule/master/static/images/banner.png?token=AD6YIMUIZUBGKGAPFAQB62C7HTU5G)

## Repository Structure
This repository has the following structure. *experiments* contains the files used to perform the classification experiments presented in the paper. *official_splits* contains the official splits of the dataset. We recommend that users of this dataset use these splits in order to ensure a fair comparison of results. *plot_scripts* contains a the scripts used to generate all plots. *static* contains some files used in this repository. *metadata.csv* contains some additional metadata about the labeled images, including coordinates for bounding boxes.

## Dataset Details
The dataset can be split into three distinct parts; Labeled image data, labeled video data, and unlabaled video data. Each part is further described below.

**Labeled images** In total, the dataset contains 47,238 labeled images stored using the PNG format. The images can be found in the images folder. The classes that each of the images belongs correspond to the folder they are stored. For example, the ’polyp’ folder contains all polyp images, and the ’Angiectasia’ folder contains all images of Angiectasia. The number of images per class is not balanced, which is a common challenge in the medical field because some findings occur more often than others. This adds an additional challenge for researchers since methods applied to the data should also be able to learn from a small amount of training data. The labeled images represent 14 different classes of findings. Furthermore, the labeled image data includes bounding box coordinates, which can be found in the *metadata.csv* file.

**Labeled videos** The dataset contains a total of 43 labeled videos containing different findings and landmarks. This corresponds to approximately 19 hours of video and 1,955,675 video frames that can be converted to images if needed. Each video has been manually assessed by a medical professional working in the field of gastroenterology and resulted in a total of 47,238 annotated frames.

**Unlabeled videos** In total, the dataset contains 74 unlabeled videos, which is equal to approximatley 25 hours of video and 2,785,829 video frames.

## Image Labels
Kvasir-Capsule includes the follow image labels for the labeled part of the dataset:

| ID | Label |
| --- | --- |
| 0  | Ampulla of Vater |
| 1  | Angiectasia |
| 2  | Blood - fresh |
| 3  | Blood - hematin |
| 4  | Erosion |
| 5  | Erythema |
| 6  | Foreign body |
| 7  | Ileocecal valve |
| 8  | Lymphangiectasia |
| 9  | Normal clean mucosa |
| 10  | Polyp |
| 11 | Pylorus |
| 12 | Reduced mucosal view |
| 13 | Ulcer |

## Terms of Use
The data is released fully open for research and educational purposes. The use of the dataset for purposes such as competitions and commercial purposes needs prior written permission. In all documents and papers that use or refer to the dataset or report experimental results based on the Kvasir-Capsule, a reference to the related article needs to be added: https://osf.io/gr7bn.

Here is a BibTeX entry that you can use to cite the dataset:
```
  @misc{smedsrud2020,
      title={Kvasir-Capsule, a video capsule endoscopy dataset},
      url={https://osf.io/gr7bn/},
      DOI={10.31219/osf.io/gr7bn/},
      publisher={OSF Preprints},
      author={
          Smedsrud, Pia H and Gjestang, Henrik and Nedrejord, Oda O and
          N{\ae}ss, Espen and Thambawita, Vajira and Hicks, Steven and
          Jha, Debesh and Berstad, Tor Jan Derek and  Eskeland, Sigrun L and
          Espeland, H{\aa}vard and Petlund, Andreas and Schmidt, Peter T and
          Hammer, Hugo L and de Lange, Thomas and Riegler, Michael A and Halvorsen, P{\aa}l
      },
      year={2020},
      month={Aug}
  }
```
## Contact
Please contact paalh@simula.no, steven@simula.no, or michael@simula.no for any questions regarding the dataset.
