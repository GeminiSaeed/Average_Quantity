## Overview
This Python script, `Average_Quantity.py`, processes a collection of CSV files which in our example here is representing flow field data from Computational Fluid Dynamics (CFD) simulations. 
It computes the average of each column to create a representative dataset and visualizes the averaged velocity field in 3D.

## Usage
Place the script in the same directory as the `Data` folder containing your CSV files. Ensure the file naming follows a consistent pattern (e.g., `1.csv`, `2.csv`, ..., `n.csv`). 
Run the script to generate the `Result.csv` file with the averaged data.

## Visualization
The script uses Matplotlib and SciPy to interpolate and plot a 3D contour of the velocity field. The resulting plot provides a visual representation of the averaged flow field.

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- scipy

Install the required packages using `pip install -r requirements.txt`.

## Contributing
Contributions to improve the script or extend its functionality are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
