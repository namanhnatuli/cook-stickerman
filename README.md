# Cook Stickerman — YouTube Content Production Pipeline

Quy trình sản xuất kịch bản và tài nguyên hình ảnh chuẩn cho kênh YouTube **Cook Stickerman** (Niche: *Cake & Baking Science Explainer*).

> **Tài liệu chuẩn mực văn phong:** Xem chi tiết bộ luật hành văn, nhịp điệu, cấu trúc câu, 6 luật bắt buộc và từ khóa tại [`brain/writing_rules.md`](brain/writing_rules.md).

---

## 📁 Cấu Trúc Lưu Trữ Dự Án (`projects/`)

Mỗi video mới được quản lý độc lập trong một thư mục con bên trong `projects/`:

```text
projects/
└── [slug-ten-video]/                 # Ví dụ: projects/every-cheesecake-explained/
    ├── 01_topic.md                   # Concept, Title, Hook angle, Thumbnail hypothesis & Knowledge depth score
    ├── 02_research_dossier.md        # Dữ liệu khoa học, lịch sử kèm Knowledge Map, Source IDs và Source Register
    ├── 03_outline.md                 # Dàn ý chia theo khối nguồn, câu nối, 3 soft CTAs & ước tính thời lượng
    ├── 04_script_draft.md            # Bản thảo kịch bản voiceover (Knowledge-first, 5-beat pedagogy arc)
    ├── 05_audit_review.md            # Báo cáo audit 8 tiêu chí (Stage 1) và bản Final Script đã duyệt (Stage 2)
    ├── 06_scene_assets.md            # Storyboard phân cảnh theo teaching beats, Mascot cue & Bảng bản quyền
    ├── 07_thumbnail.md               # Prompt tạo Final Hero Thumbnail (dựa trên visual proof) và Asset Sheet
    ├── 08_seo_metadata.md            # Mô tả video 200–300 từ, timestamps, 10 primary/secondary tags
    ├── 09_policy_check.md            # Soát lỗi kiểm duyệt YouTube (bạo lực, giật gân, an toàn quảng cáo)
    ├── 10_localized_script.md        # Bản dịch nhân bản ngôn ngữ khác (khóa mốc thời gian master)
    └── 11_post_mortem.md             # Đánh giá CTR, retention 30s và Knowledge Signals sau publish (tùy chọn)
```

---

## ⚡ Thứ Tự Chạy Prompt Khi Sản Xuất Một Video

Quy trình gồm 10 bước tuần tự, sử dụng các template prompt trong thư mục [`prompts/scripts/`](prompts/scripts/):

