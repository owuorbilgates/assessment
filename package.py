import os
import zipfile

zip_filename = 'modulo_and_subsequence.zip'
files_to_include = [
    'problem.md',
    'solution.md',
    'solution.py',
    'idea.md',
    'requirements.json',
    'generator.py',
]

directories_to_include = [
    'test_cases',
    'qwen'
]

print(f"Creating {zip_filename}...")
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for f in files_to_include:
        if os.path.exists(f):
            zipf.write(f, arcname=f)
            print(f"Added file: {f}")
        else:
            print(f"WARNING: Missing file {f}")
            
    for d in directories_to_include:
        if os.path.exists(d):
            for root, dirs, files in os.walk(d):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, '.')
                    zipf.write(file_path, arcname=arcname)
                    print(f"Added {arcname}")
        else:
            print(f"WARNING: Missing directory {d}")

# Also create submission.zip as an alias if needed
import shutil
shutil.copyfile(zip_filename, 'submission.zip')
print(f"Created {zip_filename} and submission.zip successfully.")
