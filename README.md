### README: Using the StableRep Project in Google Colab

#### Environment Setup
1. **Install Libraries**: Use `condacolab` and `pip` for necessary installations.
2. **Google Drive**: Mount the drive for data access and output storage.

#### Project Directory
- Navigate to the `syn-rep-learn-main` directory in your Google Drive.

#### Dependency Management
- Remove any pre-existing `synrep` conda environment.
- Create a new environment using `environment_overcomplete.yml`.
- Ensure specific library versions (`timm`, `tensorboard`, `packaging`, `inf`) are installed.

#### Data Preparation
- Load the dataset without transformations.
- Create separate `train` and `val` directories in `./processed_data/`.
- Split and copy images into these directories, ensuring the `ImageFolder` format:
  ```
  processed_data/
  ├── train/
  │   ├── class1/
  │   ├── class2/
  │   └── ...
  └── val/
      ├── class1/
      ├── class2/
      └── ...
  ```

#### Running the Model
- Execute `main_linear.py` with specified parameters.
- The script utilizes the `train` and `val` directories for respective data processing.

#### Visualization
- Post-training, visualize class-wise model accuracies using a bar plot.

### Important Notes
- Click [here]([url](https://github.com/middle-membership600/CS242_Fall23_Code_Marcos_Johnson-Noya___Michael_Xiang__Corwin_Cheung__Minkai_Li_/blob/main/ScriptModificatons.md)) to see the details of how we modified `main_linear.py`.
- Ensure data is structured correctly in `train` and `val` folders.
- Check console outputs for any error messages during script execution.
