from html import escape
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "hsk1"))
sys.path.insert(0, str(ROOT / "hsk2"))

from pypinyin import Style, lazy_pinyin

from generate_han1_vocab import LESSONS as HAN1_LESSONS
from generate_han2_and_combined import HAN2_LESSONS


def item(hanzi, meaning, py=None):
    return (hanzi, meaning, py)


HAN3_LESSONS = [
    ("Bài 1", "第一课 我比你更喜欢音乐", [
        item("变化", "thay đổi; biến hóa"), item("暑假", "nghỉ hè"), item("还", "còn, vẫn"),
        item("比", "so với"), item("人口", "dân số"), item("最", "nhất"), item("城市", "thành phố"),
        item("增加", "tăng thêm"), item("建筑", "kiến trúc, xây dựng"), item("过去", "trước đây; qua"),
        item("变", "thay đổi, biến thành"), item("更", "càng, hơn nữa"), item("漂亮", "đẹp"),
        item("冬天", "mùa đông"), item("暖和", "ấm áp"), item("可是", "nhưng"), item("暖气", "hệ thống sưởi"),
        item("天气", "thời tiết"), item("预报", "dự báo"), item("气温", "nhiệt độ không khí"), item("光", "chỉ, toàn"),
        item("屋子", "phòng, căn phòng"), item("感觉", "cảm giác; cảm thấy"), item("家庭", "gia đình"), item("旅馆", "khách sạn/nhà trọ"),
        item("饭店", "khách sạn; nhà hàng"), item("也许", "có lẽ"), item("古典", "cổ điển"), item("现代", "hiện đại"),
        item("世界", "thế giới"), item("名曲", "danh khúc"), item("民歌", "dân ca"), item("流行", "thịnh hành, phổ biến"),
        item("歌曲", "bài hát"), item("年轻", "trẻ"), item("歌词", "lời bài hát"), item("有些", "một vài, có chút"),
        item("遥远", "xa xôi"),
    ]),
    ("Bài 2", "第二课 我们那儿的冬天", [
        item("国家", "quốc gia"), item("样", "kiểu, dáng; như"), item("时差", "chênh lệch múi giờ"), item("夜", "đêm"),
        item("季节", "mùa"), item("春天", "mùa xuân"), item("夏天", "mùa hè"), item("秋天", "mùa thu"),
        item("热", "nóng"), item("刮风", "có gió, thổi gió"), item("下雪", "tuyết rơi"), item("下雨", "mưa"),
        item("不但", "không những"), item("而且", "mà còn"), item("得", "phải, cần", "děi"), item("只", "chỉ"),
        item("只是", "chỉ là"), item("听写", "nghe viết"), item("周末", "cuối tuần"), item("出去", "đi ra ngoài"),
        item("历史", "lịch sử"), item("产生", "sản sinh, nảy sinh"), item("画册", "album tranh/ảnh"), item("研究", "nghiên cứu"),
        item("改革", "cải cách"), item("开放", "mở cửa"), item("一切", "tất cả, mọi thứ"), item("赛", "đua, thi đấu"),
        item("马", "ngựa"), item("国王", "quốc vương"), item("等", "hạng, cấp; vân vân"), item("上等", "hạng trên"),
        item("中等", "hạng trung"), item("下等", "hạng dưới"),
    ]),
    ("Bài 3", "第三课 冬天快要到了", [
        item("爱", "yêu, thích"), item("滑冰", "trượt băng"), item("滑雪", "trượt tuyết"), item("家乡", "quê hương"),
        item("有名", "nổi tiếng"), item("风景", "phong cảnh"), item("区", "khu, vùng"), item("旅游", "du lịch"),
        item("尤其", "đặc biệt là"), item("凉快", "mát mẻ"), item("避暑", "tránh nóng, nghỉ mát"), item("人家", "người ta; nhà người khác"),
        item("经营", "kinh doanh"), item("发财", "phát tài"), item("树叶", "lá cây"), item("落", "rơi, rụng"),
        item("红叶", "lá đỏ"), item("捡", "nhặt"), item("着急", "sốt ruột, lo lắng"), item("着呢", "đấy, lắm", "zhe ne"),
        item("坏", "hỏng, xấu"), item("哎呀", "ôi, ái chà"), item("电池", "pin"), item("迟到", "đến muộn"),
        item("好事", "việc tốt"), item("坏事", "việc xấu"), item("母亲", "mẹ"), item("父亲", "bố"),
        item("地", "trợ từ trạng ngữ", "de"), item("结婚", "kết hôn"), item("离婚", "ly hôn"), item("未婚夫", "chồng chưa cưới"),
        item("未婚妻", "vợ chưa cưới"), item("将来", "tương lai"), item("这样", "như thế này"), item("那样", "như thế kia"),
    ]),
    ("Bài 4", "第四课 快上来吧，要开车了", [
        item("送", "tiễn, đưa; tặng"), item("开会", "họp"), item("教学", "giảng dạy"), item("研讨", "nghiên cứu thảo luận"),
        item("研讨会", "hội thảo"), item("经过", "trải qua; đi qua"), item("问好", "gửi lời hỏi thăm"), item("挡", "chặn, cản"),
        item("过去", "đi qua; quá khứ"), item("过来", "đi lại đây"), item("门口", "cửa ra vào"), item("辛苦", "vất vả"),
        item("麻烦", "phiền phức; làm phiền"), item("趟", "chuyến, lượt"), item("爱人", "vợ/chồng"), item("办事", "làm việc, giải quyết việc"),
        item("马上", "ngay lập tức"), item("慢", "chậm"), item("展览馆", "phòng/nhà triển lãm"), item("展览", "triển lãm"),
        item("上来", "lên đây"), item("开车", "lái xe; xe chạy"), item("相机", "máy ảnh"),
    ]),
    ("Bài 5", "第五课 我听过钢琴协奏曲《黄河》", [
        item("经历", "trải nghiệm; kinh nghiệm"), item("过", "đã từng", "guo"), item("住院", "nằm viện"), item("中医", "Đông y"),
        item("苦", "đắng, khổ"), item("中成药", "thuốc Đông y bào chế sẵn"), item("甜", "ngọt"), item("摸", "sờ, bắt"),
        item("脉", "mạch"), item("药方", "đơn thuốc"), item("按摩", "xoa bóp"), item("针灸", "châm cứu"),
        item("方法", "phương pháp"), item("治", "chữa trị"), item("扎针", "châm kim, tiêm/châm"), item("曾经", "đã từng"),
        item("好", "dễ, tốt"), item("烤鸭", "vịt quay"), item("中餐", "món Trung"), item("白薯", "khoai lang"),
        item("糖葫芦", "kẹo hồ lô"), item("什么的", "vân vân, các thứ như"), item("亲耳", "tận tai"), item("钢琴", "đàn piano"),
        item("家", "nhà; chuyên gia", "jiā"), item("互相", "lẫn nhau"), item("说谎", "nói dối"), item("谈恋爱", "yêu đương"),
        item("恋爱", "tình yêu, yêu đương"), item("老实", "thật thà"), item("分手", "chia tay"), item("大声", "to tiếng"),
    ]),
    ("Bài 6", "第六课 我是跟旅游团一起来的", [
        item("前天", "hôm kia"), item("后天", "ngày kia"), item("导游", "hướng dẫn viên du lịch"), item("研究生", "nghiên cứu sinh/học viên cao học"),
        item("打工", "làm thêm"), item("利用", "lợi dụng, tận dụng"), item("假期", "kỳ nghỉ"), item("旅行社", "công ty du lịch"),
        item("组织", "tổ chức"), item("老板", "ông chủ"), item("需要", "cần"), item("经常", "thường xuyên"),
        item("收集", "thu thập"), item("安排", "sắp xếp"), item("帮助", "giúp đỡ"), item("希望", "hy vọng"),
        item("铁路", "đường sắt"), item("风光", "phong cảnh"), item("商量", "bàn bạc"), item("古", "cổ, xưa"),
        item("故乡", "quê hương"), item("自由", "tự do"), item("活动", "hoạt động"), item("互相", "lẫn nhau"),
        item("老外", "người nước ngoài"), item("鼻子", "mũi"), item("眼睛", "mắt"), item("声调", "thanh điệu"),
        item("孔子", "Khổng Tử"), item("丹尼丝", "Denise"), item("深圳", "Thâm Quyến"), item("兼", "kiêm"),
        item("课题", "đề tài nghiên cứu"), item("与", "và; với"),
    ]),
    ("Bài 7", "第七课 我的护照你找到了没有", [
        item("斧子", "cái rìu"), item("邻居", "hàng xóm"), item("偷", "trộm, ăn cắp"), item("小偷", "kẻ trộm"),
        item("表情", "vẻ mặt, biểu cảm"), item("言行", "lời nói và hành vi"), item("举动", "cử động, hành động"), item("砍柴", "chặt củi"),
    ]),
    ("Bài 8", "第八课 我的眼镜摔坏了", [
        item("照", "chụp, soi"), item("洗", "rửa; tráng ảnh"), item("闭", "nhắm, đóng"), item("油画", "tranh sơn dầu"),
        item("放大", "phóng to"), item("倍", "lần, bội"), item("公分", "xăng-ti-mét"), item("差点儿", "suýt nữa"),
        item("碰", "va, chạm"), item("起", "vụ, lần"), item("事故", "sự cố, tai nạn"), item("整", "nguyên, trọn"),
        item("眼镜", "kính mắt"), item("别提了", "đừng nhắc nữa"), item("倒霉", "xui xẻo"), item("摔", "ngã, rơi vỡ"),
        item("地上", "trên mặt đất"), item("上班", "đi làm"), item("下班", "tan làm"), item("保证", "bảo đảm"),
        item("遵守", "tuân thủ"), item("规则", "quy tắc"), item("造成", "gây ra"), item("拥挤", "đông đúc, chen chúc"),
        item("主要", "chủ yếu"), item("原因", "nguyên nhân"), item("之", "của, giữa"), item("引起", "gây nên"),
        item("赶快", "nhanh chóng"), item("发展", "phát triển"), item("平时", "bình thường"), item("怕", "sợ"),
    ]),
    ("Bài 9", "第九课 钥匙忘拔下来了", [
        item("钥匙", "chìa khóa"), item("忘", "quên"), item("拔", "rút ra, nhổ"), item("下来", "xuống; ra khỏi"),
    ]),
    ("Bài 10", "第十课 会议厅的门开着呢", [
        item("会议厅", "phòng họp, hội trường"), item("中心", "trung tâm"), item("服务员", "nhân viên phục vụ"), item("长", "dài; cao"),
        item("个子", "vóc dáng, chiều cao"), item("左右", "khoảng, trái phải"), item("戴", "đeo, đội"), item("着", "trợ từ chỉ trạng thái tiếp diễn", "zhe"),
        item("副", "lượng từ cho kính/găng"), item("西服", "âu phục"), item("裙子", "váy"), item("干", "làm"),
        item("主持人", "người dẫn chương trình"), item("主持", "chủ trì"), item("小伙子", "chàng trai"), item("扛", "vác"),
        item("摄像机", "máy quay"), item("麦克风", "micro"), item("讲话", "phát biểu, nói chuyện"), item("婚礼", "hôn lễ"),
        item("热闹", "náo nhiệt"), item("挂", "treo"), item("灯笼", "đèn lồng"), item("新娘", "cô dâu"),
        item("棉袄", "áo bông"), item("新郎", "chú rể"), item("帅", "đẹp trai"), item("领带", "cà vạt"),
        item("热情", "nhiệt tình"), item("客人", "khách"), item("倒", "rót, đổ"), item("不停", "không ngừng"),
        item("气氛", "bầu không khí"),
    ]),
]

