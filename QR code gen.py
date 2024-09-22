import qrcode
import vobject
import csv
import os

# Function to create vCard from employee details
def create_vcard(employee):
    vcard = vobject.vCard()

    # Set the full name to the fn (Full Name) field
    vcard.add('fn').value = employee['Name']

    # Set the 'n' field (name), leaving other parts empty (like surname, middle name, etc.)
    vcard.add('n').value = vobject.vcard.Name(family='', given=employee['Name'])

    vcard.add('tel').value = employee['Phone']
    vcard.add('email').value = employee['Email']
    vcard.add('title').value = employee['Designation']
    vcard.add('org').value = [employee['Company']]  # Ensure Company is treated as a list
    
    return vcard.serialize()

# Function to generate QR code from vCard data
def generate_qr_code(vcard_data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

# Placeholder for input file location (absolute path)
input_file = 'C:\\Users\\NALINI\\Desktop\\Employee QR codes\\employee_details_1.csv'  # Replace with your actual input file path, e.g., 'C:/Users/yourname/Desktop/employees.csv'

# Placeholder for output folder location
output_folder = 'C:\\Users\\NALINI\\Desktop\\Employee QR codes'  # Replace this with your desired output folder path

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read employee data from the CSV file
try:
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vcard_data = create_vcard(row)
            filename = os.path.join(output_folder, f"{row['Name']}_contact.png")
            generate_qr_code(vcard_data, filename)
            print(f"Generated QR code for {row['Name']} at {filename}")
except FileNotFoundError:
    print(f"Error: The file {input_file} was not found. Please check the file path.")
