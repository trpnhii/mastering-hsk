# mastering-hsk

Vocabulary sheets and source scripts for the HSK learning path.

## Road to HSK 3

This branch contains generated vocabulary materials for:

- `hsk1/`: Hán 1 / 汉语教程 第一册（上）
- `hsk2/`: Hán 2 / 汉语教程 第一册（下）
- `hsk3/`: Hán 3 / 汉语教程 第二册
- Repository root: combined Hán 1 + Hán 2 + Hán 3 PDF/HTML/CSV (`Han1_Han2_Han3_tu_vung_gop.*`)
- `docs/`: flashcard web app for GitHub Pages

Numbering is continuous inside each book file, and continuous across Hán 1 → 2 → 3 in the combined files.

## Flashcards (GitHub Pages)

App nằm trong `docs/`:

- Tab **Hán tự → Nghĩa**: hiện chữ Hán, chọn nghĩa đúng (nút hiện/ẩn pinyin)
- Tab **Pinyin + Nghĩa → Hán tự**: hiện pinyin + nghĩa, chọn Hán tự đúng
- Tab **Câu → Nghĩa**: hiện câu Hán ngắn (HSK 3), chọn bản dịch; có nút hiện/ẩn pinyin
- Tab **Nhật ký**: session hiện tại, danh sách đã xem pinyin, mục gắn cờ, lịch sử các lượt ôn
- Mỗi lần ôn là 1 session (lưu local); bấm **Hiện pinyin** sẽ ghi vào nhật ký; **Gắn cờ** để đánh dấu học lại sau
- Lọc theo sách / bài (Hán 1–3); ngân hàng mục sai để ôn lại; phím `1–4` / `Enter` / `Space`

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