PINYIN_OVERRIDES = {
    "还": "hái", "得": "děi", "着呢": "zhe ne", "地": "de", "过": "guo", "什么的": "shénme de",
    "家": "jiā", "差点儿": "chàdiǎnr", "下来": "xiàlai", "着": "zhe", "左右": "zuǒyòu",
    "不但": "búdàn", "而且": "érqiě", "一切": "yíqiè", "上来": "shànglai", "过来": "guòlai",
    "过去": "guòqu", "出去": "chūqu", "也许": "yěxǔ", "有些": "yǒuxiē", "别提了": "bié tí le",
}

EXAMPLES = {
    "变化": ("这几年变化很大。", "Zhè jǐ nián biànhuà hěn dà.", "Mấy năm nay thay đổi rất nhiều."),
    "国家": ("每个国家都不一样。", "Měi ge guójiā dōu bù yíyàng.", "Mỗi quốc gia đều khác nhau."),
    "滑雪": ("冬天我喜欢滑雪。", "Dōngtiān wǒ xǐhuan huáxuě.", "Mùa đông tôi thích trượt tuyết."),
    "上来": ("快上来吧。", "Kuài shànglai ba.", "Mau lên đây đi."),
    "经历": ("这是一次难忘的经历。", "Zhè shì yí cì nánwàng de jīnglì.", "Đây là một trải nghiệm khó quên."),
    "导游": ("我是跟旅游团一起来的。", "Wǒ shì gēn lǚyóutuán yìqǐ lái de.", "Tôi đến cùng đoàn du lịch."),
    "眼镜": ("我的眼镜摔坏了。", "Wǒ de yǎnjìng shuāi huài le.", "Kính của tôi bị rơi hỏng rồi."),
    "会议厅": ("会议厅的门开着呢。", "Huìyìtīng de mén kāi zhe ne.", "Cửa phòng họp đang mở."),
}


