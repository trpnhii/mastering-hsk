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

- Tab **Hán tự → Nghĩa**: hiện chữ Hán, chọn nghĩa đúng (nút hiện/ẩn pinyin)
- Tab **Pinyin + Nghĩa → Hán tự**: hiện pinyin + nghĩa, chọn Hán tự đúng
- Tab **Câu → Nghĩa**: hiện câu Hán ngắn (HSK 3), chọn bản dịch; có nút hiện/ẩn pinyin
- Lọc theo sách / bài (tab từ); ngân hàng mục sai để ôn lại; phím `1–4` / `Enter` / `Space`

Câu dịch nằm trong `docs/sentences.json` — thêm object `{ id, hanzi, pinyin, meaning, level }` để mở rộng.

Cập nhật dữ liệu quiz sau khi sửa CSV (local):

```bash
python3 docs/build_vocab.py
```

### Deploy tự động (GitHub Actions)

Workflow: `.github/workflows/pages.yml` — build + deploy khi push nhánh **`road-to-hsk3`** (không cần `main`).

Một lần duy nhất trên GitHub:

1. **Settings → Pages → Build and deployment**
2. **Source**: chọn **GitHub Actions** (không chọn Deploy from a branch)
3. Push nhánh `road-to-hsk3` (hoặc chạy lại workflow bằng **Actions → Deploy flashcards → Run workflow**)
4. Site: `https://trpnhii.github.io/mastering-hsk/`
