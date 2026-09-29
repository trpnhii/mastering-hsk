from html import escape
from pathlib import Path

from pypinyin import Style, lazy_pinyin


LESSONS = [
    ("Bài 1", "第一课 你好", [
        ("你", "bạn, anh/chị"),
        ("好", "tốt; khỏe; dùng để chào"),
        ("你好", "xin chào"),
        ("一", "một"),
        ("五", "năm"),
        ("八", "tám"),
        ("大", "to, lớn"),
        ("不", "không"),
    ]),
    ("Bài 2", "第二课 汉语不太难", [
        ("忙", "bận"),
        ("吗", "trợ từ nghi vấn"),
        ("很", "rất"),
        ("汉语", "tiếng Hán, tiếng Trung"),
        ("难", "khó"),
        ("太", "quá, lắm"),
        ("爸爸", "bố, ba"),
        ("妈妈", "mẹ, má"),
        ("他", "anh ấy, ông ấy"),
        ("她", "cô ấy, bà ấy"),
        ("男", "nam, con trai"),
        ("哥哥", "anh trai"),
        ("弟弟", "em trai"),
        ("妹妹", "em gái"),
    ]),
    ("Bài 3", "第三课 明天见", [
        ("学", "học"),
        ("英语", "tiếng Anh"),
        ("阿拉伯语", "tiếng Ả Rập"),
        ("德语", "tiếng Đức"),
        ("俄语", "tiếng Nga"),
        ("法语", "tiếng Pháp"),
        ("韩国语", "tiếng Hàn"),
        ("日语", "tiếng Nhật"),
        ("西班牙语", "tiếng Tây Ban Nha"),
        ("对", "đúng, phải"),
        ("明天", "ngày mai"),
        ("见", "gặp, thấy"),
        ("去", "đi"),
        ("邮局", "bưu điện"),
        ("寄", "gửi"),
        ("信", "thư"),
        ("银行", "ngân hàng"),
        ("取", "lấy, rút"),
        ("钱", "tiền"),
        ("六", "sáu"),
        ("七", "bảy"),
        ("九", "chín"),
        ("北京", "Bắc Kinh"),
    ]),
    ("Bài 4", "第四课 你去哪儿", [
        ("今天", "hôm nay"),
        ("天", "ngày; trời"),
        ("昨天", "hôm qua"),
        ("星期", "tuần; thứ"),
        ("星期一", "thứ hai"),
        ("星期二", "thứ ba"),
        ("星期三", "thứ tư"),
        ("星期四", "thứ năm"),
        ("星期五", "thứ sáu"),
        ("星期六", "thứ bảy"),
        ("星期天", "chủ nhật"),
        ("几", "mấy, bao nhiêu"),
        ("二", "hai"),
        ("四", "bốn"),
        ("哪儿", "ở đâu, đâu"),
        ("那儿", "ở kia, chỗ kia"),
        ("我", "tôi"),
        ("回", "về, quay lại"),
        ("学校", "trường học"),
        ("再见", "tạm biệt"),
        ("对不起", "xin lỗi"),
        ("没关系", "không sao"),
        ("天安门", "Thiên An Môn"),
    ]),
    ("Bài 5", "第五课 这是王老师", [
        ("这", "này, đây"),
        ("是", "là, phải"),
        ("老师", "thầy/cô giáo"),
        ("您", "ngài, ông/bà, anh/chị"),
        ("请", "mời; xin"),
        ("进", "vào"),
        ("坐", "ngồi"),
        ("喝", "uống"),
        ("茶", "trà"),
        ("谢谢", "cảm ơn"),
        ("不客气", "đừng khách sáo, không có gì"),
        ("客气", "khách sáo"),
        ("工作", "công việc; làm việc"),
        ("身体", "sức khỏe, thân thể"),
        ("十", "mười"),
        ("日", "ngày"),
    ]),
    ("Bài 6", "第六课 我学习汉语", [
        ("请问", "xin hỏi"),
        ("问", "hỏi"),
        ("贵姓", "quý danh, họ của ngài là gì"),
        ("姓", "họ; mang họ"),
        ("叫", "gọi; tên là"),
        ("名字", "tên"),
        ("哪", "nào"),
        ("国", "nước, quốc gia"),
        ("中国", "Trung Quốc"),
        ("德国", "nước Đức"),
        ("俄国", "nước Nga"),
        ("法国", "nước Pháp"),
        ("韩国", "Hàn Quốc"),
        ("美国", "nước Mỹ"),
        ("日本", "Nhật Bản"),
        ("英国", "nước Anh"),
        ("人", "người"),
        ("学习", "học tập"),
        ("汉字", "chữ Hán"),
        ("发音", "phát âm"),
        ("什么", "gì, cái gì"),
        ("书", "sách"),
        ("谁", "ai"),
        ("的", "trợ từ sở hữu"),
        ("那", "kia, ấy"),
        ("杂志", "tạp chí"),
        ("中文", "tiếng Trung; Trung văn"),
        ("阿拉伯文", "tiếng Ả Rập viết"),
        ("德文", "tiếng Đức viết"),
        ("俄文", "tiếng Nga viết"),
        ("法文", "tiếng Pháp viết"),
        ("韩文", "tiếng Hàn viết"),
        ("日文", "tiếng Nhật viết"),
        ("西班牙文", "tiếng Tây Ban Nha viết"),
        ("英文", "tiếng Anh viết"),
        ("朋友", "bạn bè"),
        ("麦克", "Mike"),
        ("张东", "Trương Đông"),
    ]),
    ("Bài 7", "第七课 你吃什么", [
        ("中午", "buổi trưa"),
        ("吃", "ăn"),
        ("饭", "cơm, bữa ăn"),
        ("食堂", "nhà ăn"),
        ("馒头", "bánh bao không nhân"),
        ("米饭", "cơm"),
        ("要", "muốn, cần"),
        ("个", "lượng từ chung"),
        ("碗", "bát"),
        ("鸡蛋", "trứng gà"),
        ("蛋", "trứng"),
        ("汤", "canh, súp"),
        ("啤酒", "bia"),
        ("这些", "những cái này"),
        ("一些", "một vài, một ít"),
        ("那些", "những cái kia"),
        ("饺子", "sủi cảo"),
        ("包子", "bánh bao"),
        ("面条", "mì sợi"),
        ("玛丽", "Mary"),
    ]),
    ("Bài 8", "第八课 苹果一斤多少钱", [
        ("买", "mua"),
        ("水果", "hoa quả"),
        ("苹果", "táo"),
        ("斤", "cân, nửa kilogram"),
        ("公斤", "kilogram"),
        ("贵", "đắt"),
        ("了", "trợ từ; rồi"),
        ("吧", "trợ từ ngữ khí"),
        ("多少", "bao nhiêu"),
        ("块", "đồng; miếng"),
        ("角", "hào"),
        ("还", "còn, vẫn"),
        ("别的", "cái khác"),
        ("橘子", "quýt"),
        ("怎么", "thế nào, sao"),
        ("卖", "bán"),
        ("两", "hai"),
        ("一共", "tổng cộng"),
        ("给", "đưa, cho"),
        ("找", "trả lại tiền thừa; tìm"),
    ]),
    ("Bài 9", "第九课 我换人民币", [
        ("下午", "buổi chiều"),
        ("上午", "buổi sáng"),
        ("图书馆", "thư viện"),
        ("换", "đổi"),
        ("小姐", "cô, tiểu thư"),
        ("营业员", "nhân viên bán hàng/giao dịch"),
        ("人民币", "nhân dân tệ"),
        ("人民", "nhân dân"),
        ("百", "trăm"),
        ("美元", "đô la Mỹ"),
        ("日元", "yên Nhật"),
        ("欧元", "euro"),
        ("等", "đợi"),
        ("一会儿", "một lát"),
        ("先生", "ông, ngài"),
        ("数", "đếm"),
    ]),
    ("Bài 10", "第十课 他住哪儿", [
        ("办公室", "văn phòng"),
        ("办公", "làm việc văn phòng"),
        ("职员", "nhân viên"),
        ("在", "ở, tại"),
        ("家", "nhà; gia đình"),
        ("呢", "trợ từ ngữ khí"),
        ("住", "ở, sống"),
        ("楼", "tòa nhà; tầng"),
        ("门", "cửa"),
        ("房间", "phòng"),
        ("号", "số, hiệu"),
        ("知道", "biết"),
        ("电话", "điện thoại"),
        ("号码", "số hiệu, số điện thoại"),
        ("零", "số không"),
        ("手机", "điện thoại di động"),
        ("李昌浩", "Lý Xương Hạo"),
    ]),
    ("Bài 11", "第十一课 我们都是留学生", [
        ("秘书", "thư ký"),
        ("先", "trước, trước tiên"),
        ("介绍", "giới thiệu"),
        ("一下儿", "một chút, một lát"),
        ("位", "lượng từ chỉ người"),
        ("教授", "giáo sư"),
        ("校长", "hiệu trưởng"),
        ("欢迎", "hoan nghênh"),
        ("留学生", "lưu học sinh, du học sinh"),
        ("留学", "du học"),
        ("也", "cũng"),
        ("我们", "chúng tôi, chúng ta"),
        ("你们", "các bạn, các anh/chị"),
        ("他们", "họ, bọn họ"),
        ("都", "đều"),
        ("和", "và, với"),
        ("俩", "hai người"),
        ("学生", "học sinh, sinh viên"),
        ("没什么", "không có gì, không sao"),
        ("田芳", "Điền Phương"),
        ("罗兰", "Roland"),
        ("爱德华", "Edward"),
    ]),
    ("Bài 12", "第十二课 你在哪儿学习", [
        ("语言", "ngôn ngữ"),
        ("大学", "đại học"),
        ("怎么样", "thế nào"),
        ("觉得", "cảm thấy, cho rằng"),
        ("语法", "ngữ pháp"),
        ("听", "nghe"),
        ("比较", "tương đối; so sánh"),
        ("容易", "dễ"),
        ("读", "đọc"),
        ("写", "viết"),
        ("但是", "nhưng"),
        ("新", "mới"),
        ("同学", "bạn học"),
        ("同屋", "bạn cùng phòng"),
        ("班", "lớp"),
        ("北京语言大学", "Đại học Ngôn ngữ Bắc Kinh"),
        ("林", "họ Lâm"),
        ("文学", "văn học"),
        ("历史", "lịch sử"),
        ("法律", "pháp luật"),
        ("经济", "kinh tế"),
        ("认识", "quen biết"),
        ("旧", "cũ"),
        ("老", "già; cũ; lâu năm"),
    ]),
    ("Bài 13", "第十三课 这是不是中药", [
        ("没", "không; chưa"),
        ("没有", "không có; chưa có"),
        ("箱子", "va li, thùng"),
        ("这儿", "ở đây, chỗ này"),
        ("重", "nặng"),
        ("轻", "nhẹ"),
        ("红", "đỏ"),
        ("黑", "đen"),
        ("药", "thuốc"),
        ("中药", "thuốc Đông y"),
        ("西药", "thuốc Tây y"),
        ("茶叶", "lá trà"),
        ("里", "trong, bên trong"),
        ("日用品", "đồ dùng hằng ngày"),
        ("衣服", "quần áo"),
        ("件", "lượng từ cho quần áo/sự việc"),
        ("把", "lượng từ cho đồ có tay cầm"),
        ("雨伞", "ô, dù"),
        ("瓶", "chai, lọ"),
        ("香水", "nước hoa"),
        ("支", "lượng từ cho bút/vật thon dài"),
        ("笔", "bút"),
        ("本", "quyển; lượng từ cho sách"),
        ("词典", "từ điển"),
        ("张", "lượng từ cho giấy/bản đồ/ảnh"),
        ("光盘", "đĩa CD"),
        ("包", "túi, bao"),
        ("圆珠笔", "bút bi"),
        ("铅笔", "bút chì"),
        ("报纸", "báo"),
        ("地图", "bản đồ"),
        ("椅子", "ghế"),
        ("冰淇淋", "kem"),
        ("厕所", "nhà vệ sinh"),
        ("洗手间", "nhà vệ sinh"),
    ]),
    ("Bài 14", "第十四课 你的车是新的还是旧的", [
        ("经理", "giám đốc, quản lý"),
        ("好久", "lâu rồi"),
        ("啊", "à, a"),
        ("马马虎虎", "bình thường, tạm được"),
        ("最近", "gần đây"),
        ("开学", "khai giảng, vào học"),
        ("有点儿", "hơi, có một chút"),
        ("点儿", "một chút"),
        ("还是", "hay là"),
        ("咖啡", "cà phê"),
        ("杯", "cốc; ly; lượng từ cho đồ uống"),
        ("车", "xe"),
        ("自行车", "xe đạp"),
        ("汽车", "ô tô"),
        ("摩托车", "xe máy"),
        ("出租车", "taxi"),
        ("颜色", "màu sắc"),
        ("蓝", "màu xanh lam"),
        ("累", "mệt"),
        ("饿", "đói"),
        ("冷", "lạnh"),
        ("渴", "khát"),
        ("衬衣", "áo sơ mi"),
        ("毛衣", "áo len"),
        ("黄", "màu vàng"),
        ("灰", "màu xám"),
        ("绿", "màu xanh lá"),
        ("照相机", "máy ảnh"),
        ("忽然", "bỗng nhiên"),
        ("看见", "nhìn thấy"),
        ("它", "nó"),
        ("送", "tặng; đưa"),
        ("好看", "đẹp, dễ nhìn"),
        ("好骑", "dễ đi/đạp"),
        ("每天", "mỗi ngày"),
        ("来", "đến"),
    ]),
    ("Bài 15", "第十五课 你们公司有多少职员", [
        ("全", "toàn bộ, đều"),
        ("照片", "ảnh"),
        ("看", "xem, nhìn"),
        ("姐姐", "chị gái"),
        ("大夫", "bác sĩ"),
        ("医院", "bệnh viện"),
        ("公司", "công ty"),
        ("商店", "cửa hàng"),
        ("律师", "luật sư"),
        ("外贸", "ngoại thương"),
        ("大概", "khoảng, đại khái"),
        ("多", "nhiều; hơn"),
        ("外国", "nước ngoài"),
        ("只", "chỉ"),
        ("口", "miệng; khẩu, người trong gia đình"),
        ("有", "có"),
        ("女", "nữ, con gái"),
        ("画报", "tạp chí ảnh"),
        ("世界", "thế giới"),
        ("数码相机", "máy ảnh kỹ thuật số"),
        ("家务", "việc nhà"),
        ("高兴", "vui, phấn khởi"),
    ]),
]