def pinyin(text, override=None):
    if override:
        return override
    if text in PINYIN_OVERRIDES:
        return PINYIN_OVERRIDES[text]
    clean = text.replace("…", "").replace("/", " ")
    return " ".join(lazy_pinyin(clean, style=Style.TONE, neutral_tone_with_five=False))


def normalize_entry(entry):
    return entry if len(entry) == 3 else (entry[0], entry[1], None)


def example_for(hanzi, meaning, py=None):
    if hanzi in EXAMPLES:
        return EXAMPLES[hanzi]
    return f"这个词是{hanzi}。", f"Zhège cí shì {pinyin(hanzi, py)}.", f"Từ này là '{hanzi}' ({meaning})."


def iter_rows(lessons, book_label):
    for lesson, title, words in lessons:
        for entry in words:
            hanzi, meaning, py_override = normalize_entry(entry)
            py = pinyin(hanzi, py_override)
            ex_h, ex_p, ex_v = example_for(hanzi, meaning, py_override)
            yield book_label, lesson, title, hanzi, py, meaning, ex_h, ex_p, ex_v


def grouped_rows(lesson_sets):
    groups = []
    for book_label, lessons in lesson_sets:
        for book, lesson, title, hanzi, py, meaning, ex_h, ex_p, ex_v in iter_rows(lessons, book_label):
            if not groups or groups[-1][0] != book or groups[-1][1] != lesson:
                groups.append((book, lesson, title, []))
            groups[-1][3].append((hanzi, py, meaning, ex_h, ex_p, ex_v))
    return groups


