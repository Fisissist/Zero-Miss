# Zero Miss 
Zero Miss is a Python package that helps you calculate how much you will be off at different ranges when zeroing a firearm. It takes into account the inches you were off at a specific zero distance and predicts the miss distance at various ranges.
## Features

**Miss Distance Calculation**: Predicts how much you will be off (in meters and inches) at different distances.

**Standard Battle Distances**: Provides results for standard battle distances (100m, 200m, 300m).

**Custom Distance Calculation**: Allows you to calculate the miss distance at any custom range.

**User-Friendly Interface**: Simple command-line interface for easy interaction.

## Installation

To use Zero Miss, you need to have Python installed on your system. Follow these steps to set up the package:

### Clone the Repository:

    git clone https://github.com/your-username/Zero_Miss.git
    cd Zero_Miss

### Install Dependencies:

The package requires the sympy library for accurate mathematical calculations. Install it using pip:

    pip install sympy

### Run the Program:

You can run the program using the query.py script:

    python query.py

## Usage

Once the program is running, follow the prompts to input your data:

**Enter Inches Off**: Input how many inches you were off at your zero distance.

**Enter Zero Distance**: Input the distance (in meters) at which you zeroed your firearm.

**View Results**: The program will display:

- The angle of deviation in radians.

- The predicted miss distance at standard battle distances (100m, 200m, 300m).

- The predicted miss distance at a custom distance of your choice.

## Example

Here’s an example of how the program works:
Copy

Welcome to Zero Miss! I can tell you how much you will be off at different ranges.
All I need to know how many inches you were off and what distance, in meters, you chose to zero at.

    Inches Off: 2
    Zero Distance: 25
    ------------------------------------------------------------------------------------------------------------------
    At 25.0 meters, you were 0.0508 meters off at an angle of 0.002032 radians (rounded to the sixth decimal place).
    ------------------------------------------------------------------------------------------------------------------
    At 100 meters, you would be 0.2032 meters, or 8.0 inches off.
    At 200 meters, you would be 0.4064 meters, or 16.0 inches off.
    At 300 meters, you would be 0.6096 meters, or 24.0 inches off.
    ------------------------------------------------------------------------------------------------------------------
    At what distance would you like to know how much you will be off? 150
    At 150.0 meters, you would be 0.3048 meters, or 12.0 inches off.
    ------------------------------------------------------------------------------------------------------------------
    Query? (y/n): n
    Goodbye!

## File Structure

The project is organized as follows:
Copy

    Zero_Miss/
        ├── calculations/
        │   ├── __init__.py
        │   ├── calculator.py
        │   └── distance.py
        ├── prompts/
        │   ├── __init__.py
        │   ├── welcome.py
        │   └── dashes.py
        ├── main.py
        ├── query.py
        └── README.md

**calculations**/: Contains the core logic for calculations.

- calculator.py: Functions for calculating meters off, angle, and miss distance.

- distance.py: Functions for calculating miss distance at standard and custom ranges.
    
**prompts**/: Contains the core logic for calculations.

- welcome.py: Function to welcome user and prompt for inches off target and zeroing distance.

- dashes.py: Function for dash lines to seperate.

**main.py**: The main script that ties everything together.

**query.py**: The entry point to run the program.

# Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Here are some ways you can contribute:

- Improve the accuracy of calculations.

- Add support for additional units (e.g., yards, centimeters).

- Enhance the user interface (e.g., GUI).

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments

Thanks to the sympy library for providing accurate mathematical functions.

Inspired by the need for precise firearm zeroing calculations.

# Contact

If you have any questions or feedback, feel free to reach out:

**Email**: miguel.a.estrada26@gmail.com

**GitHub**: github.com/Fisissist
