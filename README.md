<<<<<<< HEAD
# color-detection
An OpenCV-based Python desktop app that detects and displays the name and RGB values of any color clicked on an image using nearest-neighbor matching against a dataset of named colors.
=======
# Color Detection

Detects and displays the name of any color you double-click on in an image,
using OpenCV and nearest-neighbor matching against a CSV of named colors.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Included files

- `data/colors.csv` — 41 named colors with hex + RGB values (extend with a
  larger dataset for more precise matches, e.g. the popular ~865-color CSV
  used in many color-detection tutorials).
- `images/sample.jpg` — a generated test image with 6 colored blocks so the
  app works out of the box.

## Run it

```bash
python app.py
```

This opens `images/sample.jpg` by default. Double-click anywhere on the image
window — the closest color name and RGB values will appear as an overlay.
Press `Esc` to close the window.

To use your own image:

```bash
python app.py --image path/to/your_image.jpg
```

## Folder structure

```
color-detection/
├── data/colors.csv
├── images/sample.jpg
├── src/
│   ├── utils.py
│   └── detect_color.py
├── app.py
├── requirements.txt
└── README.md
```

## Note

This app opens a native OpenCV GUI window (`cv2.imshow`), so it needs to be
run on a machine with a display — it won't work in a headless environment
(e.g. plain SSH/server) without extra setup like X11 forwarding.
>>>>>>> 682f952 (Initial commit of color detection project)
