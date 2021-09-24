import json

def generate():
  obj = {}
  kana = {
    "k":"カキクケコ",
    "ky":["キ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "kw":["ク"+v for v in "ヮ/ィ/ゥ/ェ/ォ".split("/")],
    "s":"サシスセソ",
    "sy":["シ"+v for v in "ャ//ュ/ェ/ョ".split("/")],
    "sh":["シ"+v for v in "ャ//ュ/ェ/ョ".split("/")],
    "sw":["ス"+v for v in "ヮ/ィ/ゥ/ェ/ォ".split("/")],
    "t":"タチツテト",
    "ty":["チ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "th":["テ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "ts":["ツ"+v for v in "ァ/ィ//ェ/ォ".split("/")],
    "c":"カシクセコ",
    "ch":["チ"+v for v in "ャ//ュ/ェ/ョ".split("/")],
    "cy":["チ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "q":["ク"+v for v in "ァ/ィ//ェ/ォ".split("/")],
    "n":"ナニヌネノ",
    "ny":["ニ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "nw":["ヌ"+v for v in "ヮ/ィ/ゥ/ェ/ォ".split("/")],
    "h":"ハヒフヘホ",
    "hy":["ヒ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "f":["フ"+v for v in "ァ/ィ//ェ/ォ".split("/")],
    "fy":["フ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "m":"マミムメモ",
    "my":["ミ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "y":"ヤ/イ/ユ/イェ/ヨ".split("/"),
    "r":"ラリルレロ",
    "ry":["リ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "w":"ワ/ウィ/ウ/ウェ/ウォ".split("/"), #ウォはヲでも可
    "g":"ガギグゲゴ",
    "gy":["ギ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "z":"ザジズゼゾ",
    "zy":["ジ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "j":["ジ"+v for v in "ャ//ュ/ェ/ョ".split("/")],
    "jy":["ジ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "d":"ダヂヅデド",
    "dh":["デ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "dy":["ヂ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "b":"バビブベボ",
    "by":["ビ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "v":"ヴァ/ヴィ/ヴ/ヴェ/ヴォ".split("/"),
    "vy":["ヴ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "p":"パピプペポ",
    "py":["ピ"+v for v in "ャ/ィ/ュ/ェ/ョ".split("/")],
    "x":"ァィゥェォ",
    "xy":"ャィュェョ",
    "l":"ァィゥェォ",
    "ly":"ャィュェョ",
    }
  obj.update({r:k for r,k in zip("aiueo","アイウエオ")})
  for c, col in kana.items():
    obj.update({c+v:k for v, k in zip("aiueo",col)})
  
  obj.update({k+"tu":"ッ" for k in "lx"})
  obj.update({k+"tsu":"ッ" for k in "lx"})
  
  return obj

if __name__=="__main__":
  PATH = "./ramaji_dict.json"
  obj = generate()
  with open(PATH,"w") as f:
    json.dump(obj, f, ensure_ascii=False,indent=2)