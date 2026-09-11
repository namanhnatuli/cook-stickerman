# Research Corpus Metadata & Benchmark Provenance

Tài liệu này ghi lại thông tin định danh, nguồn gốc xuất xứ (provenance), số liệu đo lường và cảnh báo kỹ thuật cho 10 kịch bản mẫu được lưu trữ trong `research/scripts/`.

---

## 📊 Bảng Danh Mục & Siêu Dữ Liệu 10 Kịch Bản Mẫu

| # | Tên Tệp (`research/scripts/`) | Tiêu Đề Video Gốc | Kênh YouTube | Số Từ (Words) | Thời Lượng Ước Tính | Hiệu Suất / Views Phổ Biến | Lý Do Lựa Chọn Vào Corpus |
|---|---|---|---|---|---|---|---|
| 1 | `Every Cake Explained in 8 Minutes.md` | Every Cake Explained in 8 Minutes | **TasteDetective** | 1,088 | ~8 phút | 500K+ views | Phân loại taxonomy món bánh, tốc độ nhịp cao, không lời chào rườm rà, tập trung vào công thức và lịch sử xuất xứ. |
| 2 | `Every Famous Dessert Explained in 11 Minutes.md` | Every Famous Dessert Explained in 11 Minutes | **Decoded Dishes** | 1,569 | ~11 phút | 1M+ views | Phân tích cơ chế vật lý (coagulation, caramelization, steam rise, emulsion) và cấu trúc đối lập crust vs. crumb. |
| 3 | `Every Steak Explained in 10 Minutes.md` | Every Steak Cut Explained in 10 Minutes | **Decoded Dishes** | 1,512 | ~10 phút | 800K+ views | Mẫu mực về giải thích cấu trúc cơ bắp, mỡ dắt, và phản ứng nhiệt độ Maillard theo từng phân khúc. |
| 4 | `Every Style of Eggs Explained in 10 Minutes.md` | Every Style of Eggs Explained in 10 Minutes | **Decoded Dishes** | 1,527 | ~10 phút | 1.2M+ views | Giải thích protein biến tính (protein denaturation) và nhiệt độ đông tụ của lòng đỏ/lòng trắng cực kỳ trực quan. |
| 5 | `Every Chocolate Explained.md` | Every Chocolate Explained in 10 Minutes | **Decoded Dishes** | 1,109 | ~8–10 phút | 400K+ views | Giải thích chuỗi chế biến bơ ca-cao, đường, sữa, tinh thể hóa (tempering) và sự khác biệt giữa các dòng sô-cô-la. |
| 6 | `Every Herb Explained.md` | Every Herb Explained | **Decoded Dishes** | 1,505 | ~10 phút | 600K+ views | Nhịp chuyển đoạn gãy gọn (Noun Drop), giải thích tinh dầu thơm và cách kết hợp nhiệt khi nấu. |
| 7 | `Every Spice Explained.md` | Every Spice Explained | **Decoded Dishes** | 2,743 | ~18 phút | 900K+ views | Mở rộng danh mục gia vị, cân bằng giữa nguồn gốc địa lý lịch sử và hợp chất hóa học tạo vị cay/nồng. |
| 8 | `Every Water Brand Explained.md` | Every Water Brand Explained | **Decoded Dishes** | 2,910 | ~19 phút | 1.5M+ views | Nghệ thuật bóc tách chiêu trò marketing, so sánh chỉ số khoáng chất TDS và nguồn nước ngầm. |
| 9 | `All Coffees Explained.md` | All Coffee Drinks Explained | **FooDiscover** | 5,962 | ~40 phút | 2M+ views | Bách khoa toàn thư về đồ uống cà phê, tỷ lệ sữa/espresso, áp suất chiết xuất và văn hóa bản địa. |
| 10 | `All Sugars Explained.md` | All Sugars Explained | **FooDiscover** | 3,483 | ~24 phút | 1M+ views | Deep-dive toàn diện về 8.000 năm lịch sử mía đường, hóa học sucrose/glucose/fructose và cơ chế hút ẩm hygroscopic. |

---

## ⚠️ CẢNH BÁO KỸ THUẬT & GIỚI HẠN DỮ LIỆU ASR (SPEECH-TO-TEXT)

### 1. Nguồn Gốc Dữ Liệu
Toàn bộ 10 tệp trong `research/scripts/` được thu thập thông qua công cụ trích xuất phụ đề tự động (YouTube Native ASR / Whisper Transcription). Do đó, văn bản thô phản ánh âm thanh phát âm của người đọc lướt chứ không phải văn bản kịch bản gốc được biên tập thủ công.

### 2. Các Lỗi ASR Điển Hình Có Trong Corpus
Khi đối chiếu với lịch sử ẩm thực và khoa học thực phẩm chính thống, phát hiện nhiều lỗi nhận diện từ ngữ nghiêm trọng:
- **Tên riêng & nhà khoa học bị méo dạng:**
  - *"Conrad von Hton"* → Đúng là **Coenraad Johannes van Houten** (nhà hóa học Hà Lan phát minh ra phương pháp kiềm hóa bột ca-cao năm 1828).
  - *"Waldorf Atoria"* → Đúng là **Waldorf Astoria** (khách sạn New York gắn với truyền thuyết Red Velvet).
  - *"Juliana Rad" / "Jacob Kristoff Rad"* → Đúng là **Jakub Kryštof Rad** (phát minh ra viên đường năm 1841).
  - *"Muan Vanang"* → Đúng là **Nguyễn Văn Giảng** (người sáng tạo món Cà phê trứng Giảng tại Hà Nội năm 1946).
- **Thuật ngữ làm bánh & món tráng miệng bị viết sai:**
  - *"M foye"* → Đúng là **Mille-feuille** (bánh ngàn lớp kiểu Pháp).
  - *"Eclair's are shoe pastries"* → Đúng là **Choux pastry** (bột choux / pâte à choux nở bằng hơi nước).
  - *"maser ponyet cream"* → Đúng là **Mascarpone cream** (phô mai Mascarpone trong tiramisu).
  - *"filow dough"* → Đúng là **Phyllo dough / Filo pastry** (trong bánh baklava).
  - *"used"* (trong Finnish coffee) → Đúng là phô mai **Leipäjuusto** (kaltost).
  - *"turbanado, dearara, musavado"* → Đúng là **Turbinado, Demerara, Muscovado**.
- **Lỗi số đếm và từ nối tự động:**
  - *"and7s"* → 1970s.
  - *"and50s"* → 1950s.
  - *"Marischino"* → Maraschino.
  - *"artisal"* → Artisanal.

### 3. Nguyên Tắc Ứng Dụng Trong Pipeline Của Kênh
> **NGUYÊN TẮC BẮT BUỘC:**
> 1. **TUYỆT ĐỐI KHÔNG** sử dụng trực tiếp các thông tin lịch sử, số liệu hay tên riêng từ các file transcript trong `research/scripts/` làm bằng chứng chân lý cho video mới. Mọi kiến thức khoa học và lịch sử phải được kiểm chứng độc lập ở Bước 2 (`research.md`).
> 2. **MỤC ĐÍCH DUY NHẤT** của 10 tệp corpus này là:
>    - Nghiên cứu nhịp độ dẫn dắt (pacing: trung bình 14–18 từ/câu, xen kẽ câu đấm 3–7 từ).
>    - Học hỏi kỹ thuật chuyển đoạn tự nhiên (**The Noun Drop**, **The Boundary Shift**).
>    - Khảo sát cách đặt câu hỏi gợi mở tò mò và mở đầu ngay lập tức không chào hỏi rườm rà.