PINYIN_OVERRIDES = {
    "不": "bù",
    "一": "yī",
    "吗": "ma",
    "爸爸": "bàba",
    "妈妈": "māma",
    "哪儿": "nǎr",
    "那儿": "nàr",
    "这儿": "zhèr",
    "的": "de",
    "个": "ge",
    "了": "le",
    "吧": "ba",
    "呢": "ne",
    "一下儿": "yíxiàr",
    "一会儿": "yíhuìr",
    "有点儿": "yǒu diǎnr",
    "点儿": "diǎnr",
    "没什么": "méi shénme",
}

EXAMPLES = {
    "你": ("你好吗？", "Nǐ hǎo ma?", "Bạn khỏe không?"),
    "好": ("我很好。", "Wǒ hěn hǎo.", "Tôi rất khỏe/tốt."),
    "你好": ("你好！", "Nǐ hǎo!", "Xin chào!"),
    "不": ("我不忙。", "Wǒ bù máng.", "Tôi không bận."),
    "忙": ("爸爸很忙。", "Bàba hěn máng.", "Bố rất bận."),
    "吗": ("你忙吗？", "Nǐ máng ma?", "Bạn có bận không?"),
    "很": ("很好。", "Hěn hǎo.", "Rất tốt."),
    "汉语": ("我学习汉语。", "Wǒ xuéxí Hànyǔ.", "Tôi học tiếng Trung."),
    "难": ("汉语难吗？", "Hànyǔ nán ma?", "Tiếng Trung khó không?"),
    "太": ("不太难。", "Bù tài nán.", "Không khó lắm."),
    "爸爸": ("爸爸很忙。", "Bàba hěn máng.", "Bố rất bận."),
    "妈妈": ("妈妈很好。", "Māma hěn hǎo.", "Mẹ rất khỏe."),
    "他": ("他是老师。", "Tā shì lǎoshī.", "Anh ấy là giáo viên."),
    "她": ("她是学生。", "Tā shì xuésheng.", "Cô ấy là học sinh/sinh viên."),
    "明天": ("明天见。", "Míngtiān jiàn.", "Ngày mai gặp nhé."),
    "学校": ("我回学校。", "Wǒ huí xuéxiào.", "Tôi về trường."),
    "老师": ("这是王老师。", "Zhè shì Wáng lǎoshī.", "Đây là thầy/cô Vương."),
    "学习": ("我学习汉语。", "Wǒ xuéxí Hànyǔ.", "Tôi học tiếng Trung."),
    "吃": ("你吃什么？", "Nǐ chī shénme?", "Bạn ăn gì?"),
    "买": ("我买苹果。", "Wǒ mǎi píngguǒ.", "Tôi mua táo."),
    "换": ("我换人民币。", "Wǒ huàn Rénmínbì.", "Tôi đổi nhân dân tệ."),
    "住": ("他住哪儿？", "Tā zhù nǎr?", "Anh ấy sống ở đâu?"),
    "介绍": ("我介绍一下儿。", "Wǒ jièshào yíxiàr.", "Tôi giới thiệu một chút."),
    "觉得": ("我觉得汉语不太难。", "Wǒ juéde Hànyǔ bú tài nán.", "Tôi thấy tiếng Trung không khó lắm."),
    "中药": ("这是不是中药？", "Zhè shì bú shì zhōngyào?", "Đây có phải thuốc Đông y không?"),
    "自行车": ("我的自行车是新的。", "Wǒ de zìxíngchē shì xīn de.", "Xe đạp của tôi là xe mới."),
    "公司": ("你们公司有多少职员？", "Nǐmen gōngsī yǒu duōshǎo zhíyuán?", "Công ty các bạn có bao nhiêu nhân viên?"),
}

