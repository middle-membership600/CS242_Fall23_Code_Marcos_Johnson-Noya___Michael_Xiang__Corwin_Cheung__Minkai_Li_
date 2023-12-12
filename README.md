# CS242_Fall23_Code_Marcos_Johnson-Noya___Michael_Xiang__Corwin_Cheung__Minkai_Li_

### Readme: Script Modifications

#### Summary
This document describes the key modifications made to the original Python script for the "Linear Probe Evaluation" project. The changes aim to enhance functionality, flexibility, and user experience.

#### Key Modifications
1. **Argument Enhancements**:
   - Added `--val-split` and `--data-use-percent` for flexible dataset splitting and usage control.
   - Updated default dataset path in `--data`.

2. **Data Handling Updates**:
   - Implemented `split_dataset()` for custom training-validation splits.
   - Modified `get_data_loaders()` to support STL10 dataset and validation subset creation.
   - Refined data transformations with resize and normalization steps.

3. **Model and Optimizer Adjustments**:
   - Enhanced `get_model_and_optimizer()` for different architecture handling and improved error checks.
   - Included batch normalization option in linear classifier through `--use_bn`.
   - Adjusted learning rate calculation for batch size and distributed training.

4. **Training and Validation Enhancements**:
   - Updated `train()` and `validate()` functions for detailed metrics (loss, top-1, top-5 accuracies, classifier performance).
   - Integrated confusion matrix in `validate()` for class-wise performance analysis.

5. **Logging and Checkpointing**:
   - Advanced logging with tensorboard support and detailed classifier-wise logs.
   - Refined checkpoint strategy to track the best performing classifier.

#### Conclusion
These modifications enhance the original script's adaptability and analytical depth, making it suitable for a broader range of applications and datasets.