| Bước | Hành động | Prompt Sử Dụng | File Đầu Ra Lưu Vào |
| :--- | :--- | :--- | :--- |
| **Bước 1** | **Chọn Chủ Đề & Giả Thuyết Đóng Gói (Hypothesis)**<br>Lên 10 concept theo tỷ lệ 60/40, đánh giá Knowledge Depth (chiều sâu kiến thức chuyển giao), Research Risk, và lên concept thumbnail sơ bộ. | [`topics.md`](prompts/scripts/topics.md) | `projects/[slug]/01_topic.md` |
| **Bước 2** | **Nghiên Cứu Sâu (Chống Hallucination & Lập Bản Đồ Tri Thức)**<br>Xây dựng Knowledge Map (Causal chain: *Nguyên liệu $\rightarrow$ Cơ chế $\rightarrow$ Kết cấu $\rightarrow$ Bài học*), phân tầng Essential vs Enrichment, gắn nhãn claim status kèm Source Register chi tiết. | [`research.md`](prompts/scripts/research.md) | `projects/[slug]/02_research_dossier.md` |
| **Bước 3** | **Lập Dàn Ý Chi Tiết Theo Khối Nguồn (Outline & Beat Sheet)**<br>Chia theo từng link nguồn (`[NGUỒN: link + mốc thời gian]`), viết câu nối mượt mà giữa các khối, rải 3 soft CTAs, đánh dấu `[CẦN KIỂM CHỨNG]`, in tổng số từ và thời lượng đọc ước tính. | [`outline.md`](prompts/scripts/outline.md) | `projects/[slug]/03_outline.md` |
| **Bước 4** | **Viết Kịch Bản Voiceover (Knowledge-First)**<br>Phóng tác từ Dàn ý đã duyệt. Ưu tiên truyền tải trọn vẹn kiến thức trước thời lượng. Áp dụng khung 5-beat pedagogy (Hook $\rightarrow$ Thesis $\rightarrow$ Causal Body $\rightarrow$ Synthesis $\rightarrow$ Actionable Outro). | [`script.md`](prompts/scripts/script.md) | `projects/[slug]/04_script_draft.md` |
| **Bước 5** | **Audit & Biên Tập Bản Kịch Bản Hoàn Chỉnh**<br>• *Stage 1:* Audit 8 tiêu chí (Knowledge Completeness, Factual Integrity & 6 Luật bắt buộc).<br>• *Stage 2 (Self-contained):* Chỉ rewrite khi có input bảng claim và định hướng cắt gọn đã duyệt. | [`review.md`](prompts/scripts/review.md) | `projects/[slug]/05_audit_review.md` |
| **Bước 6** | **Lập Storyboard & Gán Mascot Theo Nhịp Giảng Dạy**<br>Phân cụm Scene Clusters theo teaching beats (Must-Have vs Supporting), gán Mascot 5–8 lần làm điểm nhấn sư phạm, và lập bảng kiểm tra bản quyền (con người xác nhận). | [`scene_assets.md`](prompts/scripts/scene_assets.md) | `projects/[slug]/06_scene_assets.md` |
| **Bước 7** | **Thiết Kế Final Thumbnail & Asset Sheet**<br>Tạo prompt Hero Thumbnail dựa trên minh chứng thị giác (Visual Proof của bài học cốt lõi, tách riêng cú pháp Midjourney/Flux) và Asset Reference Sheet cho editor. | [`thumbnail.md`](prompts/scripts/thumbnail.md) | `projects/[slug]/07_thumbnail.md` |
| **Bước 8** | **Tạo Mô Tả Video & Bộ Thẻ Tag SEO**<br>Mô tả 200–300 từ: 2 câu đầu chứa từ khóa chính & giá trị nhận được, giữa bài tóm tắt theo timestamps, cuối có CTA. Kèm 10 từ khóa chính, 10 từ khóa phụ và danh sách thẻ tags. | [`seo_description.md`](prompts/scripts/seo_description.md) | `projects/[slug]/08_seo_metadata.md` |
| **Bước 9** | **Soát Lỗi Chính Sách YouTube (Policy Audit)**<br>Hóa thân kiểm duyệt viên khó tính: bắt lỗi bạo lực (dao/kéo), giật gân, máu me, nhạy cảm quảng cáo; giải thích nguyên nhân và viết lại phiên bản an toàn tuyệt đối. | [`policy_audit.md`](prompts/scripts/policy_audit.md) | `projects/[slug]/09_policy_check.md` |
| **Bước 10** | **Nhân Bản Sang Ngôn Ngữ Khác (Localization)**<br>Dịch nhân bản theo văn phong bản địa, giữ trọn điểm rơi cảm xúc. Khóa mốc thời gian tiếng Anh làm gốc; nếu dài hơn thì cắt bớt ở câu cuối đoạn, không xô lệch mốc sau. | [`localization.md`](prompts/scripts/localization.md) | `projects/[slug]/10_localized_script.md` |

---

## 🔁 Vòng Lặp Sau Xuất Bản (Post-Publish Feedback Loop)
Sau khi video lên sóng 48h và 14 ngày, sử dụng [`analytics_tracker.md`](prompts/scripts/analytics_tracker.md) ghi lại Impressions, Views, CTR (theo từng nguồn), retention 30s và đặc biệt là **Knowledge Signals** (khán giả đã thực sự hiểu bài hay vẫn còn hiểu lầm ở điểm nào) vào `projects/[slug]/11_post_mortem.md` để hoàn thiện tư duy làm nội dung cho các tập tiếp theo.