VERB_EXAMPLES = {
    "学": "我学汉语。",
    "见": "明天见。",
    "去": "我去邮局。",
    "寄": "我寄信。",
    "取": "我取钱。",
    "回": "我回学校。",
    "请": "请进。",
    "进": "请进。",
    "坐": "请坐。",
    "喝": "我喝茶。",
    "谢谢": "谢谢你。",
    "工作": "他在医院工作。",
    "问": "我问老师。",
    "叫": "我叫麦克。",
    "发音": "他的发音很好。",
    "要": "我要一碗汤。",
    "卖": "苹果怎么卖？",
    "给": "我给你钱。",
    "找": "找您三块。",
    "等": "请等一会儿。",
    "数": "请数数。",
    "办公": "他在办公室办公。",
    "知道": "我知道他的电话。",
    "欢迎": "欢迎你。",
    "听": "我听汉语。",
    "读": "我读课文。",
    "写": "我写汉字。",
    "认识": "我认识王老师。",
    "看见": "我看见老师。",
    "送": "他送我一本书。",
    "来": "他来学校。",
    "看": "我看照片。",
    "有": "我有一本词典。",
}


def pinyin(text: str) -> str:
    if text in PINYIN_OVERRIDES:
        return PINYIN_OVERRIDES[text]
    return " ".join(lazy_pinyin(text, style=Style.TONE, neutral_tone_with_five=False))


