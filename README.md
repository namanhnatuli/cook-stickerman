# Cook Stickerman — YouTube Content Production Pipeline

Quy trình sản xuất kịch bản và tài nguyên hình ảnh chuẩn cho kênh YouTube **Cook Stickerman** (Niche: *Cake & Baking Science Explainer*).

> **Tài liệu chuẩn mực văn phong:** Xem chi tiết cẩm nang biên tập, nhịp điệu, cấu trúc câu, tiêu chuẩn chính sách YouTube và từ khóa tại [`brain/writing_rules.md`](brain/writing_rules.md).
> **Dữ liệu chuẩn đối sánh (Corpus Benchmark):** Xem thông tin xuất xứ, lượt view và cảnh báo lỗi ASR của 10 video mẫu tại [`research/corpus_metadata.md`](research/corpus_metadata.md).

---

## 📁 Cấu Trúc Lưu Trữ Dự Án (`projects/`)

Mỗi video mới được quản lý độc lập trong một thư mục con bên trong `projects/`:

```text
projects/
└── [slug-ten-video]/                 # Ví dụ: projects/every-cheesecake-explained/
    ├── 01_topic.md                   # Concept, Title, Hook angle, Thumbnail hypothesis & Knowledge depth score
    ├── 02_research_dossier.md        # Dữ liệu khoa học, lịch sử kèm Knowledge Map, Source IDs và Source Register
    ├── 03_outline.md                 # Dàn ý tổ chức theo nhịp giảng dạy (teaching beats), câu nối & bằng chứng visual
    ├── 04_script_draft.md            # Bản thảo kịch bản voiceover (Knowledge-first, 5-beat pedagogy arc)
    ├── 05_audit_review.md            # Báo cáo audit 8 tiêu chí (Stage 1) và bản Final Script đã duyệt (Stage 2)
    ├── 06_scene_assets.md            # Storyboard phân cảnh theo teaching beats, Mascot cue & Bảng bản quyền
    ├── 07_rough_cut_timecodes.md     # Khóa mốc thời gian thực tế sau khi thu âm và dựng rough cut (Timing Lock)
    ├── 08_thumbnail.md               # Prompt tạo Final Hero Thumbnail (dựa trên visual proof) và Asset Sheet
    ├── 09_seo_metadata.md            # Mô tả video 200–300 từ, chapters theo timecode đã khóa, tags biến thể
    ├── 10_policy_check.md            # Báo cáo rủi ro chính sách theo ngữ cảnh (Context-aware safety audit & patch list)
    ├── 11_localized_package.md       # Trọn gói bản địa hóa: Voiceover, Title, Description, Thumbnail text & Glossary
    └── 12_post_mortem.md             # Đánh giá CTR theo traffic source, retention 30s và Knowledge Signals sau publish
```

---

## ⚡ Thứ Tự Chạy Prompt Khi Sản Xuất Một Video

Quy trình sản xuất gồm các bước tuần tự, sử dụng các template prompt trong thư mục [`prompts/scripts/`](prompts/scripts/):

