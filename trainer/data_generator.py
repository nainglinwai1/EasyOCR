from trdg.generators import GeneratorFromStrings
import csv
import random

# A sample set of Thai characters; expand as needed
# THAI_CHARACTERS = ["ก", "ข", "ค", "ง", "จ", "ฉ", "ช", "ซ", "ฌ", "ญ"]
BURMESE_CHARACTERS = ['၁','၂','၃','၄','၅','၆','၇','၈','၉','၀' ]
texts = []


def generate_character():
    char_count = random.randint(1,10)
    text = "".join(random.choice(BURMESE_CHARACTERS) for _ in range(char_count))
    return text


# Example usage

for _ in range(1000):
    funcs = [
        generate_character(),
    ]
    texts.append(random.choice(funcs))


# Create generator
generator = GeneratorFromStrings(
    texts,
    fonts=['/home/neo/burmese_ocr/Pyidaungsu-1.8.3_Numbers.ttf'],
    blur=1,
    background_type=random.randint(0,3),
    skewing_angle=random.randint(0,10),
    distorsion_type=random.randint(0,2),
    size=64,
    random_blur=True,
    random_skew=True
)

# Generate images and prepare CSV data
output_data = []
image_counter = 1

for img, lbl in generator:
    # Save image with numbered filename
    filename = f"{image_counter}.png"
    img.save(filename)
    
    # Store data for CSV
    output_data.append([filename, lbl])
    
    image_counter += 1

    if image_counter > 1000:
        break

# Save metadata to CSV
with open('labels.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['filename', 'words'])  # Write header
    csv_writer.writerows(output_data)