def example_for(word: str, meaning: str):
    if word in EXAMPLES:
        return EXAMPLES[word]
    sentence = VERB_EXAMPLES.get(word)
    if not sentence:
        sentence = f"这个词是{word}。"
        return sentence, f"Zhège cí shì {pinyin(word)}.", f"Từ này là '{word}' ({meaning})."
    return sentence, pinyin(sentence.rstrip("。！？?")) + ("." if sentence.endswith("。") else ""), f"Ví dụ với '{meaning}'."


def rows():
    seen = set()
    for lesson, title, words in LESSONS:
        for hanzi, meaning in words:
            key = (lesson, hanzi)
            if key in seen:
                continue
            seen.add(key)
            ex_h, ex_p, ex_v = example_for(hanzi, meaning)
            yield lesson, title, hanzi, pinyin(hanzi), meaning, ex_h, ex_p, ex_v


def build_html():
    by_lesson = {}
    for row in rows():
        by_lesson.setdefault(row[0], {"title": row[1], "rows": []})["rows"].append(row)

    nav = "".join(
        f'<a href="#{escape(lesson)}">{escape(lesson)}</a>'
        for lesson in by_lesson
    )
    sections = []
    item_no = 1
    for lesson, data in by_lesson.items():
        body = []
        for row in data["rows"]:
            i = item_no
            item_no += 1
            _, _, hanzi, py, meaning, ex_h, ex_p, ex_v = row
            body.append(
                "<tr>"
                f"<td>{i}</td><td class='hanzi'>{escape(hanzi)}</td><td>{escape(py)}</td>"
                f"<td>{escape(meaning)}</td><td><span class='hanzi small'>{escape(ex_h)}</span><br>"
                f"<span>{escape(ex_p)}</span><br><em>{escape(ex_v)}</em></td>"
                "</tr>"
            )
        sections.append(
            f"<section class='slide' id='{escape(lesson)}'>"
            f"<header><div><p>{escape(lesson)}</p><h2>{escape(data['title'])}</h2></div>"
            f"<span>{len(data['rows'])} từ/cụm từ</span></header>"
            "<table><thead><tr><th>#</th><th>Hán tự</th><th>Pinyin</th><th>Nghĩa</th><th>Ví dụ</th></tr></thead>"
            f"<tbody>{''.join(body)}</tbody></table></section>"
        )

    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Từ vựng Hán 1 - 汉语教程 第一册 上</title>