def build_html(lesson_sets, title, subtitle, start_no=1):
    groups = grouped_rows(lesson_sets)
    nav = "".join(f'<a href="#{escape(book + lesson)}">{escape(book)} {escape(lesson)}</a>' for book, lesson, _, _ in groups)
    item_no = start_no
    sections = []
    for book, lesson, lesson_title, data in groups:
        body = []
        for hanzi, py, meaning, ex_h, ex_p, ex_v in data:
            body.append(
                "<tr>"
                f"<td>{item_no}</td><td class='hanzi'>{escape(hanzi)}</td><td>{escape(py)}</td>"
                f"<td>{escape(meaning)}</td><td><span class='hanzi small'>{escape(ex_h)}</span><br>"
                f"<span>{escape(ex_p)}</span><br><em>{escape(ex_v)}</em></td>"
                "</tr>"
            )
            item_no += 1
        sections.append(
            f"<section class='slide' id='{escape(book + lesson)}'>"
            f"<header><div><p>{escape(book)} · {escape(lesson)}</p><h2>{escape(lesson_title)}</h2></div>"
            f"<span>{len(data)} từ/cụm từ</span></header>"
            "<table><thead><tr><th>#</th><th>Hán tự</th><th>Pinyin</th><th>Nghĩa</th><th>Ví dụ</th></tr></thead>"
            f"<tbody>{''.join(body)}</tbody></table></section>"
        )
    return HTML_TEMPLATE.format(title=escape(title), subtitle=subtitle, nav=nav, sections="".join(sections))

