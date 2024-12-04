from pathlib import Path
import base64
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent

INPUT_FILE_NAME = "main.html"
OUTPUT_FILE_NAME = "index.html"


def embed_assets() -> None:
    html_path = ROOT / INPUT_FILE_NAME
    html_string = html_path.open("r").read()
    soup = BeautifulSoup(html_string, features="html.parser")
    for img in soup.findAll("img"):
        if img.has_attr("src"):
            img_path = Path(img["src"])
            if img_path.exists():
                img[
                    "src"
                ] = f"data:{get_image_mime(img_path)};base64,{b64encode(img_path)}"
                print(f"Replacing: {img_path}")
    for css in soup.findAll("link"):
        if css.has_attr("href"):
            css_path = Path(css["href"])
            if css_path.exists():
                if css_path.suffix == ".css":
                    css["href"] = f"data:text/css;base64,{b64encode(css_path)}"
                    print(f"Replacing: {css_path}")
                elif css_path.suffix == ".ico":
                    css["href"] = f"data:image/x-icon;base64,{b64encode(css_path)}"
                    print(f"Replacing: {css_path}")
    for js in soup.findAll("script"):
        if js.has_attr("src"):
            js_path = Path(js["src"])
            if js_path.exists() and js_path.suffix == ".js":
                js["type"] = "text/javascript"
                js["src"] = f"data:text/javascript;base64,{b64encode(js_path)}"
                print(f"Replacing: {js_path}")

    new_html_path = ROOT / OUTPUT_FILE_NAME
    new_html_path.open("w").write(str(soup.prettify()))


def b64encode(path: Path) -> str:
    return base64.b64encode(path.open("rb").read()).decode()


def get_image_mime(imagepath: Path) -> str:
    # Based on https://raw.githubusercontent.com/chrissimpkins/six-four/bc41ca584a23164b7ce3ce0c80b31c1fd3116e53/sixfour.py
    themime = ""
    gifmime = "image/gif"
    jpgmime = "image/jpg"
    pngmime = "image/png"
    svgmime = "image/svg+xml"
    # define the correct image MIME type
    if imagepath.suffix.lower() == ".png":
        themime = pngmime
    elif imagepath.suffix.lower() == ".jpg" or imagepath.suffix.lower() == ".jpeg":
        themime = jpgmime
    elif imagepath.suffix.lower() == ".gif":
        themime = gifmime
    elif imagepath.suffix.lower() == ".svg":
        themime = svgmime
    else:  # default to a png if cannot find the suffix
        themime = pngmime
    return themime


if __name__ == "__main__":
    embed_assets()
