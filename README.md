# Cook Stickerman — YouTube Content Production Pipeline

Quy trình sản xuất kịch bản và tài nguyên hình ảnh chuẩn cho kênh YouTube **Cook Stickerman** (Niche: *Cake & Baking Science Explainer*).

---

## 📁 Cấu Trúc Lưu Trữ Dự Án (`projects/`)

Mỗi video mới được quản lý độc lập trong một thư mục con bên trong `projects/`:

```text
projects/
└── [slug-ten-video]/                 # Ví dụ: projects/every-cheesecake-explained/
    ├── 01_topic.md                   # Concept, Title, Hook angle & Đánh giá Portfolio
    ├── 02_research_dossier.md        # Dữ liệu khoa học, lịch sử và claim status đã xác thực
    ├── 03_script_draft.md            # Bản thảo kịch bản voiceover đầu tiên
    ├── 04_audit_review.md            # Báo cáo audit tính chính xác và bản final script
    ├── 05_scene_assets.md            # Storyboard phân cảnh, B-roll URLs & Mascot cue
    ├── 06_thumbnail.md               # Prompt tạo ảnh thumbnail và asset sheet
    └── 07_post_mortem.md             # Đánh giá CTR, retention 30s sau khi publish (tùy chọn)
```

---

## ⚡ Thứ Tự Chạy Prompt Khi Sản Xuất Một Video

Quy trình gồm 6 bước tuần tự, sử dụng các template prompt trong thư mục [`prompts/scripts/`](/prompts/scripts/):

| Bước | Hành động | Prompt Sử Dụng | File Đầu Ra Lưu Vào |
| :--- | :--- | :--- | :--- |
| **Bước 1** | **Chọn Chủ Đề & Đóng Gói Title/Thumb**<br>Lên 10 concept theo tỷ lệ 60/40 (Listicle vs Phân tích chuyên sâu), tính điểm và chọn 1 concept. | [`topics.md`](/prompts/scripts/topics.md) | `projects/[slug]/01_topic.md` |
| **Bước 2** | **Nghiên Cứu Sâu (Chống Hallucination)**<br>Thu thập dữ liệu khoa học, nguồn gốc có nhãn trạng thái `[CONFIRMED]` / `[DISPUTED]`. Tuyệt đối không ép drama. | [`research.md`](/prompts/scripts/research.md) | `projects/[slug]/02_research_dossier.md` |
| **Bước 3** | **Viết Kịch Bản Voiceover Thô**<br>Áp dụng tốc độ 140–150 WPM, phân bổ Hero Items và chọn góc kể chuyện linh hoạt (Science, Lore, Failure...). | [`script.md`](/prompts/scripts/script.md) | `projects/[slug]/03_script_draft.md` |
| **Bước 4** | **Audit & Biên Tập Bản Kịch Bản Hoàn Chỉnh**<br>• *Stage 1:* Audit đối chiếu fact vs dossier, bắt nhịp câu chữ.<br>• *Stage 2:* Chỉ rewrite khi đã duyệt và chốt fact. | [`review.md`](/prompts/scripts/review.md) | `projects/[slug]/04_audit_review.md` |
| **Bước 5** | **Lập Storyboard & Gán Mascot**<br>Phân 25–35 Scene Clusters (Must-Have vs Supporting), lấy link Pexels/Wikimedia và phân bổ 5–8 lần xuất hiện Mascot. | [`scene_assets.md`](/prompts/scripts/scene_assets.md) | `projects/[slug]/05_scene_assets.md` |
| **Bước 6** | **Thiết Kế Thumbnail & Asset Sheet**<br>Tạo prompt cho Hero Thumbnail (Hero cake 40–60%, tương phản cao) và Asset Sheet 3x2 nền trắng cho editor. | [`thumbnail.md`](/prompts/scripts/thumbnail.md) | `projects/[slug]/06_thumbnail.md` |

---

## 🔁 Vòng Lặp Sau Xuất Bản (Post-Publish Feedback Loop)
Sau khi video lên sóng 48h và 14 ngày, sử dụng [`analytics_tracker.md`](/prompts/scripts/analytics_tracker.md) ghi lại CTR, tỷ lệ giữ chân ở 30s và điểm tụt đồ thị sâu nhất vào `projects/[slug]/07_post_mortem.md` để tối ưu các kịch bản tiếp theo bằng dữ liệu thực tế của kênh.