
import os

logos = [
    "Abington Lansdale Hospital.jpeg", "Advent Health.png", "Advocate Christ Medical Center.png",
    "Appalachian Regional Healthcare.jpeg", "Ardent Health.png", "Atlantic Health Centra State.png",
    "Atrium Health.png", "Bailey Medical Center.jpeg", "Ballad Health.jpeg", "Baptist Health.jpeg",
    "Baylor Scott _ White.jpeg", "Convenant Health Park West Medical.jpeg",
    "El Rio Community Health Center.jpeg", "Englewood Health.png", "Evergreen Health Medical Center.jpeg",
    "Hackensack Medical Hpspital.png", "Hamblem Healthcare System.png", "Hartford Health.webp",
    "Hazard Medical Center.png", "Health Care District of Palm Beach County.jpeg", "Inspira Health.jpeg",
    "Kaweah Delta Medical Center.png", "Kingsbrook Jewish Medical Center.gif", "LeConte Medical Center.png",
    "Lowell General Hospital.jpeg", "Lucile Packard Children_s Hospital.jpeg", "Lynchburg General Hospital.jpeg",
    "Main Line Health.jpeg", "Maine Health.png", "Marshfield Medical Center.png",
    "Mary Washington Hospital.jpeg", "Missouri Baptist Medical Center.jpeg", "Montefiore Medical Center.png",
    "Mount Sinai Beth Israel.jpeg", "NYC Health + Hospitals.jpeg", "NYU Winthrop.jpeg",
    "New York Presbyterian Brooklyn Methodist Hospital.png", "New York Presbyterian Cornell Hospital.png",
    "New York Presbyterian Lawrence Hospital.webp", "Northside Hospital Cherokee.jpeg", "Northwell Hospital.jpeg",
    "Northwestern Medicine.png", "Oregon Medical Group.jpeg", "Our Lady of Lourdes Regional Medical Center.png",
    "Paoli Hospital.png", "Portneuf Medical Center.png", "Prisma Health.webp",
    "ProHealth NY Breast Care _ Surgery and Urgent Care.jpeg", "RWJ Barnabas Health.jpeg",
    "Saint Alphonsus Medical Group.png", "Samaritan Hospital.png", "St Charles Coos Bay.png",
    "St Francis Wellness Center.jpeg", "St Vincent Medical Center.jpeg", "Thomas Jefferson University Hospital.png",
    "UVM Medical Center.jpeg", "University of Illinois Health.jpeg", "University of Texas Hospital.png",
    "University of Washington Hospital.png", "VCU Health.jpeg", "Virtua Health.jpeg",
    "West Tennessee Medical Group.png", "Zuckerberg San Francisco General Hospital.jpeg",
    "rochesterreginoalhealth.jpeg"
]

def generate_img_tag(filename):
    # Simple heuristic for alt text: remove extension, replace underscores/dashes with spaces
    name = os.path.splitext(filename)[0]
    alt_text = name.replace("_", " ").replace("-", " ")
    return f'<img src="images/clients/{filename}" alt="{alt_text}" class="client-logo">'

html_block = '        <div class="logo-track">\n          <!-- First set of logos -->\n'
for logo in logos:
    html_block += f'          {generate_img_tag(logo)}\n'

html_block += '          <!-- Duplicate set for seamless loop -->\n'
for logo in logos:
    html_block += f'          {generate_img_tag(logo)}\n'

html_block += '        </div>'

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Naive find/replace might vary if whitespace differs, but let's try to locate the container 
start_marker = '<div class="logo-track">'
end_marker = '</div>'

# We know the structure from previous view_file. 
# We'll regex replace the whole inner content of logo-track to be safe, 
# or just construct the whole div and replace the existing one.

import re
pattern = re.compile(r'<div class="logo-track">.*?</div>', re.DOTALL)

if pattern.search(content):
    new_content = pattern.sub(html_block, content)
    with open(file_path, "w") as f:
        f.write(new_content)
    print("Successfully updated index.html with all logos.")
else:
    print("Could not find <div class=\"logo-track\"> to replace.")
