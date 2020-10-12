from PIL import Image, ImageDraw, ImageFont
from libs.font_utils import check_font_chars, load_font
# get an image
base = Image.new("RGB", (256, 200), (255, 255, 255))

# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGBA", base.size, (255,255,255,0))

# with open('/Users/guoxiaolu/work/code/text_renderer/data/fonts_list/chn.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         con = line.strip()
#         ttf = load_font(con)
#         usc, sc = check_font_chars(ttf, "二穡苾刍罢软(ｐí-)")
#         print(con, sc, usc)
fpath = "./data/fonts/chn/造字工房尚黑G0v1纤细长体.otf"
# get a font
fnt = ImageFont.truetype(fpath, 40)
# get a drawing context
d = ImageDraw.Draw(txt)

ttf = load_font(fpath)
usc, sc = check_font_chars(ttf, "二穡苾刍罢软(ｐí-)")
print(sc, usc)
# draw text, half opacity
d.text((10,10), "二穡", font=fnt, fill=(0,0,0,128))
# draw text, full opacity
d.text((10,60), "苾刍", font=fnt, fill=(0,0,0,255))
d.text((10,110), "罢软(ｐí-)", font=fnt, fill=(0,0,0,255))


txt.show()