| Bước | Hành động | Prompt Sử Dụng | File Đầu Ra Lưu Vào |
| :--- | :--- | :--- | :--- |
| **Bước 1** | **Chọn Chủ Đề & Giả Thuyết Đóng Gói (Hypothesis)**<br>Lên 10 concept theo tỷ lệ 60/40, đánh giá Knowledge Depth (chiều sâu kiến thức chuyển giao), Research Risk, và lên concept thumbnail sơ bộ. | [`topics.md`](prompts/scripts/topics.md) | `projects/[slug]/01_topic.md` |
| **Bước 2** | **Nghiên Cứu Sâu (Chống Hallucination & Lập Bản Đồ Tri Thức)**<br>Xây dựng Knowledge Map (Causal chain: *Nguyên liệu $\rightarrow$ Cơ chế $\rightarrow$ Kết cấu $\rightarrow$ Bài học*), phân tầng Essential vs Enrichment, gắn nhãn claim status kèm Source Register chi tiết. | [`research.md`](prompts/scripts/research.md) | `projects/[slug]/02_research_dossier.md` |
| **Bước 3** | **Lập Dàn Ý Theo Nhịp Giảng Dạy (Teaching Beats Outline)**<br>Nhóm theo khối bài giảng khoa học (không ép theo từng link nguồn riêng lẻ), xác định mục tiêu sư phạm, chuỗi nhân quả, bằng chứng visual, câu nối và đánh dấu `[CẦN KIỂM CHỨNG]`. | [`outline.md`](prompts/scripts/outline.md) | `projects/[slug]/03_outline.md` |
| **Bước 4** | **Viết Kịch Bản Voiceover (Knowledge-First)**<br>Phóng tác từ Dàn ý đã duyệt. Ưu tiên truyền tải trọn vẹn kiến thức trước thời lượng (runtime chỉ là ước tính). Áp dụng khung 5-beat pedagogy (Hook $\rightarrow$ Thesis $\rightarrow$ Causal Body $\rightarrow$ Synthesis $\rightarrow$ Actionable Outro). | [`script.md`](prompts/scripts/script.md) | `projects/[slug]/04_script_draft.md` |
| **Bước 5** | **Audit & Biên Tập Bản Kịch Bản Hoàn Chỉnh**<br>• *Stage 1:* Audit 8 tiêu chí (Knowledge Completeness, Factual Integrity, Context-based Safety & Cẩm nang biên tập).<br>• *Stage 2 (Self-contained):* Chỉ rewrite khi có input bảng claim và định hướng cắt gọn đã duyệt. | [`review.md`](prompts/scripts/review.md) | `projects/[slug]/05_audit_review.md` |
| **Bước 6** | **Lập Storyboard & Gán Mascot Theo Nhịp Giảng Dạy**<br>Phân cụm Scene Clusters theo teaching beats (Must-Have vs Supporting), gắn Evidence Basis, gán Mascot 5–8 lần làm điểm nhấn sư phạm, và lập bảng kiểm tra bản quyền (con người xác nhận). | [`scene_assets.md`](prompts/scripts/scene_assets.md) | `projects/[slug]/06_scene_assets.md` |
| **Bước 7** | **Thu Âm, Dựng Rough Cut & Khóa Timecodes (Timing Lock)**<br>*(Thực hiện trong phần mềm dựng phim)* Thu âm voiceover, dựng bản rough cut, chốt thời lượng thực tế và xuất ra bảng **Final Edit Timecodes** cho các bước sau. | *Quy trình dựng phim* | `projects/[slug]/07_rough_cut_timecodes.md` |
| **Bước 8** | **Thiết Kế Final Thumbnail & Asset Sheet**<br>Tạo prompt Hero Thumbnail dựa trên minh chứng thị giác (chọn style: Food Photography, 3D Cutaway, hoặc Flat Editorial Diagram) và Asset Reference Sheet cho editor. | [`thumbnail.md`](prompts/scripts/thumbnail.md) | `projects/[slug]/08_thumbnail.md` |
| **Bước 9** | **Tạo Mô Tả Video & Thẻ Tag Biến Thể Sai Chính Tả (SEO)**<br>Mô tả 200–300 từ tập trung vào giá trị cốt lõi, danh sách chương dựa trên Final Edit Timecodes, 1–2 chủ đề chính, và thẻ tag tập trung vào các biến thể/từ dễ viết sai. | [`seo_description.md`](prompts/scripts/seo_description.md) | `projects/[slug]/09_seo_metadata.md` |
| **Bước 10** | **Đánh Giá Rủi Ro Chính Sách Theo Ngữ Cảnh (Policy Risk Audit)**<br>Đánh giá toàn diện kịch bản, tiêu đề, thumbnail và mô tả dựa trên tiêu chuẩn YouTube chính thức (ngữ cảnh ẩm thực, không hoang tưởng từ khóa, không dùng uyển ngữ quái dị), xuất bảng khuyến nghị patch. | [`policy_audit.md`](prompts/scripts/policy_audit.md) | `projects/[slug]/10_policy_check.md` |
| **Bước 11** | **Trọn Gói Bản Địa Hóa Đa Ngôn Ngữ (Localization Package)**<br>Dịch nhân bản bảo vệ trọn vẹn Essential Insights, điều chỉnh cú pháp theo nhịp thở bản địa, bản địa hóa đơn vị đo, tạo tiêu đề, mô tả, text thumbnail và bảng thuật ngữ phát âm. | [`localization.md`](prompts/scripts/localization.md) | `projects/[slug]/11_localized_package.md` |

---

## 🔁 Vòng Lặp Sau Xuất Bản (Post-Publish Feedback Loop)
Sau khi video lên sóng 48h và 14 ngày, sử dụng [`analytics_tracker.md`](prompts/scripts/analytics_tracker.md) ghi lại Impressions, Views, CTR (phân tích bóc tách theo Browse, Search, Suggested), retention 30s và đặc biệt là **Knowledge Signals** (khán giả đã thực sự hiểu bài hay vẫn còn hiểu lầm ở điểm nào) vào `projects/[slug]/12_post_mortem.md` để hoàn thiện tư duy làm nội dung cho các tập tiếp theo.