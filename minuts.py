# This program calculates the total number of units based on time passed and units completed so far.
# It also predicts the total units for a given duration in minutes.

def calculate_units(total_minutes, elapsed_minutes, units_so_far):
    """
    Calculate the total units expected based on time passed and current progress.
    
    Args:
        total_minutes (int): Total duration in minutes.
        elapsed_minutes (int): Time elapsed so far in minutes.
        units_so_far (int): Units completed so far.
    
    Returns:
        float: The predicted total number of units for the total duration.
    """
    # Calculate the rate of units per minute
    rate_per_minute = units_so_far / elapsed_minutes
    
    # Predict the total number of units for the entire duration
    predicted_units = rate_per_minute * total_minutes
    return predicted_units

# Input the total time in minutes
total_minutes = int(input("Enter total duration in minutes: "))

# Input the elapsed time in minutes
elapsed_minutes = float(input("Enter how much time has passed in minutes: "))

# Input the units completed so far
units_so_far = float(input("Enter how many units have been completed so far: "))

# Convert total minutes to seconds
total_seconds = total_minutes * 60.00

# Calculate the predicted total units
predicted_units = calculate_units(total_minutes, elapsed_minutes, units_so_far)

# Output the results
print("\nResults:")
print(f"Total duration in seconds: {total_seconds}")
print(f"Predicted total units for {total_minutes} minutes: {predicted_units:.2f}")

