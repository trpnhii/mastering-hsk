# mastering-hsk

Vocabulary sheets and source scripts for the HSK learning path.

## Road to HSK 3

This branch contains generated vocabulary materials for:

- `hsk1/`: Hán 1 / 汉语教程 第一册（上） source PDF, generated PDF/HTML/CSV, and generator script.
- `hsk2/`: Hán 2 / 汉语教程 第一册（下） source PDF, generated PDF/HTML/CSV, and generator script.
- Repository root: combined Hán 1 + Hán 2 PDF/HTML/CSV.
- `docs/`: flashcard web app for GitHub Pages (quiz 2 chế độ).

Numbering is continuous inside each book file, and continuous from Hán 1 into Hán 2 in the combined files.

## Flashcards (GitHub Pages)

App nằm trong `docs/`:

- Tab **Hán tự → Nghĩa**: hiện chữ Hán, chọn nghĩa đúng
- Tab **Pinyin + Nghĩa → Hán tự**: hiện pinyin + nghĩa, chọn Hán tự đúng
- Lọc theo sách / bài; phím `1–4` chọn đáp án, `Enter` / `Space` sang câu tiếp

Cập nhật dữ liệu quiz sau khi sửa CSV:

```bash
python3 docs/build_vocab.py
```

Bật GitHub Pages:

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `road-to-hsk3` (hoặc `main` nếu đã merge), folder **`/docs`**
4. Save — site sẽ ở dạng `https://trpnhii.github.io/mastering-hsk/`