<style>
@page {{ size: A4 landscape; margin: 10mm; }}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: Inter, Arial, "Noto Sans", "Noto Sans CJK SC", sans-serif;
  color: #14213d;
  background: #f4f7fb;
}}
.cover, .slide {{
  width: 100%;
  min-height: 100vh;
  padding: 28px 36px;
  page-break-after: always;
}}
.cover {{
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 24px;
  background: #f7efe5;
  border-left: 16px solid #2a9d8f;
}}
h1 {{ font-size: 46px; margin: 0; letter-spacing: 0; }}
.cover p {{ max-width: 900px; font-size: 18px; line-height: 1.5; }}
.nav {{ display: flex; flex-wrap: wrap; gap: 8px; max-width: 980px; }}
.nav a {{ padding: 8px 10px; border: 1px solid #96a5b8; color: #14213d; text-decoration: none; background: #fff; }}
header {{ display: flex; align-items: end; justify-content: space-between; gap: 24px; margin-bottom: 14px; }}
header p {{ margin: 0 0 4px; color: #2a9d8f; font-weight: 700; }}
h2 {{ margin: 0; font-size: 30px; letter-spacing: 0; }}
header span {{ font-weight: 700; color: #5f6f82; }}
table {{ width: 100%; border-collapse: collapse; background: #fff; table-layout: fixed; }}
th, td {{ border: 1px solid #d6dee8; padding: 7px 8px; vertical-align: top; font-size: 13px; line-height: 1.28; }}
th {{ background: #14213d; color: #fff; text-align: left; }}
th:nth-child(1), td:nth-child(1) {{ width: 38px; text-align: center; }}
th:nth-child(2), td:nth-child(2) {{ width: 125px; }}
th:nth-child(3), td:nth-child(3) {{ width: 155px; }}
th:nth-child(4), td:nth-child(4) {{ width: 220px; }}
.hanzi {{ font-family: "Noto Serif CJK SC", "SimSun", serif; font-size: 22px; color: #111827; }}
.hanzi.small {{ font-size: 17px; }}
em {{ color: #5f6f82; font-style: normal; }}
@media print {{
  body {{ background: #fff; }}
  .cover, .slide {{ min-height: auto; padding: 0; }}
  .nav a {{ color: #14213d; }}
  th, td {{ font-size: 11px; padding: 5px 6px; }}
  .hanzi {{ font-size: 18px; }}
  .hanzi.small {{ font-size: 14px; }}
}}
</style>
</head>
<body>
<section class="cover">
  <h1>Từ vựng Hán 1<br>汉语教程 第一册（上）</h1>
  <p>Tổng hợp từ vựng theo tài liệu scan <strong>Hán-1.pdf</strong>, trình bày theo từng bài với Hán tự, pinyin, nghĩa tiếng Việt và cột ví dụ. File này thiết kế dạng slide ngang, có thể mở bằng trình duyệt và in/xuất PDF ở khổ A4 landscape.</p>
  <div class="nav">{nav}</div>
</section>
{''.join(sections)}
</body>
</html>
"""


def build_csv():
    lines = ["Bài,Tiêu đề,Hán tự,Pinyin,Nghĩa,Ví dụ Hán tự,Ví dụ pinyin,Ví dụ nghĩa"]
    for row in rows():
        escaped = []
        for cell in row:
            cell = str(cell).replace('"', '""')
            escaped.append(f'"{cell}"')
        lines.append(",".join(escaped))
    return "\n".join(lines) + "\n"


def main():
    Path("Han1_tu_vung_slide_ngang.html").write_text(build_html(), encoding="utf-8")
    Path("Han1_tu_vung.csv").write_text(build_csv(), encoding="utf-8-sig")
    print("Wrote Han1_tu_vung_slide_ngang.html")
    print("Wrote Han1_tu_vung.csv")


if __name__ == "__main__":
    main()
