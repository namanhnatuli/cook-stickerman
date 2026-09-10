# Cook Stickerman — YouTube Content Production Pipeline

Quy trình sản xuất kịch bản và tài nguyên hình ảnh chuẩn cho kênh YouTube **Cook Stickerman** (Niche: *Cake & Baking Science Explainer*).

---

## 📁 Cấu Trúc Lưu Trữ Dự Án (`projects/`)

Mỗi video mới được quản lý độc lập trong một thư mục con bên trong `projects/`:

```text
projects/
└── [slug-ten-video]/                 # Ví dụ: projects/every-cheesecake-explained/
    ├── 01_topic.md                   # Concept, Title, Hook angle, Thumbnail hypothesis & Cannibalization check
    ├── 02_research_dossier.md        # Dữ liệu khoa học, lịch sử kèm Source IDs và Source Register
    ├── 03_script_draft.md            # Bản thảo kịch bản voiceover đầu tiên (Thuật toán phân bổ từ theo trọng số)
    ├── 04_audit_review.md            # Báo cáo audit (Stage 1) và bản Final Script đã duyệt (Stage 2)
    ├── 05_scene_assets.md            # Storyboard phân cảnh (Anchor vs B-roll), Mascot cue & Bảng kiểm tra bản quyền
    ├── 06_thumbnail.md               # Prompt tạo Final Hero Thumbnail và 6-Item Asset Reference Sheet
    └── 07_post_mortem.md             # Đánh giá CTR theo nguồn, retention 30s sau khi publish (tùy chọn)
```

---

## ⚡ Thứ Tự Chạy Prompt Khi Sản Xuất Một Video

Quy trình gồm 6 bước tuần tự, sử dụng các template prompt trong thư mục [`prompts/scripts/`](prompts/scripts/):

| Bước | Hành động | Prompt Sử Dụng | File Đầu Ra Lưu Vào |
| :--- | :--- | :--- | :--- |
| **Bước 1** | **Chọn Chủ Đề & Giả Thuyết Đóng Gói (Hypothesis)**<br>Lên 10 concept theo tỷ lệ 60/40, chấm điểm heuristic, lên concept thumbnail sơ bộ và kiểm tra không trùng lặp catalog. | [`topics.md`](prompts/scripts/topics.md) | `projects/[slug]/01_topic.md` |
| **Bước 2** | **Nghiên Cứu Sâu (Chống Hallucination)**<br>Mọi claim gắn nhãn `[CONFIRMED]` / `[DISPUTED]` kèm `[Source ID]` và bảng Source Register. Không ép drama. | [`research.md`](prompts/scripts/research.md) | `projects/[slug]/02_research_dossier.md` |
| **Bước 3** | **Viết Kịch Bản Voiceover Thô**<br>Khóa tốc độ 140–150 WPM, phân bổ từ theo thuật toán trọng số (Standard = 1.0, Hero = 1.6), tuyệt đối không vượt trần thời lượng. | [`script.md`](prompts/scripts/script.md) | `projects/[slug]/03_script_draft.md` |
| **Bước 4** | **Audit & Biên Tập Bản Kịch Bản Hoàn Chỉnh**<br>• *Stage 1:* Audit đối chiếu fact vs dossier, bắt nhịp câu chữ.<br>• *Stage 2 (Self-contained):* Chỉ rewrite khi có input bảng claim đã duyệt. | [`review.md`](prompts/scripts/review.md) | `projects/[slug]/04_audit_review.md` |
| **Bước 5** | **Lập Storyboard & Gán Mascot**<br>Phân 25–35 Scene Clusters (Anchor vs Supporting), giới hạn Mascot 5–8 lần và lập bảng kiểm tra bản quyền (con người xác nhận). | [`scene_assets.md`](prompts/scripts/scene_assets.md) | `projects/[slug]/05_scene_assets.md` |
| **Bước 6** | **Thiết Kế Final Thumbnail & Asset Sheet**<br>Tạo prompt Hero Thumbnail (Hero cake 40–60%, tách riêng cú pháp Midjourney/Flux) và Asset Reference Sheet cho editor. | [`thumbnail.md`](prompts/scripts/thumbnail.md) | `projects/[slug]/06_thumbnail.md` |

---

## 🔁 Vòng Lặp Sau Xuất Bản (Post-Publish Feedback Loop)
Sau khi video lên sóng 48h và 14 ngày, sử dụng [`analytics_tracker.md`](prompts/scripts/analytics_tracker.md) ghi lại Impressions, Views, CTR (theo từng nguồn Browse/Search/Suggested), tỷ lệ giữ chân ở 30s và phân tích điểm tụt đồ thị sâu nhất vào `projects/[slug]/07_post_mortem.md` để so sánh với baseline tăng trưởng thực tế của kênh và tối ưu các video tiếp theo.