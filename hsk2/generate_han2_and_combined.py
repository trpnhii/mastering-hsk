from html import escape
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hsk1"))

from pypinyin import Style, lazy_pinyin

from generate_han1_vocab import LESSONS as HAN1_LESSONS


def item(hanzi, meaning, py=None):
    return (hanzi, meaning, py)


HAN2_LESSONS = [
    ("Bài 16", "第十六课 你常去图书馆吗", [
        item("现在", "bây giờ, hiện nay"), item("跟", "với, theo"), item("一起", "cùng nhau"),
        item("咱们", "chúng ta"), item("走", "đi"), item("常常", "thường thường"),
        item("有时候", "có lúc"), item("时候", "lúc, thời gian"), item("借", "mượn"),
        item("上网", "lên mạng"), item("资料", "tài liệu"), item("总是", "luôn luôn"),
        item("安静", "yên tĩnh"), item("晚上", "buổi tối"), item("复习", "ôn tập"),
        item("课文", "bài khóa"), item("预习", "chuẩn bị bài trước"), item("生词", "từ mới"),
        item("或者", "hoặc là"), item("练习", "luyện tập; bài tập"), item("聊天儿", "nói chuyện phiếm"),
        item("收发", "nhận và gửi"), item("伊妹儿", "email"), item("电影", "phim"),
        item("电视剧", "phim truyền hình"), item("电视", "tivi"), item("休息", "nghỉ ngơi"),
        item("宿舍", "ký túc xá"), item("公园", "công viên"), item("超市", "siêu thị"),
        item("东西", "đồ vật, thứ"), item("所以", "cho nên"),
    ]),
    ("Bài 17", "第十七课 他在做什么呢", [
        item("在", "đang; ở"), item("出来", "đi ra"), item("正在", "đang"), item("音乐", "âm nhạc"),
        item("没有", "không có; chưa"), item("正", "đúng lúc, đang"), item("录音", "ghi âm; băng ghi âm"),
        item("事", "việc"), item("书店", "hiệu sách"), item("想", "muốn, nghĩ, nhớ"),
        item("汉英", "Hán - Anh"), item("坐", "ngồi; đi bằng phương tiện"), item("挤", "chen chúc"),
        item("骑", "đạp/cưỡi"), item("行", "được, ổn"), item("门", "môn học; cửa"),
        item("课", "môn học; bài học"), item("综合", "tổng hợp"), item("口语", "khẩu ngữ, nói"),
        item("听力", "nghe hiểu"), item("阅读", "đọc hiểu"), item("文化", "văn hóa"),
        item("体育", "thể dục"), item("教", "dạy"), item("打电话", "gọi điện thoại"),
        item("飞机", "máy bay"), item("火车", "tàu hỏa"), item("走路", "đi bộ"),
        item("打的", "đi taxi"), item("电话卡", "thẻ điện thoại"), item("服务员", "nhân viên phục vụ"),
    ]),
    ("Bài 18", "第十八课 我去邮局寄包裹", [
        item("包裹", "bưu kiện"), item("顺便", "tiện thể"), item("替", "thay, giúp"),
        item("邮票", "tem"), item("份", "lượng từ cho báo/tài liệu"), item("青年", "thanh niên"),
        item("报", "báo"), item("报纸", "tờ báo"), item("拿", "cầm, lấy"), item("不用", "không cần"),
        item("旅行", "du lịch"), item("代表", "đại biểu, đại diện"), item("代表团", "đoàn đại biểu"),
        item("参观", "tham quan"), item("翻译", "phiên dịch; dịch"), item("飞机", "máy bay"),
        item("火车", "tàu hỏa"), item("回来", "trở về"), item("办", "làm, xử lý"),
        item("帮", "giúp"), item("浇", "tưới"), item("花", "hoa"), item("没问题", "không vấn đề gì"),
        item("问题", "vấn đề, câu hỏi"), item("上海", "Thượng Hải"), item("珍妮", "Janet"),
    ]),
    ("Bài 19", "第十九课 可以试试吗", [
        item("羽绒服", "áo lông vũ"), item("又…又…", "vừa... vừa..."), item("便宜", "rẻ"),
        item("长", "dài"), item("一点儿", "một chút"), item("短", "ngắn"), item("深", "đậm, sâu"),
        item("浅", "nhạt, nông"), item("试", "thử"), item("可以", "có thể"), item("当然", "đương nhiên"),
        item("肥", "rộng, béo"), item("瘦", "chật/gầy"), item("合适", "phù hợp"), item("好看", "đẹp, dễ nhìn"),
        item("种", "loại"), item("打折", "giảm giá, chiết khấu"), item("面包", "bánh mì"),
        item("鞋", "giày"), item("双", "đôi"), item("毛衣", "áo len"), item("听说", "nghe nói"),
        item("冬天", "mùa đông"), item("冷", "lạnh"), item("机场", "sân bay"), item("接", "đón"),
        item("能", "có thể"), item("展览", "triển lãm"),
    ]),
    ("Bài 20", "第二十课 祝你生日快乐", [
        item("年", "năm"), item("今年", "năm nay"), item("明年", "năm sau"), item("去年", "năm ngoái"),
        item("后年", "năm sau nữa"), item("毕业", "tốt nghiệp"), item("多", "nhiều; bao nhiêu"),
        item("多大", "bao nhiêu tuổi"), item("岁", "tuổi"), item("属", "cầm tinh"), item("狗", "chó"),
        item("月", "tháng"), item("号", "ngày; số"), item("生日", "sinh nhật"), item("正好", "vừa đúng"),
        item("打算", "dự định"), item("准备", "chuẩn bị"), item("举行", "tổ chức"), item("晚会", "buổi liên hoan tối"),
        item("参加", "tham gia"), item("时间", "thời gian"), item("点钟", "giờ"), item("就", "liền, ngay, thì"),
        item("一定", "nhất định"), item("祝", "chúc"), item("快乐", "vui vẻ"), item("祝你生日快乐", "chúc mừng sinh nhật"),
        item("新年", "năm mới"), item("春节", "Tết Nguyên đán"), item("圣诞节", "Giáng sinh"), item("健康", "sức khỏe"),
        item("大后年", "ba năm sau"), item("礼物", "quà tặng"), item("玩具", "đồ chơi"), item("有意思", "thú vị, có ý nghĩa"),
        item("出生", "ra đời, sinh ra"), item("唱歌", "hát"), item("蛋糕", "bánh kem"),
    ]),
    ("Bài 21", "第二十一课 我们明天七点一刻出发", [
        item("每", "mỗi"), item("早上", "buổi sáng sớm"), item("半", "nửa"), item("起床", "thức dậy"),
        item("早饭", "bữa sáng"), item("午饭", "bữa trưa"), item("晚饭", "bữa tối"), item("以后", "sau, sau khi"),
        item("差", "kém; thiếu"), item("分钟", "phút"), item("上课", "lên lớp, vào học"), item("节", "tiết học"),
        item("教室", "phòng học"), item("锻炼", "rèn luyện, tập thể dục"), item("洗澡", "tắm"), item("然后", "sau đó"),
        item("睡觉", "ngủ"), item("爬", "leo"), item("们", "hậu tố số nhiều"), item("山", "núi"),
        item("年级", "năm/lớp học"), item("出发", "xuất phát"), item("前", "trước"), item("集合", "tập hợp"),
        item("刻", "mười lăm phút, khắc"), item("上车", "lên xe"), item("下车", "xuống xe"), item("准时", "đúng giờ"),
        item("带", "mang theo"), item("课间", "giờ ra chơi, giữa giờ"), item("上班", "đi làm"), item("下班", "tan làm"),
        item("努力", "cố gắng"), item("加拿大", "Canada"), item("跑步", "chạy bộ"), item("打球", "chơi bóng"),
        item("洗衣服", "giặt quần áo"),
    ]),
    ("Bài 22", "第二十二课 我打算请老师教京剧", [
        item("让", "để, bảo, cho phép"), item("大家", "mọi người"), item("谈", "nói chuyện, bàn"), item("自己", "tự mình"),
        item("爱好", "sở thích"), item("京剧", "Kinh kịch"), item("喜欢", "thích"), item("非常", "vô cùng, rất"),
        item("唱", "hát"), item("玩", "chơi"), item("电脑", "máy tính"), item("下课", "tan học"),
        item("感到", "cảm thấy"), item("心情", "tâm trạng"), item("愉快", "vui vẻ"), item("业余", "ngoài giờ"),
        item("以前", "trước đây"), item("就", "đã, liền"), item("对", "đối với"), item("书法", "thư pháp"),
        item("特别", "đặc biệt"), item("感兴趣", "có hứng thú"), item("兴趣", "hứng thú"), item("派", "phái, cử"),
        item("高兴", "vui, phấn khởi"), item("画", "vẽ"), item("画儿", "tranh"), item("歌", "bài hát"),
        item("太极拳", "Thái Cực Quyền"), item("足球", "bóng đá"), item("比赛", "thi đấu, trận đấu"), item("网球", "quần vợt"),
        item("武术", "võ thuật"), item("惊讶", "ngạc nhiên"), item("老外", "người nước ngoài"), item("笔记本", "máy tính xách tay; vở"),
        item("希望", "hy vọng"), item("演出", "biểu diễn"),
    ]),
    ("Bài 23", "第二十三课 学校里边有邮局吗", [
        item("边", "bên, phía"), item("东边", "phía đông"), item("西边", "phía tây"), item("南边", "phía nam"),
        item("北边", "phía bắc"), item("前边", "phía trước"), item("后边", "phía sau"), item("左边", "bên trái"),
        item("右边", "bên phải"), item("里边", "bên trong"), item("外边", "bên ngoài"), item("上边", "bên trên"),
        item("下边", "bên dưới"), item("离", "cách"), item("远", "xa"), item("近", "gần"), item("地方", "nơi, chỗ"),
        item("足球场", "sân bóng đá"), item("足球", "bóng đá"), item("劳驾", "làm phiền, xin hỏi"), item("打听", "hỏi thăm"),
        item("博物馆", "bảo tàng"), item("和平", "hòa bình"), item("广场", "quảng trường"), item("中间", "ở giữa"),
        item("从", "từ"), item("到", "đến"), item("米", "mét"), item("一直", "thẳng, một mạch"),
        item("红绿灯", "đèn giao thông"), item("绿灯", "đèn xanh"), item("灯", "đèn"), item("往", "hướng về"),
        item("左", "trái"), item("右", "phải"), item("拐", "rẽ"), item("马路", "đường lớn"), item("座", "tòa, ngọn; lượng từ"),
        item("白色", "màu trắng"), item("平方米", "mét vuông"), item("高", "cao"), item("迷路", "lạc đường"),
        item("公共汽车", "xe buýt"), item("出租车", "taxi"), item("司机", "tài xế"), item("算了吧", "thôi vậy, bỏ đi"),
    ]),
    ("Bài 24", "第二十四课 我想学太极拳", [
        item("会", "biết, có thể"), item("打", "đánh, chơi"), item("太极拳", "Thái Cực Quyền"), item("听说", "nghe nói"),
        item("下", "dưới; tiếp theo"), item("报名", "đăng ký"), item("开始", "bắt đầu"), item("能", "có thể"),
        item("再", "lại, thêm lần nữa"), item("遍", "lần, lượt"), item("懂", "hiểu"), item("舒服", "thoải mái"),
        item("意思", "ý nghĩa"), item("次", "lần"), item("小时", "giờ, tiếng đồng hồ"), item("请假", "xin nghỉ phép"),
        item("头疼", "đau đầu"), item("头", "đầu"), item("疼", "đau"), item("发烧", "sốt"), item("可能", "có thể, có lẽ"),
        item("咳嗽", "ho"), item("感冒", "cảm cúm"), item("了", "trợ từ; rồi", "le"), item("看病", "khám bệnh"), item("病", "ốm, bệnh"),
        item("开车", "lái xe"), item("游泳", "bơi"), item("钓鱼", "câu cá"), item("停车", "đỗ xe"), item("滑冰", "trượt băng"),
        item("拍照", "chụp ảnh"), item("抽烟", "hút thuốc"), item("吸烟", "hút thuốc"), item("唱歌", "hát"), item("跳舞", "khiêu vũ"),
        item("打篮球", "chơi bóng rổ"), item("护照", "hộ chiếu"), item("驾照", "bằng lái xe"),
    ]),
    ("Bài 25", "第二十五课 她学得很好", [
        item("电视台", "đài truyền hình"), item("表演", "biểu diễn"), item("节目", "chương trình"), item("愿意", "sẵn lòng, muốn"),
        item("为什么", "tại sao"), item("得", "trợ từ kết cấu nối bổ ngữ trạng thái", "de"), item("不错", "khá tốt"), item("进步", "tiến bộ"),
        item("水平", "trình độ"), item("提高", "nâng cao"), item("快", "nhanh"), item("哪里", "đâu có; ở đâu"),
        item("准", "chuẩn, chính xác"), item("流利", "lưu loát"), item("努力", "cố gắng"), item("认真", "chăm chỉ, nghiêm túc"),
        item("看", "nhìn, xem, thấy"), item("为", "vì, để"), item("这么", "như thế này"), item("那么", "như thế kia"),
        item("早", "sớm"), item("运动", "vận động, thể thao"), item("跑步", "chạy bộ"), item("跑", "chạy"), item("篮球", "bóng rổ"),
        item("球", "bóng"), item("刚才", "vừa rồi"), item("可以", "cũng được, tạm được"), item("坚持", "kiên trì"),
        item("因为", "bởi vì"), item("晚", "muộn"), item("行", "được, ổn"), item("文章", "bài văn, bài viết"), item("摄影", "nhiếp ảnh"),
    ]),
    ("Bài 26", "第二十六课 田芳去哪儿了", [
        item("喂", "alo"), item("阿姨", "cô/dì, bác gái"), item("中学", "trung học"), item("出国", "ra nước ngoài"),
        item("打电话", "gọi điện thoại"), item("关机", "tắt máy"), item("对了", "à đúng rồi"), item("忘", "quên"),
        item("开机", "mở máy"), item("又", "lại"), item("响", "reo, vang"), item("接", "nhận, nghe điện thoại"),
        item("踢", "đá"), item("比赛", "thi đấu, trận đấu"), item("队", "đội"), item("输", "thua"), item("赢", "thắng"),
        item("比", "so, tỉ số"), item("祝贺", "chúc mừng"), item("哎", "này, ôi"), item("上", "học, tham gia lớp"),
        item("托福", "TOEFL"), item("已经", "đã"), item("考", "thi"), item("陪", "đi cùng"), item("考试", "thi, kỳ thi"),
        item("得", "được, đạt", "dé"), item("满分", "điểm tối đa"), item("最", "nhất"), item("奖学金", "học bổng"),
        item("送行", "tiễn đưa"), item("见面", "gặp mặt"), item("预祝", "chúc trước"), item("成功", "thành công"),
    ]),
    ("Bài 27", "第二十七课 玛丽哭了", [
        item("了", "trợ từ; rồi", "le"), item("病人", "bệnh nhân"), item("肚子", "bụng"), item("厉害", "dữ dội, nghiêm trọng"),
        item("片", "viên, lát; lượng từ"), item("拉肚子", "tiêu chảy"), item("鱼", "cá"), item("牛肉", "thịt bò"),
        item("化验", "xét nghiệm"), item("大便", "đại tiện; phân"), item("小便", "tiểu tiện"), item("检查", "kiểm tra"),
        item("结果", "kết quả"), item("出来", "ra, hiện ra"), item("得", "bị, mắc; được", "dé"), item("肠炎", "viêm ruột"),
        item("消化", "tiêu hóa"), item("开药", "kê thuốc"), item("打针", "tiêm"), item("后", "sau"), item("哭", "khóc"),
        item("寂寞", "cô đơn"), item("所以", "cho nên"), item("别", "đừng"), item("难过", "buồn"), item("礼堂", "hội trường"),
        item("舞会", "vũ hội"), item("跳舞", "khiêu vũ"), item("嗓子", "cổ họng"), item("出汗", "ra mồ hôi"),
    ]),
    ("Bài 28", "第二十八课 我吃了早饭就来了", [
        item("租", "thuê"), item("套", "bộ, căn; lượng từ"), item("房子", "nhà, phòng"), item("满意", "hài lòng"),
        item("有的", "có cái/có người"), item("周围", "xung quanh"), item("环境", "môi trường"), item("乱", "lộn xộn"),
        item("厨房", "nhà bếp"), item("卧室", "phòng ngủ"), item("客厅", "phòng khách"), item("面积", "diện tích"),
        item("层", "tầng"), item("平方米", "mét vuông"), item("上去", "đi lên"), item("阳光", "ánh nắng"), item("还是", "vẫn; vẫn là nên"),
        item("妻子", "vợ"), item("情况", "tình hình"), item("才", "mới, chỉ"), item("堵车", "kẹt xe"), item("赶", "đuổi kịp, gấp"),
        item("要是", "nếu"), item("房租", "tiền thuê nhà"), item("虽然", "tuy rằng"), item("真", "thật"), item("条", "lượng từ cho sông/đường/vật dài"),
        item("河", "sông"), item("交通", "giao thông"), item("方便", "thuận tiện"), item("站", "trạm, bến"), item("公共汽车", "xe buýt"),
        item("车站", "bến xe, nhà ga"), item("旁边", "bên cạnh"), item("地铁", "tàu điện ngầm"), item("附近", "gần đây, phụ cận"), item("体育馆", "nhà thi đấu"),
    ]),
    ("Bài 29", "第二十九课 我都做对了", [
        item("考试", "thi, kỳ thi"), item("题", "đề, câu hỏi"), item("完", "xong"), item("道", "lượng từ cho câu hỏi/món ăn"),
        item("成绩", "thành tích, điểm số"), item("句子", "câu"), item("干什么", "làm gì"), item("干", "làm"), item("看见", "nhìn thấy"),
        item("词", "từ"), item("糟糕", "hỏng bét, tệ quá"), item("成", "thành"), item("回信", "thư trả lời"), item("故事", "câu chuyện"),
        item("有意思", "thú vị"), item("页", "trang"), item("笑", "cười"), item("会话", "hội thoại"), item("念", "đọc"),
        item("答", "trả lời"), item("办法", "cách, biện pháp"), item("合上", "gấp/đóng lại"), item("听见", "nghe thấy"),
        item("打开", "mở ra"), item("作业", "bài tập"), item("熟", "thuộc, quen"), item("再", "lại"), item("于是", "thế là, vì vậy"),
        item("最好", "tốt nhất"), item("安娜", "Anna"),
    ]),
    ("Bài 30", "第三十课 我来了两个多月了", [
        item("生活", "cuộc sống; sinh hoạt"), item("差不多", "gần như, xấp xỉ"), item("习惯", "quen; thói quen"), item("气候", "khí hậu"),
        item("干燥", "khô ráo"), item("干净", "sạch sẽ"), item("菜", "món ăn; rau"), item("油腻", "nhiều dầu mỡ, ngấy"),
        item("牛奶", "sữa bò"), item("不过", "nhưng, có điều"), item("课间", "giờ ra chơi, giữa giờ"), item("块", "miếng; đồng"),
        item("点心", "điểm tâm, bánh ngọt"), item("从来", "từ trước đến nay"), item("午觉", "giấc ngủ trưa"), item("游泳", "bơi"),
        item("散步", "đi dạo"), item("功课", "bài học, bài vở"), item("记住", "nhớ kỹ"), item("一般", "thông thường, nói chung"),
        item("感谢", "cảm ơn"), item("父母", "cha mẹ"), item("机会", "cơ hội"), item("原来", "vốn, thì ra"), item("延长", "kéo dài"),
        item("练", "luyện"), item("气功", "khí công"), item("好", "mấy, vài; tốt"), item("不一定", "không nhất định"), item("钟头", "giờ, tiếng đồng hồ"),
        item("效果", "hiệu quả"), item("挺", "rất, khá"), item("好处", "chỗ tốt, lợi ích"), item("坏处", "chỗ xấu, tác hại"),
        item("慢性病", "bệnh mãn tính"), item("高血压", "cao huyết áp"), item("失眠", "mất ngủ"), item("必须", "phải, nhất định phải"),
        item("打鱼", "đánh cá"), item("晒", "phơi, hong"), item("怕", "sợ"), item("涂", "sơn, bôi"), item("油漆", "sơn"), item("裤子", "quần"),
    ]),
]

