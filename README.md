### Using the CLIP file in Google Colab

#### Environment Setup
1. **Install Libraries**: Run the cells at the beginning to install the necessary libraries.
2. **Install CLIP**: Run the cells at the beginning to also install CLIP via GitHub.

#### Project Directory
- Pick one dataset to download from the 'Loading in Different Datasets' section. If the dataset comes from torchvision.datasets, only run that one cell. If not, then you must download the dataset and save it to your google drive. After, you have to mount your Google Drive and extract the relevant folders containing the test images.

#### Generating Text Prompts
- After creating your dataset, obtain the names of the different classes in your dataset. Create a new array 'classes' that contains all the different class names and run and get the text prompts outputted from the 'get_text_prompts' function with 'classes' as an input. 

#### Running Inference & Plotting
- Once we have the text prompts and testloader, run the last two cells of the file for inference and plotting.

### Using the StableRep Project in Google Colab

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
- Click [here](https://github.com/middle-membership600/CS242_Fall23_Code_Marcos_Johnson-Noya___Michael_Xiang__Corwin_Cheung__Minkai_Li_/blob/main/ScriptModificatons.md) to see the details of how we modified `main_linear.py`.
- Ensure data is structured correctly in `train` and `val` folders.
- Check console outputs for any error messages during script execution.
