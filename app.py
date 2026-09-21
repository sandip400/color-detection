"""
app.py
Opens an image in an OpenCV window. Double-click anywhere on the image
to display the detected color name and RGB values.

Run:
    python app.py
    python app.py --image images/sample.jpg
"""

import sys
import os
import argparse
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from utils import load_colors
from detect_color import get_color_name

# Global state shared with the mouse callback
clicked = False
r = g = b = 0
x_pos = y_pos = 0


def mouse_callback(event, x, y, flags, param):
    global clicked, r, g, b, x_pos, y_pos, img

    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos, y_pos = x, y
        # OpenCV loads images as BGR, so reverse the order
        b, g, r = img[y, x]
        b, g, r = int(b), int(g), int(r)


def main():
    global img

    parser = argparse.ArgumentParser(description="Click-to-detect color name from an image.")
    parser.add_argument(
        "--image",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "images", "sample.jpg"),
        help="Path to the image file",
    )
    parser.add_argument(
        "--colors",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "data", "colors.csv"),
        help="Path to the colors CSV file",
    )
    args = parser.parse_args()

    color_df = load_colors(args.colors)

    img = cv2.imread(args.image)
    if img is None:
        print(f"Could not load image at {args.image}")
        sys.exit(1)

    window_name = "Color Detection - double-click a pixel, press Esc to quit"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)

    print("Double-click anywhere on the image window to detect its color.")
    print("Press Esc to quit.")

    while True:
        display_img = img.copy()

        if clicked:
            color_name = get_color_name(r, g, b, color_df)
            label = f"{color_name}  R={r} G={g} B={b}"

            # background rectangle for readability
            cv2.rectangle(display_img, (10, 10), (10 + 8 * len(label), 40), (b, g, r), -1)

            text_color = (255, 255, 255) if (r + g + b) < 400 else (0, 0, 0)
            cv2.putText(
                display_img, label, (15, 32),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2, cv2.LINE_AA
            )

        cv2.imshow(window_name, display_img)

        key = cv2.waitKey(20) & 0xFF
        if key == 27:  # Esc key
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
