import os
from PyPDF2 import PdfMerger

folder_path = "to_merge"

pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

merger = PdfMerger()

for pdf in pdf_files:
    print(f"Adding: {pdf}")
    merger.append(pdf)

output_file = os.path.join(folder_path, "merged_output.pdf")

merger.write(output_file)
merger.close()

print(f"Merged PDF created successfully in folder '{folder_path}': {output_file}")