PINYIN_OVERRIDES = {
    "了": "le", "得": "de", "的": "de", "地": "de", "着": "zhe",
    "一点儿": "yìdiǎnr", "有时候": "yǒu shíhou", "总是": "zǒngshì", "伊妹儿": "yīmèir",
    "出来": "chūlai", "回来": "huílai", "没有": "méiyǒu", "打的": "dǎdī", "没问题": "méi wèntí",
    "又…又…": "yòu... yòu...", "祝你生日快乐": "zhù nǐ shēngrì kuàilè", "点钟": "diǎn zhōng",
    "上去": "shàngqu", "干什么": "gàn shénme", "差不多": "chàbuduō", "不一定": "bù yídìng",
}

EXAMPLES = {
    "现在": ("我现在去图书馆。", "Wǒ xiànzài qù túshūguǎn.", "Bây giờ tôi đi thư viện."),
    "正在": ("他正在听音乐。", "Tā zhèngzài tīng yīnyuè.", "Anh ấy đang nghe nhạc."),
    "包裹": ("我去邮局寄包裹。", "Wǒ qù yóujú jì bāoguǒ.", "Tôi đi bưu điện gửi bưu kiện."),
    "可以": ("我可以试试吗？", "Wǒ kěyǐ shìshi ma?", "Tôi có thể thử không?"),
    "生日": ("祝你生日快乐。", "Zhù nǐ shēngrì kuàilè.", "Chúc mừng sinh nhật bạn."),
    "出发": ("我们明天七点一刻出发。", "Wǒmen míngtiān qī diǎn yí kè chūfā.", "Ngày mai 7 giờ 15 chúng tôi xuất phát."),
    "京剧": ("我打算请老师教京剧。", "Wǒ dǎsuàn qǐng lǎoshī jiāo jīngjù.", "Tôi định mời giáo viên dạy Kinh kịch."),
    "邮局": ("学校里边有邮局吗？", "Xuéxiào lǐbian yǒu yóujú ma?", "Trong trường có bưu điện không?"),
    "太极拳": ("我想学太极拳。", "Wǒ xiǎng xué tàijíquán.", "Tôi muốn học Thái Cực Quyền."),
    "进步": ("她有很大进步。", "Tā yǒu hěn dà jìnbù.", "Cô ấy tiến bộ rất nhiều."),
    "已经": ("我已经报名了。", "Wǒ yǐjīng bàomíng le.", "Tôi đã đăng ký rồi."),
    "肚子": ("我肚子疼。", "Wǒ dùzi téng.", "Tôi đau bụng."),
    "房子": ("我想租一套房子。", "Wǒ xiǎng zū yí tào fángzi.", "Tôi muốn thuê một căn nhà."),
    "考试": ("我都做对了。", "Wǒ dōu zuò duì le.", "Tôi làm đúng hết rồi."),
    "习惯": ("我已经习惯这儿的生活了。", "Wǒ yǐjīng xíguàn zhèr de shēnghuó le.", "Tôi đã quen với cuộc sống ở đây rồi."),
}


