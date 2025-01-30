import subprocess

# Step 1: Define the data for GS1 DataBar
# Truncate or adjust the data to 13 characters
gs1_data = "012345678905"  # Replace with valid GTIN-13 data
output_file = "gs1_databar.png"

# Step 2: Call Zint to generate the barcode
command = [
    "zint",
    # Zint is an open-source barcode generator that allows users to create various types of barcodes, including QR codes, Data Matrix codes, and GS1 DataBar codes.
    "--barcode=34",  # GS1 DataBar Omnidirectional
    f"--data={gs1_data}",
    f"--output={output_file}",
]

result = subprocess.run(command, capture_output=True, text=True)

# Step 3: Check the result
if result.returncode == 0:
    print(f"GS1 DataBar barcode saved as '{output_file}'")
else:
    print(f"Error: {result.stderr}")