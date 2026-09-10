# Cook Stickerman — YouTube Content Production Pipeline

Quy trình sản xuất kịch bản và tài nguyên hình ảnh chuẩn cho kênh YouTube **Cook Stickerman** (Niche: *Cake & Baking Science Explainer*).

---

## 📁 Cấu Trúc Lưu Trữ Dự Án (`projects/`)

Mỗi video mới được quản lý độc lập trong một thư mục con bên trong `projects/`:

```text
projects/
└── [slug-ten-video]/                 # Ví dụ: projects/every-cheesecake-explained/
    ├── 01_topic.md                   # Concept, Title, Hook angle, Thumbnail hypothesis & Knowledge depth score
    ├── 02_research_dossier.md        # Dữ liệu khoa học, lịch sử kèm Knowledge Map, Source IDs và Source Register
    ├── 03_script_draft.md            # Bản thảo kịch bản voiceover (Knowledge-first, 5-beat pedagogy arc)
    ├── 04_audit_review.md            # Báo cáo audit 7 tiêu chí (Stage 1) và bản Final Script đã duyệt (Stage 2)
    ├── 05_scene_assets.md            # Storyboard phân cảnh theo teaching beats, Mascot cue & Bảng bản quyền
    ├── 06_thumbnail.md               # Prompt tạo Final Hero Thumbnail (dựa trên visual proof) và Asset Sheet
    └── 07_post_mortem.md             # Đánh giá CTR, retention 30s và Knowledge Signals sau publish (tùy chọn)
```

---

## ⚡ Thứ Tự Chạy Prompt Khi Sản Xuất Một Video

Quy trình gồm 6 bước tuần tự, sử dụng các template prompt trong thư mục [`prompts/scripts/`](prompts/scripts/):

| Bước | Hành động | Prompt Sử Dụng | File Đầu Ra Lưu Vào |
| :--- | :--- | :--- | :--- |
| **Bước 1** | **Chọn Chủ Đề & Giả Thuyết Đóng Gói (Hypothesis)**<br>Lên 10 concept theo tỷ lệ 60/40, đánh giá Knowledge Depth (chiều sâu kiến thức chuyển giao), Research Risk, và lên concept thumbnail sơ bộ. | [`topics.md`](prompts/scripts/topics.md) | `projects/[slug]/01_topic.md` |
| **Bước 2** | **Nghiên Cứu Sâu (Chống Hallucination & Lập Bản Đồ Tri Thức)**<br>Xây dựng Knowledge Map (Causal chain: *Nguyên liệu $\rightarrow$ Cơ chế $\rightarrow$ Kết cấu $\rightarrow$ Bài học*), phân tầng Essential vs Enrichment, gắn nhãn claim status kèm Source Register chi tiết. | [`research.md`](prompts/scripts/research.md) | `projects/[slug]/02_research_dossier.md` |
| **Bước 3** | **Viết Kịch Bản Voiceover (Knowledge-First)**<br>Ưu tiên truyền tải trọn vẹn kiến thức trước thời lượng. Áp dụng khung 5-beat pedagogy (Hook $\rightarrow$ Thesis $\rightarrow$ Causal Body $\rightarrow$ Synthesis $\rightarrow$ Actionable Outro). Tính toán thời lượng thực tế sau khi viết. | [`script.md`](prompts/scripts/script.md) | `projects/[slug]/03_script_draft.md` |
| **Bước 4** | **Audit & Biên Tập Bản Kịch Bản Hoàn Chỉnh**<br>• *Stage 1:* Audit 7 tiêu chí (tập trung vào *Knowledge Completeness & Factual Integrity*).<br>• *Stage 2 (Self-contained):* Chỉ rewrite khi có input bảng claim và định hướng cắt gọn đã duyệt. | [`review.md`](prompts/scripts/review.md) | `projects/[slug]/04_audit_review.md` |
| **Bước 5** | **Lập Storyboard & Gán Mascot Theo Nhịp Giảng Dạy**<br>Phân cụm Scene Clusters theo teaching beats (Must-Have vs Supporting), gán Mascot 5–8 lần làm điểm nhấn sư phạm, và lập bảng kiểm tra bản quyền (con người xác nhận). | [`scene_assets.md`](prompts/scripts/scene_assets.md) | `projects/[slug]/05_scene_assets.md` |
| **Bước 6** | **Thiết Kế Final Thumbnail & Asset Sheet**<br>Tạo prompt Hero Thumbnail dựa trên minh chứng thị giác (Visual Proof của bài học cốt lõi, tách riêng cú pháp Midjourney/Flux) và Asset Reference Sheet cho editor. | [`thumbnail.md`](prompts/scripts/thumbnail.md) | `projects/[slug]/06_thumbnail.md` |

---

## 🔁 Vòng Lặp Sau Xuất Bản (Post-Publish Feedback Loop)
Sau khi video lên sóng 48h và 14 ngày, sử dụng [`analytics_tracker.md`](prompts/scripts/analytics_tracker.md) ghi lại Impressions, Views, CTR (theo từng nguồn), retention 30s và đặc biệt là **Knowledge Signals** (khán giả đã thực sự hiểu bài hay vẫn còn hiểu lầm ở điểm nào) vào `projects/[slug]/07_post_mortem.md` để hoàn thiện tư duy làm nội dung cho các tập tiếp theo.