HTML_TEMPLATE = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
@page {{ size: A4 landscape; margin: 10mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Inter, Arial, "Noto Sans", "Noto Sans CJK SC", sans-serif; color: #14213d; background: #f4f7fb; }}
.cover, .slide {{ width: 100%; min-height: 100vh; padding: 28px 36px; page-break-after: always; }}
.cover {{ display: flex; flex-direction: column; justify-content: center; gap: 24px; background: #eef6f3; border-left: 16px solid #2a9d8f; }}
h1 {{ font-size: 44px; margin: 0; letter-spacing: 0; }}
.cover p {{ max-width: 960px; font-size: 18px; line-height: 1.5; }}
.nav {{ display: flex; flex-wrap: wrap; gap: 8px; max-width: 1080px; }}
.nav a {{ padding: 8px 10px; border: 1px solid #96a5b8; color: #14213d; text-decoration: none; background: #fff; }}
header {{ display: flex; align-items: end; justify-content: space-between; gap: 24px; margin-bottom: 14px; }}
header p {{ margin: 0 0 4px; color: #2a9d8f; font-weight: 700; }}
h2 {{ margin: 0; font-size: 28px; letter-spacing: 0; }}
header span {{ font-weight: 700; color: #5f6f82; }}
table {{ width: 100%; border-collapse: collapse; background: #fff; table-layout: fixed; }}
th, td {{ border: 1px solid #d6dee8; padding: 7px 8px; vertical-align: top; font-size: 13px; line-height: 1.28; }}
th {{ background: #14213d; color: #fff; text-align: left; }}
th:nth-child(1), td:nth-child(1) {{ width: 46px; text-align: center; }}
th:nth-child(2), td:nth-child(2) {{ width: 135px; }}
th:nth-child(3), td:nth-child(3) {{ width: 165px; }}
th:nth-child(4), td:nth-child(4) {{ width: 230px; }}
.hanzi {{ font-family: "Noto Serif CJK SC", "SimSun", serif; font-size: 22px; color: #111827; }}
.hanzi.small {{ font-size: 17px; }}
em {{ color: #5f6f82; font-style: normal; }}
@media print {{ body {{ background: #fff; }} .cover, .slide {{ min-height: auto; padding: 0; }} th, td {{ font-size: 11px; padding: 5px 6px; }} .hanzi {{ font-size: 18px; }} .hanzi.small {{ font-size: 14px; }} }}
</style>
</head>
<body>
<section class="cover">
  <h1>{title}</h1>
  <p>{subtitle}</p>
  <div class="nav">{nav}</div>
</section>
{sections}
</body>
</html>
"""


def write_csv(path, lesson_sets):
    lines = ["Sách,Bài,Tiêu đề,Hán tự,Pinyin,Nghĩa,Ví dụ Hán tự,Ví dụ pinyin,Ví dụ nghĩa"]
    for book_label, lessons in lesson_sets:
        for row in iter_rows(lessons, book_label):
            cells = [str(c).replace('"', '""') for c in row]
            lines.append(",".join(f'"{c}"' for c in cells))
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8-sig")


def main():
    han3_sets = [("Hán 3", HAN3_LESSONS)]
    combined_sets = [("Hán 1", HAN1_LESSONS), ("Hán 2", HAN2_LESSONS), ("Hán 3", HAN3_LESSONS)]
    Path("hsk3/Han3_tu_vung_slide_ngang.html").write_text(
        build_html(han3_sets, "Từ vựng Hán 3", "Tổng hợp từ vựng Hán 3 từ file scan <strong>hsk3/Hán 3.pdf</strong>, gồm từ vựng chính và các mục bổ sung đọc được từ tài liệu. Số thứ tự chạy liên tục toàn quyển.", 1),
        encoding="utf-8",
    )
    Path("Han1_Han2_Han3_tu_vung_gop_slide_ngang.html").write_text(
        build_html(combined_sets, "Từ vựng Hán 1 + Hán 2 + Hán 3", "Bản gộp từ vựng Hán 1, Hán 2 và Hán 3. Số thứ tự chạy liên tục từ Hán 1 sang Hán 3, không reset theo bài.", 1),
        encoding="utf-8",
    )
    write_csv("hsk3/Han3_tu_vung.csv", han3_sets)
    write_csv("Han1_Han2_Han3_tu_vung_gop.csv", combined_sets)
    print("Wrote hsk3/Han3_tu_vung_slide_ngang.html")
    print("Wrote Han1_Han2_Han3_tu_vung_gop_slide_ngang.html")
    print("Wrote hsk3/Han3_tu_vung.csv")
    print("Wrote Han1_Han2_Han3_tu_vung_gop.csv")


if __name__ == "__main__":
    main()
