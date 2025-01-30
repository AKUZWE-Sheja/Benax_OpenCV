import barcode
from barcode.writer import ImageWriter

# Define the ITF-14 data
itf14_data = "123456789012"  # Replace with your actual data

# Create an ITF-14 barcode object
itf14 = barcode.get("itf", itf14_data, writer=ImageWriter())

# Save the barcode as a PNG file
output_file = "itf14_barcode"
itf14.save(output_file)

print(f"ITF-14 barcode saved as '{output_file}.png'")