def normalize_entry(entry):
    if len(entry) == 2:
        return entry[0], entry[1], None
    return entry


def pinyin(text, override=None):
    if override:
        return override
    if text in PINYIN_OVERRIDES:
        return PINYIN_OVERRIDES[text]
    clean = text.replace("…", "").replace("/", " ")
    return " ".join(lazy_pinyin(clean, style=Style.TONE, neutral_tone_with_five=False))


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
        current_book = None
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
    for row in iter_rows([l for _, lessons in lesson_sets for l in []], ""):
        pass
    for book_label, lessons in lesson_sets:
        for row in iter_rows(lessons, book_label):
            cells = [str(c).replace('"', '""') for c in row]
            lines.append(",".join(f'"{c}"' for c in cells))
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8-sig")


def main():
    han2_sets = [("Hán 2", HAN2_LESSONS)]
    combined_sets = [("Hán 1", HAN1_LESSONS), ("Hán 2", HAN2_LESSONS)]
    Path("Han2_tu_vung_slide_ngang.html").write_text(
        build_html(han2_sets, "Từ vựng Hán 2", "Tổng hợp từ vựng Hán 2 từ file scan <strong>Han 2 TV.pdf</strong>, gồm từ vựng chính và các mục bổ sung sau phần luyện/đọc. Số thứ tự chạy liên tục toàn quyển.", 1),
        encoding="utf-8",
    )
    Path("Han1_Han2_tu_vung_gop_slide_ngang.html").write_text(
        build_html(combined_sets, "Từ vựng Hán 1 + Hán 2", "Bản gộp từ vựng Hán 1 và Hán 2. Số thứ tự chạy liên tục từ Hán 1 sang Hán 2, không reset theo bài.", 1),
        encoding="utf-8",
    )
    write_csv("Han2_tu_vung.csv", han2_sets)
    write_csv("Han1_Han2_tu_vung_gop.csv", combined_sets)
    print("Wrote Han2_tu_vung_slide_ngang.html")
    print("Wrote Han1_Han2_tu_vung_gop_slide_ngang.html")
    print("Wrote Han2_tu_vung.csv")
    print("Wrote Han1_Han2_tu_vung_gop.csv")


if __name__ == "__main__":
    main()
